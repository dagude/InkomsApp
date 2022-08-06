from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndustryView(TemplateView):
   template_name = 'industry.html'