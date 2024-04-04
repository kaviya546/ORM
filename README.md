# Ex02 Django ORM Web Application
## Date: 03-04-2024
## AIM:
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram:
![dFYvL (1)](https://github.com/kaviya546/ORM/assets/150368823/42103218-1b41-4810-b908-d7dec1dc817f)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM:
# Models.py:
```
from django.db import models
from django.contrib import admin
class library(models.Model):
      serielno=models.IntegerField(primary_key=True);
      book_name=models.CharField(max_length=20);
      authorname=models.CharField(max_length=20);
      subject=models.CharField(max_length=50);
      publisher=models.CharField(max_length=10);
class libraryAdmin(admin.ModelAdmin):
      list_display=("serielno","book_name","authorname","subject","publisher");
```
# Admin.py:
```
from django.contrib import admin
from.models import library,libraryAdmin
admin.site.register(library,libraryAdmin)
```
## OUTPUT:
![Screenshot 2024-04-04 183413](https://github.com/kaviya546/ORM/assets/150368823/eee1bd81-a2b0-493a-8177-d52da6fd3123)

![Screenshot 2024-04-04 184747](https://github.com/kaviya546/ORM/assets/150368823/5095b3ab-8cd2-4a0b-bca7-f002680ad3c1)

## RESULT:
Thus the program for creating a database using ORM hass been executed successfully.
