from django.contrib import admin

# Register your models here.
from app23.models import Stud_reg,Teacher_reg,Bookdetail,fine

admin.site.register(Stud_reg)
admin.site.register(Teacher_reg)
admin.site.register(Bookdetail)
admin.site.register(fine)
