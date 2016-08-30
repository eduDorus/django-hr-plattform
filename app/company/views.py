from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CompanyUserForm
from .models import Company


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

            # authenticate user
            user = authenticate(username=username, password=password)

            # company logic
            try:
                company = Company.objects.get(name=company_name)
                company.permission_requests.add(user)
            except Company.DoesNotExist:
                company = Company(name=company_name)
                company.save()
                company.admins.add(user)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})
