from django.db import models
from django.utils import timezone

# Create your models here.

#自定义用户管理模型
class UsersManager(models.Manager):
    def get_queryset(self):
        return super(UsersManager, self).get_queryset().filter(isDelete=False)
    def createUser(self, userName, password, create, isAdmin=False, isDelete=False):
        user = self.model()
        #print(type(grade))
        user.userName = userName
        user.password = password
        user.createDate = create
        user.isDelete = isDelete
        user.isAdmin = isAdmin
        return user

class User(models.Model):
    #自定义模型管理器
    userManage = UsersManager()
    #用户名
    userName = models.CharField(max_length=20)
    #密码
    password = models.CharField(max_length=10)
    #用户角色
    isAdmin = models.BooleanField(default=False)
    #创建日期
    createDate = models.DateTimeField(default=timezone.now)
    #是否删除
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = "user"

    #定义一个类方法创建对象
    @classmethod
    def createUser(cls, userName, password, create=timezone.now(), isAdmin=False, isDelete=False):
        user = cls(userName = userName, password = password, createDate=create, isAdmin=False, isDelete=False)
        return user
