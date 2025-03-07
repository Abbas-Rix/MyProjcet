# echolling /views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json 
from .forms import SignupForm

def index(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index.html', context)

def index2(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-two.html', context)

def index3(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-three.html', context)

def index4(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-four.html', context)
def index5(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-five.html', context)
def index6(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-six.html', context)
def index7(request):
    context = {
        'page_title': 'Home | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'index-seven.html', context)
def about(request):
    context = {
        'page_title': 'About | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'about.html', context)
def contact(request):
    context = {
        'page_title': 'Contact Us | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'contact.html', context)
def coureses_grid(request):
    context = {
        'page_title': 'Coureses Grid  | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'coureses-grid.html', context)
def coureses_list(request):
    context = {
        'page_title': 'Coureses List | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'coureses-list.html', context)
def coureses_right_sidebar(request):
    context = {
        'page_title': 'Coureses Right Sidebar | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'coureses-right-sidebar.html', context)
def coureses_single(request):
    context = {
        'page_title': 'Coureses Single | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'coureses-single.html', context)
def events_right_sidebar(request):
    context = {
        'page_title': 'Events Right Sidebar | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'events-right-sidebar.html', context)
def events_single(request):
    context = {
        'page_title': 'Events Single | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'events-single.html', context)
def events(request):
    context = {
        'page_title': 'Events | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'events.html', context)
def instructors(request):
    context = {
        'page_title': 'Instructors | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'instructors.html', context)
def login(request):
    context = {
        'page_title': 'Login | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'login.html', context)
def profile(request):
    context = {
        'page_title': 'Profile | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'profile.html', context)
def signup(request):
    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()
        
        # redirect('index')

    else:

        form = SignupForm()

        # try:
           
        #     email = request.POST.get('Email')
        #     username = request.POST.get('username')
        #     password = request.POST.get('password')
        #     Confirm_Password = request.POST.get('Confirm_Password')

        #     if password != Confirm_Password :

        #         return JsonResponse({"status": "error", "message": "Two mismatched passwords"})
            
        #     if User.oject.create_user(email=email).exists():

        #         return JsonResponse({"status": "error", "message": "The user already exists"})
            
        #     if user == User.object.create_user(username=username , email=email , password= password):

        #         form.save()

        #         return JsonResponse({"status": "error", "message": "Registration completed successfully"})
                
                
            
        # except Exception as e:

        #     return JsonResponse({"status": "error", "message": f"An error occurred :{str(e)}"})

        # return JsonResponse({"status": "error", "message": f"The request is invalid "}, status=400)

    # context = {
    #     'page_title': 'Sign Up | Echooling - Online Education Django Template',
    #     # 'greeting': 'Hello, Django World!'
    # }
    return render(request,'signup.html', {'form': form})

def blog_details(request):
    context = {
        'page_title': 'Blog Details | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'blog-details.html', context)
def blog(request):
    context = {
        'page_title': 'Blog | Echooling - Online Education Django Template',
        # 'greeting': 'Hello, Django World!'
    }
    return render(request, 'blog.html', context)