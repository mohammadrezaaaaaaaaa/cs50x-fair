from django.contrib import admin
from .models import User , Country , Destination , Hotel , Room , Facilities , Comment , Rate , Room_Reserve
# Register your models here.

class Admin_Hotel(admin.ModelAdmin):
    list_display=("name","city","location","star")

class Admin_Room(admin.ModelAdmin):
    list_display=("hotel","number","price","status")

class Admin_Facilities(admin.ModelAdmin):
    list_display=("id","facility")

class Admin_Room_Reservation(admin.ModelAdmin):
    list_display=("id","user","room","total_days","total_price","check_in","check_out")

class Admin_Comment(admin.ModelAdmin):
    list_display=("user","hotel")

class Admin_Rate(admin.ModelAdmin):
    list_display=("user","hotel","rate")

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Destination)
admin.site.register(Hotel,Admin_Hotel)
admin.site.register(Room,Admin_Room)
admin.site.register(Room_Reserve,Admin_Room_Reservation)
admin.site.register(Facilities,Admin_Facilities)
admin.site.register(Comment,Admin_Comment)
admin.site.register(Rate,Admin_Rate)
