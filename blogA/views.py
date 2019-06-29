from django.shortcuts import render, get_object_or_404, redirect
#get_object_or_404 >> 예외처리
from .models import Blog
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth


def home(request) :
    blogs = Blog.objects #쿼리셋 #메소드

    return render(request, 'home.html', {'blogs': blogs})
    #쿼리셋과 메소드의형식
    #모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    #request 와 blog_id 를 요청

    blog_detail = get_object_or_404(Blog, pk = blog_id)
    #특정 클래스를 하나의 인자로 받고, 두 번째는 몇번 째를 가져올지.

    return render(request, 'detail.html', {'blog':blog_detail})
    #path converter <type:변수이름>
    #int str uuid
    # get_object_or_404(어떤클래스, 검색조건(몇번데이터,pk =))
    # pk = primary key 객체들의 이름표, 구분자, 데이터의 대표값

def new(request):
    return render(request, 'new.html')
    #new 만 띄어줌

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    #new name="" 을 가져온다 'title' 'body'
    blog.pub_date = timezone.datetime.now()
    blog.save()
    #데이터베이스에 저장해라 객체.delete
    #입력받은 내용을 데이터베이스로 주는 함수
    return redirect('/blog/'+str(blog.id))
    #() 속 url로 넘기세요 / url은 문자열이기떄문에 blog.id - int형을 str로 형변환
    #다른 홈페이지도 링크가능 http://google.com/
def portfolio(request):
    return render(request, 'portfolio.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')