from django.contrib import admin
from.models import CartItem,Carts,Coupon,AppliedCoupon
# Register your models here.
class CartsAdmin(admin.ModelAdmin):
    list_display=('cart_id','date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','cart','quantity','is_active')
admin.site.register(Carts,CartsAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Coupon)
admin.site.register(AppliedCoupon)
