from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse


def hello(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,'myapp/home.html',context)

class PostListView(ListView):
	model = Post
	template_name = 'myapp/home.html'
	context_object_name = 'posts'
	ordering = ['-date']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['book_name','content']

	def form_valid(self,form):
		form.instance.writer = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['book_name','content']

	def form_valid(self,form):
		form.instance.writer = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.writer:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/myapp'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.writer:
			return True
		return False

# Create your views here.
def about(request):
	return render(request,'myapp/about.html',{'title':'LOTS LOVE'})

