from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .models import customer
# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        form=myauthenticate(username=username,password=password)
        if form:
            #print('hellllllllllllldsjdbjad\n')
            #if form.is_active:
                #login(request,form)
            return render(request, 'accounts/MainPage.html')
    else:
        form=AuthenticationForm()


    return render(request,'accounts/login.html',{form:'form'})

def myauthenticate( username=None, password=None):

    try:
            # Try to find a user matching your username
        user = customer.objects.get(name=username)

            #  Check the password is the reverse of the username
        if check_password(password, user.password_en):
                # Yes? return the Django user object
            return user
        else:
                # No? return None - triggers default login failed
            return None
    except customer.DoesNotExist:
            # No user was found, return None - triggers default login failed
        return None

    # Required for your backend to work properly - unchanged in most scenarios
def get_user(self, user_id):
    try:
        return customer.objects.get(pk=user_id)
    except customer.DoesNotExist:
        return None

def check_password(password1,password2):
    if password2==password1:
        return True
    else:
        return False