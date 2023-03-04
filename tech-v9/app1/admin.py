from django.contrib import admin

# Register your models here.
from .models import nw_malfunction,print_malfunction,cartridges
from .form import signup_nw,signup_printer,signup_cartridge

# class signupadmin1(admin.ModelAdmin):
#       listdisplay = ["__str__"]
#       form1 = signup_nw
#       #form2 = signup_hw
#       form2 = signup_printer
# admin.site.register(hw_malfunction,signupadmin1)
#
#
# class signupadmin2(admin.ModelAdmin):
#       listdisplay = ["__str__"]
#       form1 = signup_nw
#      # form2 = signup_hw
#       form2 = signup_printer
# admin.site.register(nw_malfunction,signupadmin2)
#
# class signupadmin3(admin.ModelAdmin):
#       listdisplay = ["__str__"]
#       form1 = signup_nw
#      # form2 = signup_hw
#       form2 = signup_printer
# admin.site.register(print_malfunction,signupadmin3)
#
#
# class signupadmin4(admin.ModelAdmin):
#       listdisplay = ["__str__"]
#       form1 = signup_nw
#       #form2 = signup_hw
#       form2 = signup_printer
#       form5 = signup_cartridge
#
# admin.site.register(cartridges, signupadmin4)