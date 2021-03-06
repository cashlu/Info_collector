# Generated by Django 2.2.4 on 2019-08-15 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='report.City', verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='report.Reviewer', verbose_name='审核人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='report.Town', verbose_name='镇'),
        ),
        migrations.AlterField(
            model_name='report',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='report.Village', verbose_name='村'),
        ),
    ]
