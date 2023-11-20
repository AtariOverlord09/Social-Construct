from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea

from posts.models import Comment, Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text', 'group', 'image']
        widgets = {
            'text': Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'class': 'form-control',
                    'required id': 'id_text',
                }
            ),
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if not data:
            raise ValidationError('Заполните пожалуйста это поле')
        return data


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'class': 'form-control',
                    'required id': 'id_text',
                }
            ),
        }
