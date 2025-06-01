from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import BookForm
def book(request):
               return render(request, 'pages/books.html')
def index(request):
               if request.method == 'POST':
                       add_book = BookForm(request.POST,request.FILES)
                       if add_book.is_valid() :
                               add_book.save()
               context = { 'form': BookForm(),
                       'books':books.objects.all()}
               return render(request, 'pages/index.html',context)

def update(request,id):
        book_id = books.objects.get(id=id)
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
        delete_book = get_object_or_404(books,id=id)
        if request.method == 'POST':
                delete_book.delete()
                redirect('/')
        return render(request,'pages/delete.html')