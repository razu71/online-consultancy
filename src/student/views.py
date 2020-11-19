from django.shortcuts import render
from teacher.models import Question
# Create your views here.

def home(request):
    context = {}
    context['items'] = Question.objects.all()
    return render(request, 'home.html', context)