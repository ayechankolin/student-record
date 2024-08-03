# Generated by Django 5.0.6 on 2024-08-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_course_rename_record_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.TextField()),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.TextField()),
                ('gender', models.TextField()),
                ('experience', models.TextField()),
                ('address', models.TextField()),
                ('person_ID', models.TextField()),
                ('skill_set', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('fees_amount', models.TextField()),
                ('payment_status', models.TextField()),
            ],
        ),
    ]
