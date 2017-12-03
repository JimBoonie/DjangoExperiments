from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    max_length = 4000
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {'rows': 5, 'placeholder': 'What is on your mind?'}
        ), 
        max_length = max_length,
        help_text = 'The max length of this text is {0}.'.format(max_length)
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']