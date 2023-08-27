from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Resume
import openai
import os


# Set your OpenAI API key

api_key = os.environ.get('API_KEY')

def generate_custom_resume(name, email, experience, skills, job_description):
    # Combine user input and job description to create the resume
    generated_resume = f"Name: {name}\nEmail: {email}\nExperience: {experience}\nSkills: {skills}\n\nJob Description:\n{job_description}"
    return generated_resume


def generate_resume(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        experience = request.POST.get('experience')
        skills_list = request.POST.getlist('skills[]')
        skills = ', '.join(skills_list)
        job_description = request.POST.get('job_description')
        
        # Generate the resume using your AI logic
        generated_resume = generate_custom_resume(name, email, experience, skills, job_description)
        
        # Save the generated resume to the database
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            resume = Resume(user=user, name=name, experience=experience, skills=skills, job_description=job_description, generated_resume=generated_resume)
            resume.save()

        # Return the generated resume content as a JSON response
        return JsonResponse({'success': True, 'generated_resume': generated_resume})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def home(request):
    # Implement your home view logic here
    return render(request, 'home.html')