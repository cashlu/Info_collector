# Generated by Django 2.2.4 on 2019-08-23 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20190816_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='decade',
            field=models.CharField(blank=True, choices=[('1900', '1900'), ('1910', '1910'), ('1920', '1920'), ('1930', '1930'), ('1940', '1940'), ('1950', '1950'), ('1960', '1960'), ('1970', '1970'), ('1980', '1980'), ('1990', '1990'), ('2000', '2000'), ('2010', '2010')], max_length=10, null=True, verbose_name='建成年代'),
        ),
    ]