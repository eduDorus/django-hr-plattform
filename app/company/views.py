from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from user.models import Profile
from application.models import Process, Queue

from .forms import CompanyUserForm, JobModelForm
from .models import Company, Job


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
        application_process = Process(name='default', company=company)
        application_process.save()

        # Create default application elements
        Queue(name='Application Inbox', position=1, description='default', process=application_process).save()
        Queue(name='Telefon Screening', position=2, description='default', process=application_process).save()
        Queue(name='Interview', position=3, description='default', process=application_process).save()
        Queue(name='Sign Contract', position=4, description='default', process=application_process).save()

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
    form_class = JobModelForm
    template_name = 'job/job_create.html'
    slug_url_kwarg = 'company_slug'

    def form_valid(self, form):
        form.instance.company = self.request.user.profile.company
        return super(JobCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(JobCreateView, self).get_form_kwargs()
        kwargs.update({'company': self.request.user.profile.company})
        return kwargs


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
        return reverse_lazy('company-job-list', kwargs={'company_slug': self.request.user.profile.company.slug})
