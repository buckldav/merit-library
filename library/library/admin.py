from django.contrib import admin
from library.library.models import Author, Book, Checkout, DeweyDecimal, Student, Teacher
import requests
import json

# Register your models here.
 
admin.site.register(Author)
admin.site.register(DeweyDecimal)
admin.site.register(Student)
# admin.site.register(Book)
admin.site.register(Teacher)
admin.site.register(Checkout)

class BookAdmin(admin.ModelAdmin):
    fields = ['isbn', 'call_number']

    def add_view(self,request,extra_content=None):
        self.fields = ["isbn", "call_number"]
        return super(BookAdmin,self).add_view(request)

    def change_view(self,request,object_id,extra_content=None):
        self.fields = ["author", "title", "call_number", "copies", "image", "pages"]
        self.readonly_fields = ["author", "title", "pages"]
        return super(BookAdmin,self).change_view(request,object_id)

    def save_model(self, request, obj, form, change):
        
        ISBN = form.cleaned_data["isbn"] #"0765326353"

        URL = f"https://openlibrary.org/api/books.json?jscmd=data&bibkeys=ISBN:{ISBN}"
        page = requests.get(URL)
        data = json.loads(page.content.decode("utf-8"))

        obj.title = data[f"ISBN:{ISBN}"]["title"]
        if "cover" in data[f"ISBN:{ISBN}"]:
            obj.image = data[f"ISBN:{ISBN}"]["cover"]["medium"]
        if "number_of_pages" in data[f"ISBN:{ISBN}"]:
            obj.pages = data[f"ISBN:{ISBN}"]["number_of_pages"]
        obj.isbn = ISBN
        obj.call_number = form.cleaned_data["call_number"]
        author = Author.objects.create(
            first_name=" ".join(data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[0:-1]),
            last_name=data[f"ISBN:{ISBN}"]["authors"][0]["name"].split()[-1]
        )
        obj.author = author

        return super(BookAdmin, self).save_model(request, obj, form, change)

admin.site.register(Book, BookAdmin)