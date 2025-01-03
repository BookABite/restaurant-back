from django.contrib import admin
from django.contrib import messages
from .models import RestaurantCustomer
from .forms import RestaurantCustomerForm

@admin.register(RestaurantCustomer)
class RestaurantCustomerAdmin(admin.ModelAdmin):
    form = RestaurantCustomerForm
    
    list_display = (
        'restaurant_customer_id',
        'get_restaurant_names',
        'first_name',
        'last_name',
        'email',
        'country_code',
        'phone',
        'birthday'
    )
    
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'restaurants__name',
        'restaurant_customer_id'
    )
    
    list_filter = (
        'created_at',
        'country_code'
    )
    
    readonly_fields = (
        'created_at',
        'updated_at',
        'restaurant_customer_id'
    )

    fieldsets = (
        ('Restaurant Information', {
            'fields': ('restaurants', 'restaurant_customer_id')
        }),
        ('Personal Information', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'country_code',
                'phone',
                'birthday'
            )
        }),
        ('Important Dates', {
            'fields': ('created_at', 'updated_at'),
        })
    )

    def get_restaurant_names(self, obj):
        return ", ".join([restaurant.name for restaurant in obj.restaurants.all()])
    get_restaurant_names.short_description = 'Restaurants'

    def save_model(self, request, obj, form, change):
        try:
            # First save the customer
            super().save_model(request, obj, form, change)
            
            # If user is a restaurant admin, automatically associate with their restaurant
            if hasattr(request.user, 'restaurant'):
                obj.restaurants.add(request.user.restaurant)
            
            # Save the form to handle the restaurants field
            form.save()
            
            messages.success(request, f'Restaurant customer "{obj}" was saved successfully.')
        except Exception as e:
            messages.error(request, f'Error saving restaurant customer: {str(e)}')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(request.user, 'restaurant'):
            return qs.filter(restaurants=request.user.restaurant)
        return qs

    def response_add(self, request, obj, post_url_continue=None):
        """Override to ensure proper redirect after adding"""
        return super().response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        """Override to ensure proper redirect after editing"""
        return super().response_change(request, obj)