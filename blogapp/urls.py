
from django.urls import path
from .views import home,detail


urlpatterns = [
   path('',home,name='blog_home'),
   path('<int:blog_id/>',detail,name='detail'),
]