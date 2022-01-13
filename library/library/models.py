from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=60, editable=False)
    isbn = models.CharField(primary_key=True, max_length=13)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, editable=False)
    call_number = models.CharField(max_length=10, unique=True)
    copies = models.IntegerField(default=1)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True, null=True)
    pages = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title





# class CheckoutManager(models.Manager):
#     def save(self, **obj_data):
        
#         if not 'due_date' in obj_data or not obj_data['due_date']:
#             # 3 weeks
            
#             obj_data['due_date'] = obj_data['checkout_time'] + datetime.timedelta(21)

#         obj_data['email_time'] = obj_data['due_date'].total_seconds() - obj_data['checkout_time'].total_seconds()
#         return super().save(**obj_data) 





class Checkout(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    email_time = models.IntegerField(blank=True, null=True) # seconds

    def save(self, *args, **kwargs):
        if not self.checkout_time:
            self.checkout_time = timezone.now()
        if not self.due_date:
            # 3 weeks
            self.due_date = self.checkout_time + datetime.timedelta(21)

        self.email_time = self.due_date.timestamp() - self.checkout_time.timestamp()

        super(Checkout, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} {self.book} {self.checkout_time}"

    # troubleshoot code ^
    # TODO add if statement to views









# class MyModelManager(models.Manager):
#     def create(self, **obj_data):
#         # Do some extra stuff here on the submitted data before saving...
#         # For example...
#         obj_data['my_field'] = my_computed_value(obj_data['my_other_field'])

#         # Now call the super method which does the actual creation
#         return super().create(**obj_data) # Python 3 syntax!!

# class MyModel(models.model):
#     # An example model
#     my_field = models.CharField(max_length=250)
#     my_other_field = models.CharField(max_length=250)

#     objects = MyModelManager()