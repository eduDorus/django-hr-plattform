from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect

from user.models import Profile

from .forms import CompanyUserForm, ApplicationProcessForm, ApplicationElementFormSet
from .models import Company, Job, ApplicationElement, ApplicationProcess


class CompanyUserFormView(View):
    form_class = CompanyUserForm
    template_name = 'company/registration.html'

    def create_company(self, company_name, user_object):
        try:
            company = Company.objects.get(name=company_name)
            company.permission_requests.add(user_object)
        except Company.DoesNotExist:
            company = Company(name=company_name)
            company.save()

            # Create default application process
            application_process = ApplicationProcess(title='default', company=company)
            application_process.save()

            # Create default application elements
            ApplicationElement(title='Application Inbox', application_process=application_process).save()
            ApplicationElement(title='Telefon Screening', application_process=application_process).save()
            ApplicationElement(title='Interview', application_process=application_process).save()
            ApplicationElement(title='Sign Contract', application_process=application_process).save()

            company.applicationprocess_set.add(application_process)

        return company

    # Show blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user_object = form.save(commit=False)

            # Clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            company_name = form.cleaned_data['company_name']

            user_object.set_password(password)
            user_object.save()

            # Create user profile
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            # Create Company
            company = self.create_company(company_name, user_object)

            profile = Profile()
            profile.gender = gender
            profile.birthday = birthday
            profile.user = user_object
            profile.company = company
            profile.save()

            # authenticate user
            user_object = authenticate(username=username, password=password)

            if user_object is not None:

                if user_object.is_active:
                    login(request, user_object)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class CompanyProfileDetailView(generic.DetailView):
    model = Company
    template_name = 'company/profile.html'
    context_object_name = 'company'


class CompanyProfileUpdateView(generic.UpdateView):
    model = Company
    template_name = 'company/form.html'
    fields = ['logo', 'name', 'description', 'sector', 'size', 'website']


class JobListView(generic.ListView):
    model = Job
    template_name = 'company/job_list.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.profile.company.id)


class JobCreateView(generic.CreateView):
    model = Job
    template_name = 'company/job_create.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'applications_process']

    def form_valid(self, form):
        form.instance.company = self.request.user.profile.company
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(generic.UpdateView):
    model = Job
    template_name = 'company/job_update.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'applications_process']


class JobDeleteView(generic.DeleteView):
    model = Job
    template_name = 'company/job_delete.html'
    context_object_name = 'job'

    def get_success_url(self):
        return reverse_lazy('company-job-list', kwargs={'pk': self.request.user.profile.company.id})


class ApplicationProcessView(generic.ListView):
    model = ApplicationProcess
    template_name = 'application_process/application_process_list.html'
    context_object_name = 'application_process_list'

    def get_queryset(self):
        return ApplicationProcess.objects.filter(company=self.request.user.profile.company.id)


class ApplicationProcessCreateView(generic.CreateView):
    form_class = ApplicationProcessForm
    model = ApplicationProcess
    template_name = 'application_process/application_process_create.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        application_element_form = ApplicationElementFormSet()
        return self.render_to_response(self.get_context_data(form=form, application_element_form=application_element_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        application_element_form = ApplicationElementFormSet(self.request.POST)
        if (form.is_valid() and application_element_form.is_valid()):
            return self.form_valid(form, application_element_form)
        else:
            return self.form_invalid(form, application_element_form)

    def form_valid(self, form, application_element_form):
        self.object = form.save()
        application_element_form.instance = self.object
        application_element_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, application_element_form):
        return self.render_to_response(self.get_context_data(form=form, application_element_form=application_element_form,))

    def get_success_url(self):
        return reverse_lazy('company-application-process-list', kwargs={'pk': self.request.user.profile.company.id})


class ApplicationProcessUpdateView(generic.UpdateView):
    model = ApplicationProcess
    template_name = 'application_process/application_process_update.html'
    fields = ['title']


class ApplicationProcessDeleteView(generic.DeleteView):
    model = ApplicationProcess
    template_name = 'application_process/application_process_delete.html'
    context_object_name = 'application_process'

    def get_success_url(self):
        return reverse_lazy('company-application-process-list', kwargs={'pk': self.request.user.profile.company.id})
