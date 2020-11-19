from django import forms

from teacher.models import Question

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField( help_text='Required. Add a valid email address.')

    class Meta:
        model = Question
        fields = ('question_text', 'file',)