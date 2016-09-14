from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from company.models import Job
from .forms import UserForm
from .models import Profile, Education, Experience, Language, Skill


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


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'user/profile.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs.get('username'))
        return Profile.objects.get(user=user)


class ProfileEdit(generic.UpdateView):
    model = Profile
    template_name = 'user/form.html'
    fields = ['avatar', 'gender', 'birthday', 'company']
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
        job = Job.objects.get(pk=pk)
        if not job.applications.filter(pk=request.user.id).exists():
            job.applications.add(request.user)
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


class EducationCreate(generic.CreateView):
    model = Education
    template_name = 'cv/cv_form.html'
    fields = ['title', 'academic_level', 'specialization', 'school_name', 'graduate_year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationCreate, self).form_valid(form)


class EducationUpdate(generic.UpdateView):
    model = Education
    template_name = 'cv/cv_form.html'
    fields = ['title', 'academic_level', 'specialization', 'school_name', 'graduate_year']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(EducationUpdate, self).dispatch(request, *args, **kwargs)


class EducationDelete(generic.DeleteView):
    model = Education
    template_name = 'cv/education_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(EducationDelete, self).dispatch(request, *args, **kwargs)


class ExperienceCreate(generic.CreateView):
    model = Experience
    template_name = 'cv/cv_form.html'
    fields = ['title', 'position', 'employment_type', 'employer', 'start_date', 'end_date', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExperienceCreate, self).form_valid(form)


class ExperienceUpdate(generic.UpdateView):
    model = Experience
    template_name = 'cv/cv_form.html'
    fields = ['title', 'position', 'employment_type', 'employer', 'start_date', 'end_date', 'description']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(ExperienceUpdate, self).dispatch(request, *args, **kwargs)


class ExperienceDelete(generic.DeleteView):
    model = Experience
    template_name = 'cv/experience_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(ExperienceDelete, self).dispatch(request, *args, **kwargs)


class SkillList(generic.ListView):
    model = Skill
    context_object_name = 'user-skill_list'


class SkillCreate(generic.CreateView):
    model = Skill
    template_name = 'cv/cv_form.html'
    fields = ['name', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillCreate, self).form_valid(form)


class SkillUpdate(generic.UpdateView):
    model = Skill
    template_name = 'cv/cv_form.html'
    fields = ['name', 'level']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(SkillUpdate, self).dispatch(request, *args, **kwargs)


class SkillDelete(generic.DeleteView):
    model = Skill
    template_name = 'cv/skill_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(SkillDelete, self).dispatch(request, *args, **kwargs)


class LanguageList(generic.ListView):
    model = Language
    context_object_name = 'user-language_list'


class LanguageCreate(generic.CreateView):
    model = Language
    template_name = 'cv/cv_form.html'
    fields = ['language', 'level']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LanguageCreate, self).form_valid(form)


class LanguageUpdate(generic.UpdateView):
    model = Language
    template_name = 'cv/cv_form.html'
    fields = ['language', 'level']

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(LanguageUpdate, self).dispatch(request, *args, **kwargs)


class LanguageDelete(generic.DeleteView):
    model = Language
    template_name = 'cv/language_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user-cv-index', kwargs={'username': self.request.user.username})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().user == request.user:
            return HttpResponseForbidden()
        return super(LanguageDelete, self).dispatch(request, *args, **kwargs)
