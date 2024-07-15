from django.urls import path
from . import views
# from .views import GetHomeData


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
    #  path('api/get_Home/', GetHomeData.as_view(), name='get_home_data'),
      path('get_Home/', views.HomeView.as_view(), name='get_kfi'),
    path('get_Dash/', views.DashView.as_view(), name='get_Dash'),
    path('get_Asset/', views.DashassetView.as_view(), name='get_Asset'),
    path('get_Oca/', views.DashocaView.as_view(), name='get_Oca'),
    path('get_Ratio/', views.DashratioView.as_view(), name='get_Ratio'),
    path('get_Wctl/', views.DashWctlView.as_view(), name='get_Wctl'),
    path('get_ff/', views.DashffView.as_view(), name='get_ff'),
    path('get_Datavisual/', views.DatavisualView.as_view(), name='get_Datavisual'),
    path('get_Datavisual1/', views.DatavisualView1.as_view(), name='get_Datavisual1'),
    path('get_Datavisual2/', views.DatavisualView2.as_view(), name='get_Datavisual2'),
    path('get_Datavisual3/', views.DatavisualView3.as_view(), name='get_Datavisual3'),
    path('get_Datavisual4/', views.DatavisualView4.as_view(), name='get_Datavisual4'),
    path('get_Datavisual5/', views.DatavisualView5.as_view(), name='get_Datavisual5'),
    path('get_Datavisual6/', views.DatavisualView6.as_view(), name='get_Datavisual6'),

]

