from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

#list create lists all notes the user created or  create a new nod
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        #editing the serializer to incldue the readonly data, like the author
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
        
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    #list of all users that already exist
    queryset = User.objects.all()
    #what stuff we need to know to create a new user
    serializer_class = UserSerializer
    #any user can use this to create a new user
    permission_classes = [AllowAny]

