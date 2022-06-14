from django.urls import path
import example.views as views

urlpatterns = [
    path('sample-page', views.view_sample_page, name='sample_page'),
]
