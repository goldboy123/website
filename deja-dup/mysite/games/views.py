# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import random
from games.models import Const

class fgame:
   def __init__(self,key,t):
        self.num={}
	self.num[key]=t
        
   def figure(n):
        items=range(0,n)
        a=random.sample(items,4)
        return a
   def comparenum(self,num1,num2):
        s=0
        v=0
        for i in range(0,4):
            for j in range(0,4):
                if num1[i]==num2[j]:
                    if i == j:
                        s=s+1
                    else:
                        v=v+1
        result=[s,'A',v,'B']
        return result    
  
   num1=figure(9)
   
   def finput(self,num2):
         c=[]
         num={}
         for line in num2:
            c.append(int(line))
         c=self.comparenum(self.num1,c)
         if c==[4,'A',0,'B']:
            return 1
         else:
            num[str(num2)]=c
            return num


            
def games(request):    	
       if 'q' in request.GET:
           key=request.GET['q']
	   gam=fgame(key,"")
           t=gam.finput(key) 
           if t == 1:
               return HttpResponse('success!')
           else:
               return render_to_response('games.html',{'nums':t})
       else:
           t='请输入一个四位数：'
           return render_to_response('games.html',{'nums':t})

	

    
       
        
    
