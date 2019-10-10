from django.shortcuts import render, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import UserForm, CommentForm
from .models import Post, Comment
from django import template
from django.template.loader import get_template 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def pageA(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'bcmp/acceuilU.html', {'posts': posts})
    else:
        posts = Post.objects.all()
        return render(request, 'bcmp/acceuil.html', {'posts': posts})


def logout_user(request):
    logout(request)
    return redirect('/Acceuil/')

def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'bcmp/loginerror.html', {})
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/Acceuil/')
                else:
                    return render(request, 'bcmp/login.html', {'error_message': "Votre compte n'est pas disponible"})
            else:
                return render(request, 'bcmp/login.html', {'error_message': "Nom d'utilisateur ou mot de passe invalide"})
        return render(request, 'bcmp/login.html', {})
        


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/Acceuil/')
    context = {
        "form": form,
    }
    return render(request, 'bcmp/register.html', context)


def post_list(request):
    if request.user.is_authenticated:
        latest = Post.objects.order_by('-timestamp')[0:3]
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
        return render(request, 'bcmp/post_listU.html', {'posts': posts})
    else:
        latest = Post.objects.order_by('-timestamp')[0:3]
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 2)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
        return render(request, 'bcmp/post_list.html', {'posts': posts})
    

@login_required(login_url='/Connecter/')
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.filter(active=True)
    print (comments)  
        # for comment in comments:
        #   for reply in comment.replies.all():
        #       print reply.body
        #       # print reply.__dict__

        # rpy = Comment.objects.filter(active=True) 
        
    if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()


                posts_list = Post.objects.all()
                paginator = Paginator(posts_list, 4)
                page = request.GET.get('page')
                try:
                    posts = paginator.page(page)
                except PageNotAnInteger:
                    posts = paginator.page(1)
                except EmptyPage:
                    posts = paginator.page(paginator.num_pages)
                context = {
                    'posts': posts,
                    'paginate': True
                }
    else:
        comment_form = CommentForm()
        posts_list = Post.objects.all()
        paginator = Paginator(posts_list, 4)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
            'posts': posts,
            'paginate': True
        }
    return render(request,'bcmp/post_detail.html',
        {'posts': posts,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        })  
    

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler403(request, exception, template_name="403.html"):
    response = render_to_response("403.html")
    response.status_code = 403
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response
