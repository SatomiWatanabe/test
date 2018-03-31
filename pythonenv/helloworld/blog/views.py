from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
import tweepy

# Create your views here.
def article(request):
	queryset_list = Post.objects.all().order_by('-time')
	query = request.GET.get("q")
		
	if query:
		queryset_list = Post.objects.all().filter(Q(message__contains=query)).order_by('-time')

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	
		consumer_key = '****'
		consumer_secret = '****'
		access_token = '****'
		access_token_secret = '****'

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)
		api.update_status(status='newpost')

	context = {
		"object_list": queryset_list,
		"form": form
		}

	return render(request, "articles.html", context)