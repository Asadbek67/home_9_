from django.urls import path
from . import views

urlpatterns = [
    path('type/<int:types_id>/', views.type_detail, name='type_detail'),

]
