# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
@csrf_exempt
def register(request):
	context={}
	if request.method=='GET':
		return render(request,'register.html',{})
	elif request.method=='POST':
	#context['message']=message
		name=request.POST['name']
		username=request.POST['username']
		password=request.POST['password']
		contact=request.POST['contact']
		fb=request.POST['fb']
		red=request.POST['red']
		git=request.POST['git']
		dob=request.POST['dob']

		if user.objects.filter(username=username).exists():
			context['msg']='Username already exists'
			return render(request,'register.html',context)

		else:
			aa=user(
			name=name,
			username=username,
			password=password,
			contact=contact,
			dob=dob,
			fb=fb,
			red=red,
			git=git
			)
			aa.save()

			context['name']=name
			context['password']=password
			context['username']=username
			context['contact']=contact
			context['red']=red
			context['dob']=dob
			context['git']=git
			context['fb']=fb
			return render(request,'main_page.html',context)

@csrf_exempt
def login(request):
	if "username" in request.session:
			return redirect('/profile')
	if request.method=='GET':
		response2=render(request,'login.html',{})
		return response2
	elif request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		context={}
		if user.objects.filter(username=username).exists():
			user_obj=user.objects.get(username=username)
			if user_obj.password==password:
				request.session['username']=user_obj.username
				return redirect('/profile')
			else:
				msg='Password incorrect'
				context['msg']=msg			
				return render(request,'main_page.html',context)
		else:
			msg='User Not found'
			context['msg']=msg
			response2=render(request,'main_page.html',context)
			return response2
@csrf_exempt
def profile(request):
	if "username" in request.session:
		us1=request.session['username']
		context={}
		user_obj=user.objects.get(username=us1)
		context['username']=user_obj.username
		context['name']=user_obj.name		
		context['contact']=user_obj.contact
		context['fb']=user_obj.fb
		context['dob']=user_obj.dob
		context['red']=user_obj.red
		context['git']=user_obj.git

		return render(request,'profile.html',context)
	else:
		return redirect('/main_page')

@csrf_exempt  	 
def main(request):
	if "username" in request.session:
		return redirect('/profile')
	return render(request,'main_page.html',{})

@csrf_exempt
def logout(request):
	if "username" in request.session:
		del request.session['username']
		return redirect('/main_page')
