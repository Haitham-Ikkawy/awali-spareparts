from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Item, ItemBrand, Category, CarBrand, CarModel, CarEngine, \
	Accessories, Customer, Invoice, InvoiceItems
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.db.models import Q


class AdminCategoryView(DraggableMPTTAdmin):
	mptt_level_indent = 40
	save_as = True
	mptt_indent_field = "name"
	list_display = ('tree_actions', 'id', 'indented_title', 'description_2', 'related_car_model', 'related_car_engine')
	list_display_links = ('indented_title',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)

		# Add cumulative product count
		qs = Category.objects.add_related_count(
			qs,
			Item,
			'categories',
			'products_cumulative_count',
			cumulative=True)

		# Add non cumulative product count
		qs = Category.objects.add_related_count(qs,
		                                        Item,
		                                        'categories',
		                                        'products_count',
		                                        cumulative=False)
		return qs

	def related_products_count(self, instance):
		return instance.products_count

	related_products_count.short_description = 'Related products (for this specific category)'

	def related_products_cumulative_count(self, instance):
		return instance.products_cumulative_count

	related_products_cumulative_count.short_description = 'Related products (in tree)'

	search_fields = ('description_2',)

	filter_horizontal = ('car_brand', 'car_model', 'car_engine')

	list_filter = ('car_model',)


class ItemResource(resources.ModelResource):
	class Meta:
		model = Item
		import_id_fields = ('id',)
		fields = ('oem', 'description_2', 'stock', 'category', 'item_location', 'id', 'sale_price', 'cost')
		export_order = ('oem', 'description_2', 'stock', 'category', 'item_location', 'id', 'sale_price', 'cost')


class AdminItemView(ImportExportModelAdmin):
	resource_class = ItemResource

	advanced_filter_fields = ('description',)
	save_as = True

	list_display = (
	'id', 'description', 'description_2', 'weight', 'oem', 'cost', 'sale_price', 'category', 'stock', 'item_brand',
	'supplier', 'item_location')
	search_fields = ('description_2',)
	filter_horizontal = ('car_brand', 'car_model', 'car_engine', 'categories')
	list_filter = ('category',)

	autocomplete_fields = ('item_brand',)


class AdminAccessoriesView(DraggableMPTTAdmin):
	mptt_level_indent = 40

	mptt_indent_field = "name"
	list_display = ('tree_actions', 'indented_title',
	                'related_products_count', 'related_products_cumulative_count')
	list_display_links = ('indented_title',)

	def get_queryset(self, request):
		qs = super().get_queryset(request)

		# Add cumulative product count
		qs = Accessories.objects.add_related_count(
			qs,
			Item,
			'accessory',
			'products_cumulative_count',
			cumulative=True)

		# Add non cumulative product count
		qs = Accessories.objects.add_related_count(qs,
		                                           Item,
		                                           'accessory',
		                                           'products_count',
		                                           cumulative=False)
		return qs

	def related_products_count(self, instance):
		return instance.products_count

	related_products_count.short_description = 'Related products (for this accessory )'

	def related_products_cumulative_count(self, instance):
		return instance.products_cumulative_count

	related_products_cumulative_count.short_description = 'Related products (in tree)'

	search_fields = ('description', 'created_at', 'updated_at')


class AdminItemBrandView(admin.ModelAdmin):
	list_display = ('description', 'created_at', 'updated_at')
	search_fields = ('description', 'created_at', 'updated_at')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class AdminCarBrandView(admin.ModelAdmin):
	list_display = ('id', 'description', 'created_at', 'updated_at')
	search_fields = ('id', 'description', 'created_at', 'updated_at')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class CategoryInline(admin.TabularInline):
	model = Category.car_model.through


class AdminCarModelView(admin.ModelAdmin):
	list_display = ('id', 'description', 'get_related_eninges', 'car_brand', 'created_at', 'updated_at')
	search_fields = ('description', 'car_brand', 'created_at', 'updated_at')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

	inlines = [
		CategoryInline,
	]


class AdminCarEngineView(admin.ModelAdmin):
	list_display = (
	'id', 'description', 'description_2', 'get_car_brands', 'related_car_model', 'created_at', 'updated_at')
	search_fields = ('description', 'car_brand__description', 'created_at', 'updated_at')
	filter_horizontal = ('car_brand', 'car_model')
	list_filter = ()
	fieldsets = ()

	# autocomplete_fields = ('car_brand', 'car_model')

	def get_car_brands(self, obj):
		return [p.description for p in obj.car_brand.all()]

	get_car_brands.admin_order_field = 'car_brand'  # Allows column order sorting
	get_car_brands.short_description = 'Car Brand'  # Renames column head
	get_car_brands.admin_search_field = 'Car Brand Search'


class AdminCustomerView(admin.ModelAdmin):
	list_display = ('id', 'name', 'address', 'phone_number')
	search_fields = ('id', 'name', 'address', 'phone_number')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


class AdminInvoiceView(admin.ModelAdmin):
	list_display = ('id', 'customer')
	search_fields = ('id', 'customer')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Customer, AdminCustomerView)

admin.site.register(Invoice, AdminInvoiceView)

admin.site.register(CarBrand, AdminCarBrandView)

admin.site.register(CarModel, AdminCarModelView)

admin.site.register(CarEngine, AdminCarEngineView)

admin.site.register(Category, AdminCategoryView)

admin.site.register(Item, AdminItemView)

admin.site.register(ItemBrand, AdminItemBrandView)

admin.site.register(Accessories, AdminAccessoriesView)

admin.site.site_header = 'AWALI SPARE PARTS COMPANY'
