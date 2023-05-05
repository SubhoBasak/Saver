from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpRequest
from django.utils import timezone
from .models import IncidentModel
from . import forms
import datetime


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
                else:
                    messages.error(request, "You entered a wrong password!")
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR,
                                 'No user found with this email!')
        except Exception as e:
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
    if request.method == 'POST':
        tmp = IncidentModel.objects.filter(
            user=request.user).order_by('-id').last()

        if tmp and tmp.date_time <= (timezone.now() - datetime.timedelta(minutes=10)):
            messages.warning(
                request, "You have to wait 10min before reporting another incident!")
            return redirect(reverse("home"))

        inc = IncidentModel()

        inc.user = request.user
        inc.image = request.POST['img']

        inc.save()

        return render(request, 'details.html', {'iid': inc.id})

    return render(request, "capture.html")


@login_required
def detailView(request):
    if request.method == 'POST':
        if 'del-iid' in request.POST:
            inc = IncidentModel.objects.get(id=request.POST['del-iid'])
            inc.delete()
        else:
            inc = IncidentModel.objects.get(id=request.POST['iid'])

            inc.title = request.POST['title']
            inc.type = int(request.POST['type'])
            inc.location = request.POST['location']
            inc.details = request.POST['details']

            inc.save()

            messages.success(
                request, 'Incident report submitted successfully!')

    return redirect(reverse('home'))


@login_required
def profileView(request):
    if request.method == 'POST':
        if request.POST['first_name']:
            request.user.first_name = request.POST['first_name']

        if request.POST['last_name']:
            request.user.last_name = request.POST['last_name']

        request.user.save()

    return render(request, "profile.html")


@login_required
def changePasswordView(request: HttpRequest):
    if request.method == 'POST':
        if request.user.check_password(request.POST['old']):
            if request.POST['new1'] == request.POST['new2']:
                if request.POST['new1'] != request.POST['old']:
                    request.user.set_password(request.POST['new1'])
                    request.user.save()

                    messages.success(request, "Password changed successfully!")
                    return redirect(reverse("profile"))
                else:
                    messages.error(
                        request, "New & old password can't be same!")
            else:
                messages.error(request, 'New passwords doesn\'t match!')
        else:
            messages.error(request, 'Old password doesn\'t match!')

    return render(request, 'password.html')


@login_required
def incidentsView(request: HttpRequest):
    incidents = IncidentModel.objects.filter(user=request.user).order_by('-id')

    return render(request, 'incidents.html', {'incidents': incidents})


@login_required
def reportView(request: HttpRequest, iid):
    try:
        incident = IncidentModel.objects.get(id=iid)

        gps = False

        if incident.location != None and incident.location.startswith("[::GPS::]"):
            loc = incident.location[9:]
            loc = loc.split('|')

            gps = f'https://www.google.com/maps/@{loc[0]},{loc[1]},18z'

        return render(request, 'view.html', {'incident': incident, 'gps': gps})
    except IncidentModel.DoesNotExist:
        return redirect(reverse("home"))
