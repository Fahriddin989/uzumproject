# Generated by Django 4.2.2 on 2023-06-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(choices=[('S', 'SELLER'), ('C', 'CUSTOMER')], default='C', max_length=1),
        ),
    ]