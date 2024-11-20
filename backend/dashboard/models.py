from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)  # Add primary key
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_categories')  # Add related_name
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # hex color

class Schedule(models.Model):
    eventID = models.AutoField(primary_key=True)  # Add primary key
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_schedule')  # Add related_name
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='schedules')  # Add related_name
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # hex color

class Folders(models.Model):
    folderID = models.AutoField(primary_key=True)  
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_folders')  # Add related_name
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='folders')  # Add related_name
    title = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  

class Links(models.Model):
    folder = models.ForeignKey(Folders, on_delete=models.CASCADE, related_name='links', null=True)
    link = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_links')


class FolderLink(models.Model):
    folderLinksID = models.AutoField(primary_key=True)  # Add primary key
    folderID = models.ForeignKey(Folders, on_delete=models.CASCADE, related_name='folder_links')  # Add related_name
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE, related_name='folder_links')  # Add related_name

class Tags(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_tags', null=True)  # Add related_name
    folderID = models.ForeignKey(Folders, on_delete=models.CASCADE, related_name='folder_tags', null=True)  # Add related_name
    tagsID = models.AutoField(primary_key=True)  # Add primary key
    tag = models.CharField(max_length=50)



class LinksTag(models.Model):
    linksTagsID = models.AutoField(primary_key=True)  # Add primary key
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE, related_name='link_tags')  # Add related_name
    tagsID = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='tag_links')  # Add related_name
