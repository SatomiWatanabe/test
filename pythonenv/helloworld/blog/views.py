from django.shortcuts import render
from .models import *

# Create your views here.
def article(request):
	queryset_list = Post.objects.all()

	context = {
		"object_list": queryset_list,
		}
	return render(request, "articles.html", context)