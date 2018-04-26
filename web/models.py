from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Map(models.Model):
    SatelliteID=(
                    ('1','高分二号'),
                    ('2','高景一号'),
                    ('3','资源一号')
    )
    SatelliteID=models.CharField(max_length=20,choices=SatelliteID,default=False)
    Maptype=(
        ('1','多光谱'),
        ('2','全色彩'),
        ('3','融合')
    )
    Maptype=models.CharField(max_length=8,choices=Maptype,default=False,blank=True)
    SensorID=models.CharField(max_length=20,default=False,blank=True)
    ReceiveTime=models.DateField(default=False,blank=True)
    name=models.TextField(max_length=500,default=False,blank=True)
    Bands=models.IntegerField(default=False,blank=True)
    WidthInPixels=models.IntegerField(default=False,blank=True)
    HeightInPixels=models.IntegerField(default=False,blank=True)
    EarthEllipsoid=models.CharField(max_length=10,default=False,blank=True)
    TopLeftLatitude=models.FloatField(default=False,blank=True)
    TopLeftLongitude=models.FloatField(default=False,blank=True)
    TopRightLatitude=models.FloatField(default=False,blank=True)
    TopRightLongitude=models.FloatField(default=False,blank=True)
    BottomRightLatitude=models.FloatField(default=False,blank=True)
    BottomRightLongitude=models.FloatField(default=False,blank=True)
    BottomLeftLatitude=models.FloatField(default=False,blank=True)
    BottomLeftLongitude=models.FloatField(default=False,blank=True)
    filepath=models.TextField(max_length=500,default=False,blank=True)
    cut_row=models.IntegerField(default=False,blank=True)
    cut_col=models.IntegerField(default=False,blank=True)
    gen_date=models.DateField(default=False,blank=True)
    folder=models.TextField(max_length=500,default=False,blank=True)
    isPublish=models.BooleanField(default=False,blank=True)
    ProductLevel=models.CharField(max_length=10,default=False,blank=True)

class SliceMap(models.Model):
    index_raw=models.IntegerField()
    index_col=models.IntegerField()
    filepath=models.FileField()
    parent_map=models.ForeignKey(Map,on_delete=models.CASCADE)

class Myuser(AbstractUser):
    email=models.CharField(max_length=40,blank=True)
    first_name = models.CharField(max_length=20,default='a',blank=True)
    last_name = models.CharField(max_length=20, default='b',blank=True)
    is_active=models.BooleanField(default=True,blank=True)
    is_staff=models.BooleanField(default=True,blank=True)
    is_superuser=models.BooleanField(default=False,blank=True)
    date_joined=models.DateTimeField(blank=True,default=timezone.now)
    department_name=models.CharField(max_length=20,default='a',blank=True)
    contact_usr=models.CharField(max_length=20,blank=True,default='a')
    phone=models.CharField(max_length=20,blank=True,default='123')


    class Meta():
        permissions = (
            ("user_management", "用户管理"),
            ("ibuild_management", "违建管理"),
            ("demolition_management", "拆迁管理"),
            ("recource_management", "资源管理")
        )
#    def __str__(self):
#    # 在Python3中使用 def __str__(self):
#        return self.name

class GraphicLabel(models.Model):
    GraphicType=(
        ('1','建筑'),
        ('2','道路'),
        ('3','河流')
    )
    GraphicLabel = (
        ('1', '拆迁'),
        ('2', '违建')
    )
    name = models.CharField(max_length=16)
    grahpictype = models.CharField(max_length=4,choices=GraphicType)#地物类型如建筑、森林、河流
    grahpiclabel = models.CharField(max_length=4,choices=GraphicLabel)#标注类型如拆迁、违建
    context = models.TextField()#坐标数据
    discrib = models.TextField()
    square = models.FloatField(default=0)
    graphic_provide= models.ForeignKey(Myuser,on_delete=models.CASCADE)
    coordinate_x = models.FloatField(default=0)
    coordinate_y = models.FloatField(default=0)