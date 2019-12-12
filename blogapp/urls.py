
from django.urls import path
from .views import home,detail, BlogCreateView

app_name='blogapp'

urlpatterns = [
   path('',home,name='blog_home'),
   path('blogapp/<int:id>/',detail,name='detail'),
   path('create/', BlogCreateView.as_view(), name='blog_create')

]