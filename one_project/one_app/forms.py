from django import forms
from django.core import validators
from one_app.models import Users as UserModel, UserProfileInfo
from django.contrib.auth.models import User


# you can define custom validators.
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name should start with z")

class UserForm(forms.Form):
    #first_name = forms.CharField(validators=[check_for_z])
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField() #(widget=forms.Textarea)
    verify_email = forms.EmailField(label="Enter you email again:")
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)]
    )

    #to get all clean data.
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make suer email match!")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #
    #     return botcatcher


# Model form, another way to bind form to a model
class UserModelForm(forms.ModelForm):
    #fields will be here if you want extra validation etc.
    class Meta:
        model  = UserModel
        fields = '__all__'
      #  fields = ['first_name', 'last_name' , 'email']
      #  fields = ('first_name', 'last_name')
      #  exclude= ['first_name', 'email']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields= ("username", "email", "password")

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ["profile_pic", "portfolio_site"]