from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from company.models import Job
from .forms import UserForm
from .models import Profile


class UserFormView(View):
    form_class = UserForm
    template_name = 'user/registration.html'

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
            user.set_password(password)
            user.save()

            # Create user profile
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            profile = Profile()
            profile.gender = gender
            profile.birthday = birthday
            profile.user = user
            profile.save()

            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'user/profile.html'
    context_object_name = 'profile'


class ProfileEdit(generic.UpdateView):
    model = Profile
    template_name = 'user/form.html'
    fields = ['gender', 'birthday', 'company']


class JobListView(generic.ListView):
    model = Job
    template_name = 'user/job_list.html'
    context_object_name = 'job_list'


class JobDetailView(generic.DetailView):
    model = Job
    template_name = 'user/job_detail.html'
    context_object_name = 'job'


def apply_for_job(request, pk):
    if request.method == 'POST':
        job = Job.objects.get(pk=pk)
        if not job.applications.filter(pk=request.user.id).exists():
            job.applications.add(request.user)
        return HttpResponseRedirect(reverse_lazy('user-job-list'))
    else:
        return HttpResponse(request)
