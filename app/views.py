from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import Teacher, Student, Group
from app.serializer import TeacherModelSerializer, StudentModelSerializer, GroupSerializer


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherModelSerializer(teachers, many=True)
        return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherModelSerializer(teacher)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
# @permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def teacher_update_delete(request, pk):
    try:
        teacher = Teacher.objects.filter(owner=request.user).get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherModelSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def teacher_update(request, pk):
    try:
        teacher = Teacher.objects.filter(owner=request.user).get(pk=pk)
    except Teacher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherModelSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherModelSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def group_detail(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def group_participants(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        students = Student.objects.all().filter(group=pk)
        return Response(StudentModelSerializer(students, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def teacher_students(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        students = Student.objects.all().filter(group=teacher.pk)
        return Response(StudentModelSerializer(students, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def group_list(request):
    if request.method == 'GET':
        if request.query_params.get('name'):
            groups = Group.objects.filter(
                name__contains=request.query_params.get('name'))
        else:
            groups = Group.objects.all()
        return Response(GroupSerializer(groups, many=True).data, status=status.HTTP_200_OK)
