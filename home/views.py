from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from . import forms


def indexView(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    return render(request, "index.html")


def registerView(request):
    form = forms.UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            try:
                User.objects.get(email=obj.email)
                messages.add_message(
                    request, messages.WARNING, 'Account already exists with this email!')
            except User.DoesNotExist:
                obj.username = obj.email
                obj.set_password(obj.password)
                obj.save()

                login(request, obj)
                return redirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid request! Please try again.")

    return render(request, 'register.html')


def loginView(request):
    if request.method == 'POST':
        try:
            if not request.POST['email']:
                messages.add_message(request, messages.WARNING,
                                     'Please enter the email')

            if not request.POST['password']:
                messages.add_message(request, messages.WARNING,
                                     'Please enter the password')

            if request.POST['email'] and request.POST['password']:
                user = User.objects.get(email=request.POST['email'])
                if user.check_password(request.POST['password']):
                    login(request, user)
                    return redirect(reverse('home'))

        except Exception:
            messages.add_message(request, messages.ERROR,
                                 'Something went wrong! Please try again.')

    return render(request, 'login.html')


class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'


@login_required
def homeView(request):
    return render(request, "home.html")


@login_required
def captureView(request):
    return render(request, "capture.html")


@login_required
def profileView(request):
    if request.method == 'POST':
        if request.POST['first_name']:
            request.user.first_name = request.POST['first_name']

        if request.POST['last_name']:
            request.user.last_name = request.POST['last_name']

        request.user.save()

    return render(request, "profile.html")
