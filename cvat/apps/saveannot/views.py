from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from cvat.apps.authentication.decorators import login_required
from .forms import AnnotationListForm
from django.shortcuts import render_to_response
from django.template import RequestContext
import os
from . import webapis
import json
from . import annotationgenerator

@login_required
def SaveAnnotView(request):
    #annotationchoices=[(1,"One\t\t15th Jul 19"),(2,"Two\t\t1st Jun 19")] #Replace this with code that calls the API to list the (id,task)
    tasksJson=webapis.getListOfTasks()
    annotationchoices=[]
    datasubmitted=None
    
    for result in tasksJson['results']:
        thisid=result['id']
        thisname=result['name']
        thisdate=result['updated_date']
        annotationchoices.append((thisid,thisname+"\t"+thisdate))
    
    if request.method == 'GET':
       annotlistform = AnnotationListForm(choices=annotationchoices)
 
    elif request.method == 'POST':
       annotlistform = AnnotationListForm(request.POST,choices=annotationchoices)
       if annotlistform.is_valid():
          pickedtasks = annotlistform.cleaned_data.get('tasks')
          pickedformat= annotlistform.cleaned_data.get('annotationformat')


          #Insert code to generate the annotation for the selected tasks
          annotationgenerator.generateannotations(pickedtasks,pickedformat)
          #return render(request,'downloadlist/downloadlist.html',{'form':downloadlistform})  
          response = redirect('/downloadlist/')
          return response          
       else:
          print('Form not valid!')       
    
    return render(request,'saveannot/mypage.html',{'form':annotlistform, 'datasubmitted':datasubmitted})   


    
