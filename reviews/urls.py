from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrivieveUpdateDestroyView


urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrivieveUpdateDestroyView.as_view(), name='review-detail-update-delete')
]
