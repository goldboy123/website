# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from blog.models import BlogPost
from blog.models import IndexContent
def PostShowIndex(request):
	posts=BlogPost.objects.all()
        num=posts.count
	return render_to_response("article.html",{"posts":posts,"num":num})
def PostShow(request,num):
	posts=BlogPost.objects.all()
	return render_to_response("showarc.html",{"title":posts[int(num)].title,"content":posts[int(num)].body})
		
def ListArc(request):
	posts=BlogPost.objects.all()
	return render_to_response("list.html",{"posts":posts})	
def Index(request):
	content=IndexContent.objects.all()
	return render_to_response("index.html",{"content":content[0].content})
def Works(request):
	return render_to_response("works.html")
def About(request):
	return render_to_response("about.html")
