from django.shortcuts import render, redirect
from allauth.account.decorators import verified_email_required


def frontpage(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    else:
        return render(request, 'core/frontpage.html')

@verified_email_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


@verified_email_required
def profile(request):
    return render(request, 'core/profile.html')