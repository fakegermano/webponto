from django import forms
from django.contrib.auth.models import User

# app's forms go in here
from accounts.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('ra',)

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        try:
            int_ra = int(self.ra)
            self.ra = str(int_ra)
        except (SyntaxError, ValueError) as e:
            raise forms.ValidationError('RA invalido', code='invalid')
        finally:
            return cleaned_data
