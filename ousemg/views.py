from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import InternForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import requests 

def HomeView(request):
    form = InternForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        subject = 'Intern Signup Request'
        message = '%s would like to Signup for the OUSEMG internship program ' % instance.email
        from_email = instance.email
        to_email = settings.EMAIL_HOST_USER

        print('from %s' % from_email)
        print('to %s' % to_email)

        def send_simple_message():
            return requests.post(
                "https://api.mailgun.net/v3/sandbox96030f4f31da4080ae7a462b835ad414.mailgun.org",
                auth=("api", "key-5fec34b1d872aa8e6dad3368d540dfc1"),
                data={
                    "from": "<mailgun@OUSEMG>",
                    "to": [to_email, "marcus.yeagle@gmail.com"],
                    "subject": subject,
                    "text": message
                })


        send_simple_message()
        messages.success(request, "Sucessfully Sent Email!")
        
    context = {
        "form":form,
    }

    return render(request, "index.html", context) 

class AboutView(TemplateView):
    template_name = "about.html"


class PerformanceView(TemplateView):
    template_name = "performance.html"
