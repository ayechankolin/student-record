# Generated by Django 5.0.6 on 2024-08-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_instructor_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_caption', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
            ],
        ),
    ]
