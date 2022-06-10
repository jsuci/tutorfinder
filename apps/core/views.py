from django.shortcuts import render, redirect
from allauth.account.decorators import verified_email_required


def homepage(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    else:
        return redirect("/login/")

@verified_email_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


@verified_email_required
def profile(request):
    return render(request, 'core/profile.html')


def search(request):
    return render(request, 'core/search.html')
