from django.shortcuts import render
from allauth.account.decorators import verified_email_required


@verified_email_required
def profile(request):
    return render(request, 'profiles/profile.html')