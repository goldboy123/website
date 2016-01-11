# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from blog.models import BlogPost,Catalog,MsgPost
from blog.models import IndexContent,AboutIndex,InsPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def PostShowIndex(request):
	posts=BlogPost.objects.all()
        num=posts.count
	return render_to_response("article.html",{"posts":posts,"num":num})
def Catagory(request,pk):
	posts = BlogPost.objects
	catas = Catalog.objects
	cata = catas.get(id = pk)	
	cposts = posts.filter(catalog= cata).all() 
	posts = posts.all().reverse()
	return render_to_response("cats.html",{"cposts":cposts,"posts":posts[:4],"catas":catas.all(),"cata":cata})
def PostShow(request,num):
	posts = BlogPost.objects
	post = posts.get(id = num)
	catas = Catalog.objects.all()
	return render_to_response("art1.html",{"article":post,"posts":posts.all()[:4],"catas":catas})
def InsIndex(reques):
	posts = BlogPost.objects.all()
	catas = Catalog.objects.all()
	posts = posts.reverse()
	inss = InsPost.objects.all()
	return render_to_response("ins.html",{"insposts":inss,"posts":posts.all()[:4],"catas":catas})	
def ListArc(request):
	catas = Catalog.objects.all()
	posts=BlogPost.objects.all()
	posts = posts.reverse()
	paginator = Paginator(posts,3)
	page = request.GET.get('page')
	try:
		ps = paginator.page(page)
	except PageNotAnInteger:
		ps = paginator.page(1)
	except EmptyPage:
		ps = paginator.page(paginator.num_pages)
	return render_to_response("list.html",{"posts":posts[:4],"catas":catas,"pos":ps})	
def Index(request):
	posts = BlogPost.objects.all()
	catas = Catalog.objects.all()
	posts = posts.reverse()
	posts = posts[:4]
	pp = posts[:2]
	content=IndexContent.objects.all()
	return render_to_response("index.html",{"content":content[0].content,"catas":catas,"lpost":pp,"posts":posts})
def MsgIndex(request):
	posts = BlogPost.objects.all()
	posts = posts.reverse()
	res=""
	catas = Catalog.objects.all()
	msgs = MsgPost.objects.all().reverse()
	if request.method == 'POST':
		gets = request.POST
		user = gets['author']
		email = gets['email']
		url = gets['url']
		content = gets['comment']
		if user and email and content:
			s=MsgPost(user =user,email = email,website =url,content =content)
			s.save()
			res = "<script>alert('留言成功！');</script>"
		else:
			res = "<script>alert('留言失败！');</script>"
	return render_to_response("msg.html",{"catas":catas,"messages":msgs,"response":res,"posts":posts[:4]})
def About(request):
	posts = BlogPost.objects.all()
	posts = posts.reverse()
	abouts = AboutIndex.objects.all()
	catas = Catalog.objects.all()
	return render_to_response("about.html",{"catas":catas,"abouts":abouts,"posts":posts[:4]})
