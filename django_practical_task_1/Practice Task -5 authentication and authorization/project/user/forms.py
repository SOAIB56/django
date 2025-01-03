from django import forms 


from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm, SetPasswordForm




from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length = 50)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UpdateProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    
# There is no need to logout