from django.urls import path
from .views import IndexPageView, BookListView, InputBookView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('listbook/', BookListView.as_view(), name='listbook'),
    path('inputbook/', InputBookView.as_view(), name='input_book'),
]