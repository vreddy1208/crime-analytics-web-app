from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.utils import timezone
from updates.forms import Postform


# Create your views here.
def port(request):
    return render(request, 'pst.html')

def add_model(request):

    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            if hasattr(model_instance, 'timestamp'):
                model_instance.timestamp = timezone.now(auto_now_add=True)
            model_instance.save()
            return redirect('/updates')
        else:
            # If the form is invalid, re-render the form with error messages
            return render(request, "add.html", {'form': form})


    else:

        form = Postform()

        return render(request, "add.html", {'form': form})

