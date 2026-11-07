from django.contrib import admin

# import the model you want to register
from .models import Author, Blogpost, Books, Emp

# Register your models here.
admin.site.register(Emp)
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Blogpost)
