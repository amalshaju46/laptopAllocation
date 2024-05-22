
from django.db import models

class Batch(models.Model):
    batch_number = models.IntegerField(unique=True, editable=False)

    TIME_SLOTS = [
        ( '09-09:45','09-09:45 '),
        ( '10-10:45','10-10:45 '),
        ( '11-11:45','11-11:45 '),
        ( '12-12:45','12-12:45 '),
        ( '02-02:45','02-02:45 '),
    ]

    time_slot = models.CharField(unique=True,max_length=20,choices=TIME_SLOTS)
    
    def __str__(self):
        return str(self.batch_number)+' - '+self.time_slot

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    company_laptop_required = models.BooleanField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name
    
class Laptop(models.Model):
    serial_number = models.CharField(unique=True,editable=False,max_length=10)
    model_name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.serial_number)+' - '+self.model_name
    
class Allocation(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_of_allocation = models.DateField()

    def __str__(self):
        return str(self.laptop.serial_number)+' - '+self.student.full_name+' - '+str(self.student.batch)+' - '+str(self.date_of_allocation)
