from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from users.forms import RegistrationForm
# Create your views here.

def home_screen_view(request):
	
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts

	return render(request, "users/home.html", context)

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleanned_data.get("email")
            raw_password = form.cleaned_data.get("raw_password")
            account = authenticate(email=email,password=password)
            return redirect('home')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form 
    return render(request, 'users/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("home")

	 if request.POST:
	 	form = AccountAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			return redirect("home")

	 else:
	 	form = AccountAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'users/login.html', context)

