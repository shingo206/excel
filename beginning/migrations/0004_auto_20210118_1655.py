# Generated by Django 3.1.4 on 2021-01-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beginning', '0003_delete_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
