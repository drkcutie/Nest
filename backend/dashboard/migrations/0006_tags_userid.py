# Generated by Django 5.1.1 on 2024-10-19 04:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_tags_folderid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_tags', to=settings.AUTH_USER_MODEL),
        ),
    ]
