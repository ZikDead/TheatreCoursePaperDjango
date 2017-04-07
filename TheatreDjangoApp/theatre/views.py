from django.shortcuts import render
from django.http import HttpResponse

#from django.views.decorators.http import require_POST
#from django.core.urlresolvers import reverse
# reverse ('name_of_url', args(10,), kwargs = {'pk':7})


def home(request):
    return HttpResponse("Hello, fucking world.")

