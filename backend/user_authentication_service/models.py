from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    # profile_pic = models.CharField(max_length=1000)
    # bio = models.CharField(max_length=255)
    #
    pass


class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # hex color


class Schedule(models.Model):
    eventID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # hex color


class Folders(models.Model):
    folderID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subheading = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # hex color


class Links(models.Model):
    link = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FolderLink(models.Model):
    folderLinksID = models.AutoField(primary_key=True)
    folderID = models.ForeignKey(Folders, on_delete=models.CASCADE)
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE)


class Tags(models.Model):
    tagsID = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=50)


class LinksTag(models.Model):
    linksTagsID = models.AutoField(primary_key=True)
    linkID = models.ForeignKey(Links, on_delete=models.CASCADE)
    tagsID = models.ForeignKey(Tags, on_delete=models.CASCADE)
