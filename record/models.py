from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.TextField()
    gender = models.TextField()
    experience = models.TextField()
    address = models.TextField()
    guardian = models.CharField(max_length=255)
    guardian_phone_number = models.TextField()
    person_ID = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_duration = models.TextField()
    course_schedule = models.TextField()
    course_level = models.TextField()
    course_instructor = models.CharField(max_length=255)
    course_requirement = models.TextField()
    course_participant_count = models.TextField()

    def __str__(self):
        return self.course_name

class Registration(models.Model):
    course_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    fees_amount = models.TextField()
    payment_status = models.TextField()

    def __str__(self):
        return self.name

class Instructor(models.Model):

    name = models.CharField(max_length=255)
    age = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.TextField()
    gender = models.TextField()
    experience = models.TextField()
    address = models.TextField()
    person_ID = models.TextField()
    skill_set = models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):

    blog_title = models.CharField(max_length=255)
    blog_caption = models.CharField(max_length=255)
    purpose = models.TextField()