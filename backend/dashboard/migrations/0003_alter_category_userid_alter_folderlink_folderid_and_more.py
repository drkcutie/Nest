# Generated by Django 5.1.1 on 2024-10-10 13:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='folderlink',
            name='folderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folder_links', to='dashboard.folders'),
        ),
        migrations.AlterField(
            model_name='folderlink',
            name='linkID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folder_links', to='dashboard.links'),
        ),
        migrations.AlterField(
            model_name='folders',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='folders',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_folders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='links',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_links', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='linkstag',
            name='linkID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_tags', to='dashboard.links'),
        ),
        migrations.AlterField(
            model_name='linkstag',
            name='tagsID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_links', to='dashboard.tags'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='dashboard.category'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
