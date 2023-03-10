from django.urls import path

from . import views


urlpatterns = [

    path('', views.pro, name='pro'),

    path('project/<str:pk>/', views.sngle, name='sngle'),


    path('create-project', views.createproject, name='create-project'),
    path('update-project/<str:pk>', views.updateproject, name='update-project'),
    path('delete/<str:pk>', views.deleteproject, name='delete-project'),
    path('log', views.logproject, name='log-project'),
    path('welcome', views.welcomeproject, name='welcome-project'),
    path('logout', views.logoutproject, name='lougout'),
    path('regis', views.regproject, name='reg-project'),

    #path('review', views.reviewproject, name='review-project'),
    



]
