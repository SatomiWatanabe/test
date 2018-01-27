from django.db import models

class Post(models.Model):
	name = models.CharField(max_length=120)
	time = models.DateTimeField(auto_now=True, auto_now_add=False)
	message = models.TextField()
	image = models.ImageField(upload_to="",
		null=True,
		blank=True)
		