from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'logout$', views.logout_view, name='logout'),
    url(r'about$', views.about, name='about'),
    url(r'work$', views.work, name='work'),
]
