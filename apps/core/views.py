from django.shortcuts import render
from allauth.account.decorators import verified_email_required


def frontpage(request):
    return render(request, 'core/frontpage.html')

@verified_email_required
def dashboard(request):
    return render(request, 'core/dashboard.html')