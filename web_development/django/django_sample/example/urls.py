from django.urls import path
import example.views as views

urlpatterns = [
    path('sample-page', views.view_sample_page, name='sample_page'),
    path('template-sample', views.view_template_sample, name='template_sample'),  # Responds to the /template-sample url
]
