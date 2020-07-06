from django.urls import path
from user import views
urlpatterns = [
    path('user_api/', views.UserAPIView.as_view()),
    path('emp/', views.EmployeeView.as_view()),
    path('emp/<str:id>', views.EmployeeView.as_view()),
    # path('check/', views.RegisterView.as_view({"get":"check_user"})),
]