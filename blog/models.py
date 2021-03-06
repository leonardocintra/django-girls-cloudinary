from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField



class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image_url = CloudinaryField('imagem', blank=True, null=True)

	def publish(sefl):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title