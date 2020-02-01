from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import User

#Creation Form
#users/artist
class UserCreateForm(UserCreationForm):
    class Meta:
        # fields = ( "first_name", "last_name", "display_name","email","password1", "password2", "is_artist", "is_nonprofit")
        fields = ( "first_name", "last_name", "display_name","email","password1", "password2" )

        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label= 'First Name'
        self.fields['last_name'].label= 'Last Name'
        self.fields['email'].label = "Email Address"
        # self.fields['is_artist'].label= 'Are you an Artist?'
        # self.fields['is_nonprofit'].label= 'Are you a nonprofit?'

#organization create form
class organizationCreateForm(UserCreateForm):
    class Meta(UserCreateForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_nonprofit = True
        if commit:
            user.save()
        return user

#artist create form
class artistCreateForm(UserCreateForm):
    class Meta(UserCreateForm.Meta):
        model= User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_artist = True
        if commit:
            user.save()
        return user

#Edit Forms
#users/artists
class UserEditForm(UserChangeForm):

    class Meta:
      model = User
      fields = ( "first_name", "last_name", "display_name","email", "profile_pic")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
