from django.db import models
# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
import os
from datetime import datetime, timedelta
from datetime import date
from django.utils.timezone import now
import datetime
from multiselectfield import MultiSelectField
from decimal import Decimal
from smart_selects.db_fields import ChainedForeignKey,ChainedManyToManyField,GroupedForeignKey

class headsectormanager(models.Manager):
      def get_queryset(self):
          return super(headsectormanager,self).get_queryset().filter()


class users(models.Model):
      user_name = models.CharField(max_length=120, null=True)
      user_code = models.CharField(max_length=120, null=True)

      def __str__(self):
          return '%s' % (self.user_name,self.user_code)



class hsectors(models.Model):
      sectors = models.CharField(max_length=120,null=True)
      def __str__(self):
           return '%s' % (self.sectors)

#//////////////////////LAW MASTER///////////////////////////////////////////////////////////////////////////////////////////
class casedep(models.Model):
    dep = models.CharField(max_length=120, null=True, verbose_name='الدائره')

    def __str__(self):
        return '%s' % (self.dep)



class case_depart_type(models.Model):
      dep_type = models.CharField(max_length=120, null=True,verbose_name='نوع الدائره')

      def __str__(self):
        return '%s' % (self.dep_type)


class case_classification(models.Model):
      cas_class = models.CharField(max_length=120, null=True,verbose_name='نوع الدعوى')

      def __str__(self):
        return '%s' % (self.cas_class)


class case_category(models.Model):
    category = models.CharField(max_length=120,blank=True, null=True,verbose_name='تصنيف الدعوى')

    def __str__(self):
        return '%s' % (self.category)




class case_court_name(models.Model):
    court = models.CharField(max_length=120, blank=True, null=True,verbose_name='اسم المحكمه')

    def __str__(self):
        return '%s' % (self.court)


class case_current_status(models.Model):
    status = models.CharField(max_length=120, blank=True, null=True,verbose_name='حالة الدعوى')

    def __str__(self):
        return '%s' % (self.status)

class case_lawyer(models.Model):
    lawyer = models.CharField(max_length=120, blank=True, null=True,verbose_name='اسم المحامى')

    def __str__(self):
        return '%s' % (self.lawyer)



class litigationdeg(models.Model):
    deg = models.CharField(max_length=120, blank=True, null=True,verbose_name='درجة التقاضى')

    def __str__(self):
        return '%s' % (self.deg)
#----------------------

class oponent(models.Model):
    oponent = models.CharField(max_length=120, blank=True, null=True,verbose_name='الخصم ')

    def __str__(self):
        return '%s' % (self.oponent)

class oponentrep(models.Model):
    oponent_rep = models.CharField(max_length=120, blank=True, null=True,verbose_name='صفة الخصم ')

    def __str__(self):
        return '%s' % (self.oponent_rep)

class gainwtpercent(models.Model):
    gainprct = models.CharField(max_length=120, blank=True, null=True,verbose_name='نسبة ترجيح الكسب ')

    def __str__(self):
        return '%s' % (self.gainprct)
class comprep(models.Model):
    companyrepre = models.CharField(max_length=120, blank=True, null=True,verbose_name='صفة الشركه')

    def __str__(self):
        return '%s' % (self.companyrepre)


#//////////////////////LAW MASTER///////////////////////////////////////////////////////////////////////////////////////////
class sector(models.Model):
      hsectors = models.ForeignKey(hsectors,null=True)
      sector_name = models.CharField(max_length=120,null=True)
      def __str__(self):
          return '%s' % (self.sector_name)
