from django import forms
class UsersForm(forms.Form):
	emailid=forms.CharField(max_length=50)
	password=forms.CharField(max_length=50)
	username=forms.CharField(max_length=50)
	gender=forms.CharField(max_length=50)
	birthdate=forms.DateField()
	country=forms.CharField(max_length=50)
	contactno=forms.CharField(max_length=50)
	picture=forms.FileField()
	userstatus=forms.CharField(max_length=50)
class MediaFilesForm(forms.Form):
	mediafile=forms.FileField()
	filetype=forms.CharField(max_length=50)
	uploadbyemailid=forms.CharField(max_length=50)
	uploadbyadminoruser=forms.CharField(max_length=10)
	uploaddate=forms.DateField()
	topicname=forms.CharField(max_length=100)
	description=forms.CharField(max_length=1000)	
	likescount=forms.IntegerField()
	videostatus=forms.CharField(max_length=50)
class NewsForm(forms.Form):
	newsheading=forms.CharField(max_length=500)
	newsdescription=forms.CharField(max_length=5000)
	media=forms.FileField()
	newsstatus=forms.CharField(max_length=50)

	