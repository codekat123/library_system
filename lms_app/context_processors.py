from .models import Books, category

def sidebar_data(request):
    return {
        'sidebar_books': Books.objects.all(),
        'sidebar_categories': category.objects.all(),
        # Add any other data you want to pass to the sidebar
    } 