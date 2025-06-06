from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',views.add_task,name='add_task'),
    path('edit/<int:task_id>/',views.edit_task,name = 'edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_status, name='toggle_status'),
    path('signup/', signup, name='signup'),
]