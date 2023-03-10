from django.urls import path
from django.urls import path
from . import views

from users.views import profile

urlpatterns = [

    path('', views.profile, name='profile'),
    path('userprofile/<str:pk>/', views.userprofile, name='user-profile'),
    path('useraccount/', views.useraccount, name='user-account'),
    path('editprofile/<str:pk>', views.editprofile, name='edit-profile'),
    path('skills/', views.skillform, name='create-skills'),
    path('editskill/<str:pk>', views.editskills, name='edit-skill'),
    path('deleteskill/<str:pk>', views.deleteskills, name='delete-skill'),
    path('sendMessage/<str:pk>', views.sendMessage, name='send-message'),
    path('inbox/', views.inbox, name='inbox'),







]
