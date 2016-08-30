from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, CompanyUserForm


class UserFormView(View):
    form_class = UserForm
    template_name = 'account/registration_user.html'

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

            # authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class CompanyUserFormView(View):
    form_class = CompanyUserForm
    template_name = 'account/registration_company.html'

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
            company = form.cleaned_data['company_name']

            user.set_password(password)
            user.save()

            # authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('index')

        return render(request, self.template_name, {'form': form})
