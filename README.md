## Create The Project Directory 📁
```
mkdir Website
```
## Create Virtualenv For Your Owner Project 📁
```
python -m venv backend
```
## Activate Your Virtualenv => [ ✔️ ]
```
backend\Scripts\activate
```
## Install Django => [ 📦 ]
```
pip install django
```
## Create A Django Project => [ ✔️ ]
```
django-admin startproject backend .
```
## Create An App => [ 💻 ]
```
python manage.py startapp library
```
Run Server => [ 💻 ]
```
python manage.py runserver
```
## [ Go To ] 👉️
```
http://127.0.0.1:8000/
```
## [ Go To ] 👉️
```
http://127.0.0.1:8000/admin/
```
## Add Your App To Settings.py In Project => [ 📝 ]
```
INSTALLED_APPS = [
    'library',
    # . . .
]
```
## Add Your App To Urls.py In Project => [ 📝 ]
```
from django.urls import include
urlpatterns = [
    path('', include('library.urls')),
]
```
## Create File urls.py In Side App => [ 📝 ]
```
urls.py
```
```
from django.urls import path
from . import views
urlpatterns = [
  path('', views.library, name='library'),
]
```
## Create Templates Folder => [ 📁 ]
```
📁 backend
📁 library
📁 templates
  📁 pages
  └── 📝 books.html
  └── 📝 delete.html
  └── 📝 index.html
  └── 📝 update.html
  📁 parts
  └── 📝 footer.html
  └── 📝 navbar.html
  └── 📝 sidbar.html
  └── 📝 head.html

templates\base.html
pages\books.html
delete.html
index.html
update.html
parts\footer.html
navbar.html
sidbar.html
head.html
```
## Style Of Page [ base.html ] => [ 📝 ]
```
<!DOCTYPE html>
<html  lang="en">
  <head>
    {% include 'parts/head.html' %}
  </head>
  <body>
    {% include 'parts/navbar.html' %}
    {% include 'parts/sidbar.html' %}
    {% block content %}
    {% endblock content %}
    {% include 'parts/footer.html' %}
  </body>
</html>
```
## Style Of Page [ navbar.html ] => [ 📝 ]
```
<nav>
</nav>
```
## Style Of Page [ sidebar.html ] => [ 📝 ]
```
<aside>
</aside>
```
## Style Of Page [ footer.html ] => [ 📝 ]
```
<footer>
</footer>
```
## Style Of Page [ index.html ] => [ 📝 ]
```
{% extends "base.html" %}
{% block content %}
<div class="content-wrapper">
</div>
{% endblock content %}

```
## Edite Views File In Side App => [ 📝 ] 
```
from django.shortcuts import render
# Create your views here.
def library(request):
  return render(request, 'index.html')
```
## Add Your Templates To Settings.py In Project => [ 🖥️ ]
```
import os
```
```
TEMPLATES = [
  {
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    # ...
  },
]
```
________________
## Create Static Folder => [ 📁 ]
```
📁 website
  📁 backend
    📁 static
      ├── 📁 css
      │   └── 📝 style.css
      ├── 📁 js
      │   └── 📝 script.js
      └── 📁 images

static/css/style.css
js/script.js
images
```
## Add Your Static To Settings.py In Project => [ 🖥️ ]
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'backend/static')
]
```
### Collect Static Files  => [ 📁 ]
```
python manage.py collectstatic
```
### How To Use [ 👌 ]
```
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/script.js' %}"></script>
<img src="{% static 'images/1.png' %}">
```
_____________________________
### Create Model [ 📝 ]
```

