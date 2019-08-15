# Generated by Django 2.2.4 on 2019-08-16 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20190815_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='advice',
            field=models.ManyToManyField(blank=True, null=True, to='report.Advice', verbose_name='处理建议'),
        ),
        migrations.AlterField(
            model_name='report',
            name='appraiser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='鉴定人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='assess_level',
            field=models.CharField(blank=True, choices=[('a', 'A 完好无损'), ('b', 'B 轻微破损，可以使用'), ('c', 'C 破损经修缮后可以使用'), ('d', 'D 严重破坏，不能使用'), ('e', '倒塌')], max_length=10, null=True, verbose_name='评定等级'),
        ),
        migrations.AlterField(
            model_name='report',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.City', verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='report',
            name='fence',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10, null=True, verbose_name='围护结构'),
        ),
        migrations.AlterField(
            model_name='report',
            name='fence_detail',
            field=models.ManyToManyField(blank=True, null=True, to='report.FenceDetail', verbose_name='围护结构说明'),
        ),
        migrations.AlterField(
            model_name='report',
            name='groundsill',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10, null=True, verbose_name='地基基础'),
        ),
        migrations.AlterField(
            model_name='report',
            name='groundsill_detail',
            field=models.ManyToManyField(blank=True, null=True, to='report.GroundsillDetail', verbose_name='地基基础说明'),
        ),
        migrations.AlterField(
            model_name='report',
            name='identity',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='report',
            name='purpose',
            field=models.IntegerField(blank=True, choices=[(1, '住宅'), (2, '厂房'), (3, '公共建筑')], null=True, verbose_name='用途'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Reviewer', verbose_name='审核人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='security',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10, null=True, verbose_name='场地安全程度'),
        ),
        migrations.AlterField(
            model_name='report',
            name='security_detail',
            field=models.ManyToManyField(blank=True, null=True, to='report.SecurityDetail', verbose_name='场地安全程度说明'),
        ),
        migrations.AlterField(
            model_name='report',
            name='street_contract',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='镇（街道）联系人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='street_contract_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='镇（街道）联系人电话'),
        ),
        migrations.AlterField(
            model_name='report',
            name='structure',
            field=models.IntegerField(blank=True, choices=[(1, '混凝土结构'), (2, '砌体结构'), (3, '木结构'), (4, '钢结构'), (5, '石结构'), (6, '生土结构')], null=True, verbose_name='结构形式'),
        ),
        migrations.AlterField(
            model_name='report',
            name='tilt',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10, null=True, verbose_name='房屋整体倾斜'),
        ),
        migrations.AlterField(
            model_name='report',
            name='tilt_detail',
            field=models.ManyToManyField(blank=True, null=True, to='report.TiltDetail', verbose_name='房屋整体倾斜说明'),
        ),
        migrations.AlterField(
            model_name='report',
            name='town',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Town', verbose_name='镇'),
        ),
        migrations.AlterField(
            model_name='report',
            name='upon',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=10, null=True, verbose_name='上部承重结构'),
        ),
        migrations.AlterField(
            model_name='report',
            name='upon_detail',
            field=models.ManyToManyField(blank=True, null=True, to='report.UponDetail', verbose_name='上部承重结构说明'),
        ),
        migrations.AlterField(
            model_name='report',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Village', verbose_name='村'),
        ),
        migrations.AlterField(
            model_name='report',
            name='village_contract',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='村联系人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='village_contract_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='村联系人电话'),
        ),
    ]
