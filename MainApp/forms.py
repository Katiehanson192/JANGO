from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm): #this lets users enter texts from their side of the website 
    class Meta: #sub class since we want to save this information directly to the website
        model = Topic
        fields = ['text']
        labels = {'text':''}


class EntryForm(forms.ModelForm): #this lets users enter texts from their side of the website 
    class Meta: #sub class since we want to save this information directly to the website
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}