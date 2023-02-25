from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.http import HttpResponse
import os


# Create your views here
class HomeTemplateView(TemplateView):
    template_name = "home.html"

    # overide get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["services"] = Service.objects.all()
        context["works"] = RecentWork.objects.all()
        context["clients"] = Client.objects.all()

        return context

    def post(self, request):
        if request.method == "POST":
            message = request.POST["message"]
            full_name = request.POST["name"]
            email = request.POST["email"]

            # Send inquiry mail
            mail_subject = "Codi"

        return render(request, "home.html", self.get_context_data())
