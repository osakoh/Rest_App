from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Student
from .serializers import StudentSerializer


# function based view/endpoints
@api_view(['GET', 'POST'])
def student_list(request):
    """ Handles GET and POST request method i.e, non-primary key based operations """

    # retrieve all the students from the DB
    if request.method == 'GET':
        students = Student.objects.all()  # retrieves the student list from the DB
        # creates a serializer instance, specifying that a list of students will be received
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)  # returns a serialised data

    # creates a Student object and save in the DB
    elif request.method == 'POST':
        # deserialized the incoming data, passing the data from the request
        serializer = StudentSerializer(data=request.data)
        # check if what the user filled is valid and has been deserialized
        if serializer.is_valid():
            # save data
            serializer.save()
            # return a success status
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        else:
            # return an error status
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

