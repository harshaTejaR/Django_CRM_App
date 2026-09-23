from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label = "",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), max_length=254)
    first_name = forms.CharField(Label = "",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=30)
    last_name = forms.CharField(Label = "",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Required. At least 8 characters. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
            