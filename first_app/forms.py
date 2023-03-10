from django import forms
from django.core import validators
from first_app.models import User


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")


# class FormName(forms.Form):
#     # name = forms.CharField(validators=[check_for_z])
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                 widget=forms.HiddenInput,
#                                 validators=[validators.MaxLengthValidator(0)])
#
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         vmail = all_clean_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("Make Sure Email Match!")

# ModelForm used to accept input and pass it to a model.
# Here we import User model from models.py and create NewUserForm to get input and
# pass it to DB User model using Meta()
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