def get_file_path1(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('blueprints', filename)
def get_file_path01(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('working_emp', filename)   
def get_file_path02(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('retired_emp', filename)     
def get_file_path2(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('cartridges', filename)
def get_file_path3(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('spareparts', filename)
def get_file_path4(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s.%s" % ( datetime.datetime.now(),uuid.uuid4(), ext)
    return os.path.join('passrecovery', filename)
class hw_malfunction(models.Model):
      sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)
      user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
      hsectors = models.ForeignKey(hsectors,blank=True,null=True,verbose_name='رئاسة القطاعات')
      user_sector = models.ForeignKey(sector,blank=True,null=True,verbose_name='القطاع')
      pc_type = models.CharField(max_length=120,verbose_name='نوع الكومبيوتر')
      problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
      problem_desc = models.TextField(verbose_name='وصف المشكله')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      publisher = models.ForeignKey(User,null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False,null=True,max_length=120)
      closed_by = models.CharField(blank=False, null=True, max_length=120)
      close_date = models.DateTimeField(auto_now_add=True, null=True)

      def __str__(self):
          return '%s %s %s %s %s %s ' %      (self.user_fullname,self.user_sector,self.pc_type,self.problem_date,self.problem_desc,self.timestamp,)
      def get_absolute_url(self):
          return "/app1/%s/" %(self.id)

class nw_malfunction(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        nettype=(('WIRE','WIRE'),('WIRELESS-CARD','WIRLESS-CARD'),('WIRELESS-USB','WIRELESS-USB'))
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        netwk_type = models.CharField(max_length=120,choices=nettype,verbose_name='نوع الشبكه')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
        problem_desc = models.TextField(verbose_name='وصف المشكله')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        status = models.BooleanField(default=True)
        publisher = models.ForeignKey(User,null=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s' % (self.user_fullname, self.user_sector, self.netwk_type, self.problem_date, self.problem_desc)


class print_malfunction(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        printer_type = models.CharField(max_length=120,verbose_name='نوع الطابعه')
        problem_date = models.DateTimeField(verbose_name='تاريخ المشكله')
        problem_desc = models.TextField(verbose_name='وصف المشكله')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True,blank=False)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s' % (self.user_fullname, self.user_sector, self.printer_type, self.problem_date, self.problem_desc)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)



class analytics(models.Model):
      sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
      years = (
          ('2018','2018'),
          ('2019','2019'),
          ('2020','2020'),
          ('2021','2021'),
          ('2022','2022'),
          ('2023','2023'),
          ('2024','2024'),
          ('2025','2025'),
          ('2026','2026'),
          ('2027','2027'),
          ('2028','2028'),
          ('2029','2029'),
          ('2030','2030'),
          ('2031','2031'),
          ('2032','2032'),
          ('2033','2033'),
          ('2034','2034'),
          ('2035','2035'),
          ('2036','2036'),
          ('2037','2037'),
          ('2038','2038'),
          ('2039','2039'),
          ('2040','2040'),
          ('2041','2041'),
          ('2042','2042'),
          ('2043','2043'),
          ('2044','2044'),
          ('2045','2045'),
          ('2046','2046'),
          ('2047','2047'),
          ('2048','2048'),
          ('2049','2049'),
          ('2050','2050'),
          ('2051','2051'),
          ('2052','2052'),
          ('2053','2053'),
          ('2054','2054'),
          ('2055','2055'),
          ('2056','2056'),
          ('2057','2057'),
          ('2058','2058'),
          ('2059','2059'),
          ('2060','2060'),
          ('2061','2061'),
          ('2062','2062'),
          ('2063','2063'),
          ('2064','2064'),
          ('2065','2065'),
          ('2066','2066'),
          ('2067','2067'),
          ('2068','2068'),
          ('2069','2069'),
          ('2070','2070'),
          ('2071','2071'),
          ('2072','2072'),
          ('2073','2073'),
          ('2074','2074'),
          ('2075','2075'),
          ('2076','2076'),
          ('2077','2077'),
          ('2078','2078'),
          ('2079','2079'),
          ('2080','2080'),
          ('2081','2081'),
          ('2082','2082'),
          ('2083','2083'),
          ('2084','2084'),
          ('2085','2085'),
          ('2086','2086'),
          ('2087','2087'),
          ('2088','2088'),
          ('2089','2089'),
          ('2090','2090'),
          ('2091','2091'),
          ('2092','2092'),
          ('2093','2093'),
          ('2094','2094'),
          ('2095','2095'),
          ('2096','2096'),
          ('2097','2097'),
          ('2098','2098'),
          ('2099','2099'),
          ('2100','2100'),
          ('2101','2101'),
      )
      select_sector = models.CharField(blank=False,max_length=120,choices=sectors,verbose_name='SectorName')
      select_year = models.CharField(blank=True, null=True,max_length=120,choices=years,verbose_name='SectorName')

      def __str__(self):
          return ( self.select_sector)

class tag:
      typechecked = models.BooleanField()
      sectchecked = models.BooleanField()
      usechecked = models.BooleanField()

class search(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        problem = (('HardWare','HardWare'),('Printers','Printers'),('Network','Network'))
        demand = (('Cartridge','Cartridge'),('Passrecovery','Passrecovery'),('Spareparts','Spareparts'))
        select_sector = models.CharField(blank=True,max_length=120,choices=sectors,verbose_name='SectorName')
        select_problem = models.CharField(blank=True,max_length=120,choices=problem,verbose_name='Problem Type')
        select_user = models.CharField(blank=True,max_length=120,verbose_name='اسم المستخدم')
        select_Demand = models.CharField(blank=True,max_length=120,choices=demand,verbose_name='Demand Type')
        demand_date_from = models.DateTimeField(verbose_name='تاريخ الطلب من')
        demand_date_to = models.DateTimeField(verbose_name='تاريخ الطلب الى')

        def __str__(self):
          return '%s %s %s %s %s %s' % (self.select_sector, self. select_problem, self.select_user,self.select_Demand,self.demand_date_from,self.demand_date_to)





class cartridges(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
              )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ الطلب')
        printer_type = models.CharField(max_length=120,verbose_name='نوع الطابعه')
        printer_model = models.CharField(max_length=120,verbose_name='موديل الطابعه')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path2,null=True,blank=True,default="NULL",verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.demand_date,self.printer_type,self.printer_model,self.timestamp,)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)



class   passrecovery(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ طلب الاسترداد')
        app_name= models.CharField(max_length=120,verbose_name='اسم التطبيق')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path4,null=True,default="NULL",blank=True,verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.pc_type,self.problem_date,self.problem_desc,self.timestamp,)
        def get_absolute_url(self):
            return "/app1/%s/" %(self.id)

class spareparts(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        demand_date = models.DateTimeField(verbose_name='تاريخ الطلب')
        part_type = models.CharField(max_length=120, verbose_name='نوع القطعه')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        thefile = models.FileField(upload_to = get_file_path3,null=True, blank=True, verbose_name='صورة الطلب المرفق')
        ip = models.CharField(blank=False,null=True,max_length=120)
        closed_by = models.CharField(blank=False, null=True, max_length=120)
        close_date = models.DateTimeField(auto_now_add=True,null=True)

        def __str__(self):
          return '%s %s %s %s %s %s ' % (
          self.user_fullname, self.user_sector, self.pc_type, self.problem_date, self.problem_desc, self.timestamp,)

        def get_absolute_url(self):
          return "/app1/%s/" % (self.id)



class accessory(models.Model):
      accessory = models.CharField(blank=False,null=True,max_length=120,)
      def __str__(self):
          return '%s' % (self.accessory)


class asset_pc(models.Model):
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)
      branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
      pctype=(('compatible','compatible'),('Brand','Brand'))
      ramtype=(('SDRAM','SDRAM'),('DDRAM','DDRAM'),('DDRAM2','DDRAM2'),('DDRAM3','DDRAM3'),('DDRAM4','DDRAM4'),)
      ramsize=(('128M','128M'),('256M','256M'),('512M','512M'),('756M','756M'),('1G','1G'),('1.128G',''),('1.256G','1.256G'),('1.512G','1.512G'),('1.768G','1.768G'),('2G','2G'),('2.128G','2.128G'),('2.256G','2.256G'),('2.512G','2.512G'),('2.768G','2.768G'),('3G','3G'),('3.128G','3.128G'),('3.256G','3.256G'),('3.512G','3.512G'),('3.768G','3.768G'),('4G','4G'),('4.128G','4.128G'),('4.256G','4.256G'),('4.512G','4.512G'),('4.768G','4.768G'),('5G','5G'),('6G','6G'),('7G','7G'),('8G','8G'))
      proctype=(('celeron','celeron'),('Pentium','Pentium'),('PentiumD','PentiumD'),('Pentium4','Pentium4'),('DualCore','DualCore'),('Core2Duo','Core2Duo'),('CoreI3','CoreI3'),('CoreI5','CoreI5'),('CoreI7','CoreI7'),('',''),)
      montype=(('CRT','CRT'),('LCD','LCD'),('LED','LED'),)
      os=(('NONE','NONE'),('WINDOWS XP','WINDOWS XP'),('WINDOWS 7','WINDOWS 7'),('WINDOWS 8','WINDOWS 8'),('WINDOWS 10','WINDOWS 10'),('LINUX','LINUX'),('MS-DOS','MS-DOS'))
      os_license=(('Licensed','Licensed'),('No License','No License'),)
      office=(('OFFICE 2003','OFFICE 2003'),('OFFICE 2007','OFFICE 2007'),('OFFICE 2010','OFFICE 2010'),('OFFICE 2013','OFFICE 2013'),('OFFICE 2016','OFFICE 2016'))
      accessories=(('DVD-ROM','DVD-ROM'),('CD-ROM','CD-ROM'),('KEYBOARD/MOUSE','KEYBOARD/MOUSE'),('DVD-RW','DVD-RW'),('FLASH-MEM','FLASH-MEM'),)

      user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
      hsectors = models.ForeignKey(hsectors,blank=True,null=True,verbose_name='رئاسة القطاعات')
      user_sector = models.ForeignKey(sector,blank=True,null=True,verbose_name='القطاع')
      os_version = models.CharField(blank=False,null=True,max_length=120,choices=os,verbose_name='نسخة نظام التشغيل الحاليه')
      os_version_oem = models.CharField(blank=True,null=True,max_length=120,default="None",choices=os,verbose_name='OEM OS LABELED VERSION')

      os_license = models.CharField(blank=False,null=True,max_length=120,choices=os_license,verbose_name='ترخيص نظام التشغيل')
      office_version = models.CharField(blank=False,null=True,max_length=120,choices=office,verbose_name='نسخة الاوڤيس')
      accessory = MultiSelectField(blank=False,max_length=120,null=True,choices=accessories,verbose_name='الملحقات')

      #accessory = models.ManyToManyField(accessory,blank=False,max_length=120,verbose_name='الملحقات')
      #user_sector = ChainedForeignKey('sector',chained_field="hectors",chained_model_field="hsectors",null=True,verbose_name='القطاع')
      bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
      pc_type = models.CharField(max_length=120,choices=pctype,verbose_name='نوع الجهاز',editable=True)
      pc_model = models.CharField(max_length=120,verbose_name='موديل الجهاز')
      ram_type= models.CharField(max_length=120,choices=ramtype,verbose_name='نوع الذاكره')
      ram_size= models.CharField(max_length=120,choices=ramsize,verbose_name='حجم الذاكره')
      processor_type= models.CharField(max_length=120,choices=proctype,verbose_name='نوع المعالج')
      harddisk_size= models.CharField(max_length=120,verbose_name='حجم وحدة التخزين')
      monitor_type= models.CharField(max_length=120,choices=montype,verbose_name='نوع الشاشه الجهاز')
      monitor_size= models.CharField(max_length=120,verbose_name='حجم الشاشه')
      nettype=(('WIRE','WIRE'),('WIRELESS-STICK','WIRELESS-STICK'),('WIRELESS-CARD','WIRELESS-CARD'),('NO-CONNECTION','NO-CONNECTION'))
      networking = models.CharField(blank=False,null=True,max_length=120,choices=nettype,verbose_name='نوع الشپگه')
      domain=(('JOINED','JOINED'),('UNJOINED','UNJOINED'),)
      joined = models.CharField(blank=True, null=True,max_length=120,choices=domain,verbose_name='الرپط پالدومين')
      notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
      timestamp = models.DateTimeField(auto_now_add=True,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)  
      publisher = models.ForeignKey(User,null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False,null=True,max_length=120)
      def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.user_head_sector,self.pc_type,self.timestamp,)
      def get_absolute_url(self):
          return "/app1/%s/" %(self.id)


class asset_printer(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        contype =(('USB','USB'),('ETHERNET','ETHERNET'),('USB+ETHERNET','USB+ETHERNET'),('LTP-PORT','LTP-PORT'),)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        printtype=(('LaserJet','LaserJet'),('OfficeJet','OfficeJet'),('DeskJet','DeskJet'),('InkJet','InkJet'),('MFP','MFP'))
        conntype=(('PARALLEL(ltp)','PARALLEL(ltp)'),('USB','USB'),('ETHERNET','ETHERNET'),('WIRELESS','WIRELESS'),('USB & ETHERNET','USB & ETHERNET'),('USB+ETHERNET+PARALLEL','USB+ETHERNET+PARALLEL'))
        bransh = models.CharField(blank=False,null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        printer_type = models.CharField(max_length=120,choices=printtype, verbose_name='نوع الطابعه')
        conn_type = models.CharField(max_length=120,choices=conntype,default="NULL" ,verbose_name='نوع التوصيل')
        printer_model = models.CharField(max_length=120, verbose_name='موديل الطابعه')
        cartridge_number = models.CharField(blank=True,max_length=120, verbose_name='رقم عبوة الحبر')
        black_number = models.CharField(blank=True, null=True,max_length=120, verbose_name='رقم عبوة الحبر الاسود')
        color_number = models.CharField(blank=True, null=True,max_length=120, verbose_name='رقم عبوة الحبر الالوان')

        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)

class asset_scanner(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
        scantype=(('LowSpeedNormal','LowSpeedNormal'),('HighSpeedMultiScan','HighSpeedMultiScan'),)
        user_fullname = models.CharField(max_length=120, verbose_name='اسم المستخدم')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        bransh = models.CharField(blank=False, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        scanner_model = models.CharField(max_length=120, verbose_name='موديل الماسح الضوئى')
        scanner_type = models.CharField(max_length=120,default="Null", choices=scantype,verbose_name='نوع الماسح الضوئى')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)

class asset_copier(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
        copiertype =(('USB','USB'),('ETHERNET','ETHERNET'),('USB+ETHERNET','USB+ETHERNET'),('NO-DATA-CONNECTION','NO-DATA-CONNECTION'),)
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        user_sector = models.ForeignKey(sector, blank=True, null=True, verbose_name='القطاع')
        bransh = models.CharField(blank=True,null=True,max_length=120, choices=branshes, verbose_name='اسم الفرع')
        copier_model = models.CharField(max_length=120, verbose_name='موديل ماكينة التصوير')
        cartridge_number = models.CharField(max_length=120, verbose_name='رقم عبوة الحبر')
        conn_type = models.CharField(blank=True,null=True,max_length=120, default="NO-DATA-CONNECTION",choices=copiertype, verbose_name='نوع التوصيل الشبكى')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
            return '%s %s %s %s %s %s ' % (self.user_fullname, self.user_sector, self.printer_type, self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_server(models.Model):
      id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

      branshes = (
            ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
            ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
      floores = (
        ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
        ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'),('الاول','الاول'))
      bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
      floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
      server_vendor = models.CharField(max_length=120, verbose_name='المصنع')
      server_model = models.CharField(max_length=120, verbose_name='الموديل')
      montype = (('CRT','CRT'), ('LCD','LCD'), ('LED','LED'),)
      monitor_type = models.CharField(blank=True, null=True,max_length=120, choices=montype, verbose_name='نوع الشاشه الجهاز')
      ram_size = models.CharField(max_length=120, verbose_name='الذاكره')

      monitor_size = models.CharField(blank=True, null=True,max_length=120, verbose_name='حچم وموديل الشاشه')
      processor = models.CharField(max_length=120, verbose_name='المعالج ',null=True)
      harddisk_size = models.CharField(max_length=120, verbose_name='حجم التخزين')
      created = models.DateTimeField(auto_now_add=True,null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)  
      publisher = models.ForeignKey(User, null=True)
      status = models.BooleanField(default=True)
      ip = models.CharField(blank=False, null=True, max_length=120)

      def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.server_model, self.server_vendor, self.bransh, self.floor,self.ram_size,self.harddisk_size,self.processor)

      def get_absolute_url(self):
        return "/app1/%s/" % (self.id)




      #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_switch(models.Model):
        branshes = (
          ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
          ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
        floores = (
          ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
          ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
        switch_vendor = models.CharField(max_length=120, verbose_name='المصنع')
        switch_model = models.CharField(max_length=120, verbose_name='الموديل')
        port_numbers = models.CharField(max_length=120, verbose_name='عدد المنافذ')
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)
        created = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)  

        def __str__(self):
          return '%s %s %s %s ' % (
            self.bransh, self.floor, self.switch_model, self.switch_vendor,)



        def get_absolute_url(self):
          return "/app1/%s/" % (self.id)



#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_accesspoint(models.Model):
          branshes = (
            ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
            ('سيتى بنك','سيتى بنك'),
            ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
          floores = (
            ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
            ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
          id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

          bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
          floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
          accesspoint_vendor = models.CharField(max_length=120, verbose_name='المصنع')
          accesspoint_model = models.CharField(max_length=120, verbose_name='الموديل')
          publisher = models.ForeignKey(User, null=True)
          ip = models.CharField(blank=False, null=True, max_length=120)
          created = models.DateTimeField(auto_now_add=True, null=True)
          updated = models.DateTimeField(auto_now_add=True,null=True)
          updater = models.CharField(blank=False, null=True, max_length=120)  
          def __str__(self):
            return '%s %s %s %s ' % (self.bransh, self.floor, self.accesspoint_model, self.accesspoint_vendor,)

          def get_absolute_url(self):
            return "/app1/%s/" % (self.id)



#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_stick(models.Model):
        sectors = (
        ('مكتب السيد رئيس مجلس الإدارة والعضو المنتدب','مكتب السيد رئيس مجلس الإدارة والعضو المنتدب'),
        ('مكتب العضو المنتدب للشئون المالية والأدارية','مكتب العضو المنتدب للشئون المالية والأدارية'),
        ('قطاع المعلومات','قطاع المعلومات'),
        ('قطاعات ادارة الشركة والمتابعة','قطاعات ادارة الشركة والمتابعة'),
        ('قطاعات ادارة الاصول والاستثمارات','قطاعات ادارة الاصول والاستثمارات'),
        ('قطاعات الشئون المالية والموازنات','قطاعات الشئون المالية والموازنات'),
        ('قطاعات الرقابة علي الفنادق و الاستثمار','قطاعات الرقابة علي الفنادق و الاستثمار'),
        ('قطاعات الشئون التجارية والاحتياجات','قطاعات الشئون التجارية والاحتياجات'),
        ('قطاعات الشئون الادارية','قطاعات الشئون الادارية'),
        ('قطاعات التدريب والمعاهد الفندقية','قطاعات التدريب والمعاهد الفندقية'),
        ('قطاعات العلاقات العامة والشئون الطبية والخدمات','قطاعات العلاقات العامة والشئون الطبية والخدمات'),
        ('قطاعات الشئون الهندسية','قطاعات الشئون الهندسية'),
        ('قطاعات الشئون القانونية','قطاعات الشئون القانونية'),
        ('قطاع الامن','قطاع الامن'),
        ('قطاع الرقابة الداخلية','قطاع الرقابة الداخلية'),
        )
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم',default="NULL")
        user_sector = models.CharField(blank=False,editable=True,max_length=120,choices=sectors,verbose_name='رئاسة القطاعات',default="NULL")
        branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
        ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
        floores = (
        ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
        ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
        bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
        stick_vendor = models.CharField(max_length=120, verbose_name='المصنع')
        stick_model = models.CharField(max_length=120, verbose_name='الموديل')
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)
        created = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        def __str__(self):
            return '%s %s %s %s ' % ( self.bransh, self.floor, self.stick_model, self.stick_vendor,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)





            #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_router(models.Model):
              branshes = (
                ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
                ('سيتى بنك','سيتى بنك'),
                ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
              floores = (
                ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
                ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
              bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                        verbose_name='اسم الفرع')
              id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
              floor = models.CharField(blank=True, null=True, max_length=120, choices=floores, verbose_name='رقم الطابق')
              router_vendor = models.CharField(max_length=120, verbose_name='المصنع')
              router_model = models.CharField(max_length=120, verbose_name='الموديل')
              publisher = models.ForeignKey(User, null=True)
              ip = models.CharField(blank=False, null=True, max_length=120)
              created = models.DateTimeField(auto_now_add=True, null=True)
              updated = models.DateTimeField(auto_now_add=True,null=True)
              updater = models.CharField(blank=False, null=True, max_length=120)  
              def __str__(self):
                return '%s %s %s %s ' % ( self.bransh, self.floor, self.router_model, self.router_vendor,)
              def get_absolute_url(self):
                return "/app1/%s/" % (self.id)







              #---------------------------------------------------------------------------------
#*********************************************************************************
class asset_repeater(models.Model):
                branshes = (
                  ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
                  ('سيتى بنك','سيتى بنك'),
                  ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
                floores = (
                  ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
                  ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
                bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                          verbose_name='اسم الفرع')
                floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,
                                         verbose_name='رقم الطابق')
                id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
                repeater_vendor = models.CharField(max_length=120, verbose_name='المصنع')
                repeater_model = models.CharField(max_length=120, verbose_name='الموديل')
                publisher = models.ForeignKey(User, null=True)
                status = models.BooleanField(default=True)
                ip = models.CharField(blank=False, null=True, max_length=120)
                created = models.DateTimeField(auto_now_add=True, null=True)
                updated = models.DateTimeField(auto_now_add=True,null=True)
                updater = models.CharField(blank=False, null=True, max_length=120)  
                def __str__(self):
                  return '%s %s %s %s ' % (self.bransh, self.floor, self.repeater_model, self.repeater_vendor,)


                def get_absolute_url(self):
                  return "/app1/%s/" % (self.id)






#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_rack(models.Model):
                  branshes = (
                    ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
                    ('سيتى بنك','سيتى بنك'),
                    ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
                  floores = (
                    ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
                    ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
                  racktype = (
                    ('Wall_Mounted','Wall_Mounted'), ('STAND_ALONE','STAND_ALONE'), ('STAND_ALONE_SMALL','STAND_ALONE_SMALL'),)
                  id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
                  bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,verbose_name='اسم الفرع')
                  floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,verbose_name='رقم الطابق')
                  rack_type= models.CharField(blank=True, null=True, max_length=120, choices=racktype,verbose_name='نوع الراك')
                  publisher = models.ForeignKey(User, null=True)
                  status = models.BooleanField(default=True)
                  ip = models.CharField(blank=False, null=True, max_length=120)
                  created = models.DateTimeField(auto_now_add=True, null=True)
                  updated = models.DateTimeField(auto_now_add=True,null=True)
                  updater = models.CharField(blank=False, null=True, max_length=120)  
                  def __str__(self):
                    return '%s %s %s  ' % ( self.bransh, self.floor, self.rack_type,)



                  def get_absolute_url(self):
                    return "/app1/%s/" % (self.id)




#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_device(models.Model):
                    id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

                    branshes = (
                      ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
                      ('سيتى بنك','سيتى بنك'),
                      ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
                    floores = (
                      ('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
                      ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
                    id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

                    bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,
                                              verbose_name='اسم الفرع')
                    floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,
                                             verbose_name='رقم الطابق')
                    device_name = models.CharField(max_length=120, verbose_name='اسم الجهاز')
                    device_desc =  models.TextField(verbose_name='وصف الجهاز')
                    publisher = models.ForeignKey(User, null=True)
                    ip = models.CharField(blank=False, null=True, max_length=120)
                    created = models.DateTimeField(auto_now_add=True, null=True)
                    updated = models.DateTimeField(auto_now_add=True,null=True)
                    updater = models.CharField(blank=False, null=True, max_length=120)  
                    def __str__(self):
                      return '%s %s %s %s ' % (self.bransh, self.floor, self.device_name, self.device_desc,)

                    def get_absolute_url(self):
                      return "/app1/%s/" % (self.id)




#---------------------------------------------------------------------------------
#*********************************************************************************
class asset_blueprint(models.Model):
      id= models.CharField(max_length=120,primary_key=True,default = uuid.uuid4)

      branshes = (('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'),
                 ('سيتى بنك','سيتى بنك'),
                 ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
      floores = (('التاسع','التاسع'), ('الثامن','الثامن'), ('العاشر','العاشر'), ('السابع','السابع'),('السادس','السادس'),
                ('الرابع','الرابع'), ('الحادى عشر','الحادى عشر'), ('الاول','الاول'))
      bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes,verbose_name='اسم الفرع')
      floor = models.CharField(blank=True, null=True, max_length=120, choices=floores,verbose_name='رقم الطابق')
      name = models.CharField(blank=False, null=True, max_length=120,verbose_name='اسم المخطط')
      ip = models.CharField(blank=False, null=True, max_length=120)
      publisher = models.ForeignKey(User, null=True)
      image = models.FileField(upload_to = get_file_path1,null=True,blank=True,verbose_name='صورة المخطط')
      imagesrc = models.FileField(null=True,blank=True,verbose_name='ملف المصدر')
      created = models.DateTimeField(auto_now_add=True, null=True)
      updated = models.DateTimeField(auto_now_add=True,null=True)
      updater = models.CharField(blank=False, null=True, max_length=120)
      def __str__(self):
        return '%s %s %s %s ' % (self.bransh, self.floor, self.image, self.imagesrc,)

      def get_absolute_url(self):
        return "/app1/%s/" % (self.id)






        #---------------------------------------------------------------------------------
#*********************************************************************************

class asset_lab(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
        os = (('WINDOWS XP','WINDOWS XP'), ('WINDOWS 7','WINDOWS 7'), ('WINDOWS 8','WINDOWS 8'),
              ('WINDOWS 10','WINDOWS 10'), ('LINUX','LINUX'), ('MS-DOS','MS-DOS'))
        user_fullname = models.CharField(max_length=120,verbose_name='اسم المستخدم')
        user_sector = models.ForeignKey(sector,blank=False,max_length=120,null=True,verbose_name='القطاع')
        hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
        os_version = models.CharField(blank=False, null=True, max_length=120, choices=os,verbose_name='نسخة نظام التشغيل الحاليه')
        os_version_oem = models.CharField(blank=False, null=True, max_length=120, choices=os,verbose_name='OEM OS LABELED VERSION')
        bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
        lab_model = models.CharField(max_length=120,verbose_name='موديل الجهاز')
        lab_vendor = models.CharField(max_length=120,verbose_name='اسم الشركه المصنعه')
        lab_serial = models.CharField(max_length=120,verbose_name='الرقم التسلسلى للجهاز')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User,null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        def __str__(self):
          return '%s %s %s %s %s %s ' % (self.user_fullname,self.user_sector,self.hsectors,self.lab_type,self.timestamp,)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)


#---------------------------------------------------------------------------
class junk_parts(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)
        branshes=(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),)
        jtype = (('COMPUTER','COMPUTER'), ('PRINTER','PRINTER'), ('SCANNER','SCANNER'), ('SWITCH','SWITCH'), ('ROUTER','ROUTER'), ('ACCESSPOINT','ACCESSPOINT'), ('SERVER','SERVER'), ('REPEATER','REPEATER'), ('KEYBORAD','KEYBORAD'), ('MOUSE','MOUSE'),('POWER CABLE','POWER CABLE'), ('NETWORK CARD','NETWORK CARD'),('POWER SUPPLY','POWER SUPPLY'),('MONITOR','MONITOR'),('OTHER','OTHER'),)
        places =(('الفواله','الفواله'),('المهندسيين','المهندسيين'),('جاردن سيتى','جاردن سيتى'),('سيتى بنك','سيتى بنك'),('قصر النيل','قصر النيل'),('التوفيقيه','التوفيقيه'),('مخزن','مخزن'))
        cplaces =(('پالمقر','پالمقر'),('چهه اخرى','چهه اخرى'))
        junk_type = models.CharField(max_length=120,choices=jtype,verbose_name='نوع القطعه التالڤه')
        junk_brand  = models.CharField(max_length=120,blank=True,verbose_name='اسم وموديل القطعه')
        damadge_type = models.CharField(max_length=120,blank=True,verbose_name='نوع التلڤ')
        user_sector = models.ForeignKey(sector,blank=True,null=True,max_length=120,verbose_name=' القطاع')
        hsectors = models.ForeignKey(hsectors,blank=True, null=True, verbose_name='رئاسة القطاعات')
        junk_user = models.CharField(max_length=120,blank=True,verbose_name='اسم المستخدم')
        bransh = models.CharField(blank=False,null=True,max_length=120,choices=branshes,verbose_name='اسم الفرع')
        notes = models.TextField(blank=True, null=True,verbose_name='ملاحظات')
        timestamp = models.DateTimeField(auto_now_add=True,null=True)
        updated = models.DateTimeField(auto_now_add=True,null=True)
        updater = models.CharField(blank=False, null=True, max_length=120)
        publisher = models.ForeignKey(User,null=True)
        pstatus = models.BooleanField(default=True)
        ip = models.CharField(blank=False,null=True,max_length=120)
        cplace = models.CharField(max_length=120,blank=True,choices=cplaces,default='پالمقر',verbose_name='المگان الحالى')
        transto= models.CharField(max_length=120,blank=True,choices=places,verbose_name='نقل الى')
        def __str__(self):
          return '%s  ' % (self.timestamp)
        def get_absolute_url(self):
          return "/app1/%s/" %(self.id)




#----------------------------------------------------------------------------------------------
class searchassets(models.Model):
    branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)
    objects = (('COMPUTERS','COMPUTERS'), ('LABTOPS','LABTOPS'), ('PRINTERS','PRINTERS'), ('SCANNERS','SCANNERS'),
               ('COPIERS','COPIERS'))
    select_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
    select_hsectors = models.ForeignKey(hsectors, blank=True, null=True, verbose_name='رئاسة القطاعات')
    select_sector = models.ForeignKey(sector, blank=True, null=True, max_length=120, verbose_name=' القطاع')
    select_user = models.CharField(blank=True,null=True ,max_length=120, verbose_name='اسم المستخدم')
    select_object = models.CharField(blank=True,null=True, max_length=120, choices=objects, verbose_name='نوع الاصل')
#-------------------computers
    proctype = (('celeron','celeron'), ('Pentium','Pentium'), ('PentiumD','PentiumD'), ('Pentium4','Pentium4'),
                ('DualCore','DualCore'), ('Core2Duo','Core2Duo'), ('CoreI3','CoreI3'), ('CoreI5','CoreI5'),
                ('CoreI7','CoreI7'), ('',''),)
    processor_type = models.CharField(blank=True, null=True,max_length=120, choices=proctype, verbose_name='نوع المعالج')
    domain = (('JOINED','JOINED'), ('UNJOINED','UNJOINED'),)
    joined = models.CharField(blank=True, null=True, max_length=120, choices=domain, verbose_name='الرپط پالدومين')
    harddisk_size = models.CharField(blank=True, null=True,max_length=120, verbose_name='حجم وحدة التخزين')
    pc_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الجهاز')
    montype = (('CRT','CRT'), ('LCD','LCD'), ('LED','LED'),)
    monitor_type = models.CharField(blank=True, null=True,max_length=120, choices=montype, verbose_name='نوع الشاشه الجهاز')
    os_license = (('Licensed','Licensed'), ('No License','No License'),)
    os_license = models.CharField(blank=True, null=True, max_length=120, choices=os_license,verbose_name='ترخيص نظام التشغيل')

#-------------------labs
    lab_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الجهاز')
    lab_vendor = models.CharField(blank=True, null=True,max_length=120, verbose_name='اسم الشركه المصنعه')
#-------------------printers
    printtype = (
    ('LaserJet','LaserJet'), ('OfficeJet','OfficeJet'), ('DeskJet','DeskJet'), ('InkJet','InkJet'), ('MFP','MFP'))
    printer_type = models.CharField(blank=True, null=True,max_length=120, choices=printtype, verbose_name='نوع الطابعه')
    printer_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الطابعه')

    #--------------------scanners
    scantype = (('LowSpeedNormal','LowSpeedNormal'), ('HighSpeedMultiScan','HighSpeedMultiScan'),)
    scanner_type = models.CharField(blank=True, null=True,max_length=120, default="Null", choices=scantype, verbose_name='نوع الماسح الضوئى')
    scanner_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل الماسح الضوئى')

    #--------------------copiers
    copier_model = models.CharField(blank=True, null=True,max_length=120, verbose_name='موديل ماكينة التصوير')
    copiertype = (('USB','USB'), ('ETHERNET','ETHERNET'), ('USB+ETHERNET','USB+ETHERNET'),
                  ('NO-DATA-CONNECTION','NO-DATA-CONNECTION'),)
    conn_type = models.CharField(blank=True, null=True, max_length=120, default="NO-DATA-CONNECTION",choices=copiertype, verbose_name='نوع التوصيل الشبكى')


def __str__(self):
    return '%s %s %s %s' % (self.select_sector, self.select_hsectors, self.select_user,select_object)
#---------------------------------------------------------------------------------------------------------------
class missions(models.Model):
        id = models.CharField(max_length=120, primary_key=True, default=uuid.uuid4)

        branshes = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'),)


        places = (
        ('الفواله','الفواله'), ('المهندسيين','المهندسيين'), ('جاردن سيتى','جاردن سيتى'), ('سيتى بنك','سيتى بنك'),
        ('قصر النيل','قصر النيل'), ('التوفيقيه','التوفيقيه'), ('مخزن','مخزن'))
        places = (('داخل الشرگه','داخل الشرگه'), ('چهه اخرى','چهه اخرى'))

        partners = (
                    (' محمد احمد ','محمد احمد'),(' عبد المنعم رفعت ','عبد المنعم رفعت'),(' أحمد سعيد ','أحمد سعيد'),(' وائل علاء الدين ','وائل علاء الدين'),(' مصطفى نادى ','مصطفى نادى'),(' احمد رفقى ','احمد رفقى'),

                    (' وائل الطويل ','وائل الطويل'),(' اسلام عبد الوهاب ','اسلام عبد الوهاب'),(' أحمد حجازى ','أحمد حجازى'),(' أحمد صلاح ','أحمد صلاح'),(' رامز سمير ','رامز سمير'),(' أحمد عبيد  ','أحمد عبيد '),

                    (' أحمد إبراهيم ','أحمد إبراهيم'),(' محمد جاد ','محمد جاد'),(' ياسمين الجوهرى ','ياسمين الجوهرى'),(' اميرة عبد العال ','اميرة عبد العال'),(' مها محمد ','مها محمد'),(' أمجد أبو السعود ','أمجد أبو السعود'),

                    (' أسامة فتحى ','أسامة فتحى'),(' محمد مصطفى ','محمد مصطفى'),(' دينا سراج ','دينا سراج'),(' محمد شعبان ','محمد شعبان'),(' هانى مصطفى ','هانى مصطفى'),(' محمد جاد  ','محمد جاد '),(' محمد احمد ','محمد احمد'),

                    (' احمد عصام ','احمد عصام'),(' إسلام عبد الوهاب ','إسلام عبد الوهاب'))









        mission1 = models.TextField(max_length=120,blank=True, verbose_name='المهامه الاولى')
        mission2 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الثانيه')
        mission3 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الثالثه')
        mission4 = models.TextField(max_length=120, blank=True,verbose_name='المهامه الراپعه')
        mission5 = models.TextField(max_length=120,blank=True, verbose_name='المهامه الخامسه')
        it_partners = models.CharField(max_length=120,blank=True,choices=partners,default='داخل الشرگه',verbose_name='المشترگين ڤى الاعمال')
        m1_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m2_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m3_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m4_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')
        m5_bransh = models.CharField(blank=True, null=True, max_length=120, choices=branshes, verbose_name='اسم الفرع')

        m1_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m2_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m3_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m4_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m5_out_premisis = models.CharField(max_length=120, blank=True, verbose_name='چهة خارچ الشرگه')
        m1_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان')
        m2_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان')
        m3_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان')
        m4_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان')
        m5_place = models.CharField(max_length=120,blank=True,choices=places,default='داخل الشرگه',verbose_name='المگان')
        timestamp = models.DateTimeField(auto_now_add=True, null=True)
        publisher = models.ForeignKey(User, null=True)
        ip = models.CharField(blank=False, null=True, max_length=120)


        def __str__(self):
            return '%s  ' % (self.timestamp)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#=================================================================
class LAW(models.Model):

        case_name = models.CharField(max_length=120, verbose_name='اسم القضيه')
        case_type = models.CharField(blank=True, max_length=120, null=True, verbose_name='نوع القضيه')
        court_name = models.CharField( blank=True, null=True,max_length=120, verbose_name='المحگمه المتداول پها القضيه')
        case_start_date = models.DateTimeField(blank=True, null=True, max_length=120, verbose_name=' تاريخ پدا القضيه')
        lawyer_name = models.CharField(blank=True, null=True, max_length=120, verbose_name='اسم المحامى متولى القضيه')
        about_case = models.TextField(blank=True, null=True, max_length=120,  verbose_name='نپذه عن القضيه')
        last_case_update = models.TextField(max_length=2048, verbose_name='اخر تحديث للقضيه')
        timestamp = models.DateTimeField(auto_now_add=True, null=True)
        updated = models.DateTimeField(auto_now_add=True, null=True)
        publisher = models.ForeignKey(User, null=True)
        status = models.BooleanField(default=True)
        ip = models.CharField(blank=True, null=True, max_length=120)

        def __str__(self):
            return '%s' % (self.timestamp,)

        def get_absolute_url(self):
            return "/app1/%s/" % (self.id)
#------------------------------------------------------------------------------
class search_case(models.Model):
          case_name = models.CharField(blank=True, max_length=120,verbose_name='الپحث پاسم القضيه')
          lawyer_name = models.CharField(blank=True, max_length=120,verbose_name=' الپحث پاسم المحامى')
          court_name = models.CharField(blank=True, max_length=120, verbose_name='الپحث پاسم المحگمه')

          def __str__(self):
                  return '%s %s %s ' % ( self.case_name, self.lawyer_name, self.court_name,)

#*****************************************************************************************************************************
#*****************************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------------------------

class law_cases(models.Model):
      yrs =(('1900','1900'),
            ('1901','1901'),
            ('1902','1902'),
            ('1903','1903'),
            ('1904','1904'),
            ('1905','1905'),
            ('1906','1906'),
            ('1907','1907'),
            ('1908','1908'),
            ('1909','1909'),
            ('1910','1910'),
            ('1911','1911'),
            ('1912','1912'),
            ('1913','1913'),
            ('1914','1914'),
            ('1915','1915'),
            ('1916','1916'),
            ('1917','1917'),
            ('1918','1918'),
            ('1919','1919'),
            ('1920','1920'),
            ('1921','1921'),
            ('1922','1922'),
            ('1923','1923'),
            ('1924','1924'),
            ('1925','1925'),
            ('1926','1926'),
            ('1927','1927'),
            ('1928','1928'),
            ('1929','1929'),
            ('1930','1930'),
            ('1931','1931'),
            ('1932','1932'),
            ('1933','1933'),
            ('1934','1934'),
            ('1935','1935'),
            ('1936','1936'),
            ('1937','1937'),
            ('1938','1938'),
            ('1939','1939'),
            ('1940','1940'),
            ('1941','1941'),
            ('1942','1942'),
            ('1943','1943'),
            ('1944','1944'),
            ('1945','1945'),
            ('1946','1946'),
            ('1947','1947'),
            ('1948','1948'),
            ('1949','1949'),
            ('1950','1950'),
            ('1951','1951'),
            ('1952','1952'),
            ('1953','1953'),
            ('1954','1954'),
            ('1955','1955'),
            ('1956','1956'),
            ('1957','1957'),
            ('1958','1958'),
            ('1959','1959'),
            ('1960','1960'),
            ('1961','1961'),
            ('1962','1962'),
            ('1963','1963'),
            ('1964','1964'),
            ('1965','1965'),
            ('1966','1966'),
            ('1967','1967'),
            ('1968','1968'),
            ('1969','1969'),
            ('1970','1970'),
            ('1971','1971'),
            ('1972','1972'),
            ('1973','1973'),
            ('1974','1974'),
            ('1975','1975'),
            ('1976','1976'),
            ('1977','1977'),
            ('1978','1978'),
            ('1979','1979'),
            ('1980','1980'),
            ('1981','1981'),
            ('1982','1982'),
            ('1983','1983'),
            ('1984','1984'),
            ('1985','1985'),
            ('1986','1986'),
            ('1987','1987'),
            ('1988','1988'),
            ('1989','1989'),
            ('1990','1990'),
            ('1991','1991'),
            ('1992','1992'),
            ('1993','1993'),
            ('1994','1994'),
            ('1995','1995'),
            ('1996','1996'),
            ('1997','1997'),
            ('1998','1998'),
            ('1999','1999'),
            ('2000','2000'),
            ('2001','2001'),
            ('2002','2002'),
            ('2003','2003'),
            ('2004','2004'),
            ('2005','2005'),
            ('2006','2006'),
            ('2007','2007'),
            ('2008','2008'),
            ('2009','2009'),
            ('2010','2010'),
            ('2011','2011'),
            ('2012','2012'),
            ('2013','2013'),
            ('2014','2014'),
            ('2015','2015'),
            ('2016','2016'),
            ('2017','2017'),
            ('2018','2018'),
            ('2019','2019'),
            ('2020','2020'),
            ('2021','2021'),
            ('2022','2022'),
            ('2023','2023'),
            ('2024','2024'),
            ('2025','2025'),
            ('2026','2026'),
            ('2027','2027'),
            ('2028','2028'),
            ('2029','2029'),
            ('2030','2030'),
            ('2031','2031'),
            ('2032','2032'),
            ('2033','2033'),
            ('2034','2034'),
            ('2035','2035'),
            ('2036','2036'),
            ('2037','2037'),
            ('2038','2038'),
            ('2039','2039'),
            ('2040','2040'),
            ('2041','2041'),
            ('2042','2042'),
            ('2043','2043'),
            ('2044','2044'),
            ('2045','2045'),
            ('2046','2046'),
            ('2047','2047'),
            ('2048','2048'),
            ('2049','2049'),
            ('2050','2050'),
            ('2051','2051'),
            ('2052','2052'),
            ('2053','2053'),
            ('2054','2054'),
            ('2055','2055'),
            ('2056','2056'),
            ('2057','2057'),
            ('2058','2058'),
            ('2059','2059'),
            ('2060','2060')
            )
      case_number = models.CharField(max_length=120, verbose_name='رقم الدعوى')
      case_year = models.CharField(blank=True,max_length=120, null=True, verbose_name='سنة الدعوى')
      case_depart = models.ForeignKey(casedep,blank=True, null=True, max_length=120, verbose_name='  الدائره')
      case_depart_type = models.ForeignKey(case_depart_type,blank=True, null=True, max_length=120, verbose_name=' نوع الدائره  ')
      case_court = models.ForeignKey(case_court_name,blank=True, null=True, max_length=120, verbose_name='المحكمه  ')
      degree_of_litigation = models.ForeignKey(litigationdeg,blank=True, null=True, max_length=120, verbose_name='درجة التقاضى')
      adversary  = models.ForeignKey(oponent,max_length=2048, verbose_name='الخصم ')
      adversay_represent = models.ForeignKey(oponentrep,blank=True, null=True, max_length=120,verbose_name='صفة الخصم ')
      comapny_represent = models.ForeignKey(comprep,blank=True, null=True, max_length=120,verbose_name='صفة الشركه ')
      case_subject = models.CharField(max_length=120,blank=True, null=True, verbose_name='موضوع الدعوى')
      case_subject_detail = models.TextField(max_length=120, verbose_name='موضوع الدعوى تفصيلا')
      #sitting_sequences = models.CharField(max_length=120, verbose_name='تتابع الجلسات')
      last_sitting = models.CharField(max_length=120, verbose_name='اخر جلسه')
      expected_financial_affairs = models.CharField(max_length=120, verbose_name='الاعباء الماليه المتوقعه')
      weighted_percent_of_gain = models.ForeignKey(gainwtpercent,max_length=120, verbose_name='ترجيح ونسبة الكسب')
      notes = models.TextField(max_length=120,blank=True, null=True, verbose_name='ملاحظات')
      #lawyers_successions = models.CharField(max_length=120, verbose_name='تتابع المحامين')
      date_of_establsihment = models.CharField(max_length=120, verbose_name='تاريخ الورود')
      case_classification = models.ForeignKey(case_classification,blank=True, null=True,max_length=120, verbose_name='نوع الدعوى')
      case_current_status= models.ForeignKey(case_current_status,blank=True, null=True,max_length=120, verbose_name='حالة الدعوى')
      current_lawyer = models.ForeignKey(case_lawyer,max_length=120,blank=True, null=True, verbose_name='المحامى المباشر')
      case_category = models.ForeignKey(case_category,max_length=120,blank=True, null=True, verbose_name='تصنيف الدعوى')
      publisher = models.ForeignKey(User, null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      def __str__(self):
          return '%s' % (self.timestamp,)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)


class case_sittings(models.Model):
    case_number = models.CharField(max_length=120, verbose_name='رقم الدعوى')
    sitting_date = models.DateTimeField(blank=True, max_length=120, null=True, verbose_name='تاريخ الجلسه')
    sitting_decision = models.TextField(blank=True, null=True, max_length=120, verbose_name='   قرار الجلسه')
    attend_lawyer = models.ForeignKey(case_lawyer,blank=True, null=True, max_length=120, verbose_name='اسم المحامى  الحاضر')
    publisher = models.ForeignKey(User, null=True)
    ip = models.CharField(blank=True, null=True, max_length=120)

    def __str__(self):
        return '%s' % (self.timestamp,)

    def get_absolute_url(self):
        return "/app1/%s/" % (self.id)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        

#####master
class working_pationt(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      job_title = models.CharField(max_length=120,null=True, blank=True, verbose_name='الدرجة الوظيفية')
      patient_age = models.CharField(max_length=120, verbose_name='سن المريض ')
      medical_number = models.CharField(max_length=120, verbose_name=' الرقم الطبى ')
      notes_number = models.CharField(max_length=120, verbose_name='رقم الدفتر ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name='العيادة التابعة')
      the_image_file = models.FileField(upload_to = get_file_path01,null=True, blank=True, verbose_name='صورة الطلب المرفق')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)



      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)
      
class retired_pationt(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      job_title = models.CharField(max_length=120,null=True, blank=True, verbose_name=' الدرجة الوظيفية عند المعاش')
      patient_age = models.CharField(max_length=120, verbose_name='سن المريض ')
      medical_number = models.CharField(max_length=120, verbose_name=' الرقم الطبى ')
      notes_number = models.CharField(max_length=120, verbose_name='رقم الدفتر ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name='العيادة التابعة') 
      the_image_file = models.FileField(upload_to = get_file_path02,null=True, blank=True, verbose_name='صورة الطلب المرفق')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True) 
      publisher = models.ForeignKey(User,null=True)
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)
class mgmt_board_membr(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      job_title = models.CharField(max_length=120,null=True, blank=True, verbose_name='الدرجة الوظيفية')
      patient_age = models.CharField(max_length=120, verbose_name='سن المريض ')
      medical_number = models.CharField(max_length=120, verbose_name=' الرقم الطبى ')
      notes_number = models.CharField(max_length=120, verbose_name='رقم الدفتر ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name='العيادة التابعة') 
      the_image_file = models.FileField(upload_to = get_file_path01,null=True, blank=True, verbose_name='صورة الطلب المرفق')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True) 
      publisher = models.ForeignKey(User,null=True)
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)           
      
class midicine(models.Model):
      midicine_name = models.CharField(max_length=120, verbose_name='اسم الدواء ')
      midicine_price = models.DecimalField(blank=True, null=True, max_digits=19, decimal_places=5, verbose_name='السعر')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)                                                                                                                                                                  
      
class hospital(models.Model):
      hospital_name = models.CharField(max_length=120, verbose_name='اسم المستشفى ')
      hospital_addr = models.CharField(max_length=120, verbose_name='عنوان المستشفى ')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)

      def __str__(self):
          return '%s' % (self.hospital_name)      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 
      
      
class laboratory(models.Model):
      lab_name = models.CharField(max_length=120, verbose_name='اسم المعمل ')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)



      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 
      
class scan_center(models.Model):

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)   

      pass
class doctor_clinic(models.Model):
      doc_name = models.CharField(max_length=120, verbose_name=' اسم الطبيب  ')
      clinic_addr= models.CharField(max_length=120, verbose_name=' العنوان ')
      clinic_spesilization = models.CharField(max_length=120, verbose_name=' التخصص ')
      clinic_price = models.CharField(max_length=120, verbose_name='سعر الكشف')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)

      def __str__(self):
          return '%s' % (self.doc_name)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 


      

#####transaction         




class medical_script1(models.Model):
      auth_doctor=(('محمد','محمد'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      date_of_op = models.DateField(auto_now_add=False, auto_now=False,null=True,verbose_name='التاريخ  ')    
      medic1_name = models.CharField(max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True,default=Decimal('0.000'),  max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True,default=Decimal('0.000'),  max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True,default=Decimal('0.000'),  max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True,default=Decimal('0.000'),  max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True,default=Decimal('0.000'),  max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      total_medic_cost= models.DecimalField(blank=True, null=True,default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='إجمالى التكاليف   ')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      updated = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      def _get_total_cost(self):
          return (self.medic1_cost1+self.medic1_cost2+self.medic1_cost3)

      total_cost = property(_get_total_cost)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)    


class medical_script2(models.Model):
      auth_doctor=(('mohamed','mohamed'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      date_of_op = models.DateField(auto_now_add=False, auto_now=False,null=True,verbose_name='التاريخ  ')    
      medic1_name = models.CharField(max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      total_medic_cost= models.DecimalField(blank=True, null=True,default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='إجمالى التكاليف   ')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      updated = models.DateField(auto_now_add=True, auto_now=False,null=True)
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)
class medical_script3(models.Model):
      auth_doctor=(('mohamed','mohamed'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      date_of_op = models.DateField(auto_now_add=False, auto_now=False,null=True,verbose_name='التاريخ  ')    
      medic1_name = models.CharField(max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      total_medic_cost= models.DecimalField(blank=True, null=True,default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='إجمالى التكاليف   ')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)          

class monthly_medical_script1(models.Model):
      auth_doctor=(('mohamed','mohamed'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      medic1_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      medic8_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 8')
      medic9_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='9 علاج ')
      medic10_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='10 علاج ')
      medic11_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='11  علاج')  
      medic12_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 12  ')
      medic13_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='13 علاج ')
      medic14_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 14  ')     
      medic15_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 15')
      medic16_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='16 علاج ')
      medic17_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='17 علاج ')
      medic18_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='18  علاج')  
      medic19_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 19  ')
      medic20_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='20 علاج ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      medic8_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 8')
      medic9_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 9')
      medic10_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 10')
      medic11_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 11')
      medic12_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 12')
      medic13_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 13')
      medic14_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 14')
      medic15_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 15')
      medic16_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 16')
      medic17_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 17')
      medic18_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 18')
      medic19_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 19')
      medic20_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')
      total_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      Added   = models.BooleanField(default=False)
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      master = models.BooleanField(default=False)
      # def _get_total_cost(self):
      #     return (self.medic1_cost1+self.medic1_cost2+self.medic1_cost3)

      # total_cost = property(_get_total_cost)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)


class monthly_medical_script2(models.Model):
      auth_doctor=(('mohamed','mohamed'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      medic1_name = models.CharField(max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      medic8_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 8')
      medic9_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='9 علاج ')
      medic10_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='10 علاج ')
      medic11_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='11  علاج')  
      medic12_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 12  ')
      medic13_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='13 علاج ')
      medic14_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 14  ')     
      medic15_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 15')
      medic16_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='16 علاج ')
      medic17_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='17 علاج ')
      medic18_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='18  علاج')  
      medic19_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 19  ')
      medic20_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='20 علاج ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      medic8_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 8')
      medic9_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 9')
      medic10_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 10')
      medic11_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 11')
      medic12_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 12')
      medic13_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 13')
      medic14_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 14')
      medic15_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 15')
      medic16_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 16')
      medic17_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 17')
      medic18_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 18')
      medic19_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 19')
      medic20_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')
      total_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      master = models.BooleanField(default=False)
      Added   = models.BooleanField(default=False)
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)     

class monthly_medical_script3(models.Model):
      auth_doctor=(('mohamed','mohamed'),('',''),('',''),('',''),('',''))
 
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor,verbose_name='طبيب العيادة ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      medic1_name = models.CharField(max_length=120, verbose_name='علاج 1')
      medic2_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='2 علاج ')
      medic3_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='3 علاج ')
      medic4_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='4  علاج')  
      medic5_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 5  ')
      medic6_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='6 علاج ')
      medic7_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 7  ')
      medic8_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 8')
      medic9_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='9 علاج ')
      medic10_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='10 علاج ')
      medic11_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='11  علاج')  
      medic12_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 12  ')
      medic13_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='13 علاج ')
      medic14_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 14  ')     
      medic15_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 15')
      medic16_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='16 علاج ')
      medic17_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='17 علاج ')
      medic18_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='18  علاج')  
      medic19_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='علاج 19  ')
      medic20_name = models.CharField(blank=True, null=True,max_length=120, verbose_name='20 علاج ')
      cost_flag    = models.BooleanField(default=False)
      medic1_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 1')
      medic2_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 2')
      medic3_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 3')
      medic4_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 4')
      medic5_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 5')
      medic6_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 6')
      medic7_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 7')
      medic8_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 8')
      medic9_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 9')
      medic10_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 10')
      medic11_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 11')
      medic12_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 12')
      medic13_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 13')
      medic14_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 14')
      medic15_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 15')
      medic16_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 16')
      medic17_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 17')
      medic18_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 18')
      medic19_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 19')
      medic20_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')      
      total_cost  = models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة علاج رقم 20')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      master = models.BooleanField(default=False)
      Added   = models.BooleanField(default=False)
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)     




