# Generated by Django 2.1.1 on 2018-11-05 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_group_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='info_ecocharacter',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='summary.Info_ExperiLocation', verbose_name='试验点'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info_fieldcharacter',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='summary.Info_ExperiLocation', verbose_name='试验点'),
            preserve_default=False,
        ),
    ]
