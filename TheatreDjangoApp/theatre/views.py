from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.decorators.http import require_POST
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
            else:
                return HttpResponseRedirect('/')
    else:
        form = LogInForm()
    return render(request, 'home.html', {'form': form})


def logout_view(request):
    logout(request)
    print('kek')
    return HttpResponseRedirect('/')


# @require_POST
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Правильный пароль и пользователь "активен"
#         auth.login(request, user)
#         # Перенаправление на "правильную" страницу
#         return HttpResponseRedirect("/account/loggedin/")
#     else:
#         # Отображение страницы с ошибкой
#         return HttpResponseRedirect("/account/invalid/")