class mdeical_transform1(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      auth_doctor=(('محمد','محمد'),('',''),('',''),('',''),('',''))
      to=(('عيادة','عيادة'),('معمل','معمل'),('مستشفى','مستشفى'))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب العيادة ')
      to_hospital = models.ForeignKey(hospital,max_length=120,blank=True, null=True, verbose_name=' اختر المستشفى')  
      to_clinic = models.ForeignKey(doctor_clinic,max_length=120,blank=True, null=True,verbose_name=' اختر العيادة خارجية')  
      to_lab = models.ForeignKey(laboratory,max_length=120,blank=True, null=True,verbose_name='اختر المعمل   ') 
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name='العيادة التابعة ')
      cost_flag    = models.BooleanField(default=False)
      transform_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة التحويل الطبى')
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      trans_to =models.CharField(blank=True, null=True,max_length=120,choices=to, verbose_name='التحويل الـى')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)

      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 


class mdeical_transform2(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      to=(('عيادة','عيادة'),('معمل','معمل'),('مستشفى','مستشفى'))
      auth_doctor=(('محمد','محمد'),('',''),('',''),('',''),('',''))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب العيادة ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية ')
      cost_flag    = models.BooleanField(default=False)
      transform_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة التحويل الطبى')
      trans_to =models.CharField(blank=True, null=True,max_length=120,choices=to, verbose_name='التحويل الـى')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)

      to_hospital = models.ForeignKey(hospital,max_length=120, verbose_name=' اختر المستشفى')  
      to_clinic = models.ForeignKey(doctor_clinic,max_length=120,choices=clinic, verbose_name=' اختر العيادة خارجية')  
      to_lab = models.ForeignKey(laboratory,max_length=120,choices=clinic, verbose_name='اختر المعمل او مركز الاشعة  ') 
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name=' ')  
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 

