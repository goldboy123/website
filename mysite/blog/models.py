from django.db import models
from ckeditor.fields import RichTextField
class Catalog(models.Model):
        cats=models.CharField(max_length=30)
        def __unicode__ (self):
                return self.cats
class BlogPost(models.Model):
	title=models.CharField(max_length=100)
        catalog=models.ForeignKey(Catalog)
	writer=models.CharField(max_length=20)
	body=RichTextField('Content')
	time=models.DateTimeField()

 	class Meta:
		ordering=['time']
	def __unicode__(self):
		return self.title
class IndexContent(models.Model):	
	content=RichTextField('Content')
	time=models.DateTimeField()
class LinkFriend(models.Model):
	name=models.CharField(max_length=10)
	link=models.CharField(max_length=100)

class MsgPost(models.Model):
	user =models.CharField(max_length = 20)
	email = models.EmailField()
	website = models.CharField(max_length = 50)
	content =models.TextField()
	time = models.DateTimeField(auto_now_add =True)
	def __unicode__(self):
		return self.user

class AboutIndex(models.Model):
	content = RichTextField('Content')
	def __unicode__(self):
		return self.content

class InsPost(models.Model):
	time = models.DateTimeField(auto_now_add = True)
	content = RichTextField()
	def __unicode__(self):
		return self.content

