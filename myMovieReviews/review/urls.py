from django.urls import path
from .views import *
from . import views

app_name = 'review'

urlpatterns = [
    # 기본 경로
    path('', review_list, name='review_list'),  

    #리스트 url
    #path('list/', review_list, name='review_list'),

    #create url
    path('create/', review_create, name='review_create'),

    #detail url
    path('detail/<int:pk>', review_detail, name='review_detail'),

    #update url
    path('update/<int:pk>', review_update, name='review_update'),

    #delete url
    path('delete/<int:pk>', review_delete, name='review_delete')
]

# 요청 -> config/urls.py -> review.urls -> review_list -> review/list.html