class mdeical_transform3(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      to=(('عيادة','عيادة'),('معمل','معمل'),('مستشفى','مستشفى'))
      
      auth_doctor=(('',''),('',''),('',''),('',''),('',''))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب العيادة ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      cost_flag    = models.BooleanField(default=False)
      to_hospital = models.ForeignKey(hospital,max_length=120, verbose_name=' اختر المستشفى')  
      to_clinic = models.ForeignKey(doctor_clinic,max_length=120,choices=clinic, verbose_name=' اختر العيادة خارجية')  
      to_lab = models.ForeignKey(laboratory,max_length=120,choices=clinic, verbose_name='اختر المعمل او مركز الاشعة  ') 
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية ')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name=' ')  
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      transform_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة التحويل الطبى')
      trans_to =models.CharField(blank=True, null=True,max_length=120,choices=to, verbose_name='التحويل الـى')
      paper_code = models.CharField(max_length=120,default=uuid.uuid4)
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id) 

class searching(models.Model):
          mnths=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))

          employee_name = models.CharField(blank=True, max_length=120,verbose_name='الپحث پاسم الموظف')
          month = models.CharField(blank=True, null=True,max_length=120,choices=mnths, verbose_name=' اختر  الشهر')  


          def __str__(self):
                  return '%s  ' % ( self.employee_name)
