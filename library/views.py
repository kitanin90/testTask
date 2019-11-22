from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Assignment, Book, User
from .serializers import UserSerializer, BookSerializer, AssignmentSerializer


class AssignmentView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user'))
        book = get_object_or_404(Book, id=self.request.data.get('book'))
        return serializer.save(user=user, book=book)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
