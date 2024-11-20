from django.contrib import admin

from .models import Category, Schedule, Folders, Links, FolderLink, Tags, LinksTag
# Register your models here.
admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(Folders)
admin.site.register(Links)
admin.site.register(FolderLink)
admin.site.register(Tags)
admin.site.register(LinksTag)