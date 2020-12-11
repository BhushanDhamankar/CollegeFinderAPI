from django.contrib import admin
from . models import Branch,Category,College,Mapping
# Register your models here.
admin.site.register(Branch)
admin.site.register(Category)
admin.site.register(College)
admin.site.register(Mapping)