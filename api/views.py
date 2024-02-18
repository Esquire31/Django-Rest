from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer
from .models import Course as course
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'To return all courses': '/courses',
        'To add a new course': '/courses/add',
        'Update a Course': '/courses/{CourseId}/update',
        'Delete a Course': '/courses/{CourseId}/delete'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_courses(request):
    courses = course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_courses(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_courses(request, id):
    try:
        task = course.objects.get(id=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(task, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Updated Successfully"
        return Response(data=data)
    return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_courses(request, id):
    try:
        task = course.objects.get(id=id)
    except task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(task, data=request.data)
    data = {}
    operation = task.delete()
    if operation:
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
