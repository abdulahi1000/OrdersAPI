# Generated by Django 4.1.1 on 2022-09-21 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_order_paymentmethod_alter_order_totalprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
