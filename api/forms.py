from .models import UserInfo
from .models import Posts
from django import forms


#A form for user registration
class UserRegistrationForm(forms.Form):

    name = forms.CharField(max_length = 50)
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50,widget = forms.PasswordInput())

    def save(self, commit=False):
        user = UserInfo.objects.create(
             name=self.cleaned_data['name'],
             username=self.cleaned_data['username'],
             password=self.cleaned_data['password']
        )
        return user
class PostForm(forms.Form):
    title =  forms.CharField(max_length = 100)
    content = forms.CharField(widget=forms.Textarea)   
#class UsersToFollow(forms.Form):
    #users = forms.ModelMultipleChoiceField(queryset=UserInfo.objects.all()['username'])
    