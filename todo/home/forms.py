from django import forms
from django.db.models import fields
from .models import Task

#creating a form
class TaskForm(forms.ModelForm):
    # creating meta class
    class Meta:
        #specify model to be used
        model = Task

        #specify feilds to be used
        fields = ["user","taskTitle","taskDesc"]