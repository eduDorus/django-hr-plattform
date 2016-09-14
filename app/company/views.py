from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.http import HttpResponseRedirect

from user.models import Profile

from .forms import CompanyUserForm, ApplicationProcessForm, ApplicationElementFormSet
from .models import Company, Job, ApplicationElement, ApplicationProcess


# Create your views here.
def hello_world(request):
    return render(request, template_name='company/index.html')


def create_company(company_name, user_object):
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


class CompanyUserFormView(View):
    form_class = CompanyUserForm
    template_name = 'company/registration.html'

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
            user_object.first_name = form.cleaned_data['first_name'].title()
            user_object.last_name = form.cleaned_data['last_name'].title()
            user_object.email = form.cleaned_data['email'].lower()
            company_name = form.cleaned_data['company_name']

            user_object.set_password(password)
            user_object.save()

            # Create user profile
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            # Create Company
            company = create_company(company_name, user_object)

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
    template_name = 'company/company_profile_detail.html'
    context_object_name = 'company'
    slug_url_kwarg = 'company_slug'


class CompanyProfileUpdateView(generic.UpdateView):
    model = Company
    template_name = 'company/company_profile_update.html'
    fields = ['logo', 'name', 'description', 'sector', 'size', 'website']
    slug_url_kwarg = 'company_slug'


class JobListView(generic.ListView):
    model = Job
    template_name = 'job/job_list.html'
    context_object_name = 'jobs_list'
    slug_url_kwarg = 'company_slug'

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.profile.company.id).order_by('start_date')


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'job/job_detail.html'
    context_object_name = 'job'
    slug_url_kwarg = 'company_slug'

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.profile.company.id)


class JobCreateView(generic.CreateView):
    model = Job
    template_name = 'job/job_create.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'start_date', 'applications_process']
    slug_url_kwarg = 'company_slug'

    def form_valid(self, form):
        form.instance.company = self.request.user.profile.company
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(generic.UpdateView):
    model = Job
    template_name = 'job/job_update.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'start_date', 'applications_process']
    slug_url_kwarg = 'company_slug'


class JobDeleteView(generic.DeleteView):
    model = Job
    template_name = 'job/job_delete.html'
    context_object_name = 'job'
    slug_url_kwarg = 'company_slug'

    def get_success_url(self):
        return reverse_lazy('company-job-list', kwargs={'pk': self.request.user.profile.company.id})


class FormsetMixin(object):
    object = None

    def get(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        if getattr(self, 'is_update_view', False):
            self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset_class = self.get_formset_class()
        formset = self.get_formset(formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def get_formset_class(self):
        return self.formset_class

    def get_formset(self, formset_class):
        return formset_class(**self.get_formset_kwargs())

    def get_formset_kwargs(self):
        kwargs = {
            'instance': self.object
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return redirect(self.object.get_absolute_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ApplicationProcessView(generic.ListView):
    model = ApplicationProcess
    template_name = 'application_process/application_process_list.html'
    context_object_name = 'application_process_list'

    def get_queryset(self):
        return ApplicationProcess.objects.filter(company=self.request.user.profile.company.id)


class ApplicationProcessCreateView(FormsetMixin, generic.CreateView):
    form_class = ApplicationProcessForm
    formset_class = ApplicationElementFormSet
    model = ApplicationProcess
    template_name = 'application_process/application_process_form.html'

    def get_success_url(self):
        return reverse_lazy('company-application-process-list', kwargs={'pk': self.request.user.profile.company.id})


class ApplicationProcessUpdateView(generic.UpdateView):
    form_class = ApplicationProcessForm
    formset_class = ApplicationElementFormSet
    model = ApplicationProcess
    is_update_view = True
    template_name = 'application_process/application_process_form.html'

    def get_success_url(self):
        return reverse_lazy('company-application-process-list', kwargs={'pk': self.request.user.profile.company.id})



class ApplicationProcessDeleteView(generic.DeleteView):
    model = ApplicationProcess
    template_name = 'application_process/application_process_delete.html'
    context_object_name = 'application_process'

    def get_success_url(self):
        return reverse_lazy('company-application-process-list', kwargs={'pk': self.request.user.profile.company.id})
