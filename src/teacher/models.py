from django.db import models

# Create your models here.

class Question(models.Model):
    objects = None
    question_text = models.CharField(max_length=200)
    file = models.FileField(upload_to='lecture/', null=True)

    def __str__(self):
        return self.question_text + ": " + str(self.file)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
