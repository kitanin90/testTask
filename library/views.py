from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Assignment, Book, User
from .serializers import UserSerializer, BookSerializer, AssignmentSerializer


class AssignmentView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response({"assignments": serializer.data})

    def post(self, request):
        assigment = request.data.get('assigment')
        serializer = AssignmentSerializer(data=assigment)

        if serializer.is_valid(raise_exception=True):
            assigment_saved = serializer.save()
        return Response({"Успешно": "Назначение '{} - {}' создано успешно".format(assigment_saved.book,
                                                                                  assigment_saved.name)})

    def put(self, request, pk):
        saved_assignment = get_object_or_404(Assignment.objects.all(), pk=pk)
        data = request.data.get('assignment')
        serializer = AssignmentSerializer(instance=saved_assignment, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            assigment_saved = serializer.save()
        return Response({"Успешно": "Изменены '{} - {}'".format(assigment_saved.book,
                                                                assigment_saved.name)})


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

    def post(self, request):
        book = request.data.get('book')
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"Успешно": "Книга '{}' добавлена успешно".format(book_saved.title)})

    def put(self, request, pk):
        saved_book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data.get('book')
        serializer = BookSerializer(instance=saved_book, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"Успешно": "Изменена книга - '{}'".format(book_saved.title)})


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"Успешно": "Пользователь '{}' добавлен успешно".format(user_saved.name)})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('book')
        serializer = BookSerializer(instance=saved_user, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"Успешно": "Изменен пользователь - '{}'".format(user_saved.name)})

