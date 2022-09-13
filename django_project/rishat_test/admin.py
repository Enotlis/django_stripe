from django.contrib import admin
from django import forms
from . import models

class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = "__all__"

    def clean_price(self):
    '''Проверка что цена на товар введена корректно'''
        if self.cleaned_data["price"] < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return self.cleaned_data["price"]

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'currency')
    search_fields = ("name__startswith",)
    form = ItemAdminForm

admin.site.register(models.Item, ItemAdmin)
