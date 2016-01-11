from django.contrib import admin
from blog.models import BlogPost,IndexContent,Catalog

class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title','writer','time')
	search_fields=('title',)
	list_filter=('time','title')
class IndexAdmin(admin.ModelAdmin):
	list_display=('content')

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(IndexContent)
admin.site.register(Catalog)
