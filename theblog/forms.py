from django import forms
from .models import Post , Category , Comment

# choices = [('Coding' , 'Coding') , ('Entertainment' , 'Entertainment') , ('Sports' , 'Sports') , ('Education' , 'Education') , ('Gaming' , 'Gaming')]
choices = Category.objects.all().values_list('name' , 'name')
choices_list = [

]

for item in choices:
    choices_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' 

        widgets = {
            'tittle':forms.TextInput(attrs={'class':'form-control'}),
            'tittle_tag':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_list ,attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['tittle', 'tittle_tag' , 'body'] 

        widgets = {
            'tittle':forms.TextInput(attrs={'class':'form-control'}),
            'tittle_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'comment' : forms.TextInput(attrs={'class':'form-control'}),
        }