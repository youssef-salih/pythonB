from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from book_management.forms import BookForm
from django.urls import reverse_lazy


# Create your views here.

class BookListView(FormView):
    template_name = 'book_management/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('form_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Book Record Saved Successfully')