class external_clinic_cure1(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      
      auth_doctor=(('محمد','محمد'),('',''),('',''),('',''),('',''))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب الشركة  ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      cost_flag    = models.BooleanField(default=False)
      to_clinic = models.CharField(max_length=120,verbose_name=' اسم العيادة الخارجية')  
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية المقدمة')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name=' ')  
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      check_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة الكشف الطبى')
      midicine_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة  العلاج')
      
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)

class external_clinic_cure2(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      
      auth_doctor=(('',''),('',''),('',''),('',''),('',''))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب الشركة  ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      cost_flag    = models.BooleanField(default=False)
      to_clinic = models.CharField(max_length=120,verbose_name=' اسم العيادة الخارجية')  
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية المقدمة')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name=' ')  
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      check_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة الكشف الطبى')
      midicine_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة  العلاج')
      
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)

class external_clinic_cure3(models.Model):
      clinic=(('جاردن سيتى','جاردن سيتى'),('الفوالة','الفوالة'),('المهندسيين','المهندسيين'))
      
      auth_doctor=(('',''),('',''),('',''),('',''),('',''))
      patient_name = models.CharField(max_length=120, verbose_name='اسم المريض ')
      medical_number = models.CharField(max_length=120, verbose_name='الرقم الطبى ')
      auth_doc = models.CharField(max_length=120,choices=auth_doctor, verbose_name='طبيب الشركة  ')
      position = models.CharField(blank=True, null=True,max_length=120, verbose_name='الدرجة الوظيفية')
      cost_flag    = models.BooleanField(default=False)
      to_clinic = models.CharField(max_length=120,verbose_name=' اسم العيادة الخارجية')  
      rcvd_service =models.CharField(max_length=120,blank=True, null=True, verbose_name='نوع الرعاية الطبية المقدمة')
      followed_clinic = models.CharField(max_length=120,choices=clinic, verbose_name=' ')  
      timestamp = models.DateField(auto_now_add=True, auto_now=False,null=True)
      ip = models.CharField(blank=True, null=True, max_length=120)
      publisher = models.ForeignKey(User,null=True)
      updater = models.CharField(blank=True, null=True,max_length=120, verbose_name='مستخدم المالى')
      check_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة الكشف الطبى')
      midicine_cost =models.DecimalField(blank=True, null=True, default=Decimal('0.000'), max_digits=19, decimal_places=3, verbose_name='تكلفة  العلاج')
      
      
      def get_absolute_url(self):
          return "/app1/%s/" % (self.id)














