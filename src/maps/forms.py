from django.contrib.auth.models import User, Group, Permission
from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

#from django.allauth.accounts.adapter import clean_email

ORGANIZATION = (
  ('', '--Select Organization--'),
  ('KH', 'Cambodia'),
  ('EC', 'Ecuador'),
  ('HN', 'Honduras'),
  ('KE', 'Kenya'),
  ('MM', 'Myanmar'),
  ('PH', 'Philippines'),
  ('LK', 'Sri Lanka'),
  ('TZ', 'Tanzania'),
  ('UG', 'Ugnada'),
  ('ZM', 'Zambia'),
  ('VFI', 'VisionFund International'),
  ('AFR', 'Africa Regional'),
  ('ASR', 'Asia Regional'),
  ('LAR', 'Latin America Regional'),
)


class email_adapter(DefaultAccountAdapter):
    def clean_email(self, email):
        domain = email.split('@')[1].lower()     
        allowed_emails = ['wvi.org', 'vfi.org', 'globalparametrics.com']
        if domain not in allowed_emails:
            raise forms.ValidationError("You must use a WorldVision or VisionFund email address")
        return email

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True,     widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    
    last_name = forms.CharField(max_length=30, label='Last Name', required=True,         widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    
    organization = forms.ChoiceField(choices=ORGANIZATION, required=True)

      
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'organization']

        
    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.organization = self.cleaned_data['organization']
        user.profile.save()
        
        group = Group.objects.get(name = user.profile.organization)
#        permissions = Permission.objects.get(name = 'KE')
        print(group)
#        print(type(group))
#        user.user_permissions.set(['KE'])
#        user.user_permissions.add(0)

#        print(group.permissions)
#        permission = Permission.objects.get(name = group)
#        print(permission)
#        group.permissions.set(permission)
        user.groups.add(group)
        



        
        