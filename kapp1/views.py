from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from kapp1.forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('Templates/home.html')
        else:
            form=CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form':form})
    
def user_login(request):
    if request.method=='POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('Templates/home.html')
        else:
            form=CustomAuthenticationForm()
        return render(request, 'registration/login.html',{'form':form})