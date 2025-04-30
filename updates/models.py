from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField(editable=True)

	def __str__(self):
		return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"



