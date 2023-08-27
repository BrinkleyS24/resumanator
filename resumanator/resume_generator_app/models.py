from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'resume_generator_app'

# Define the Resume model
class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    job_description = models.TextField()
    generated_resume = models.TextField()  # Store the generated resume content

    def __str__(self):
        return self.name
