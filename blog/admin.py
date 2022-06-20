from django.contrib import admin
from .models import Post

admin.site.register(Post)

class Post(admin.ModelAdmin):
    list_display =["Title", "Text", "Author", "Created_Date", "Published_Date"]
