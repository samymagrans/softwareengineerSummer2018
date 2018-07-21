from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product
from carts.models import Cart
<<<<<<< HEAD
=======
from django.db.models import F
>>>>>>> 23181ea5e2a22513cfd099a19227eac9976f9e35

class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()

class ProductFeaturedDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()



class ProductListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
<<<<<<< HEAD
=======
		method_dict = request.GET
		query4 = method_dict.get('s', None)
		if query4 is not None and query4=="titleASC":
			return Product.objects.all().order_by(F("title").asc())
		elif query4 is not None and query4=="titleDESC":
			return Product.objects.all().order_by(F("title").desc())
		elif query4 is not None and query4=="authorASC":
			return Product.objects.all().order_by(F("author").asc())
		elif query4 is not None and query4=="authorDESC":
			return Product.objects.all().order_by(F("author").desc())
		elif query4 is not None and query4=="priceLH":
			return Product.objects.all().order_by(F("price").asc())
		elif query4 is not None and query4=="priceHL":
			return Product.objects.all().order_by(F("price").desc())
		elif query4 is not None and query4=="rateHL":
			return Product.objects.all().order_by(F("rate").asc())
		elif query4 is not None and query4=="rateLH":
			return Product.objects.all().order_by(F("rate").desc())
>>>>>>> 23181ea5e2a22513cfd099a19227eac9976f9e35
		return Product.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	return context

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, "products/list.html", context)

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context


	def get_object(self, *args, **kwargs):
		request = self.request
		slug= self.kwargs.get('slug')
		#instance = get_object_or_404(Product, slug=slug)
		try:
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404("Not found ...")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404("Something unexpected happened :(")
		return instance

class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk= self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product does not exist")
		return instance

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk= self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)

def product_detail_view(request, pk=None, *args, **kwargs):
	#instance = Product.objects.get(pk=pk)
	#instance = get_object_or_404(Product, pk=pk)

	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product does not exist")
	# print(instance)

	# qs = Product.objects.filter(id=pk)
	# if qs.exists() and qs.count()==1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product does not exist")
	cart_obj, new_obj = Cart.objects.new_or_get(request)

	print(cart_obj, new_obj)
	context = {
		'object': instance,
		'cart': cart_obj,
		'new_cart': new_cart,
		'in_cart':False
	}
	if instance in cart_obj:
		print("Exists")
		context['in_cart'] = True
	else:
		print("Does Not Exist")
		context['in_cart'] = False

	return render(request, "products/detail.html", context)



def update_quantity(request, pk=None, *args, **kwargs):
	print(request)


# def change_product_quantity(request)