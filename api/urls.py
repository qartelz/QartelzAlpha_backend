from django.urls import path
from . import views
from .views import GetHomeData


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('save_opstmt/', views.SaveOpstmtView.as_view(), name='save_opstmt'),
    path('save_assets/', views.SaveAssetsView.as_view(), name='save_assets'),
    path('save_oca/', views.SaveOcaView.as_view(), name='save_oca'),
    path('save_ratio/', views.SaveRatioView.as_view(), name='save_ratio'),
    path('save_wctl/', views.SaveWctlView.as_view(), name='save_wctl'),
    path('save_ff/', views.SaveFfView.as_view(), name='save_ff'),
    path('save_kfi/', views.SaveKfiView.as_view(), name='save_kfi'),
     path('api/get_Home/', GetHomeData.as_view(), name='get_home_data'),

]

