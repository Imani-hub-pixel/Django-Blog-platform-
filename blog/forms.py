from django import forms
from .models import Post, Comment   

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your comment here...'}),
        }
        labels = {
            'content': 'Comment',
        }
        