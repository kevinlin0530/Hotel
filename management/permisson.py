from rest_framework import permissions


#!　判定使用者是否為代理
class IsOwnerOrAgent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or obj.agent == request.user