from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'testapp/index.html')

def dynamic_content(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'testapp/dynamic.html', {'time': current_time})

def contact_form(request):
    return render(request, 'testapp/form.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        with open('submissions.txt', 'a') as file:
            file.write(f"Name: {name}, Email: {email}\n")
        return render(request, 'testapp/form.html', {'message': 'Form submitted successfully!'})
    return render(request, 'testapp/form.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse

def submit(request):
    if request.method == 'POST':
        # Process the submitted data
        name = request.POST.get('name')
        email = request.POST.get('email')
        # You can store this data or do something with it
        return HttpResponse(f"Received: {name}, {email}")
    else:
        return HttpResponse("Invalid request method.")
