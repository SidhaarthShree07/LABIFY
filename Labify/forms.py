from django import forms
from myapp.models import Post , Posting

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = "__all__"
        
class PostForming(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['user', 'text']
        widgets = {
            'post': forms.HiddenInput(),
            'time': forms.HiddenInput(),# Hide the post field in the form
        }

