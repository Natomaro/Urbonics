from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import sklearn_svm_load_model_and_assess

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    return render(request, 'mysite/urbonics.html')

def submit(request):
    info=request.POST['info']
    print(info)
    print(type(info))
    info_list = info.split(",")
    print(info_list)
    ph = info_list[0]
    EC = info_list[1]
    percent_light = info_list[2]
    water_level = info_list[3]
    result = sklearn_svm_load_model_and_assess.classify_plant(ph,EC,percent_light,water_level)
    print(result)
    return render(request, 'mysite/urbonics.html')
# Create your views here.
