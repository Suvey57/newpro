from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	book_name = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	writer = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.book_name

	def get_absolute_url(self):
		return reverse('post-detail', kwargs = {'pk':self.pk})
		
