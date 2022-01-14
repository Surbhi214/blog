from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post , Category , Comment
from .forms import PostForm , UpdateForm , CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# def home(request):
    # return render(request, 'home.html')
# @login_required

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # category = Category.objects.fields(__all__)
    # ordering = ['-post_date']
    # ordering = ['-id']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats' : cats.title() , 'category_posts':category_posts} )

class Article_Detail_View(DetailView):
    model = (Post)
    template_name = 'article_deatils.html'
    # fields = ['comment']

class AddPostCreateView(CreateView):
    model = Post
    form_class= PostForm
    template_name = "add_post.html" 
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    # form_class= PostForm
    template_name = "add_category.html" 
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = "update_post.html"
    # fields = ['tittle' , 'tittle_tag' , 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

