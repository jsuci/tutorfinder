from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form):
        data = form.cleaned_data

        # declare all fields used here 
        user.username = data['username']
        user.email = data['email']
        user.user_type = data['user_type']


        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
            
        self.populate_username(request, user)

        user.save()
        return user