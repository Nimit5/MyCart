# Generated by Django 2.1.5 on 2020-01-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
