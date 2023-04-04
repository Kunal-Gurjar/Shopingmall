# Generated by Django 4.2 on 2023-04-03 13:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subcategory_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('category', models.ManyToManyField(blank=True, to='shop.categories')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='subcategory',
            field=models.ManyToManyField(to='shop.subcategories'),
        ),
    ]