from django.shortcuts import render
from portfolio.serializers import CategorySerializer,ProjectSerializer,ImageSerializer
from rest_framework import status
from portfolio.models import Category,Project,Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.




@api_view(['GET','POST'])
def categoryList(request):

      if request.method=='GET':
          categories = Category.objects.all()
          serialized_data = CategorySerializer(categories,many=True)
          return Response(serialized_data.data,status=status.HTTP_200_OK)

      elif request.method=='POST':
           serialized_data = CategorySerializer(data=request.data)
           if serialized_data.is_valid():
             serialized_data.save()
             return Response(serialized_data.data,status=status.HTTP_201_CREATED)

           else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def categoryDetail(request,pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'message':'category not found'},status=status.HTTP_400_BAD_REQUEST)
    

    if request.method=='GET':
        serialized_data = CategorySerializer(category)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialized_data = CategorySerializer(category,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def ProjectList(request):
    if request.method=='GET':
        projects = Project.objects.all()
        serialized_data = ProjectSerializer(projects,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
         serialized_data = ProjectSerializer(data=request.data)

         if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
         else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ProjectDetail(request,pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'message':'project not found'},status=status.HTTP_400_BAD_REQUEST)
    

    if request.method=='GET':
        serialized_data = ProjectSerializer(project)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialized_data = ProjectSerializer(project,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def ImageList(request):
    if request.method=='GET':
        try:
           images = Image.objects.get(project__id=request.data['project_id'])
        except:
            images = Image.objects.all()
        serialized_data = ImageSerializer(images,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
         serialized_data = ImageSerializer(data=request.data)

         if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
         else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def ImageDetail(request,pk):
    try:
        image = Image.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response({'message':'image not found'},status=status.HTTP_400_BAD_REQUEST)
    

    if request.method=='GET':
        serialized_data = ImageSerializer(image)
        return Response(serialized_data.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialized_data = ProjectSerializer(image,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_200_OK)
        else:
              return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

