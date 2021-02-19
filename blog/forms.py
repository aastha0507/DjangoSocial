from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':10}))
    class Meta: 
        model = Post
        fields = ['content', 'pic']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
