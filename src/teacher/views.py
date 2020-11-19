from django.shortcuts import render, redirect
from teacher.form import QuestionForm
from teacher.models import Question
from django.core.files.storage import FileSystemStorage
# Create your views here.

# Dashboard view
def dashboard(request):
    context = {}
    context['questions'] = Question.objects.all()
    return render(request, 'dashboard.html', context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'lecture_add.html')

# Adding lecture and redirect
def lectureAdd(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lecture')
    else:
        return render(request, 'lecture_add.html', {})

# Showing lecture list
def lectureList(request):
    context = {}
    context['items'] = Question.objects.all()
    return render(request, 'lecture_list.html', context)
