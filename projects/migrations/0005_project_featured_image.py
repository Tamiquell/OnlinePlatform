# Generated by Django 3.2.6 on 2021-08-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_demo_project_demo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='стхм.jpg', null=True, upload_to=''),
        ),
    ]
