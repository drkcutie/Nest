from django.contrib import admin

from .models import User, Category, Schedule, Folders, Links, FolderLink, Tags, LinksTag

# Register your models here.
admin.register(User)
admin.register(Category)
admin.register(Schedule)
admin.register(Folders)
admin.register(Links)
admin.register(FolderLink)
admin.register(Tags)
admin.register(LinksTag)
