from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#계정 class
from django.contrib import auth
#계정권한
from django.views.decorators.csrf import csrf_exempt
#csrf 토큰 오류 

def signup(request):
    if request.method == 'POST' :
        if request.POST['password1'] == request.POST['password2'] : 
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)
        #데이터베이스에서 회원명단이 맞는지 확인시켜주는 함수
        if user is not None:
            auth.login(request, user)
            return redirect('home.html')
        else:
            return render(request, 'home.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')