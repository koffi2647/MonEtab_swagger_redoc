from django.urls import path, include
from rest_framework import routers


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .viewsets.student_viewset import StudentViewset
from .viewsets.teacher_viewset import TeacherViewset
from .viewsets.appSetting_viewset import AppSettingViewset
from .viewsets.school_viewset import SchoolViewset
from .viewsets.role_user_viewset import Role_user_viewset
from .viewsets.student_card_viewset import StudentCardViewset
from .viewsets.absence_viewset import AbsenseViewset
from .viewsets.custom_user_viewset import CustomUserViewset
from .viewsets.address_viewset import Address_Viewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
    TokenVerifyView,
)

app_name = 'api'


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'students', StudentViewset)
router.register(r'teachers', TeacherViewset)
router.register(r'AppSettings', AppSettingViewset)
router.register(r'school', SchoolViewset)
router.register(r'rolUser', Role_user_viewset)
router.register(r'studentCard', StudentCardViewset)
router.register(r'absence', AbsenseViewset)
router.register(r'customUser', CustomUserViewset)
router.register(r'Adress',Address_Viewset)



urlpatterns = [
    path('', include(router.urls)),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('token-sliding/', TokenObtainSlidingView.as_view(), name='token_obtain_sliding'),
    path('token-sliding/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh_sliding'),

    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   
    
 ]