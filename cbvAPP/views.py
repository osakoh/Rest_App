from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer


class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)  # returns a serialised data

    def post(self, request):
        # deserialized the incoming data, passing the data from the request
        serializer = StudentSerializer(data=request.data)
        # check if what the user filled is valid and has been deserialized
        if serializer.is_valid():
            # save data
            serializer.save()
            # return a success status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:  # serializer's not valid
            # return an error status
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def get_object(self, pk):
        # first retrieve the student with the specified primary key
        try:
            return Student.objects.get(pk=pk)  # retrieve a single student
        except Student.DoesNotExist:  # handles the case were a Student is not found
            raise Http404
        # student = get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)  # create a serialized student object
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)  # overrides the current student data
        if serializer.is_valid():  # check if valid
            serializer.save()  # save to DB
            return Response(serializer.data)
        else:  # serializer's not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
