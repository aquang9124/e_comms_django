from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import forms, authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserCreateForm, AuthForm
from django.views.generic import View
from .models import Post, Like
# Create your views here.
class Login(View):
	form = AuthForm
	def get(self, request):
		context = { 'form': self.form() }
		return render(request, 'accounts/login.html', context)
	def post(self, request):
		form = self.form(None, request.POST)
		context = { 'form': form }
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('accounts-success')
			else:
				return render(request, 'accounts/login.html', context)
		else:
			return render(request, 'accounts/login.html', context)

class Register(View):
	form = UserCreateForm
	def get(self, request):
		context = { 'form': self.form() }
		return render(request, 'accounts/register.html', context)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts-success')
		else:
			context = { 'form': form }
			return render(request, 'accounts/register.html', context)

class Success(View):
	def get(self, request):
		ideas = Post.objects.all().order_by('-likes')
		context = {
			"ideas": ideas,
		}
		return render(request, 'accounts/index.html', context)

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/login')

def create(request, user_id):
	if len(request.POST['idea']) < 10 or request.POST['idea'] == "":
		messages.error(request, 'Your post must be longer than ten characters. A great idea deserves some explanation.')
		return redirect('accounts-success')
	else:
		content = request.POST['idea']
		poster = User.objects.get(id = user_id)

		print poster.username
		idea = Post.objects.create(content=content, user=poster, likes=0)

		print idea
		messages.success(request, 'Thanks for posting a new idea.')
		return redirect('accounts-success')

def delete(request, post_id):
	idea = Post.objects.get(id = post_id)
	idea.delete()
	messages.success(request, 'Your idea has been successfully deleted. Have a good day.')
	return redirect('accounts-success')

def show_profile(request, user_id):
	user_data = User.objects.get(id = user_id)
	posts = Post.objects.filter(user = user_data)
	likes = Like.objects.filter(user = user_data)
	likes_count = 0
	idea_count = 0
	for post in posts:
		idea_count += 1

	for like in likes:
		likes_count += 1

	context = {
		"user_info": user_data,
		"num_posts": idea_count,
		"num_likes": likes_count,
	}
	return render(request, 'accounts/profile.html', context)

def show_idea(request, post_id):
	idea = Post.objects.get(id = post_id)
	liked = Like.objects.filter(post = post_id).distinct('user')
	context = {
		"idea": idea,
		"liked": liked,
	}

	return render(request, 'accounts/details.html', context)

def like_post(request, post_id):
	idea = Post.objects.get(id = post_id)
	user = User.objects.get(id = request.user.id)
	idea.likes += 1
	idea.save()
	Like.objects.create(user=user, post=idea)
	messages.success(request, "You like an idea! Have a cookie.")
	return redirect('accounts-success')