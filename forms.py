'''
Created on 21-Jun-2017

@author: BALASUBRAMANIAM
'''
from django import forms

class RouterForm(forms.Form):
   router_name=forms.CharField(label="Router Name",max_length=25,min_length=5)
   router_ipAddress=forms.CharField(label="IP Address",max_length=25,min_length=16)