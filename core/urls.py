from django.urls import path
from core import views

urlpatterns = [
    path('core/get_categories/', views.get_categories),
    path('core/last_entries/', views.last_entries),
    path('core/per_categories/<str:id>/', views.per_categories),
    path('core/article_details/<str:pk>/', views.article_details),
]