from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from user.models import User,Employee


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = "__all__"
        fields = ("username", "password", "real_name", "gender")
        extra_kwargs = {
            "username":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名必填",
                    "min_length":"用户名长度不够"
                },
            },
            "password":{
                "required":True,
                "min_length":6,
                "error_messages":{
                    "required":"密码必填",
                    "min_length":"密码长度不够"
                },
            },
            "real_name":{
                "required":True,
                "min_length":2,
                "write_only": True,
                "error_messages":{
                    "required":"真实姓名必填",
                    "min_length":"真实姓名长度不够"
                },
            },
            "gender":{
                "required":True,
                "write_only": True,
                "error_messages":{
                    "required":"性别必选",
                },
            },
        }

    def validate(self, attrs):
        username = attrs.get("username")
        re_username = User.objects.filter(username=username).first()
        if re_username:
            raise exceptions.ValidationError("用户已被注册")
        # password = attrs.get("password")
        # re_password = attrs.get("re_password")
        # attrs.pop("re_password")
        # # 两次密码不一致  无法保存
        # if password != re_password:
        #     raise exceptions.ValidationError("两次密码不一致")
        return attrs


# class EmployeeListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
#         for id, obj in enumerate(instance):
#             self.child.update(obj, validated_data[id])
#         return instance


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        # list_serializer_class = EmployeeListSerializer
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名必填",
                    "min_length": "用户名长度不够"
                },
            }
        }
