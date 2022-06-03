import sqlite3
from Life.forms import UsersForm
from Life.forms import MediaFilesForm
from Life.forms import NewsForm
from Life.models import Users
from Life.models import MediaFiles
from Life.models import Admin
from Life.models import MediaLikes
from Life.models import News
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context,loader
from datetime import date
from django.contrib.auth import logout
from django.shortcuts import redirect
def index(request):
	return render(request,'index.html')

def register(request):
	return render(request,'index.html')

def registersave(request):
	saved=False
	if request.method=="POST":
		usersform=UsersForm(request.POST,request.FILES)
		if usersform.is_valid():
			users=Users()
			users.emailid=usersform.cleaned_data["emailid"]
			users.password=usersform.cleaned_data["password"]
			users.username=usersform.cleaned_data["username"]
			users.gender=usersform.cleaned_data["gender"]
			users.birthdate=usersform.cleaned_data["birthdate"]
			users.country=usersform.cleaned_data["country"]
			users.contactno=usersform.cleaned_data["contactno"]
			users.picture=usersform.cleaned_data["picture"]
			users.userstatus=usersform.cleaned_data["userstatus"]
			users.save()
			msg="Registration Successful"
		else:
			msg="Sorry! Can Not Register"
		return render(request,'message.html',{"msg":msg})

def checkemail(request):
	emailid=request.GET["emailid"]
	q=Users.objects.filter(emailid=emailid)
	if q:
		msg="Email Id already exists "
	else:
		msg=" Email Id doesn't exist"
	resp=HttpResponse(msg)
	return(resp)

def adminlogin(request):
	return render(request,'index.html')

def adminlogincheck(request):
	emailid=request.POST["emailid"]
	password=request.POST["password"]
	q=Admin.objects.filter(emailid=emailid,password=password)
	if q:
		request.session['emailid']=emailid
		request.session['password']=password
		#ls=list(q)
		return render(request,'adminhome.html',{"emailid":q[0].emailid})
	else:
		msg="<h1>For admin use only.</h1>"
		resp=HttpResponse(msg)
		return(resp)

def login(request):
	return render(request,'index.html')

def logincheck(request):
	emailid=request.POST["emailid"]
	password=request.POST["password"]
	q=Users.objects.filter(emailid=emailid,password=password)
	if q:
		if q[0].userstatus=="Active":
			request.session['emailid']=emailid
			request.session['password']=password
			#ls=list(q)
			pic="/media/"+str(q[0].picture)
			return render(request,'home.html',{"emailid":q[0].emailid,"pic":pic})
		else:
			msg="<h1>Your account has been deactivated.</h1>"
			resp=HttpResponse(msg)
			return(resp)
	else:	
		msg="<h1>Invalid Emailid or Password.</h1>"
		resp=HttpResponse(msg)
		return(resp)

def home(request):
	emailid=request.session.get("emailid")
	qs=MediaFiles.objects.all()
	v="<table>"
	v+='''<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="/static/bootstrap.min.css" />
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	<script src="/static/jquery-3.3.1.js" ></script>
	<script>
	$(document).ready(function ()	{
		$(".chk").click(function(){
			alert($(this).val());
			vid=$(this).val();
			c=$(this);
			$.get("likemedia?vid="+vid,function(data,status){
				$(c).prop("disabled","true");
				//alert(data);
				
			});
		});
	});
	</script>
	</head>
	</html>'''	
	for rec in qs:
		if rec.videostatus=="Active":
			vid=id
			v+="<tr><td><video width=300 height=300 controls><source src='/media/"+str(rec.mediafile)+"' /></video>"
			qs_ml=MediaLikes.objects.filter(likebyemailid=emailid,mediaid=vid)
			if qs_ml:
				v+="<br/><input type=checkbox name=cb class=chk  value="+str(rec.id)+" checked disabled />Likes("+str(rec.likescount)+")</td>"
			else:
				v+="<br/><input type=checkbox name=cb class=chk  value="+str(rec.id)+" />Likes("+str(rec.likescount)+")</td>"
	v+="</tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)

def changepassword(request):
	return render(request,'changepassword.html')

def changepasswordsave(request):
	emailid=request.session.get("emailid")
	password=request.session.get("password")
	currentpassword=request.POST["currentpassword"]
	newpassword=request.POST["newpassword"]
	q=Users.objects.filter(emailid=emailid)
	if password==currentpassword and q:
		q[0].password=newpassword
		q[0].save()
		a="<h1>Password Changed Successfully</h1>"
		resp=HttpResponse(a)
		return(resp)
	else:
		a="<h1>Wrong Current Password</h1>"
		resp=HttpResponse(a)
		return(resp)			

def signout(request):
	logout(request)
	return redirect(index)

def adminchangepassword(request):
	return render(request,'adminchangepassword.html')

