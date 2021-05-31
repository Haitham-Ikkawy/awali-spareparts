# Generated by Django 3.1.4 on 2021-05-31 09:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='img/accessories')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='awali_admin.accessories')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessories',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img/carbrands')),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Car Brand',
                'verbose_name_plural': 'Cars Brands',
            },
        ),
        migrations.CreateModel(
            name='CarEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('description_2', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('car_brand', models.ManyToManyField(blank=True, to='awali_admin.CarBrand')),
            ],
            options={
                'verbose_name': 'Car Engine',
                'verbose_name_plural': 'Cars Engines',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('description_2', models.CharField(blank=True, max_length=150)),
                ('finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awali_admin.carbrand')),
            ],
            options={
                'verbose_name': 'Car Model',
                'verbose_name_plural': 'Cars Models',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('description_2', models.CharField(blank=True, max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='img/categories')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('car_brand', models.ManyToManyField(blank=True, to='awali_admin.CarBrand')),
                ('car_engine', models.ManyToManyField(blank=True, to='awali_admin.CarEngine')),
                ('car_model', models.ManyToManyField(blank=True, to='awali_admin.CarModel')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='awali_admin.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('phone_number', phone_field.models.PhoneField(help_text='Customer phone number', max_length=31, unique=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awali_admin.customer')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='ItemBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Item Brand',
                'verbose_name_plural': 'Items Brands',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('description_2', models.CharField(blank=True, max_length=150, null=True)),
                ('remark', models.CharField(blank=True, max_length=150, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('min_sale_num', models.IntegerField(default=1)),
                ('min_stock_quantity', models.IntegerField(blank=True, null=True)),
                ('max_stock_quantity', models.IntegerField(blank=True, null=True)),
                ('item_location', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('width', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/items')),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('supplier', models.CharField(blank=True, max_length=10, null=True)),
                ('oem', models.CharField(blank=True, max_length=150)),
                ('cross_numbers', models.TextField(blank=True)),
                ('is_free_shipping', models.BooleanField(default=False)),
                ('own_delivery', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated_at')),
                ('accessory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awali_admin.accessories')),
                ('car_brand', models.ManyToManyField(blank=True, to='awali_admin.CarBrand')),
                ('car_engine', models.ManyToManyField(blank=True, to='awali_admin.CarEngine')),
                ('car_model', models.ManyToManyField(blank=True, to='awali_admin.CarModel')),
                ('categories', models.ManyToManyField(blank=True, to='awali_admin.Category')),
                ('item_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awali_admin.itembrand')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_sale_price', models.FloatField()),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awali_admin.invoice')),
                ('item', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='awali_admin.item')),
            ],
        ),
        migrations.AddField(
            model_name='carengine',
            name='car_model',
            field=models.ManyToManyField(blank=True, to='awali_admin.CarModel'),
        ),
    ]
