from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from .forms import UserForm
from .models import Profile, Education, Experience, Language, Skill
from application.models import Application
from company.models import Job


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

            user_object = form.save(commit=False)

            # Clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user_object.first_name = form.cleaned_data['first_name'].title()
            user_object.last_name = form.cleaned_data['last_name'].title()
            user_object.email = form.cleaned_data['email'].lower()
            user_object.set_password(password)
            user_object.save()

            # Create user profile
            gender = form.cleaned_data['gender']
            birthday = form.cleaned_data['birthday']

            profile = Profile()
            profile.gender = gender
            profile.birthday = birthday
            profile.user = user_object
            profile.save()

            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs.get('username'))
        return Profile.objects.get(user=user)


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = 'user/profile_update.html'
    fields = ['avatar', 'motivation', 'gender', 'birthday', 'company']
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs.get('username'))
        return Profile.objects.get(user=user)


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
        job = Job.objects.get(id=pk)
        if not Application.objects.filter(user=request.user.id, job=job).exists():
            application_object = Application(user=request.user, job=job, queue=job.applications_process.queue_set.get(position=1))
            application_object.save()
        return HttpResponseRedirect(reverse_lazy('user-job-list'))
    else:
        return HttpResponse(request)


class CVView(generic.TemplateView):
    template_name = 'cv/cv.html'
    context_object_name = 'cv_data_list'

    def get_context_data(self, **kwargs):
        context = super(CVView, self).get_context_data(**kwargs)
        context['education_list'] = Education.objects.filter(user=self.request.user)
        context['experience_list'] = Experience.objects.filter(user=self.request.user)
        context['skill_list'] = Skill.objects.filter(user=self.request.user)
        context['language_list'] = Language.objects.filter(user=self.request.user)
        return context


class EducationCreateView(generic.CreateView):
    model = Education
    template_name = 'cv/cv_form.html'
    fields = ['title', 'academic_level', 'specialization', 'school_name', 'graduate_year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationCreateView, self).form_valid(form)


class EducationUpdateView(generic.UpdateView):
    model = Education
    template_name = 'cv/cv_form.html'
    fields = ['title', 'academic_level', 'specialization', 'school_name', 'graduate_year']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(EducationUpdateView, self).dispatch(request, *args, **kwargs)


class EducationDeleteView(generic.DeleteView):
    model = Education
    template_name = 'cv/education_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(EducationDeleteView, self).dispatch(request, *args, **kwargs)


class ExperienceCreateView(generic.CreateView):
    model = Experience
    template_name = 'cv/cv_form.html'
    fields = ['title', 'position', 'employment_type', 'employer', 'start_date', 'end_date', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExperienceCreateView, self).form_valid(form)


class ExperienceUpdateView(generic.UpdateView):
    model = Experience
    template_name = 'cv/cv_form.html'
    fields = ['title', 'position', 'employment_type', 'employer', 'start_date', 'end_date', 'description']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(ExperienceUpdateView, self).dispatch(request, *args, **kwargs)


class ExperienceDeleteView(generic.DeleteView):
    model = Experience
    template_name = 'cv/experience_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(ExperienceDeleteView, self).dispatch(request, *args, **kwargs)


class SkillListView(generic.ListView):
    model = Skill
    context_object_name = 'user-skill_list'


class SkillCreateView(generic.CreateView):
    model = Skill
    template_name = 'cv/cv_form.html'
    fields = ['name', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillCreateView, self).form_valid(form)


class SkillUpdateView(generic.UpdateView):
    model = Skill
    template_name = 'cv/cv_form.html'
    fields = ['name', 'level']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(SkillUpdateView, self).dispatch(request, *args, **kwargs)


class SkillDeleteView(generic.DeleteView):
    model = Skill
    template_name = 'cv/skill_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(SkillDeleteView, self).dispatch(request, *args, **kwargs)


class LanguageListView(generic.ListView):
    model = Language
    context_object_name = 'user-language_list'


class LanguageCreateView(generic.CreateView):
    model = Language
    template_name = 'cv/cv_form.html'
    fields = ['language', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LanguageCreateView, self).form_valid(form)


class LanguageUpdateView(generic.UpdateView):
    model = Language
    template_name = 'cv/cv_form.html'
    fields = ['language', 'level']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(LanguageUpdateView, self).dispatch(request, *args, **kwargs)


class LanguageDeleteView(generic.DeleteView):
    model = Language
    template_name = 'cv/language_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(LanguageDeleteView, self).dispatch(request, *args, **kwargs)
