from django.contrib import admin
from blog.models import BlogPost,IndexContent,Catalog
from blog.models import AboutIndex
from blog.models import MsgPost,InsPost
class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title','writer','time')
	search_fields=('title',)
	list_filter=('time','title')
class IndexAdmin(admin.ModelAdmin):
	list_display=('content')

class MsgAdmin(admin.ModelAdmin):
	list_display = ('user','email','time')
class InsAdmin(admin.ModelAdmin):
	list_display = ('time','content')

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(IndexContent)
admin.site.register(Catalog)
admin.site.register(AboutIndex)
admin.site.register(MsgPost,MsgAdmin)
admin.site.register(InsPost,InsAdmin)
