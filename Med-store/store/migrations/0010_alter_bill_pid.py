# Generated by Django 3.2.4 on 2021-06-26 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210626_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='store.patient'),
        ),
    ]
