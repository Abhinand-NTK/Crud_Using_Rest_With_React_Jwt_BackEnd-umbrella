# from rest_framework.views import APIView  
# from rest_framework import permissions,status
# from rest_framework.response import Response
# from .serializers import UserCreateSerializer,UserSerializer
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.authentication import JWTAuthentication

# User = get_user_model()



# class RegisterView(APIView):
#     def post(self,request):
#         data = request.data

#         serializer = UserCreateSerializer(data=data)

#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#         user = serializer.create(serializer.validated_data)
#         user = UserSerializer(user)

#         return Response(user.data,status=status.HTTP_201_CREATED)

# class RetriveUserView(APIView):

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data, status=status.HTTP_200_OK)
    
# class AllUsersView(APIView):

#     authentication_classes = [JWTAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



from .serializers import UserSerializer,myTokenObtainPairSerializer
from .models import UserAccount
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = myTokenObtainPairSerializer

class UserRegister(CreateAPIView):
    serializer_class = UserSerializer

class UserList(ListCreateAPIView):
    queryset = UserAccount.objects.all().exclude(is_superuser=True)
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['email', 'first_name']

class UserDetails(RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    print("-------- view ----------")
    def get_object(self):
        user_id = self.kwargs.get('id')
        user = get_object_or_404(UserAccount, id=user_id)
        print("---------", user)
        return user

    def perform_update(self, serializer):
        # Your custom update logic in the serializer
        serializer.save()

