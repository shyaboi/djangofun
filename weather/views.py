from django.shortcuts import render
from django.template import loader
import time
def index(request):
    ok = time.strftime('%X %x %Z')
    thing = {'some_kind_of_object': ok}
    return render(request, 'weather/index.html', {"thing":thing})