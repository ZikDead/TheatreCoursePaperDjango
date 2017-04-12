from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from .forms import LogInForm
from django.contrib.auth import login, logout

#from django.core.urlresolvers import reverse
# reverse ('name_of_url', args(10,), kwargs = {'pk':7})


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
    return  render(request, 'work.html')