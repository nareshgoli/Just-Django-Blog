from django import forms

from .models import Post

#class PostForm(forms.Form):
 #   title = forms.CharField()
  #  description = forms.CharField()
   # image = forms.CharField()



class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','author','image']    