from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import random


# ---------------- SIGNUP ---------------- #

def signup_page(request):

    if request.user.is_authenticated:
        return redirect('recipie')

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account Created Successfully")
        return redirect("login")

    return render(request, "signup.html")


# ---------------- LOGIN ---------------- #

def login_page(request):

    if request.user.is_authenticated:
        return redirect("recipie")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("recipie")

        messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


# ---------------- LOGOUT ---------------- #

def logout_page(request):

    logout(request)
    return redirect("login")


# ---------------- FORGOT PASSWORD ---------------- #

def forgot_password(request):

    if request.method == "POST":

        email = request.POST.get("email")

        if not User.objects.filter(email=email).exists():
            messages.error(request, "Email not registered")
            return redirect("forgot_password")

        otp = random.randint(100000, 999999)

        send_mail(
            subject="Password Reset OTP",
            message=f"Your OTP is: {otp}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        request.session["reset_email"] = email
        request.session["reset_otp"] = str(otp)
        request.session["otp_expiry"] = (
            timezone.now() + timedelta(minutes=5)
        ).isoformat()

        messages.success(request, "OTP Sent Successfully")

        return redirect("verify_otp")

    return render(request, "forgot_password.html")


# ---------------- VERIFY OTP ---------------- #

def verify_otp(request):

    if request.method == "POST":

        user_otp = request.POST.get("otp")

        expiry = request.session.get("otp_expiry")

        if expiry:

            expiry = timezone.datetime.fromisoformat(expiry)

            if timezone.now() > expiry:

                messages.error(request, "OTP Expired")
                return redirect("forgot_password")

        if user_otp == request.session.get("reset_otp"):

            messages.success(request, "OTP Verified Successfully")
            return redirect("reset_password")

        else:

            messages.error(request, "Invalid OTP")
            return redirect("verify_otp")

    return render(request, "verify_otp.html")


# ---------------- RESET PASSWORD ---------------- #

def reset_password(request):

    if request.method == "POST":

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:

            messages.error(request, "Passwords do not match")
            return redirect("reset_password")

        email = request.session.get("reset_email")

        user = User.objects.get(email=email)

        user.set_password(password)
        user.save()

        request.session.pop("reset_email", None)
        request.session.pop("reset_otp", None)
        request.session.pop("otp_expiry", None)

        messages.success(request, "Password Reset Successfully")

        return redirect("login")

    return render(request, "reset_password.html")