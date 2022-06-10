from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, AddEmailForm
from django import forms


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input mb-3'
            })

class CustomSignUpForm(SignupForm):
    # set custom fields here
    USER_TYPE_CHOICES = [
        ('STUDENT', 'Student'),
        ('TEACHER', 'Teacher')
    ]

    user_type = forms.CharField(label='Account Type', widget=forms.Select(choices=USER_TYPE_CHOICES))

    # set default styling once form is loaded
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input mb-3'
            })


    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)

        # assign custom fields
        user.user_type = self.cleaned_data['user_type']

        # save return user
        user.save()
        return user

class CustomResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input mb-3'
            })


class CustomAddEmailForm(AddEmailForm):

    def __init__(self, *args, **kwargs):
        super(CustomAddEmailForm, self).__init__(*args, **kwargs)

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input mb-3'
            })

