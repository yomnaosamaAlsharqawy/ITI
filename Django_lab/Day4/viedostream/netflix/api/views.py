from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from netflix.api.serializers import MoviesSerializers, UserSerializer
from netflix.models import Movies


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("netflix.view_movie")


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success": False,
                "errors": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "success": True,
            "message": "User has been created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", ])
@permission_classes([IsAuthenticated, IsManager])
def index(request):
    movies = Movies.objects.all()
    print(movies)
    serializer = MoviesSerializers(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class ListMovies(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers


class CreateMovie(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializers
    # permission_classes = [IsAuthenticated]
