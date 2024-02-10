from django.urls import path
from .views import BookListView, FormSuccessView, BookCreateView, BookDetailView, BookFormView, BookUpdateView, \
    BookDeleteView, DeleteSuccessView

urlpatterns = [
    #path('', IndexView.as_view(), name='book_form'),
    path('book_form/', BookFormView.as_view(), name='book_form'),
    path('form_success/', FormSuccessView.as_view(), name='form_success'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('entry_success/', BookListView.as_view(), name='entry_success'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('delete_sucess/', DeleteSuccessView.as_view(), name='book_deletes'),

]
