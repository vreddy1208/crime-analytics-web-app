from django.urls import path,include,re_path
from django.views.generic import ListView, DetailView
from updates.models import Post
from . import views

urlpatterns = [ path('', ListView.as_view(queryset=Post.objects.all().order_by("-date") [:25],
	template_name = "blog.html")),

				re_path(r'(?P<pk>\d+)', DetailView.as_view(model = Post,template_name='post.html')),
				path('port', views.port , name = 'port'),

				path('add', views.add_model , name = 'add_model'),
				


]