def adminchangepasswordsave(request):
	emailid=request.session.get("emailid")
	password=request.session.get("password")
	currentpassword=request.POST["currentpassword"]
	newpassword=request.POST["newpassword"]
	q=Admin.objects.filter(emailid=emailid)
	if password==currentpassword and q:
		q[0].password=newpassword
		q[0].save()
		a="<h1>Password changed successfully</h1>"
		resp=HttpResponse(a)
		return(resp)
	else:
		a="<h1>Wrong current password</h1>"
		resp=HttpResponse(a)
		return(resp)			

def adminsignout(request):
	logout(request)
	return redirect(index)

def upload(request):
	emailid=request.session.get('emailid')
	curdate=date.today()
	uploaddate=curdate.strftime("%Y-%m-%d")
	return render(request,'upload.html',{"uploaddate":uploaddate,"emailid":emailid})

def uploadsave(request):
	saved=False
	if request.method=="POST":
		mediafilesform=MediaFilesForm(request.POST,request.FILES)
		if mediafilesform.is_valid():
			media=MediaFiles()
			media.mediafile=mediafilesform.cleaned_data["mediafile"]
			media.filetype=mediafilesform.cleaned_data["filetype"]
			media.uploadbyemailid=mediafilesform.cleaned_data["uploadbyemailid"]
			media.uploadbyadminoruser=mediafilesform.cleaned_data["uploadbyadminoruser"]
			media.uploaddate=mediafilesform.cleaned_data["uploaddate"]
			media.topicname=mediafilesform.cleaned_data["topicname"]
			media.description=mediafilesform.cleaned_data["description"]
			media.likescount=mediafilesform.cleaned_data["likescount"]
			media.videostatus=mediafilesform.cleaned_data["videostatus"]
			media.save()
			msg="File Uploaded Successfully"
		else:
			msg="Sorry! Can Not Upload File"
		return render(request,'message.html',{"msg":msg})

def adminupload(request):
	emailid=request.session.get('emailid')
	curdate=date.today()
	uploaddate=curdate.strftime("%Y-%m-%d")
	return render(request,'adminupload.html',{"uploaddate":uploaddate,"emailid":emailid})

def adminuploadsave(request):
	saved=False
	if request.method=="POST":
		mediafilesform=MediaFilesForm(request.POST,request.FILES)
		if mediafilesform.is_valid():
			media=MediaFiles()
			media.mediafile=mediafilesform.cleaned_data["mediafile"]
			media.filetype=mediafilesform.cleaned_data["filetype"]
			media.uploadbyemailid=mediafilesform.cleaned_data["uploadbyemailid"]
			media.uploadbyadminoruser=mediafilesform.cleaned_data["uploadbyadminoruser"]
			media.uploaddate=mediafilesform.cleaned_data["uploaddate"]
			media.topicname=mediafilesform.cleaned_data["topicname"]
			media.description=mediafilesform.cleaned_data["description"]
			media.likescount=mediafilesform.cleaned_data["likescount"]
			media.save()
			msg="File Uploaded Successfully"
		else:
			msg="Sorry! Can Not Upload File"
		return render(request,'message.html',{"msg":msg})

def adminuserbase(request):
	emailid=request.session.get("emailid")
	userbase=Users.objects.all()
	v="<table width=100% border='1'>"
	v+="<tr><th>EmailId</th>"
	v+="<th>User Name</th>"
	v+="<th>Gender</th>"
	v+="<th>Birth Date</th>"
	v+="<th>Country</th>"
	v+="<th>Contact No.</th>"
	v+="<th>Picture</th>"
	v+="<th>Status</th></tr>"
	for rec in userbase:
		v+="<tr>"
		v+="<td>"+rec.emailid+"</td>"
		v+="<td>"+rec.username+"</td>"	
		v+="<td>"+rec.gender+"</td>"
		v+="<td>"+str(rec.birthdate)+"</td>"
		v+="<td>"+rec.country+"</td>"
		v+="<td>"+rec.contactno+"</td>"
		v+="<td><img src='/media/"+str(rec.picture)+"' width=50 height=50 /></td>"
		v+="<td><a href='deactivate?emailid="+rec.emailid+"' >Deactivate</a></td>"
		v+="</tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)		

