# Generated by Django 2.2.4 on 2019-08-15 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20190815_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='report_pics', to='report.Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='appraiser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='鉴定人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.City', verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Reviewer', verbose_name='审核人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Town', verbose_name='镇'),
        ),
        migrations.AlterField(
            model_name='report',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Village', verbose_name='村'),
        ),
    ]