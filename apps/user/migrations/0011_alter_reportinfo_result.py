# Generated by Django 3.2.8 on 2022-05-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_reportinfo_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportinfo',
            name='result',
            field=models.IntegerField(choices=[(0, '未违规'), (1, '违规')], default=0, verbose_name='处理结果'),
        ),
    ]
