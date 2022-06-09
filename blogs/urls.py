from django.urls import path, include
from blogs.views import BlogDetailView,  TagBasedBlogsView

urlpatterns = [
    path('<id>/', BlogDetailView.as_view(), name='blog'),
    path('tag/<tag>', TagBasedBlogsView.as_view(), name='tag based blog'),

]
