# from django.core import validators
# from django import forms


# class StudentRegistration(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     first_name = forms.CharField(label='First Name')
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

# def clean(self):
#     cleaned_data = super().clean()
#     pas = self.cleaned_data['password']
#     cpas = self.cleaned_data['confirm_password']
#     if pas != cpas:
#         raise forms.ValidationError("Passwords do not match.")

from django import forms


class StudentRegistration(forms.Form):
    error_css_class = 'error'
    required_css_class ='required'
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    # first_name = forms.CharField(label='First Name')
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pas = cleaned_data.get('password')  # Use `get` to avoid KeyError
        cpas = cleaned_data.get('confirm_password')
        if pas and cpas and pas != cpas:  # Ensure both fields are present
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
