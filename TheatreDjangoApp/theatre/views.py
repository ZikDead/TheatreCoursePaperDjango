import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import EventList
from .forms import LogInForm
from django.template import loader


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


@login_required(login_url='/')
def load_performances(request):
    date = request.POST.get('date')
    events = EventList.objects.filter(date=date)
    return render(request, 'ajax-work-eventlist.html', {'events': events})


@login_required(login_url='/')
def load_performance(request):
    id_event = request.POST.get('id')
    try:
        id_event = int(id_event)
    except ValueError:
        return Http404('Wrong id')
    event = EventList.objects.get(id=id_event)

    html = loader.get_template('hall-%d.html' % event.hall.number_of_hall)
    html = html.render({}, request)
    return HttpResponse(json.dumps({'html': html, 'json': event.place,
                                    'cost': float(event.performance.cost_of_ticket)}), content_type="application/json")


@login_required(login_url='/')
def save_performance(request):
    id_event = request.POST.get('id')
    try:
        id_event = int(id_event)
    except ValueError:
        return Http404('Wrong id')
    event = EventList.objects.get(id=id_event)
    event.place = request.POST.get('json')
    event.save()
    return HttpResponse(request.POST)