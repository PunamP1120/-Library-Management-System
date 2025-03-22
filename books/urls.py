from django.urls import path
from .views import BookListCreateView, BookDetailView, StudentBookListView, RegisterAdminView, LoginView

urlpatterns = [
    path('register/', RegisterAdminView.as_view(), name='register-admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('students/books/', StudentBookListView, name='student-books'),
]
