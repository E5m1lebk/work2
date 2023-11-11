from django.shortcuts import render

from blog.form import AuthorForm 

def index_view(request):
    return render(request, 'index.html')


def Blog_list_view(request):
    return render(request, 'Blog_list.html')


def add_author_view(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST) 
        
        if author_form.is_valid():
          author_form.save()
        
    else: 
        author_form = AuthorForm()   
      
    context = {
    'form':author_form,
    } 
    
    return render(request= "add_author.html" context,) # type: ignore
      
      

