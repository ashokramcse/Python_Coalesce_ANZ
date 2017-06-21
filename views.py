from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .forms import RouterForm
# Create your views here.
def home(request):
    message="<h1 align='center' style='color:blue'>Welcome to ANZ Lab</h1>"
    return HttpResponse(message)
    
def routerData(request):
    if request.method == 'POST':
        form = RouterForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #print("hello")
            global rname,rip 
            rname = form.cleaned_data['router_name']
            rip=form.cleaned_data['router_ipAddress']
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RouterForm()

    return render(request, 'name.html', {'form': form})