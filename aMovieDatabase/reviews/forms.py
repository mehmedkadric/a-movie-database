from django import forms
from .models import Reviewinfo

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.title = kwargs.pop('title', None)
        self.username = kwargs.pop('username', '')
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = self.title
        self.fields['title'].widget = forms.HiddenInput()
        self.fields['author'].initial = self.username
        self.fields['author'].widget.attrs['readonly'] = True

    class Meta:
        model = Reviewinfo
        fields = ['title', 'author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
        required = {
            'author': False
        }
