from django.shortcuts import render
from testapp.models import *

def index(request):
    return render(request, 'testapp/index1.html')

def hydjob1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/hydjobs.html',context=my_dict)

def bangalorejob2(request):
    jobs_list=bangalorejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/bangalorejobs.html',context=my_dict)

def punejob3(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/punejobs.html',context=my_dict)

def chennaijob4(request):
    jobs_list=chennaijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request, 'testapp/chennaijobs.html',context=my_dict)
    