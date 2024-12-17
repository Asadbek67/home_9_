from django.urls import path
from . import views

urlpatterns = [
    path('type/<int:types_id>/', views.type_detail, name='type_detail'),
    path('flower/<int:flower_id>/', views.flower_detail, name='flower_detail'),
]
