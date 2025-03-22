from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import Book
from .serializers import AdminUserSerializer, BookSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

# Admin Registration API
class RegisterAdminView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# Admin Login API (Token Authentication)
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})



# List & Create Books (Admin)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

# Retrieve, Update, Delete Books (Admin)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# List Books (Student View - No Auth Required)
def StudentBookListView(request):
    books = Book.objects.all()
    return render(request, 'books/student_view.html', {'books': books})