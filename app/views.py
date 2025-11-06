from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#local
from .models import Classroom, Student
from .serializers import ClassroomSerializers, StudentSerializers

@api_view(['GET'])
def classroom_list(req):
    classroom = Classroom.objects.all()
    serializer = ClassroomSerializers(classroom, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createClassroom(req):
    serializer = ClassroomSerializers(data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_class(req, pk):
    try:
        classroom = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return Response({'error':"Class No"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ClassroomSerializers(classroom,data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def classroom_delete(req, pk):
    try:
        classroom = Classroom.objects.get(pk=pk)
    except Classroom.DoesNotExist:
        return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)
    classroom.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
        

# STUDENT -------------------STUDENT -------------------STUDENT -------------------STUDENT -------------------STUDENT -------------------STUDENT


@api_view(['GET'])
def student_list(req):
    student = Student.objects.all()
    serializer = StudentSerializers(student, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createStudent(req):
    serializer = StudentSerializers(data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_student(req, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error':"Student No"}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializers(student, data = req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])
def student_delete(req, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
        

# Create your views here.
