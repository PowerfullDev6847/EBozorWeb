from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def main_page(request: HttpRequest):
    return HttpResponse(f"<h1 style='text-align: center;'><i>Home</i></h1><a href='/about/'>About</a> <a href='/contact/'>Contact</a>")

def about_page(request: HttpRequest):
    return HttpResponse("<h1 style='text-align: center;'>About Page</h1><a href='/'>Home</a> <a href='/contact/'>Contact</a>")

def contact_page(request: HttpRequest):
    return HttpResponse("<h1 style='text-align: center;'>Contact Page</h1><a href='/about/'>About</a> <a href='/'>Home</a>")

