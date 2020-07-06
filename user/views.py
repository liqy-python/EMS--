from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.viewsets import ViewSet

from user.serializers import UserModelSerializer,EmployeeModelSerializer
from rest_framework.views import APIView
from utils.response import APIResponse
from user.models import User, Employee


# Create your views here.


class UserAPIView(APIView):
    # 用户注册
    def post(self,request,*args,**kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        return APIResponse(200,True,results=UserModelSerializer(user_obj).data)

    # 用户登录
    def get(self,request,*args,**kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        user = User.objects.filter(username=username,password=password).first()
        if user:
            data = UserModelSerializer(user).data
            return APIResponse(200, True,results=data)
        return APIResponse(400,False)


class EmployeeView(ListModelMixin,CreateModelMixin,GenericAPIView,DestroyModelMixin,RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        emp_id = kwargs.get("id")
        user_list = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=user_list.data)

    # 增加
    def post(self, request, *args, **kwargs):
        emp_id = kwargs.get("id")
        print(emp_id)
        if "emp_id" in kwargs:
            emp_obj = Employee.objects.get(pk=emp_id)
            emp_obj.delete()
            response = self.create(request, *args, **kwargs)
            return APIResponse(200, True, results=response.data)
        else:
            user_obj = self.create(request, *args, **kwargs)
            return APIResponse(200, True, results=user_obj.data)

    # 删除
    def delete(self, request, *args, **kwargs):
        emp_id = kwargs.get("id")
        print(emp_id)
        response = self.destroy(request, *args, **kwargs)
        if response:
            return APIResponse(200, True, results=response.data)
