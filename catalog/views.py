from django.shortcuts import render

from .models import Book,Author,BookInstance, Genre
# Create your views here.

def index(request):
    """View function for home page of the site."""
    
    #Generate counts of some of the main objets
    
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    
    #Available books
    
    num_instances_avaialable=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    
    #Render the HTML template index.html with the data in the context variable 
    
    return render(request, 'index.html', context={'num_books':num_books, 'num_instances':num_instances,'num_instances_available':num_instances_avaialable,'num_authors':num_authors })
                                                                                                                                 
