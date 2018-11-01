from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ContactForm, LoginForm


def home_page(request):
    context = {"title": "hello world"}
    return render(request, "index.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {"title": "hello contact",
               "form": contact_form
               }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    print(request.user.is_authenticated())
    if form.is_valid():
        name = form.cleaned_data.get("name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
            context['form']= LoginForm()
            return redirect("/login")
        else:
            print("Error")

        print(form.cleaned_data)
    return render(request, "auth/login.html", context)


def register_page(request):
    context = {"": ""}
    return render(request, "auth/register.html", context)