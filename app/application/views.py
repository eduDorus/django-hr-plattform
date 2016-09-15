from company.models import Company
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import ProcessForm
from .models import Process


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
        process = form.save(commit=False)
        company_id = self.request.user.profile.company.id
        process.company = Company.objects.get(id=company_id)
        process.save()

        self.object = process
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProcessView(generic.ListView):
    model = Process
    template_name = 'application/process_list.html'
    context_object_name = 'process_list'
    slug_url_kwarg = 'company_slug'

    def get_queryset(self):
        return Process.objects.filter(company=self.request.user.profile.company.id)


class ApplicationProcessCreateView(FormsetMixin, generic.CreateView):
    form_class = ProcessForm
    formset_class = QueueFormSet
    model = Process
    template_name = 'application/process_form.html'
    slug_url_kwarg = 'company_slug'

    def get_success_url(self):
        return reverse_lazy('application-process-list', kwargs={'company_slug': self.request.user.profile.company.slug})


class ApplicationProcessUpdateView(FormsetMixin, generic.UpdateView):
    form_class = ProcessForm
    formset_class = QueueFormSet
    model = Process
    is_update_view = True
    template_name = 'application/process_form.html'
    slug_url_kwarg = 'company_slug'

    def get_success_url(self):
        return reverse_lazy('application-process-list', kwargs={'company_slug': self.request.user.profile.company.slug})


class ApplicationProcessDeleteView(generic.DeleteView):
    model = Process
    template_name = 'application/process_delete.html'
    context_object_name = 'process'
    slug_url_kwarg = 'company_slug'

    def get_success_url(self):
        return reverse_lazy('application-process-list', kwargs={'company_slug': self.request.user.profile.company.slug})
