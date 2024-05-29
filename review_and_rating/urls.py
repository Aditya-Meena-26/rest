from django.urls import path
from . import views

urlpatterns = [
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
]