from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import EventList
from .forms import LogInForm


def home(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = form.auth()
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LogInForm()
    return render(request, 'home.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@require_GET
def about(request):
    form = LogInForm()
    return render(request, 'about.html', {'form': form})


@login_required(login_url='/')
def work(request):
    weekdays = EventList.get_last_days(10)
    return render(request, 'work.html', {'weekdays': weekdays})


def load_performance(request):
    date = request.POST.get('date')
    events = EventList.objects.filter(date=date)
    return render(request, 'ajax-work-eventlist.html', {'events': events})
