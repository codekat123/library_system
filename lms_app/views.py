from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
def book(request):
               if 'search_name' in request.GET :
                       content = request.GET['search_name']
                       search = Books.objects.all()
                       if content:
                               search = search.filter(title__icontains = content)
                               
               context = {
                       'data':search,
                       'category':category.objects.all(),
               }
               return render(request, 'pages/books.html',context)
def index(request):
               if request.method == 'POST':
                       add_book = BookForm(request.POST,request.FILES)
                       add_category = CategoryForms(request.POST,request.FILES)
                       if add_category.is_valid():
                               add_category.save()
                       if add_book.is_valid() :
                               add_book.save()
               context = { 'form': BookForm(),
                       'books':Books.objects.all(),
                        'category':category.objects.all(),
                        'number_of_book':Books.objects.filter(active =True ).count(),
                        'available':Books.objects.filter(status = 'available' ).count(),
                        'sold':Books.objects.filter(status = 'sold' ).count(),
                        'rental':Books.objects.filter(status = 'rental' ).count(),
                        'formcat':CategoryForms(),

                        }
               return render(request, 'pages/index.html',context)

def update(request,id):
        book_id = Books.objects.get(id=id)
        if request.method == 'POST':
                book_save = BookForm(request.POST,request.FILES,instance=book_id)
                if book_save.is_valid():
                        book_save.save()
                        return redirect('/')
        else:
                book_save = BookForm(instance=book_id)
                context = {
                        'form':book_save
                }
        return render(request,'pages/update.html',context)
def delete(request,id):
        delete_book = get_object_or_404(Books,id=id)
        if request.method == 'POST':
                delete_book.delete()
                return redirect('/')
        return render(request,'pages/delete.html')
def side(request):
        data = {
                'data':category.objects.all()
        }
        return render(request,'parts/sidebar.html',data)
def base(request):
        data ={
                'books':Books.objects.all(),
        }
        return render(request , 'base.html' , data)