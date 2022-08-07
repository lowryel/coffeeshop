from django.contrib import admin
from .models import FileModel, Comment
# Register your models here.
admin.site.register(FileModel)

class CommentAdmin(admin.ModelAdmin):
    ...

admin.site.register(Comment, CommentAdmin)