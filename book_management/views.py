from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from book_management.forms import BookForm
from django.urls import reverse_lazy
from .models import Book


# Create your views here.
#class IndexView(View):
   # def get(self, request):
      # return render(request,"book_management/base.html")

class BookFormView(FormView):
    template_name = 'book_management/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('form_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Book Record Saved Successfully')


class EntrySuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Book entry success Record Saved Successfully')


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']

    success_url = reverse_lazy("form_success")


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_management/book_detail.html'


class BookListView(ListView):
    model = Book
    queryset = Book.objects.order_by('name')
    context_object_name = 'book_list'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_management/book_form.html'
    success_url = "/book_management/entry_success"


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_management/book_delete.html'
    success_url = reverse_lazy("book_deletes")


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Book Delete success Record Saved Successfully')
