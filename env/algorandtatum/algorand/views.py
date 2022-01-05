from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
from .tatum import generatewallet






def index(request):
    data = {}
    return render(request, "algorand/index.html", data)

# Create your views here.

def four(request):
    data = {}
    return render(request, "algorand/404.html", data)

def explore(request):
    data = {}
    if  request.user.is_authenticated:
        data = {}
        return render(request, "algorand/explores.html", data)
    else:
        return redirect("signin.html")

    














def itemdetails(request):
    data = {}
    return render(request, "algorand/item-details.html", data)

def live(request):
    data = {}
    return render(request, "algorand/live.html", data)



def signin(request):
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    messages.info(request, "You are now logged in as {username}.")
			    return redirect("index.html")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="algorand/signin.html", context={"login_form":form})



def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="algorand/signup.html", context={"register_form":form})







def wallet(request):
    if  request.user.is_authenticated:
        walletinfo = 0
        if walletinfo == False:
            walletinfo = generatewallet()
            address = walletinfo['address']
            key = walletinfo['secret']
        current_user = request.user
        # if current_user.wallet = '': update user model wallet
        username = current_user.username
        data = {'username': username, 'address': address, 'key':key}
        return render(request, "algorand/wallet.html", data)
    else:
        return redirect("signin.html")