```
### Install Pillow If You Use Image Data [ 🖥️ ]
```
pip install pillow
```
#### Send Model(Class) To Django [ 🖥️ ]
```
python manage.py makemigrations
```
#### Send Django Model(Class) To Admin Page
```
python manage.py migrate
```
_____________________________
### Create a superuser to access the admin [ 🖥️ ]
```
python manage.py createsuperuser
```
```
admin
admin@yahoo.com
kb216407
```
### Admin File Inside App 
> ##### Your Path => [ 📍 ] E:Website\backend\library\admin.py
```
# Import Classes From Page Models
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
```
_____________________________
### Edite Media
##### Open File Setting.py
```
# Media إعدادات ال 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
##### Open File urls.py In Project
```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static  import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```
_____________________________
## Get Data To Html
#### Open File Views.py In App [ 📝 ]
```
from django.shortcuts import render
from .models import *  # noqa: F403

def index(request):
  # كل المنتجات
  AllItems = {
    'items':Book.objects.all()  # noqa: F405
    }  
  return render(request, 'pages/index.html', AllItems)
```
#### Open File index.html In Templates [ 📝 ]
```
<ul class="nav">
  {% for cat in category|slice:'5' %}
  <li>
    <a>{{cat.name}}</a>
  </li>
  {% endfor %}
</ul>
<!-- Start Book (Item) -->
<div class="">
  {% for item in items %}
    {% if item.book_photo %}
      <div style="background: url({{item.book_photo.url}});">
    {% else %}
      <div class="bg-info">
    {% endif %}
      </div>
  <div>{{item.title|slice:5}}</div>
  <div>{{item.author|slice:5}}</div>
  {% endfor %}
</div>
```
_____________________________
## Send Book Data From Index Like Admin Page
#### 1 - Create File Forms.py In App
```
forms.py
```
#### Edite File forms.py
```
from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # All Form In Model Book
        # fields = '__all__'
        # Get Single Input In Sild Form
        fields = [
            "title",
            "author",
            "book_photo",
        ]
        # Add Attribute To Element 
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "author": forms.TextInput(attrs={'class':'form-control'}),
            "book_photo": forms.FileInput(attrs={'class':'form-control'}),
        }
```
#### 2 - Open File Views.py  - 
```
from django.shortcuts import render
from .models import *  # noqa: F403
from .forms import BookForm

def library(request):
  return render(request, 'pages/index.html')

def index(request):
  if request.method == 'POST':
    add_book = BookForm(request.POST, request.FILES)
    if add_book.is_valid():
      add_book.save()
  # كل المنتجات
  AllItems = {
    'items':Book.objects.all(),  # noqa: F405
    'category':Category.objects.all()  ,# noqa: F405
    'form': BookForm()
    }  
  return render(request, 'pages/index.html', AllItems)

def books(request):
  AllItems = {
    'items':Book.objects.all(),  # noqa: F405
    'category':Category.objects.all()  # noqa: F405
    }  
  return render(request, 'pages/books.html', AllItems)
```
#### 3 - Open File Index.html To Adding New Form Models [ 📁 ]
```
<form method="POST" enctype="multipart/form-data">
  <div>              
    {{form}}
    <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
  </div>
  <div>
    <button type="submit" >اضافة</button>
  </div>
</form>
```
_____________________________
## Send Category Data From Index Like Admin Page
#### 1 -  Edite File forms.py
```
from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # All Form In Model Book
        # fields = '__all__'
        # Get Single Input In Sild Form
        fields = [
            "title",
            "author",
            "book_photo",
        ]
        widgets = {
          "title": forms.TextInput(attrs={'class':'form-control'}),
            "author": forms.TextInput(attrs={'class':'form-control'}),
            "book_photo": forms.FileInput(attrs={'class':'form-control'}),
        }

# 
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # All Form In Model Book
        # fields = '__all__'
        # Get Single Input In Sild Form
        fields = [
            "name",
        ]
        # Add Attribute To Element 
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
        }
```
#### 2 - Open File Views.py  - 
```
from django.shortcuts import render
from .models import *  # noqa: F403
from .forms import BookForm, CategoryForm

def library(request):
  return render(request, 'pages/index.html')

def index(request):
  if request.method == 'POST':
    # Add Book
    add_book = BookForm(request.POST, request.FILES)
    if add_book.is_valid():
      add_book.save()
    
    # Add Category
    add_category = CategoryForm(request.POST)
    if add_category.is_valid():
      add_category.save()
  
  # كل المنتجات
  AllItems = {
    'items':Book.objects.all(),  # noqa: F405
    'category':Category.objects.all()  ,# noqa: F405
    'form': BookForm(),
    'formCategory': CategoryForm(),
    }  
  return render(request, 'pages/index.html', AllItems)

def books(request):
  AllItems = {
    'items':Book.objects.all(),  # noqa: F405
    'category':Category.objects.all()  # noqa: F405
    }  
  return render(request, 'pages/books.html', AllItems)

  
```

