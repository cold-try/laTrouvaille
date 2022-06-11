from django.urls import path
from core import views

urlpatterns = [
    path('core/get_bestof/', views.get_bestof),
    path('core/get_categories/', views.get_categories),
    path('core/get_selection/', views.get_selection),
    path('core/last_entries/', views.last_entries),
    path('core/per_categories/<str:id>/', views.per_categories),
    path('core/article_details/<str:pk>/', views.article_details),
    path('core/send_commentary/', views.send_commentary),
    path('core/input-completion/', views.input_completion),
]