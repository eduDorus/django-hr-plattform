from django import forms
from django.forms.models import inlineformset_factory

from .models import Process, Queue

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['name']


class QueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['name']

QueueFormSet = inlineformset_factory(Process, Queue, extra=0, min_num=1, max_num=10, fields=('name',))