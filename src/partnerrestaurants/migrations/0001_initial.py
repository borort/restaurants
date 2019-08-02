# Generated by Django 2.2.4 on 2019-08-02 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_sell_count', models.IntegerField(blank=True, default=0)),
                ('rest_sell_count', models.IntegerField(blank=True, default=0)),
                ('total_sell_tk', models.FloatField(blank=True, default=0.0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0.0)),
                ('delivery_type', models.CharField(max_length=100)),
                ('destination', models.CharField(blank=True, default='', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('foods', models.ManyToManyField(to='foods.Food')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partnerrestaurants.PartnerRestaurant')),
            ],
        ),
    ]
