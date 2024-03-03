from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('save/', views.save_data, name = 'save-page'),
    path('delete/', views.delete_data, name = 'delete-page'),
    path('edit/', views.edit_data, name = 'edit-page'),
]
