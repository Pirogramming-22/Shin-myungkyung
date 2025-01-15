from django.urls import path
from apps.idea import views

app_name = 'idea'

urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update-interest/', views.update_interest, name='update_interest'),
    path('<int:idea_id>/toggle_like/', views.toggle_like, name='toggle_like'),
]