#### 3 - Open File Sidbar.html To Adding New Form Models [ 📁 ]
```
<form method="POST" enctype="multipart/form-data">
  <div>              
    {{formCategory}}
    <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
  </div>
  <div>
    <button type="submit" >اضافة</button>
  </div>
</form>
```
_____________________________
## Update Item
#### 1 - Create Path Open File urls.py Inside Project
```
from django.urls import path
from . import views
urlpatterns = [
  path('library', views.library, name='library'),
  path('', views.index, name='index'),
  path('books', views.books, name='books'),
  path('update/<int:id>', views.update, name='update'),
]
```
#### 2 - Open File Index.html [ 📝 ]
```
<a href="{% url 'update' item.id %}">تعديل</a>
```
#### 3 - Open File Views.py Inside App [ 📝 ]
```
from django.shortcuts import render
from django.shortcuts import redirect

from .models import *  # noqa: F403

from .forms import BookForm, CategoryForm

def library(request):
    return render(request, "pages/index.html")

def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        # Add
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    # كل المنتجات
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
        "form": BookForm(),
        "formCategory": CategoryForm(),
    }
    return render(request, "pages/index.html", AllItems)

def books(request):
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
    }
    return render(request, "pages/books.html", AllItems)

def update(request, id):
    # Get Item Of Id
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")
    else:
        book_save = BookForm(instance=book_id)
    # كل المنتجات
    AllItems = {
        "itemUpdate": book_save,
    }
    return render(request, "pages/update.html", AllItems)

```
_____________________________
_____________________________
## Delete Item 
#### 1 - Create Path Open File urls.py Inside Project [ 📝 ]
```
from django.urls import path
from . import views

urlpatterns = [
    path("library", views.library, name="library"),
    path("", views.index, name="index"),
    path("books", views.books, name="books"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
```

#### 2 - Open File Index.html [ 📝 ]
```
<a href="{% url 'delete' item.id %}">حذف</a>
```
#### 3 - Open File Views.py Inside App [ 📝 ]
```
from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

from .models import *  # noqa: F403
# from .models import Book, Category

from .forms import BookForm, CategoryForm

def library(request):
    return render(request, "pages/index.html")

def index(request):
    if request.method == "POST":
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        # Add
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    # كل المنتجات
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
        "form": BookForm(),
        "formCategory": CategoryForm(),
    }
    return render(request, "pages/index.html", AllItems)

def books(request):
    AllItems = {
        "items": Book.objects.all(),  # noqa: F405
        "category": Category.objects.all(),  # noqa: F405
    }
    return render(request, "pages/books.html", AllItems)


def update(request, id):
    # Get Item Of Id
    book_id = Book.objects.get(id=id)
    if request.method == "POST":
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")
    else:
        book_save = BookForm(instance=book_id)
    # كل المنتجات
    AllItems = {
        "itemUpdate": book_save,
    }
    return render(request, "pages/update.html", AllItems)


def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book_delete.delete()
        return redirect("/")
    return render(request, "pages/delete.html")
```

_____________________________
_____________________________
## Configure category links in the navbar
### تهيئة روابط ال Category و الروابط بشكل عام في الموقع
### 1 - Open File Index.html [ 📝 ]
#### اضافة كلاس لكل عنصر من عناصر الاقصام عن طريق ال Id
```
<ul class="nav">
  {% for cat in category|slice:'5' %}
  <li class="nav-item cat{{cat.id}}">
    <a id="" class="nav-link bg-primary" href="#">{{cat.name}}</a>
  </li>
  {% endfor %}
</ul>
```
#### اضافة كلاس على كل عنصر من عناصر الكتاب الكلاس الاول لاخفاء جميع الكتب و الكلاس الثانى لاظهار الكتب اللى ال Id بيساوى ال الخاص بى نوع من انواع الاقسام
```
{% for item in items %}
<div class="bookHide book{{item.category.id}} book{{item.status}}">
</div>
```
### 2 - Open File Sidebar.html [ 📝 ]
```
{% for cat in category %}
<li class="cat{{cat.id}}"></li>
{% endfor %}

<li class="nav-item statussold">
</li>
<li class="nav-item statusrental">
</li>
<li class="nav-item statusavailable">
</li>
<!-- Linke Index -->
<a href="{% url 'index' %}" >Home</a>
<a href="{% url 'books' %}" >Books</a>

```
### 3 - Open File Script.html [ 📝 ]
#### Add a JavaScript function to hide and show elements based on categories
#### أضف وظيفة JavaScript لإخفاء العناصر وإظهارها بناءً على الفئات
```
<script>
  {% for item in items %}
  $(".cat{{item.category.id}}").click(function(){
    $(".bookHide").hide()
    $(".book{{item.category.id}}").show()
  })
  $(".status{{item.status}}").click(function(){
    $(".bookHide").hide()
    $(".book{{item.status}}").show()
  })
  {% endfor %}
</script>
```

