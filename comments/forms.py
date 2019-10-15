
from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        """form settings"""
        #model = Comment
        #fields = ('user','comments',)