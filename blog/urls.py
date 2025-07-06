from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    # path('', post_list, name='home'),
    # path('post/<int:post_id>/', post_detail, name='detail'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('post/new_post/', BlogCreateView.as_view(), name='post_new'),
    path('post/edit_post/<int:pk>/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/delete_post/<int:pk>/', BlogDeleteView.as_view(), name='post_delete')
]
