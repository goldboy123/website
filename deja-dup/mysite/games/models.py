from django.db import models

class Const(models.Model):
	const=models.IntegerField(max_length=4,blank=False)
	num=models.CharField(max_length=20,blank=True)
