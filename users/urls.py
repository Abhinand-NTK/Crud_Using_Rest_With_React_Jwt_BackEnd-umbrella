# from django.contrib import admin
# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('register/',RegisterView.as_view(),),
#     path('user/',RetriveUserView.as_view(),),
#     path('all-users/', AllUsersView.as_view(), name='all_users'),

# ]



from django.urls import path
from .views import UserList,UserDetails,MyTokenObtainPairView,UserRegister
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user-list/',UserList.as_view(),name='user_list'),
    path('user-detail/<int:id>/',UserDetails.as_view(),name='user_details'),
    path('user-register/', UserRegister.as_view(),name="user_register"),
]