def adminlibrary(request):
	emailid=request.session.get("emailid")
	library=MediaFiles.objects.all()
	v="<table width=100% border='1'>"
	v+="<tr><th>Media File</th>"
	v+="<th>File Type</th>"
	v+="<th>Upload By Emailid</th>"
	v+="<th>Upload By Admin or User</th>"
	v+="<th>Upload Date</th>"
	v+="<th>Topic Name</th>"
	v+="<th>Description</th>"
	v+="<th>Status</th></tr>"
	for rec in library:
		v+="<tr>"
		v+="<td><video width=100 height=100 controls><source src='/media/"+str(rec.mediafile)+"' /></video></td>"
		v+="<td>"+rec.filetype+"</td>"	
		v+="<td>"+rec.uploadbyemailid+"</td>"
		v+="<td>"+rec.uploadbyadminoruser+"</td>"
		v+="<td>"+str(rec.uploaddate)+"</td>"
		v+="<td>"+rec.topicname+"</td>"
		v+="<td>"+rec.description+"</td>"
		v+="<td><a href='deactivatefile?uploadbyemailid="+rec.uploadbyemailid+"'>Deactivate</a></td>"
		v+="</tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)		

def search(request):
	emailid=request.session.get('emailid')
	srch=request.POST["search"]
	q=MediaFiles.objects.filter(description__icontains=srch)
	v='''<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="/static/bootstrap.min.css" />
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	<script src="/static/jquery-3.3.1.js" ></script>
	<script>
	$(document).ready(function ()	{
		$(".chk").click(function(){
			alert($(this).val());
			vid=$(this).val();
			c=$(this);
			$.get("likemedia?vid="+vid,function(data,status){
				$(c).prop("disabled","true");
				//alert(data);
				
			});
		});
	});
	</script>
	</head>
	</html>'''	
	for rec in q:
		vid=rec.id	
		v+="<table width=100% align=center>"
		v+="<td><video width=300 height=300 controls><source src='/media/"+str(rec.mediafile)+"' /></video>"
		qs_ml=MediaLikes.objects.filter(likebyemailid=emailid,mediaid=vid)
		if qs_ml:
			v+="<br/><input type=checkbox name=cb class=chk  value="+str(vid)+" checked disabled />Likes("+str(rec.likescount)+")</td>"
		else:
			v+="<br/><input type=checkbox name=cb class=chk  value="+str(vid)+" />Likes("+str(rec.likescount)+")</td>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)		

def likemedia(request):
	emailid=request.session.get('emailid')
	vid=request.GET["vid"]
	q=MediaFiles.objects.filter(id=vid)	
	if q:
		q[0].likescount=q[0].likescount+1
		q[0].save()
		ml=MediaLikes()
		ml.mediaid=vid
		ml.likebyemailid=emailid
		curdate=date.today()
		ldate=curdate.strftime("%Y-%m-%d")
		ml.likedate=ldate
		ml.save()
	resp=HttpResponse("done")
	return(resp)		

def mylikes(request):
	emailid=request.session.get('emailid')
	qs1=MediaLikes.objects.filter(likebyemailid=emailid)
	v="<table width=100% align=center>"
	for rec in qs1:
		mediaid=rec.mediaid
		qs2=MediaFiles.objects.filter(id=mediaid)		
		v+="<td><video width=300 height=300 controls><source src='/media/"+str(qs2[0].mediafile)+"' /></video>"
		v+="<br/>Likes("+str(qs2[0].likescount)+")</td>"
	v+="</table>"		
	resp=HttpResponse(v)
	return(resp)

def myvideos(request):
	emailid=request.session.get('emailid')
	qs=MediaFiles.objects.filter(uploadbyemailid=emailid)
	v="<table width=100% align=center>"
	for rec in qs:
		v+="<td><video width=300 height=300 controls><source src='/media/"+str(rec.mediafile)+"' /></video>"
		v+="<br/>Likes("+str(qs[0].likescount)+")"
		v+="<a href='deletevideo?id="+str(rec.id)+"' style='margin-left:200px'>Delete</a><td>"
	v+="</table>"		
	resp=HttpResponse(v)
	return(resp)

def forgotpassword(request):
	return render(request,'forgotpassword.html')		

def forgotpasswordsave(request):
	emailid=request.POST["emailid"]
	birthdate=request.POST["birthdate"]
	a="<table>"
	q=Users.objects.filter(emailid=emailid,birthdate=birthdate)
	if q:
		if q[0].userstatus=="Active":
			request.session['emailid']=emailid
			request.session['birthdate']=birthdate
			#ls=list(q)
			return render(request,'resetpassword.html')
		else:
			a+="<h1>Cannot Change Password. Your account has been deactivated.</h1>"
			a+="<h2><a href=index>Click here to move to home page</a><h2>"
		a+="</table>"	
		resp=HttpResponse(a)
		return(resp)
	else:
		msg="<h1>Invalid emailid and birthdate</h1>"
		resp=HttpResponse(msg)
		return(resp)

