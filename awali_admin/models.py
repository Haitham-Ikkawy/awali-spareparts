from django.db import models
from mptt.admin import DraggableMPTTAdmin
from django.utils.timezone import now
from mptt.models import MPTTModel, TreeForeignKey
from phone_field import PhoneField
from awali import settings

from django.utils import timezone
from datetime import timedelta

database_time = timezone.now()
expire_time = timezone.now() + timedelta(hours=24)



# from django.contrib.auth import


class CarBrand(models.Model):
	auto_increment_id = models.AutoField
	image = models.ImageField(upload_to='img/carbrands', blank=True)
	description = models.CharField(max_length=150)
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "Car Brand"
		verbose_name_plural = "Cars Brands"

class CarModel(models.Model):
	auto_increment_id = models.AutoField
	car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
	description = models.CharField(max_length=150)
	description_2 = models.CharField(max_length=150, blank=True)

	finished = models.BooleanField(default=False)
	created_at = models.DateTimeField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def get_related_eninges(self):
		return " / ".join([str(p) for p in CarEngine.objects.filter(car_model=self.id)])

	def __str__(self):
		return str(self.id) + '_' + self.description

	class Meta:
		verbose_name = "Car Model"
		verbose_name_plural = "Cars Models"

class CarEngine(models.Model):
	auto_increment_id = models.AutoField
	description = models.CharField(max_length=150)
	description_2 = models.CharField(max_length=150)
	car_brand = models.ManyToManyField(CarBrand, blank=True)
	car_model = models.ManyToManyField(CarModel, blank=True)
	created_at = models.DateTimeField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def related_car_brands(self):
		return " / ".join([p.description for p in self.car_brand.all()])

	def related_car_model(self):
		return " / ".join([p.description for p in self.car_model.all()])

	def __str__(self):
		return str(self.id) + '_' + self.description

	class Meta:
		verbose_name = "Car Engine"
		verbose_name_plural = "Cars Engines"

class ItemBrand(models.Model):
	auto_increment_id = models.AutoField
	description = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "Item Brand"
		verbose_name_plural = "Items Brands"

class Category(MPTTModel):
	auto_increment_id = models.AutoField
	description = models.CharField(max_length=150)
	description_2 = models.CharField(max_length=150, blank=True)
	image = models.ImageField(upload_to='img/categories', blank=True)
	car_brand = models.ManyToManyField(CarBrand, blank=True)
	car_model = models.ManyToManyField(CarModel, blank=True)
	car_engine = models.ManyToManyField(CarEngine, blank=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def related_car_model(self):
		return " / ".join([p.description for p in self.car_model.all()])

	def related_car_engine(self):
		return " / ".join([p.description for p in self.car_engine.all()])

	class MPTTMeta:
		order_insertion_by = ['description']

	def __str__(self):
		return str(self.id) + '_' + self.description

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "categories"

class Accessories(MPTTModel):
	auto_increment_id = models.AutoField
	description = models.CharField(max_length=150)
	image = models.ImageField(upload_to='img/accessories', blank=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	class MPTTMeta:
		order_insertion_by = ['description']

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "Accessory"
		verbose_name_plural = "Accessories"

class Item(models.Model):
	CURRENCY_CHOICES = (
		("Dollar", "dollar"),
		("Yen", "yen"),
		("Euro", "euro"),
	)

	auto_increment_id = models.AutoField

	item_code = models.CharField(max_length=150, null=False, blank=False)
	description = models.CharField(max_length=150, null=False, blank=False)
	description_2 = models.CharField(max_length=150, null=True, blank=True)
	remark = models.CharField(max_length=150, null=True, blank=True)
	stock = models.IntegerField(null=True, blank=True)
	cost = models.FloatField(null=True, blank=True)
	sale_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7, )
	min_sale_num = models.IntegerField(null=False, blank=False, default=1)
	min_stock_quantity = models.IntegerField(null=True, blank=True)
	max_stock_quantity = models.IntegerField(null=True, blank=True)
	item_location = models.CharField(null=True, max_length=20, blank=True)
	weight = models.FloatField(null=True, blank=True)
	height = models.FloatField(null=True, blank=True)
	width = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to='img/items', blank=True, null=True)
	car_brand = models.ManyToManyField(CarBrand, blank=True)
	car_model = models.ManyToManyField(CarModel, blank=True)
	car_engine = models.ManyToManyField(CarEngine, blank=True)
	categories = models.ManyToManyField(Category, blank=True)
	accessory = models.ForeignKey(Accessories, blank=True, on_delete=models.CASCADE, null=True)
	category = models.CharField(blank=True, null=True, max_length=10)
	supplier = models.CharField(blank=True, null=True, max_length=10)
	item_brand = models.ForeignKey(ItemBrand, blank=True, null=True, on_delete=models.CASCADE)
	oem = models.CharField(max_length=150, blank=True)
	cross_numbers = models.TextField(blank=True)
	is_free_shipping = models.BooleanField(default=False)
	own_delivery = models.BooleanField(default=False)
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def related_categories(self):
		return " / ".join([p.description for p in self.categories.all()])

	def related_brands_car_brands(self):
		return " / ".join([p.description for p in self.car_brand.all()])

	# def related_item_brand(self):
	#
	# 	return " / ".join([p.description for p in self.item_brand.all()])

	def related_car_engine(self):
		return " / ".join([p.description for p in self.car_engine.all()])

	def related_car_model(self):
		return " / ".join([p.description for p in self.car_model.all()])

	def __str__(self):
		return self.description

	class Meta:
		verbose_name = "Item"
		verbose_name_plural = "Items"

class Customer(models.Model):
	auto_increment_id = models.AutoField
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=150)
	phone_number = PhoneField(blank=False, unique=True, help_text='Customer phone number')
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"

class Invoice(models.Model):
	auto_increment_id = models.AutoField
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
	created_at = models.DateField('created_at', default=now)
	updated_at = models.DateTimeField('updated_at', default=now)

	def invoice_items(self):
		return " / ".join([str(p.item) for p in InvoiceItems.objects.filter(invoice=self.id)])

	# def __str__(self):
	# 	return self.description

	class Meta:
		verbose_name = "Invoice"
		verbose_name_plural = "Invoices"

class InvoiceItems(models.Model):
	auto_increment_id = models.AutoField
	invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
	item = models.ForeignKey(Item, blank=True, on_delete=models.CASCADE, null=False,)
	customer_sale_price = models.FloatField(null=False, blank=False)