_____________________________
_____________________________
_____________________________
# Usfull Commends 
```
backend\Scripts\activate
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

_____________________________
_____________________________
_____________________________

## Update Project On Github
- Create Repository
- Clone the repository from your account to your local machine using this command: `git clone https
://github.com/[YourUsername]/LibraryManagementSystem.git`

_____________________________
_____________________________
_____________________________
## Deploy Django On Pythonanywhere 

### 1. Go To => [ https://www.pythonanywhere.com ] 🌍
### 2. Click On Pricing [ 🖱️ ]
### 3. Click On Create Beginner Account [ 🖱️ ]
### 3. Sign Up/Log In to PythonAnywhere
### 4. Create On Bash
### 5. Clone The Repository
```
pwd
git clone https://github.com/LearnCodingEasy/management_system
mkvirtualenv --python=/usr/bin/python3.9 backend
pip install django
```
### 6. Go To Dashboard [ https://www.pythonanywhere.com/user/rashadhossamrashad/ ] 
### 7. Click On Open Web Tab
### 8. Click To [ Add a New Web App ]
### 9. Your Web App's Domain Name [ Click On Next ]
### 10. Select a Python Web Framework [ Click On Menual Configuration ]
### 11. Select Python Varsion [ Click On Python 3.10 ]
### 12. Manual Configuration [ Click On Next ]
### 13. New You Are On Page [ https://www.pythonanywhere.com/user/rashadhossamrashad/webapps/#tab_id_rashadhossamrashad_pythonanywhere_com ]
### 14. Go To Virtualenv  Location On Page And Type [ backend ]
### 15. Click On WSGI configuration file
### 16. Type This
```
# This file contains the WSGI configuration required to serve up your
# web application at http://rashadhossamrashad.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/rashadhossamrashad/mysite/mysite/settings.py'
## and your manage.py is is at '/home/rashadhossamrashad/mysite/manage.py'
path = '/home/rashadhossamrashad/mysite'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
### 17. Go To Bash 
```
cd management_system
```
### 18. Get Your Path 
```
pwd
```
### 19. Copy The Output And Paste Into `Path` Variable At PythonAnyWhere In `WSGI Configuration File`.
```
/home/rashadhossamrashad/management_system
```
### 20. Go To 
```
https://www.pythonanywhere.com/user/rashadhossamrashad/files/var/www/rashadhossamrashad_pythonanywhere_com_wsgi.py?edit
```
### 21. Chenge Path To 
```
/home/rashadhossamrashad/management_system
```
### 22. Chinge [os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'] To [os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings']
### 23. Click On Save
### 24. Go To 
```
https://www.pythonanywhere.com/user/rashadhossamrashad/files/home/rashadhossamrashad
```
### 25. Click On Your Project 
### 26. Go To Setting.py 
### 27. Add This Line In Settings Py
```
ALLOWED_HOSTS = ['rashadhossamrashad.pythonanywhere.com']
```
### 28. Save It.
### 29. Go To [https://www.pythonanywhere.com/user/rashadhossamrashad/webapps/#tab_id_rashadhossamrashad_pythonanywhere_com] 
### 30. Click On Reload 
### 31. Click On [ http://rashadhossamrashad.pythonanywhere.com/ ]
##################################
##################################
##################################
##################################

### قم بتثبيت المكتبات المطلوبة:
```
pip freeze > requirements.txt
```
