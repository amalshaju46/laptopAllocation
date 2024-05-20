from django.contrib import admin

from laptopAllocation.models import Student, Laptop, Batch, Allocation

admin.site.register(Laptop)
admin.site.register(Student)
admin.site.register(Allocation)
admin.site.register(Batch)