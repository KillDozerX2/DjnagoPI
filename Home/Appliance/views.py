from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.renderers import JSONRenderer
from .models import Appliance
from .serializers import ApplianceSerializer
from django.http import HttpResponseRedirect,HttpResponse
import os
# Create your views here.

### This is for the app!

###All the Instanes of Appliance model are having the name in this pattern ([A-Z][a-z]+)
###I have used only get methods to handle the request from the app

#This class handles the part where application asks for state of appliance
class ApplianceList(APIView):
    def get(self, request,appliance_name):
        if appliance_name == "All":
            Appli = Appliance.objects.all()
            serializer = ApplianceSerializer(Appli,many=True)
        else:
            Appli = Appliance.objects.get(Name=appliance_name)
            serializer = ApplianceSerializer(Appli)
        return Response(serializer.data)


###This will handle turning on or off of the appliance
def StateHandler(request,name_of_appliance,command):
    subject = Appliance.objects.get(Name=name_of_appliance)
    if (command == 'turnon'):
        subject.state = 'ON'
        subject.turnon()
        subject.save()
        return HttpResponse(str(name_of_appliance) + " has been turned "+"on")
    if (command == 'turnoff'):
        subject.state = 'OFF'
        subject.turnoff()
        subject.save()
        return HttpResponse(str(name_of_appliance) + " has been turned " + "off")




###This is the web part!!!!It has nothing to do with android app
###But we will be taking inspiration from this
def home(request):
    queryset = Appliance.objects.all()
    context = {
        'Appliances' : queryset,
    }
    if request.method == "POST":
        subject = Appliance.objects.get(Name = request.POST.get('appliance'))
        desired_state = request.POST.get('state')
        if (desired_state == 'on'):
            subject.state = 'ON'
            subject.turnon()
            subject.save()
        
        if (desired_state == None):
            subject.state = 'OFF'
            subject.turnoff()
            subject.save()
        redirect("/")
    return render(request, 'Homepage.html',context)
