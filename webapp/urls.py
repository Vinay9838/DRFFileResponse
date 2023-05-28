from django.urls import path

from webapp import views

urlpatterns = [
 path('download-result/<str:res_type>',views.EmployeeViewSet.as_view(),name='employee_view')
]
