from __future__ import unicode_literals

from django.db import models

# Create your models here.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

import socket
import time

##This is the command function for inner arduino
innerhost = "192.168.0.105"
innerport = 6100

def TellInnerArduino(command):
    s = socket.socket()
    s.connect((innerhost , innerport))
    command += "\n"
    s.send(command)
    time.sleep(0.05)
    data = s.recv(1024)
    s.close()
    return str(data)


###All the Instanes of this model are having the name in this pattern ([A-Z][a-z]+)
class Appliance(models.Model):
    Name = models.CharField(max_length=25)
    
    Pin = models.IntegerField(default=0)
    
    Type = models.CharField(max_length=11, default = 'USUALLY_OFF')
            
    state = models.CharField(max_length=3, default = 'OFF')
            
    def __unicode__(self):
        return self.Name + "     state = " + self.state
    def __str__(self):
        return self.Name + "     state = " + self.state


    def setup(self):
        if self.Type == 'USUALLY_OFF':
            if self.state:
                GPIO.setup(self.Pin,GPIO.IN)
            else:
                GPIO.setup(self.Pin,GPIO.OUT)
        if self.Type == 'USUALLY_ON':
            if self.state:
                GPIO.setup(self.Pin,GPIO.OUT)
            else:
                GPIO.setup(self.Pin,GPIO.IN)
    def turnon(self):
        if self.Type == 'USUALLY_ON':
            GPIO.setup(self.Pin,GPIO.IN)
        if self.Type == 'USUALLY_OFF':
            GPIO.setup(self.Pin,GPIO.OUT)
        if self.Type == 'InnerRoom':
            command = str(self.Name) + "ON"
            TellInnerArduino(command)
        if self.Type == 'OuterRoom':
            GPIO.setup(self.Pin,GPIO.OUT)
    def turnoff(self):
        if self.Type == 'USUALLY_ON':
            GPIO.setup(self.Pin,GPIO.OUT)
        if self.Type == 'USUALLY_OFF':
            GPIO.setup(self.Pin,GPIO.IN)
        if self.Type == 'InnerRoom':
            command = str(self.Name) + "OFF"
            TellInnerArduino(command)
            
        
