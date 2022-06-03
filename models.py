from django.db import models
class Users(models.Model):
	emailid=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	birthdate=models.DateField()
	country=models.CharField(max_length=50)
	contactno=models.CharField(max_length=50)
	picture=models.FileField(upload_to="")
	userstatus=models.CharField(max_length=50)
class MediaFiles(models.Model):
	mediafile=models.FileField(upload_to="")
	filetype=models.CharField(max_length=50)
	uploadbyemailid=models.CharField(max_length=50)
	uploadbyadminoruser=models.CharField(max_length=10)
	uploaddate=models.DateField()
	topicname=models.CharField(max_length=100)
	description=models.CharField(max_length=1000)	
	likescount=models.IntegerField()
	videostatus=models.CharField(max_length=50)
class Admin(models.Model):
	emailid=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
class MediaLikes(models.Model):
	mediaid=models.CharField(max_length=50)
	likebyemailid=models.CharField(max_length=50)
	likedate=models.DateField()
class News(models.Model):
	newsheading=models.CharField(max_length=500)
	newsdescription=models.CharField(max_length=5000)
	media=models.FileField(upload_to="")
	newsstatus=models.CharField(max_length=50)