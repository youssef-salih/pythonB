from django.urls import path
from .views import BookListView, FormSuccessView

urlpatterns = [
    path('book_form/', BookListView.as_view(), name='book_form'),
    path('form_success/', FormSuccessView.as_view(), name='form_success'),
]
