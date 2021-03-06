# Generated by Django 3.2.8 on 2022-05-16 13:31

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户账户')),
                ('password', models.CharField(max_length=255, verbose_name='用户密码')),
                ('nickname', models.CharField(blank=True, default='个人账户', max_length=20, verbose_name='用户名称')),
                ('score', models.IntegerField(default=10, verbose_name='个人积分')),
                ('login_time', models.DateField(auto_now_add=True, verbose_name='上次登录时间')),
                ('photo', models.ImageField(default='img1/default.jpg', null=True, upload_to=user.models.img1_save_path, verbose_name='个人头像')),
                ('violation', models.IntegerField(default=0, verbose_name='违规次数')),
                ('continuous', models.IntegerField(default=1, verbose_name='连续登入天数')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False, verbose_name='文件编号')),
                ('fname', models.CharField(max_length=50, verbose_name='文件名称')),
                ('ave_score', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='评分')),
                ('comment_times', models.IntegerField(default=0, verbose_name='评论次数')),
                ('sum_score', models.IntegerField(default=0, verbose_name='评分总数')),
                ('download_times', models.IntegerField(default=0, verbose_name='下载次数')),
                ('collection_times', models.IntegerField(default=0, verbose_name='收藏次数')),
                ('f_fees', models.IntegerField(default=0, verbose_name='消耗积分')),
                ('file', models.FileField(upload_to=user.models.file_save_path, verbose_name='文件地址')),
                ('publisher', models.CharField(max_length=40, null=True, verbose_name='出版社')),
                ('ISBN_num', models.CharField(max_length=40, null=True, verbose_name='ISBN码')),
                ('category', models.CharField(max_length=40, verbose_name='类别')),
                ('content', models.TextField(null=True, verbose_name='简介')),
                ('isvalid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('file_photo', models.ImageField(default='img2/default.jpg', upload_to=user.models.img2_save_path, verbose_name='书籍头像')),
                ('uploader', models.ForeignKey(db_column='uploader', on_delete=django.db.models.deletion.CASCADE, related_name='userid_0', to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
            ],
            options={
                'verbose_name': '文件表',
                'db_table': 'myfiles',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, verbose_name='用户令牌')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'user_token',
            },
        ),
        migrations.CreateModel(
            name='ReportInfo',
            fields=[
                ('reportid', models.AutoField(db_column='reportid', primary_key=True, serialize=False, verbose_name='举报编号')),
                ('Reporttime', models.DateTimeField(default=datetime.datetime.now, verbose_name='举报时间')),
                ('details', models.TextField()),
                ('range', models.CharField(max_length=20, verbose_name='违规范围')),
                ('isdealt', models.BooleanField(default=False, verbose_name='是否处理1')),
                ('adminstrate', models.IntegerField(null=True, verbose_name='处理人1')),
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.CASCADE, related_name='fid_4', to='user.fileinfo')),
                ('imformer', models.ForeignKey(db_column='imformer', on_delete=django.db.models.deletion.CASCADE, related_name='imformer_id', to=settings.AUTH_USER_MODEL)),
                ('reported', models.ForeignKey(db_column='reported', on_delete=django.db.models.deletion.CASCADE, related_name='reported_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '举报表',
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='下载时间')),
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.CASCADE, related_name='fid_1', to='user.fileinfo')),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, related_name='userid_1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '下载历史',
                'db_table': 'download_history',
            },
        ),
        migrations.CreateModel(
            name='DailyInfo',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False, verbose_name='日常推荐id')),
                ('daily_time', models.DateField(auto_now_add=True, db_column='daily_time', verbose_name='推荐时间')),
                ('fid', models.ForeignKey(db_column='daily_fid', on_delete=django.db.models.deletion.CASCADE, related_name='fid_5', to='user.fileinfo')),
            ],
            options={
                'verbose_name': '每日推荐',
                'db_table': 'daily_recommend',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('grade', models.IntegerField(default=5, verbose_name='个人评分')),
                ('evaluation', models.CharField(max_length=255, verbose_name='个人评价')),
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.CASCADE, related_name='fid_3', to='user.fileinfo')),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, related_name='userid_3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '评论表',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏日期')),
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.CASCADE, related_name='fid_2', to='user.fileinfo')),
                ('userid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, related_name='userid_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '收藏表',
                'db_table': 'collections',
            },
        ),
    ]
