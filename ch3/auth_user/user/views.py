from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View
from user.forms import CustomUserCreationForm

class HomeView(View):
    def get(self, request):
        # context = {"user": user, "perm": perms}
        return render(request, "home.html")


class SignUpView(View):
    def get(self, request):
        return render(
            request, "registration/sign_up.html",
            {"form": CustomUserCreationForm}
        )
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # session login
        return redirect("home")
