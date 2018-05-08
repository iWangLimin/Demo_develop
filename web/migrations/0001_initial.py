# Generated by Django 2.0.4 on 2018-05-07 02:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.CharField(blank=True, max_length=40)),
                ('first_name', models.CharField(blank=True, default='a', max_length=20)),
                ('last_name', models.CharField(blank=True, default='b', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('department_name', models.CharField(blank=True, default='a', max_length=20)),
                ('contact_usr', models.CharField(blank=True, default='a', max_length=20)),
                ('phone', models.CharField(blank=True, default='123', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('user_management', '用户管理'), ('ibuild_management', '违建管理'), ('demolition_management', '拆迁管理'), ('recource_management', '资源管理')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='GraphicLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('graphictype', models.CharField(choices=[('1', '建筑'), ('2', '道路'), ('3', '河流')], max_length=4)),
                ('graphiclabel', models.CharField(choices=[('1', '拆迁'), ('2', '违建')], max_length=4)),
                ('context', models.TextField()),
                ('discrib', models.TextField()),
                ('square', models.FloatField(default=0)),
                ('coordinate_x', models.FloatField(default=0)),
                ('coordinate_y', models.FloatField(default=0)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('graphicaddress', models.CharField(default='default', max_length=16)),
                ('graphic_provide', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GlobeID', models.IntegerField(default=0)),
                ('SatelliteID', models.CharField(choices=[('1', '高分二号'), ('2', '高景一号'), ('3', '资源一号')], default=False, max_length=20)),
                ('Maptype', models.CharField(blank=True, choices=[('1', '多光谱'), ('2', '全色彩'), ('3', '融合')], default=False, max_length=8)),
                ('SensorID', models.CharField(blank=True, default=False, max_length=20)),
                ('ReceiveTime', models.DateField(blank=True, default=False)),
                ('name', models.TextField(blank=True, default=False, max_length=500)),
                ('Bands', models.IntegerField(blank=True, default=False)),
                ('WidthInPixels', models.IntegerField(blank=True, default=False)),
                ('HeightInPixels', models.IntegerField(blank=True, default=False)),
                ('EarthEllipsoid', models.CharField(blank=True, default=False, max_length=10)),
                ('TopLeftLatitude', models.FloatField(blank=True, default=False)),
                ('TopLeftLongitude', models.FloatField(blank=True, default=False)),
                ('TopRightLatitude', models.FloatField(blank=True, default=False)),
                ('TopRightLongitude', models.FloatField(blank=True, default=False)),
                ('BottomRightLatitude', models.FloatField(blank=True, default=False)),
                ('BottomRightLongitude', models.FloatField(blank=True, default=False)),
                ('BottomLeftLatitude', models.FloatField(blank=True, default=False)),
                ('BottomLeftLongitude', models.FloatField(blank=True, default=False)),
                ('filepath', models.TextField(blank=True, default=False, max_length=500)),
                ('cut_row', models.IntegerField(blank=True, default=False)),
                ('cut_col', models.IntegerField(blank=True, default=False)),
                ('gen_date', models.DateField(blank=True, default=False)),
                ('folder', models.TextField(blank=True, default=False, max_length=500)),
                ('isPublish', models.BooleanField(default=False)),
                ('ProductLevel', models.CharField(blank=True, default=False, max_length=10)),
                ('ImageDesc', models.TextField(default='Describe This Image', max_length=500)),
                ('IsUnit8', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SliceMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_raw', models.IntegerField()),
                ('index_col', models.IntegerField()),
                ('filepath', models.FileField(upload_to='')),
                ('parent_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Map')),
            ],
        ),
    ]
