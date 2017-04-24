from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'logout$', views.logout_view, name='logout'),
    url(r'about$', views.about, name='about'),
    url(r'work$', views.work, name='work'),
    url(r'load_performances$', views.load_performances, name='ajax_load_performances'),
    url(r'load_performance$', views.load_performance, name='ajax_load_performance'),
    url(r'save_performance$', views.save_performance, name='ajax_save_performance'),
]

