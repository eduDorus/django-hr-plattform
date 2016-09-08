from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from .forms import CompanyUserForm
from .models import Company, Job


# Create your views here.
def hello_world(request):
    return render(request, template_name='company/index.html')


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

            user = form.save(commit=False)

            # Clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            company_name = form.cleaned_data['company_name']

            user.set_password(password)
            user.save()

            # Create user profile
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            profile = user.models.Profile()
            profile.gender = gender
            profile.birthday = birthday
            profile.user = user
            profile.save()

            # authenticate user
            user = authenticate(username=username, password=password)

            # company logic
            try:
                company = Company.objects.get(name=company_name)
                company.permission_requests.add(user)
            except Company.DoesNotExist:
                company = Company(name=company_name)
                company.save()
                profile.company = company

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class CompanyProfileDetailView(generic.DetailView):
    model = Company
    template_name = 'company/profile.html'
    context_object_name = 'company'


class CompanyProfileUpdateView(generic.UpdateView):
    model = Company
    template_name = 'company/form.html'
    fields = ['name', 'description', 'sector', 'size', 'website']


class JobListView(generic.ListView):
    model = Job
    template_name = 'company/job_list.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user.profile.company.id)


class JobCreateView(generic.CreateView):
    model = Job
    template_name = 'company/job_create.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'office']

    def form_valid(self, form):
        form.instance.company = self.request.user.profile.company
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(generic.UpdateView):
    model = Job
    template_name = 'company/job_update.html'
    fields = ['title', 'description', 'employment_grade', 'min_degree', 'office']
