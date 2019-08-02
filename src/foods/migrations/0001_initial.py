# Generated by Django 2.2.4 on 2019-08-02 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='item_photos/', verbose_name='item_photo', width_field='width_field')),
                ('key', models.CharField(blank=True, default='', max_length=128)),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('ratio', models.CharField(default='1:1', max_length=50)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('ordered_in_restaurant', models.IntegerField(blank=True, default=0)),
                ('ordered_in_home', models.IntegerField(blank=True, default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.FoodCategory')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