def resetpasswordsave(request):
	confirmpassword=request.POST["confirmpassword"]
	newpassword=request.POST["newpassword"]
	emailid=request.session.get("emailid")
	birthdate=request.session.get("birthdate")
	a="<table>"
	q=Users.objects.filter(emailid=emailid,birthdate=birthdate)
	if q:
		q[0].password=newpassword
		q[0].save()
		a+="<h1>Password changed successfully</h1>"
		a+="<h2><a href=index>Click here to move to home page</a></h2>"
	else:
		a="<h1>Wrong current password</h1>"
	a+="</table>"
	resp=HttpResponse(a)
	return(resp)			

def deactivate(request):
	emailid=request.GET["emailid"]
	q=Users.objects.filter(emailid=emailid)
	if q:
		q[0].userstatus="Inactive"
		q[0].save()
	a="<h1>Profile deactivated successfully.</h1>"
	resp=HttpResponse(a)
	return(resp)			

def deactivatefile(request):
	uploadbyemailid=request.GET["uploadbyemailid"]
	q=MediaFiles.objects.filter(uploadbyemailid=uploadbyemailid)
	if q:
		q[0].videostatus="Inactive"
		q[0].save()
	a="<h1>Video deactivated successfully.</h1>"
	resp=HttpResponse(a)
	return(resp)			

def deleteaccount(request):
	emailid=request.session.get('emailid')
	q=Users.objects.filter(emailid=emailid)	
	if q:
		qs1=MediaFiles.objects.filter(uploadbyemailid=emailid)
		qs1.delete()
		qs2=MediaLikes.objects.filter(likebyemailid=emailid)
		qs2.delete()
		q.delete()
		return redirect(index)	

def deletevideo(request):
	id=request.GET["id"]
	q=MediaFiles.objects.filter(id=id)
	if q:
		q.delete()	
		return redirect(home)

def mostlikedvideos(request):
	v="<table width=100% align=center>"
	qs=MediaFiles.objects.all().order_by('-likescount')
	for rec in qs:
		v+="<td><video width=300 height=300 controls><source src='/media/"+str(rec.mediafile)+"' /></video>"
		v+="<br/>Likes("+str(rec.likescount)+")</td>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)

def newsupload(request):
	return render(request,'newsupload.html')

def newsuploadsave(request):
	saved=False
	if request.method=="POST":
		newsform=NewsForm(request.POST,request.FILES)
		if newsform.is_valid():
			news=News()
			news.newsheading=newsform.cleaned_data["newsheading"]
			news.newsdescription=newsform.cleaned_data["newsdescription"]
			news.media=newsform.cleaned_data["media"]
			news.newsstatus=newsform.cleaned_data["newsstatus"]
			news.save()
			msg="News Uploaded Successfully"
		else:
			msg="Sorry! Can Not Upload News"
		return render(request,'message.html',{"msg":msg})

def news(request):
	v='''<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset="utf-8" />	
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="/static/bootstrap.min.css" />
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	<script src="/static/jquery-3.3.1.js" ></script>
	</head>'''
	v+="<body>"		
	v+="<div class=well ><h1 align=center style='font-weight:bold;font-family:Lucida Handwriting'>NEWS</h1></div>"
	qs=News.objects.all()
	for rec in qs:
		if rec.newsstatus=="Active":
			v+="<div class='well'>"
			v+="<h2 align=center >"
			v+=rec.newsheading+"</h2>"
			v+="</div>"
			v+="<div align=center>"
			v+="<video width=300 height=300 controls>"
			v+="<source src='/media/"+str(rec.media)+"' />"
			v+="</video>"	
			v+="</div>"
			
			v+="<div class=well><h4 align=center style='line-height:20pt;padding-left:30px;padding-right:30px'>"
			v+=rec.newsdescription+"</h4></div>"
	v+="</body>"
	v+="</html>"
	resp=HttpResponse(v)
	return(resp)

def update(request):
	emailid=request.session.get('emailid')
	q=Users.objects.filter(emailid=emailid)
	return render(request,'update.html',{"emailid":emailid,"password":q[0].password,"username":q[0].username,"gender":q[0].gender,"birthdate":q[0].birthdate,"country":q[0].country,"contactno":q[0].contactno,"picture":q[0].picture,"userstatus":q[0].userstatus})

def updatesave(request):
	emailid=request.session.get('emailid')
	password=request.session.get('password')
	newusername=request.POST["username"]
	newcountry=request.POST["country"]
	newcontactno=request.POST["contactno"]
	newpicture=request.POST["picture"]
	q=Users.objects.filter(emailid=emailid)
	if q:
		q[0].username=newusername
		q[0].country=newcountry		
		q[0].contactno=newcontactno
		if request.method=="POST":
			usersform=UsersForm(request.POST,request.FILES)
			if usersform.is_valid():
				users=Users()
				users.q[0].picture=UsersForm.cleaned_data["newpicture"]
		q[0].save()
		msg="Updated Successfully"
	else:
		msg="Sorry! Can Not Update"
		return render(request,'message.html',{"msg":msg})

		