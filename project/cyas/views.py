from django.shortcuts import render
from django.views.generic import CreateView
from .models import Survey

class SurveyCreateView(CreateView):
    model = Survey
    fields = "__all__"
    success_url = "/thanks"

