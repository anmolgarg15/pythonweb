from django.urls import path
from . import views
urlpatterns=[
path('index',views.index),
path('register',views.register),
path('registersave',views.registersave),
path('checkemail',views.checkemail),
path('adminlogin',views.adminlogin),
path('adminlogincheck',views.adminlogincheck),
path('login',views.login),
path('logincheck',views.logincheck),
path('home',views.home),
path('changepassword',views.changepassword),
path('changepasswordsave',views.changepasswordsave),
path('signout',views.signout),
path('adminchangepassword',views.adminchangepassword),
path('adminchangepasswordsave',views.adminchangepasswordsave),
path('adminsignout',views.adminsignout),
path('upload',views.upload),
path('uploadsave',views.uploadsave),
path('adminupload',views.adminupload),
path('adminuploadsave',views.adminuploadsave),
path('adminuserbase',views.adminuserbase),
path('adminlibrary',views.adminlibrary),
path('search',views.search),
path('likemedia',views.likemedia),
path('mylikes',views.mylikes),
path('myvideos',views.myvideos),
path('forgotpassword',views.forgotpassword),
path('forgotpasswordsave',views.forgotpasswordsave),
path('resetpasswordsave',views.resetpasswordsave),
path('deactivate',views.deactivate),
path('deactivatefile',views.deactivatefile),
path('deleteaccount',views.deleteaccount),
path('deletevideo',views.deletevideo),
path('mostlikedvideos',views.mostlikedvideos),
path('newsupload',views.newsupload),
path('newsuploadsave',views.newsuploadsave),
path('news',views.news),
path('update',views.update),
path('updatesave',views.updatesave),
]