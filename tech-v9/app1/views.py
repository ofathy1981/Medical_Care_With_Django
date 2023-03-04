from django.db.models import *
from django.db.models import  Expression
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,request
from django.shortcuts import render
from .form import  add_working_pationt,add_retired_pationt,add_midicine,add_hospital,add_laboratory,add_doctor_clinic,add_medical_script1,add_medical_script2,add_mdeical_transform1,add_mdeical_transform2,add_monthly_medical_script1,add_monthly_medical_script2,signup_hw,signup_nw,add_law_note,update_law_note,signup_printer,add_lab,add_junk,req_analytics,search1,search2,search3,search4,search8,search6,signup_passrecovery,signup_spareparts,signup_cartridge,add_pc,add_scanner,add_printer,add_copier,add_server,add_switch,add_accesspoint,add_stick,add_router,add_repeater,add_rack,add_device,add_blueprint,trans_junk,searchassetmain,searchassetcomputers,searchassetlabs,searchassetprinters,searchassetscanners,searchassetcopiers,selectobj,record_mission,searchlaw,add_law_cases,add_case_sittings,add_casedep,add_case_depart_type,add_case_classification,add_case_category,add_case_court_name,add_case_lawyer,add_case_current_status,add_litigationdeg,add_opponent,add_opponent_rep,add_gainwtpercent,add_comprep,add_monthly_medical_script3,add_mdeical_transform3,add_medical_script1_cost,searching_frm,add_medical_script3,add_medical_transform1_cost,add_monthly_medic_cost1,add_external_clinic_cure1,add_cost_external_clinic_cure1
from django.template import *
from django.urls import reverse
from app1.models import working_pationt,retired_pationt,midicine,hospital,laboratory,doctor_clinic,monthly_medical_script1,monthly_medical_script2,medical_script1,medical_script2,mdeical_transform1,mdeical_transform2,LAW,hw_malfunction,users,junk_parts,asset_lab, nw_malfunction, print_malfunction,analytics,search,cartridges,spareparts,passrecovery,asset_pc,asset_copier,asset_scanner,asset_printer,asset_server,asset_router,asset_rack,asset_accesspoint,asset_switch,asset_repeater,asset_stick,asset_device,asset_blueprint,searchassets,missions,search_case,law_cases,case_sittings,casedep,case_depart_type,case_classification,case_category,case_court_name,case_lawyer,case_current_status,litigationdeg,oponent,oponentrep,gainwtpercent,comprep,monthly_medical_script3,mdeical_transform3,medical_script3,external_clinic_cure1,external_clinic_cure2,external_clinic_cure3
# working_pationt,retired_pationt,midicine,hospital,laboratory,doctor_clinic,monthly_medical_script1,monthly_medical_script2,medical_script1,medical_script2,mdeical_transform1,mdeical_transform2
from datetime import datetime, timedelta
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
import uuid
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from itertools import chain
from django import template
from django.contrib.auth.models import Group
from django.utils.timezone import now
from datetime import timedelta as tdelta
from django.utils import timezone
from django.core import serializers
import time
from decimal import Decimal
from django.db.models.functions import ExtractMonth




###########################################################################################

register = template.Library()
#loggedadmin = request.user
@register.filter(name='has_group')

def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False



#############################################################################################

def index(request):
    return HttpResponse("<center><h1>here you are Osama</h1></center>")
# def home(request):
#      form1 = signup_hw((request.POST or None))
#      title1= ""
#      if form1.is_valid():
#         instance1 = form1.save(commit=False)
#         instance1.save()
#      form2 = signup_nw((request.POST or None))
#      title2 = ""
#      if form2.is_valid():
#         instance2 = form2.save(commit=False)
#         instance2.save()
#      form3 = signup_printer((request.POST or None))
#      title3 = ""
#
#      if form3.is_valid():
#         instance3 = form3.save(commit=False)
#         instance3.save()
#      context = {"form1_title": title1, "form1": form1,"form2_title": title2, "form2": form2,"form3_title": title3, "form3": form3,}
#      return render(request,"home.html",context)
# Create your views here.


@login_required
def demandsuccess(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:    
        request.session['form-submitted'] = False
        return render(request,"demand_success.html", {})
@login_required
def pc(request):
   # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   # if x_forwarded_for:
    #    ip = x_forwarded_for.split(',')[0]
   # else:
  # #     ip = request.META.get('REMOTE_ADDR')
   # return ip

  #  ipaddr=ip

    form1 = signup_hw((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        hw_malfunction.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "pc-trouble.html", context)
@login_required
def netwk(request):

    form2 = signup_nw((request.POST or None))
    title2 = ""
    if form2.is_valid():
        request.session['form-submitted'] = True
        instance2 = form2.save(commit=False)
        instance2.ip = request.META['REMOTE_ADDR']
        instance2.publisher = request.user
        nw_malfunction.id=str(uuid.uuid4())
        instance2.save()
        return HttpResponseRedirect(reverse('success'))
    form3 = signup_printer((request.POST or None))
    title3 = ""

    context = {"form2_title": title2, "form2": form2,}
    return render(request, "network-trouble.html", context)
@login_required
def printer(request):
    form3 = signup_printer((request.POST or None))
    title3 = ""

    if form3.is_valid():
        request.session['form-submitted'] = True
        instance3 = form3.save(commit=False)
        instance3.ip = request.META['REMOTE_ADDR']
        instance3.publisher = request.user
        print_malfunction.id=str(uuid.uuid4())
        instance3.save()
        return HttpResponseRedirect(reverse('success'))
    context = {"form3_title": title3,"form3": form3,}
    return render(request, "printer-trouble.html", context)


@login_required
def cartridge(request):
    form3 = signup_cartridge(request.POST or None,request.FILES or None)
    title3 = ""

    if form3.is_valid():
        request.session['form-submitted'] = True
        instance3 = form3.save(commit=False)
        instance3.ip = request.META['REMOTE_ADDR']
        instance3.publisher = request.user
        instance3.user = request.user
        cartridges.id=str(uuid.uuid4())
        instance3.save()
        return HttpResponseRedirect(reverse('demandsuccess'))
    context = {"form3_title": title3,"form3": form3,}
    return render(request, "demand-cartridge.html", context)

@login_required
def passrec(request):
    form3 = signup_passrecovery(request.POST or None,request.FILES or None)
    title3 = ""

    if form3.is_valid():
        request.session['form-submitted'] = True
        instance3 = form3.save(commit=False)
        instance3.ip = request.META['REMOTE_ADDR']
        instance3.publisher = request.user
        instance3.user = request.user
        passrecovery.id=str(uuid.uuid4())
        instance3.save()
        return HttpResponseRedirect(reverse('success'))
    context = {"form3_title": title3,"form3": form3,}
    return render(request, "demand-passrecovery.html", context)



@login_required
def spare(request):
    form3 = signup_spareparts(request.POST or None,request.FILES or None)
    title3 = ""

    if form3.is_valid():
        request.session['form-submitted'] = True
        instance3 = form3.save(commit=False)
        instance3.ip = request.META['REMOTE_ADDR']
        instance3.publisher = request.user
        spareparts.id=str(uuid.uuid4())
        instance3.save()
        return HttpResponseRedirect(reverse('success'))
    context = {"form3_title": title3,"form3": form3,}
    return render(request, "demand-spareparts.html", context)

@login_required
def anlytics1(request):
    return render(request, "analytics.html", context)

@login_required
def detail(request,id=None):
        instance1 = get_object_or_404(hw_malfunction,id=id)

       # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
       # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    #    print ('req is',almalomat1)
        context = {"instance1":instance1,"desc": instance1.problem_desc,"date": instance1.problem_date,"name": instance1.user_fullname,"sect": instance1.user_sector,"type": instance1.pc_type}
        return render(request,"hw_details.html", context)



@login_required
def prob_detail1(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())


    pr_res = print_malfunction.objects.all()




    #*********************************************************
   # pr_res_list = print_malfunction.objects.all()
    if has_group(request.user,"fawallaa"):
       pr_res_list = print_malfunction.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
       pr_res_list = print_malfunction.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
       pr_res_list = prin_malfunction.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
       pr_res_list = print_malfunction.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
       pr_res_list = print_malfunction.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
       pr_res_list = print_malfunction.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
       pr_res_list = print_malfunction.objects.order_by('-id')
    paginator = Paginator(pr_res_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        pr_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pr_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pr_res = paginator.page(paginator.num_pages)
  
    return render(request, "problems_details1.html", {"pr_res":pr_res})

#---------------------------------------------------------------------------------------------------------------------------------
@login_required
def prob_detail2(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
   
    nw_res = nw_malfunction.objects.all()



  
    #nw_res_list = nw_malfunction.objects.all()
    if has_group(request.user,"fawallaa"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
      nw_res_list =nw_malfunction.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
      nw_res_list =nw_malfunction.objects.order_by('-id')
    paginator = Paginator(nw_res_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
            nw_res = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            nw_res = paginator.page(1)
    except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            nw_res = paginator.page(paginator.num_pages)
    #*********************************************************
   


    return render(request, "problems_details2.html", {"nw_res":nw_res })

#---------------------------------------------------------------------------------------------------------------------------------
@login_required
def prob_detail4(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
   

    cart_res = cartridges.objects.all()



  
    #cart_res_list = cartridges.objects.all()
    if has_group(request.user,"fawallaa"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
       cart_res_list = cartridges.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
       cart_res_list = cartridges.objects.order_by('-id')
    paginator = Paginator(cart_res_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        cart_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cart_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cart_res = paginator.page(paginator.num_pages)
    #******************************************************************
    



    return render(request, "problems_details4.html", { "cart_res":cart_res,})

#---------------------------------------------------------------------------------------------------------------------------------
@login_required
def prob_detail3(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    
    pass_res = passrecovery.objects.all()


    #pass_res_list = passrecovery.objects.all()
    if has_group(request.user,"fawallaa"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
        pass_res_list =  passrecovery.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
        pass_res_list =  passrecovery.objects.order_by('-id')
    paginator = Paginator(pass_res_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        pass_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pass_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pass_res = paginator.page(paginator.num_pages)
    #**********************************************************************
  
    return render(request, "problems_details3.html", {"pass_res":pass_res,})

#---------------------------------------------------------------------------------------------------------------------------------
@login_required
def prob_detail5(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    spare_res = spareparts.objects.all()

   # spare_res_list = spareparts.objects.all()
    if has_group(request.user,"fawallaa"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
         spare_res_list =   spareparts.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
         spare_res_list =   spareparts.objects.order_by('-id')
    paginator = Paginator(spare_res_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        spare_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        spare_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        spare_res = paginator.page(paginator.num_pages)



    return render(request, "problems_details5.html", {"spare_res":spare_res})

#---------------------------------------------------------------------------------------------------------------------------------



@login_required
def main(request):
    if request.user.groups.filter(name='it'):
       return HttpResponseRedirect(reverse('mission_main'))
    elif request.user.groups.filter(name='law'):
       return HttpResponseRedirect(reverse('law_affairs_main'))

    return render(request, "index.html", {})
@login_required
def rest(request):
    return render(request, "restricted.html", {})
@login_required
def prob_detail(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    #hw_res = hw_malfunction.objects.filter(timestamp=today).order_by("user_fullname")#.filter(timestamp=today)

    today = str(date.today())
    #hw_res = hw_malfunction.objects.filter(timestamp=today).order_by("user_fullname")#.filter(timestamp=today)
    hw_res = hw_malfunction.objects.order_by('-id')
   # today = datetime.date.today()

    #hw_res_list = hw_malfunction.objects.all().filter(publisher=request.user)
    
    if has_group(request.user,"fawallaa"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.64').order_by('id')
    elif has_group(request.user,"mohandseen"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.63').order_by('id')
    elif has_group(request.user,"kasr"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.65').order_by('id')
    elif has_group(request.user,"citybank"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.67').order_by('id')
    elif has_group(request.user,"tawfikia"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.105').order_by('id')
    elif has_group(request.user,"gardencity"):
       hw_res_list = hw_malfunction.objects.all().filter(ip__icontains='192.168.62').order_by('id')
    else:
       hw_res_list = hw_malfunction.objects.order_by('-id')
    paginator = Paginator(hw_res_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        hw_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hw_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hw_res = paginator.page(paginator.num_pages)


    return render(request, "problems_details.html", {"hw_res":hw_res})

@login_required
def  prdetail(request,id=None):
        instance= get_object_or_404(print_malfunction,id=id)
        context = {"instance":instance,"desc": instance.problem_desc,"date": instance.problem_date,"name": instance.user_fullname,"sect": instance.user_sector,"type": instance.printer_type}
        return render(request,"pr_details.html", context)

@login_required
def nwdetail(request,id=None):
        instance = get_object_or_404(nw_malfunction,id=id)
        context = {"instance":instance,"desc": instance.problem_desc,"date": instance.problem_date,"name": instance.user_fullname,"sect": instance.user_sector,"type": instance.netwk_type}
        return render(request,"nw_details.html", context)

@login_required
def cartridgedetail(request,id=None):
        instance = get_object_or_404(cartridges,id=id)
        context = {"instance":instance,"date": instance.demand_date,"name": instance.user_fullname,"sect": instance.user_sector,"type": instance.printer_type}
        return render(request,"cartridge_details.html", context)
@login_required
def passdetail(request,id=None):
        instance = get_object_or_404(passrecovery,id=id)
        context = {"instance":instance,"sect": instance.user_sector}
        return render(request,"passrec_details.html", context)

@login_required
def sparepartsdetail(request,id=None):
        instance = get_object_or_404(spareparts,id=id)
        context = {"instance":instance,"name": instance.user_fullname,"sect": instance.user_sector,}
        return render(request,"spareparts_details.html", context)






















def remove(request,id=None):  
    instance = get_object_or_404(hw_malfunction, id=id)
    instance.delete()
    return render(request,"removed.html",{})
 
@login_required
def user_detail(request,id=None):
    instance = get_object_or_404(hw_malfunction,id=id)
    #almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    context = {"instance":instance,"desc": instance.problem_desc,"date": instance.problem_date,"name":instance.user_fullname,"sect": instance.user_sector,"type":instance.pc_type,}
    print ('req is')
    return render(request,"user_details.html", context)


@login_required
def user_detail1(request,id=None):
    instance = get_object_or_404(print_malfunction,id=id)
    context = {"instance":instance,}
    print ('req is')
    return render(request,"user_details1.html", context)
#---------------------------------------------------------------
@login_required
def user_detail2(request,id=None):
    instance = get_object_or_404(nw_malfunction,id=id)
    context = {"instance":instance,}
    print ('req is')
    return render(request,"user_details2.html", context)
#---------------------------------------------------------------
@login_required
def user_detail3(request,id=None):
    instance = get_object_or_404(passrecovery,id=id)
    context = {"instance":instance,}
    print ('req is')
    return render(request,"user_details3.html", context)
#---------------------------------------------------------------
@login_required
def user_detail4(request,id=None):
    instance = get_object_or_404(cartridges,id=id)
    context = {"instance":instance,}
    print ('req is')
    return render(request,"user_details4.html", context)
#---------------------------------------------------------------
@login_required
def user_detail5(request,id=None):
    instance = get_object_or_404(spareparts,id=id)
    context = {"instance":instance,}
    print ('req is')
    return render(request,"user_details5.html", context)
#---------------------------------------------------------------

def solved(request,id=None):
    instance = get_object_or_404(hw_malfunction,id=id)  
    cuser = str(request.user)
    instance.status = False
    instance.closed_by = cuser
    instance.close_date =  datetime.now()
    instance.save()
    return render(request,"solved.html",{})
#---------------------------------------------------------------

def solved1(request,id=None):
    instance = get_object_or_404(print_malfunction,id=id)
    instance.status = False
    instance.closed_by = str(request.user)
    instance.close_date = datetime.now()
    instance.save()
    return render(request,"solved.html",{})
#---------------------------------------------------------------

def solved2(request,id=None):
    instance = get_object_or_404(nw_malfunction,id=id)
    instance.status = False
    instance.closed_by =str(request.user)
    instance.close_date = datetime.now()
    instance.save()
    return render(request,"solved.html",{})
#---------------------------------------------------------------

def solved3(request,id=None):
    instance = get_object_or_404(passrecovery,id=id)
    instance.status = False
    instance.closed_by =str(request.user)
    instance.close_date = datetime.now()
    instance.save()
    return render(request,"solved.html",{})
#---------------------------------------------------------------

def solved4(request,id=None):
    instance = get_object_or_404(cartridges,id=id)
    instance.status = False
    instance.closed_by = str(request.user)
    instance.close_date = datetime.now()
    instance.save()
    return render(request,"solved.html",{})
#---------------------------------------------------------------

def solved5(request,id=None):
    instance = get_object_or_404(spareparts,id=id)
    instance.status = False
    instance.closed_by = str(request.user)
    instance.close_date = datetime.now()
    instance.save()
    return render(request,"solved.html",{})

def assets(request,id=None):
    return render(request,"assets.html",{})
@login_required
def search(request):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    return render(request,"searchmain.html",{})
#-------------------------------------------------------------
def searchp(request):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    form1 = search1((request.POST or None))
    form2 = search2(request.POST or None)
    form3 = search3(request.POST or None)

   
 


    if form1.is_valid() and form2.is_valid() and form3.is_valid():
         sectorname = form1.cleaned_data['select_sector'] 
         problem = form2.cleaned_data['select_problem']        
         username = form3.cleaned_data['select_user']
         if  sectorname ==''  and problem == '' and username == '':
               title="there is no search criteria entered"
               res = ""
               context={"f1":form1,"f2":form2,"f3":form3,"title":title}
         
         elif  sectorname and problem == 'HardWare' and username == '':
               res = hw_malfunction.objects.filter(user_sector__icontains = sectorname)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)

         elif  sectorname and problem == 'Network' and username == '':
               res = nw_malfunction.objects.filter(user_sector__icontains = sectorname)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)

         elif  sectorname and problem == 'Printers' and username == '':
               res = print_malfunction.objects.filter(user_sector__icontains = sectorname)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)

         elif  sectorname   and problem == '' and username == '':
               hw_qs = hw_malfunction.objects.filter(user_sector__icontains = sectorname)
               nw_qs = nw_malfunction.objects.filter(user_sector__icontains = sectorname)
               p_qs = print_malfunction.objects.filter(user_sector__icontains = sectorname)
               res = list(chain(hw_qs, nw_qs,p_qs))
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)
          
         elif  sectorname and username and problem == '':
               hw_qs = hw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               nw_qs = nw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               p_qs = print_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               res = list(chain(hw_qs, nw_qs,p_qs))
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)
         elif  sectorname and username and problem == 'HardWare':
               res = hw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)
         elif  sectorname and username and problem == 'Network':
               res= nw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)
         elif  sectorname and username and problem == 'Printers':
               res = print_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               cont1={"q":res,"f1":form1,"f2":form2,"f3":form3}
               return render(request,"searchc.html",cont1)
         elif  sectorname == ''and username == '' and problem == 'HardWare':
               res = hw_malfunction.objects.all()
               cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
               return render(request, "searchc.html", cont1)

         elif  sectorname == '' and username == '' and problem == 'Network':
               res = nw_malfunction.objects.all()
               cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
               return render(request, "searchc.html", cont1)
         elif  sectorname == '' and username == '' and problem == 'Print':
               res = print_malfunction.objects.all()
               cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
               return render(request, "searchc.html", cont1)
         elif  sectorname == '' and  problem == ''and username :
               hw_qs = hw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               nw_qs = nw_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               p_qs = print_malfunction.objects.filter(user_sector__icontains = sectorname,user_fullname__icontains =username)
               res = list(chain(hw_qs, nw_qs, p_qs))
               cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
               return render(request, "searchc.html", cont1)

    context={"f1":form1,"f2":form2,"f3":form3,}
    return render(request,"searchc.html",context)
#-------------------------------------------------------------
def searchd(request):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    form4 = search4((request.POST or None))
    form8 = search8(request.POST or None)
    form6 = search6(request.POST or None)

   
 


    if form4.is_valid() and form8.is_valid() and form6.is_valid():
         sectorname = form4.cleaned_data['select_sector'] 
         fromdate = form8.cleaned_data['demand_date_from']   
         todate = form8.cleaned_data['demand_date_to']             
         demandtype = form6.cleaned_data['select_Demand']
         if  sectorname ==''  and fromdate == '' and todate == '' and demandtype =='':
               title="there is no search criteria entered"
               res = ""
               context={"f4":form4,"f8":form8,"f6":form6,"title":title}
               return render(request,"searchdemands.html",context)         
         elif  sectorname and fromdate == '' and todate == '' and demandtype =='':
               res1 = cartridges.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               res2 = passrecovery.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               res3 = spareparts.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               res = list(chain(res1, res2,res3))

               cont1={"q":res,"f4":form4,"f8":form8,"f6":form6}
               return render(request,"searchdemands.html",cont1)

         elif  sectorname and fromdate  and todate  and demandtype =='Cartridge' :
               res = cartridges.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               cont1={"q":res,"f4":form4,"f8":form8,"f6":form6}
               return render(request,"searchdemands.html",cont1)

         elif  sectorname and fromdate  and todate  and demandtype =='Passrecovery' :
               res = passrecovery.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               cont1={"q":res,"f4":form4,"f8":form8,"f6":form6}
               return render(request,"searchdemands.html",cont1)

         elif  sectorname and fromdate  and todate  and demandtype =='Spareparts' :
               res = Spareparts.objects.filter(user_sector__icontains = sectorname,demand_date__range=(fromdate,todate))
               cont1={"q":res,"f4":form4,"f8":form8,"f6":form6}
               return render(request,"searchdemands.html",cont1)

    context={"f4":form4,"f8":form8,"f6":form6,}
    return render(request,"searchdemands.html",context)
#-------------------------------------------------------------

#def get_signups(request):


#----------
# def get_signups(request):
#     if request.is_ajax():
#         message = "This is ajax"
#     else:
#         message = "Not ajax"
#
#     context={"test":message}
#     return render(request,"search.html",context)
#
#    # return HttpResponse(data, mimetype)
#
# #-------------------------------------------
# def clicker(request):
#     form1 = signupform()
#     instance = form1.save(commit=True)
#     instance.fullname = "akrate"
#     instance.email = "akrate@ff.gov"
#     instance.title = "akrate"
#     instance.save(commit=True)
#     return true
@login_required
def user_prob_detail(request,id=None):
    
    #hw_res = hw_malfunction.objects.filter(timestamp=today).order_by("user_fullname")#.filter(timestamp=today)
    cuser = request.user
    today = str(date.today())
    #hw_res = hw_malfunction.objects.filter(timestamp=today).order_by("user_fullname")#.filter(timestamp=today)
    nw_res = nw_malfunction.objects.all()
    #pr_res = print_malfunction.objects.all()
    cart_res = cartridges.objects.all()
    pass_res = passrecovery.objects.all()
    spare_res = spareparts.objects.all()

    # today = datetime.date.today()

    # hw_res_list = hw_malfunction.objects.all().filter(publisher=request.user).filter(publisher=request.user)
    hw_res_list = hw_malfunction.objects.all().filter(publisher=request.user)
    paginator = Paginator(hw_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        hw_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hw_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hw_res = paginator.page(paginator.num_pages)
        nw_res_list = nw_malfunction.objects.all().filter(publisher=request.user)
        paginator = Paginator(hw_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
        try:
            nw_res = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            nw_res = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            nw_res = paginator.page(paginator.num_pages)
    # *********************************************************
    pr_res_list = print_malfunction.objects.all().filter(publisher=request.user).filter(publisher=cuser)
    paginator = Paginator(pr_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        pr_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pr_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pr_res = paginator.page(paginator.num_pages)
        paginator = Paginator(pr_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')

    # *****************************************************************
    cart_res_list = cartridges.objects.all().filter(publisher=request.user)
    paginator = Paginator(cart_res_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        cart_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cart_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cart_res = paginator.page(paginator.num_pages)
    # ******************************************************************
    pass_res_list = passrecovery.objects.all().filter(publisher=request.user)
    paginator = Paginator(pass_res_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        pass_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pass_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pass_res = paginator.page(paginator.num_pages)
    # **********************************************************************
    spare_res_list = spareparts.objects.all().filter(publisher=request.user)
    paginator = Paginator(spare_res_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        spare_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        spare_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        spare_res = paginator.page(paginator.num_pages)
    return render(request, "user_problems_details.html",
                  {"hw_res": hw_res, "nw_res": nw_res, "pr_res": pr_res, "cart_res": cart_res, "pass_res": pass_res,
                   "spare_res": spare_res})
#---------------------------------------------------------------
@login_required
def user_prob_detail2(request,id=None):
    cuser = request.user
    print(cuser)
    print(cuser)
    today = str(date.today())
    nw_res_list = nw_malfunction.objects.all().filter(publisher=cuser).order_by('-id')
    

    paginator = Paginator(nw_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        nw_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        nw_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pr_res = paginator.page(paginator.num_pages)
        paginator = Paginator(nw_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
    return render(request, "user_problems_details2.html",{ "nw_res": nw_res,})


# ---------------------------------------------------------------
@login_required
def user_prob_detail1(request, id=None):
    cuser = request.user
    print(cuser)
    print(cuser)
    today = str(date.today())
    pr_res_list = print_malfunction.objects.all().filter(publisher=cuser).order_by('-id')

    paginator = Paginator(pr_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        pr_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pr_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pr_res = paginator.page(paginator.num_pages)
        paginator = Paginator(pr_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
    return render(request, "user_problems_details1.html", {"pr_res": pr_res, })


# ---------------------------------------------------------------
@login_required
def user_prob_detail4(request, id=None):
    cuser = request.user
    print(cuser)
    print(cuser)
    today = str(date.today())
    cart_res_list = cartridges.objects.all().filter(publisher=cuser).order_by('-id')

    paginator = Paginator(cart_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        cart_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cart_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cart_res = paginator.page(paginator.num_pages)
        paginator = Paginator(cart_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
    return render(request, "user_problems_details4.html", {"cart_res": cart_res, })


# ---------------------------------------------------------------
@login_required
def user_prob_detail3(request, id=None):
    cuser = request.user
    print(cuser)
    print(cuser)
    today = str(date.today())
    pass_res_list = passrecovery.objects.all().filter(publisher=cuser).order_by('-id')

    paginator = Paginator(pass_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        pass_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pass_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pass_res = paginator.page(paginator.num_pages)
        paginator = Paginator(pass_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
    return render(request, "user_problems_details3.html", {"pass_res": pass_res, })


# ---------------------------------------------------------------
@login_required
def user_prob_detail5(request, id=None):
    cuser = request.user
    print(cuser)
    print(cuser)
    today = str(date.today())
    spare_res_list = spareparts.objects.all().filter(publisher=cuser).order_by('-id')

    paginator = Paginator(spare_res_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        spare_res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        spare_res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        spare_res = paginator.page(paginator.num_pages)
        paginator = Paginator(spare_res_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
    return render(request, "user_problems_details5.html", {"spare_res": spare_res, })


# ---------------------------------------------------------------



#-----------------------------------------------------
def analytics(request):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    form = req_analytics(request.POST or None)
    term='تصالات'
    if form.is_valid():
       sector = form.cleaned_data['select_sector']
       year = form.cleaned_data['select_year']
    compmgmt = hw_malfunction.objects.filter(user_sector__sector_name__icontains=term).filter(timestamp__year=1).filter(timestamp__month=1).count()



   #data = form.clean(req_analytics.cleaned_data['select_sector'])
    context = {"form":form}

    #form = req_analytics((request.POST or None))
    #search_query = request.GET.get("search_box")
   # if not data :
    #   data ='$'

    #print ('req is',almalomat1)
    return render(request,"analytics.html", context)

#-------------------------------------------------------------------------------------
def analytics1(request,select_sector = None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    form = req_analytics(request.POST or None)
    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1,timestamp__year=2018).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # commun1 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=1).count()
    # commun2 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=2).count()
    # commun3 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=3).count()
    # commun4 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=4).count()
    # commun5 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=5).count()
    # commun6 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=6).count()
    # commun7 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=7).count()
    # commun8 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=8).count()
    # commun9 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=9).count()
    # commun10 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=10).count()
    # commun11 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=11).count()
    # commun12 = hw_malfunction.objects.filter(user_sector__icontains='الإتصالات', timestamp__month=12).count()

    # htlneeds1 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=1).count()
    # htlneeds2 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=2).count()
    # htlneeds3 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=3).count()
    # htlneeds4 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=4).count()
    # htlneeds5 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=5).count()
    # htlneeds6 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=6).count()
    # htlneeds7 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=7).count()
    # htlneeds8 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=8).count()
    # htlneeds9 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=9).count()
    # htlneeds10 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=10).count()
    # htlneeds11 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=11).count()
    # htlneeds12 = hw_malfunction.objects.filter(user_sector__icontains='الإحتياجات', timestamp__month=12).count()

    # invhist1 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=1).count()
    # invhist2 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=2).count()
    # invhist3 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=3).count()
    # invhist4 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=4).count()
    # invhist5 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=5).count()
    # invhist6 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=6).count()
    # invhist7 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=7).count()
    # invhist8 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=8).count()
    # invhist9 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=9).count()
    # invhist10 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=10).count()
    # invhist11 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=11).count()
    # invhist12 = hw_malfunction.objects.filter(user_sector__icontains='التاريخية', timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

    # almalomat1 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=1).count()
    # almalomat2 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=2).count()
    # almalomat3 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=3).count()
    # almalomat4 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=4).count()
    # almalomat5 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=5).count()
    # almalomat6 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=6).count()
    # almalomat7 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=7).count()
    # almalomat8 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=8).count()
    # almalomat9 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=9).count()
    # almalomat10 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=10).count()
    # almalomat11 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=11).count()
    # almalomat12 = hw_malfunction.objects.filter(user_sector__icontains='المعلومات',timestamp__month=12).count()

   #data = form.clean(req_analytics.cleaned_data['select_sector'])
    context = {"form":form}

    #form = req_analytics((request.POST or None))
    #search_query = request.GET.get("search_box")
   # if not data :
    #   data ='$'

    # print ('req is',almalomat1)
    return render(request,"analytics1.html", context)

# asset management of pc's************************33333333333333333********************************************************************

@login_required
def asset_add_success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:    
        request.session['form-submitted'] = False
        return render(request,"asset_add_success.html", {})

#==========================================================
@login_required
def law_add_success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:
        request.session['form-submitted'] = False
        return render(request,"law_add_success.html", {})
#==========================================================
@login_required
def asset_remove_success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:    
        request.session['form-submitted'] = False
        return render(request,"asset_remove_success.html", {})

#----------------------------------------------====
@login_required
def asset_update_success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:    
        request.session['form-submitted'] = False
        return render(request,"asset_update_success.html", {})
#*******************************************



@login_required
def add_asset_pc(request):
    form1 = add_pc((request.POST or None))
    title1 = ""
    qs=users.objects.all()
    qslen=users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        asset_pc.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "asset-pc.html", context)

@login_required
def pc_update(request,id=None):
    pc_res = get_object_or_404(asset_pc,id=id)
    form1 = add_pc(request.POST or None,instance=pc_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
    context={"pc_res":pc_res,"form1":form1}
    return render(request,"asset-pc.html",context)
@login_required
def pc_remove1(request,id=None):
    instance = get_object_or_404(asset_pc, id=id)
    instance.delete()
    return render(request,"removed.html",{})

@login_required
def computers_detail(request):


        if request.user.id == 1:
           computers_list = asset_pc.objects.all().order_by('bransh')
        else:
           computers_list = asset_pc.objects.all().filter(publisher=request.user)
        context = {"computers_list":computers_list}
        return render(request,"computers_detail.html", context)
@login_required
def computer_detail(request,id=None):
    pc_res = get_object_or_404(asset_pc,id=id)
    return render(request, "computer-detail.html",{"pc_res": pc_res,})


@login_required
def computers_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    comps_lst = asset_pc.objects.all()
    if request.user.id == 1:
        comps_lst_list = asset_pc.objects.all().order_by('bransh')
    else:
        comps_lst_list = asset_pc.objects.all().filter(publisher=request.user)
    paginator = Paginator(comps_lst_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        comps_lst = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comps_lst = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comps_lst = paginator.page(paginator.num_pages)


     #***************************************************

    return render(request, "computer-list.html", {"comps_lst":comps_lst })


@login_required
def computers_list_ordered(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    comps_lst = asset_pc.objects.all()
    if request.user.id == 1:
        comps_lst_list = asset_pc.objects.all().order_by('processor_type')
    else:
        comps_lst_list = asset_pc.objects.all().filter(publisher=request.user)
    paginator = Paginator(comps_lst_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        comps_lst = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comps_lst = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comps_lst = paginator.page(paginator.num_pages)


     #***************************************************

    return render(request, "computer-list.html", {"comps_lst":comps_lst })


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


@login_required
def add_asset_lab(request):
    form1 = add_lab((request.POST or None))
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        asset_lab.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "asset-lab.html", context)

def getusercode(request):
    username = request.GET.get("username", None)
    data = serializers.serialize('json', users.objects.filter(user_name__icontains=username).only("user_code"), fields=('user_code',))
    return JsonResponse(data[45:67],safe=False)
@login_required
def lab_update(request,id=None):
    lab_res = get_object_or_404(asset_lab,id=id)
    form1 = add_lab(request.POST or None,instance=lab_res)
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
    context={"lab_res":lab_res,"form1":form1,"qs":qs,"qslen":qslen}
    return render(request,"asset-lab.html",context)
@login_required
def lab_remove1(request,id=None):
    instance = get_object_or_404(asset_lab, id=id)
    instance.delete()
    return render(request,"removed.html",{})

@login_required
def labs_detail(request):
        if request.user.id==1:
          labs_list = asset_lab.objects.all().order_by('bransh')
        else:
          labs_list = asset_lab.objects.all().filter(publisher=request.user)
        context = {"labs_list":labs_list}
        return render(request,"labs_detail.html", context)
@login_required
def lab_detail(request,id=None):
    lab_res = get_object_or_404(asset_lab,id=id)
    return render(request, "lab-detail.html",{"lab_res": lab_res,})


@login_required
def labs_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    labs_list = asset_lab.objects.all()
    if  request.user.id==1:
        labs_list_list = asset_lab.objects.all().order_by('bransh')
    else:
        labs_list_list = asset_lab.objects.all().filter(publisher=request.user)
    paginator = Paginator(labs_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        labs_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        labs_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        labs_list = paginator.page(paginator.num_pages)


     #***************************************************

    return render(request, "lab-list.html", {"labs_list":labs_list })














# asset management of printers*******************************************************************

@login_required
def add_asset_printer(request):
    form1 = add_printer((request.POST or None))
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        asset_printer.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "asset-printer.html", context)


@login_required
def printer_update(request,id=None):
    printer_res = get_object_or_404(asset_printer,id=id)
    form1 = add_printer(request.POST or None,instance=printer_res)
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":printer_res,"form1":form1,"qs":qs,"qslen":qslen}
    return render(request,"asset-printer.html",context)
@login_required
def printer_remove2(request,id=None):
    instance = get_object_or_404(asset_printer, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def printers_detail(request):
        if request.user.id==1:
           printers_list = asset_printer.objects.all().order_by('bransh')
        else:
           printers_list = asset_printer.objects.all().filter(publisher=request.user)
        context = {"printers_list":printers_list}
        return render(request,"printers_detail.html", context)
@login_required
def printer_detail(request,id=None):
    printer_res = get_object_or_404(asset_printer,id=id)
    return render(request, "printer-detail.html",{"printer_res": printer_res,})


@login_required
def printers_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    prints_list = asset_printer.objects.all()
    if request.user.id == 1:
        prints_list_list = asset_printer.objects.all().order_by('bransh')
    else:
        prints_list_list = asset_printer.objects.all().filter(publisher=request.user)
    paginator = Paginator(prints_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        prints_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        prints_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        prints_list = paginator.page(paginator.num_pages)




    return render(request, "printer-list.html", {"prints_list":prints_list })

# asset management of scanners*******************************************************************





@login_required
def add_asset_scanner(request):
    form1 = add_scanner((request.POST or None))
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        asset_scanner.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "asset-scanner.html", context)

@login_required
def scanner_update(request,id=None):
    scanner_res = get_object_or_404(asset_scanner,id=id)
    form1 = add_scanner(request.POST or None,instance=scanner_res)
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"scanner_res":scanner_res,"form1":form1,"qs":qs,"qslen":qslen}
    return render(request,"asset-scanner.html",context)

@login_required

def scanner_remove3(request,id=None):
    instance = get_object_or_404(asset_scanner, id=id)
    instance.delete()
    return render(request,"removed.html",{})




@login_required
def scanners_detail(request):
        if request.user.id==1:
           scanners_list = asset_scanner.objects.all().order_by('bransh')
        else:
           scanners_list = asset_scanner.objects.all().filter(publisher=request.user)
        context = {"scanners_list":scanners_list}
        return render(request,"scanners_detail.html", context)
@login_required
def scanner_detail(request,id=None):
    scanner_res = get_object_or_404(asset_scanner,id=id)
    return render(request, "scanner-detail.html",{"scanner_res": scanner_res,})


@login_required
def scanners_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    scanners_list = asset_scanner.objects.all()
    if request.user.id==1:
        scans_list_list = asset_scanner.objects.all().order_by('bransh')
    else:
        scans_list_list = asset_scanner.objects.all().filter(publisher=request.user)
    paginator = Paginator(scans_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        scans_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        scans_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        scans_list = paginator.page(paginator.num_pages)


     #***************************************************

    return render(request, "scanner-list.html", {"scans_list":scans_list })

# asset management of copiers*******************************************************************


@login_required
def add_asset_copier(request):
    form1 = add_copier((request.POST or None))
    title1 = ""
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        asset_copier.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-copier.html", context)


@login_required
def copier_update(request,id=None):
    copier_res = get_object_or_404(asset_copier,id=id)
    form1 = add_copier(request.POST or None,instance=copier_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"copier_res":copier_res,"form1":form1}
    return render(request,"asset-copier.html",context)
@login_required
def copier_remove4(request,id=None):
    instance = get_object_or_404(asset_copier, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def copiers_detail(request):
        if request.user.id == 1:
           copiers_list = asset_copier.objects.all().order_by('bransh')
        else:
           copiers_list = asset_copier.objects.all().filter(publisher=request.user)
        context = {"copiers_list":copiers_list}
        return render(request,"copiers_detail.html", context)
@login_required
def copier_detail(request,id=None):
    copier_res = get_object_or_404(asset_copier,id=id)
    return render(request, "copier-detail.html",{"copier_res": copier_res,})


@login_required
def copiers_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    copiers_list = asset_copier.objects.all()
    if request.user.id == 1:
       copiers_list_list = asset_copier.objects.all().order_by('bransh')
    else:
       copiers_list_list = asset_copier.objects.all().filter(publisher=request.user)
    paginator = Paginator(copiers_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        copiers_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        copiers_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        copiers_list = paginator.page(paginator.num_pages)


    return render(request, "copier-list.html", {"copiers_list":copiers_list })

# asset management of servers*******************************************************************

@login_required
def add_asset_server(request):
    form1 = add_server((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_server.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-server.html", context)


@login_required
def server_update(request,id=None):
    server_res = get_object_or_404(asset_server,id=id)
    form1 = add_server(request.POST or None,instance=server_res)
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":server_res,"form1":form1}
    return render(request,"asset-server.html",context)
@login_required
def server_remove1(request,id=None):
    instance = get_object_or_404(asset_server, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def servers_detail(request):
        if request.user.id == 1:
           servers_list = asset_server.objects.all().order_by('bransh')
        else :
           servers_list = asset_server.objects.all().filter(publisher=request.user)
        context = {"servers_list":servers_list}
        return render(request,"servers_detail.html", context)
@login_required
def server_detail(request,id=None):
    server_res = get_object_or_404(asset_server,id=id)
    return render(request, "server-detail.html",{"server_res": server_res,})


@login_required
def servers_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    servers_list = asset_server.objects.all()
    if request.user.id ==1 :
       servers_list_list = asset_server.objects.all().order_by('bransh')
    else:
        servers_list_list = asset_server.objects.all().filter(publisher=request.user)

    paginator = Paginator(servers_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        servers_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        servers_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        servers_list = paginator.page(paginator.num_pages)




    return render(request, "server-list.html", {"servers_list":servers_list })








# asset management of switches*******************************************************************

@login_required
def add_asset_switch(request):
    form1 = add_switch((request.POST or None))
    title1 = ""

    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_switch.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-switch.html", context)


@login_required
def switch_update(request,id=None):
    switch_res = get_object_or_404(asset_switch,id=id)
    form1 = add_switch(request.POST or None,instance=switch_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":switch_res,"form1":form1}
    return render(request,"asset-switch.html",context)
@login_required
def switch_remove1(request,id=None):
    instance = get_object_or_404(asset_switch, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def switchs_detail(request):
       if request.user.id ==1 :
          switchs_list = asset_switch.objects.all().order_by('bransh')
       else:
          switchs_list = asset_switch.objects.all().filter(publisher=request.user)

       context = {"switchs_list":switchs_list}
       return render(request,"switchs_detail.html", context)
@login_required
def switch_detail(request,id=None):
    switch_res = get_object_or_404(asset_switch,id=id)
    return render(request, "switch-detail.html",{"switch_res": switch_res,})


@login_required
def switchs_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    switchs_list = asset_switch.objects.all()
    if request.user.id == 1:
       switchs_list_list = asset_switch.objects.all().order_by('bransh')
    else:
       switchs_list_list = asset_switch.objects.all().filter(publisher=request.user)

    paginator = Paginator(switchs_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        switchs_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        switchs_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        switchs_list = paginator.page(paginator.num_pages)




    return render(request, "switch-list.html", {"switchs_list":switchs_list })




# asset management of accesspoint*******************************************************************

@login_required
def add_asset_accesspoint(request):
    form1 = add_accesspoint((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.created = datetime.now()
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.publisher = request.user
        asset_accesspoint.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-accesspoint.html", context)


@login_required
def accesspoint_update(request,id=None):
    accesspoint_res = get_object_or_404(asset_accesspoint,id=id)
    form1 = add_accesspoint(request.POST or None,instance=accesspoint_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"accesspoint_res":accesspoint_res,"form1":form1}
    return render(request,"asset-accesspoint.html",context)

def accesspoint_remove1(request,id=None):
    instance = get_object_or_404(asset_accesspoint, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def accesspoints_detail(request):
        if request.user.id ==1:
           accesspoints_list = asset_accesspoint.objects.all().order_by('bransh')
        else:
           accesspoints_list = asset_accesspoint.objects.all().filter(publisher=request.user)

        context = {"accesspoints_list":accesspoints_list}
        return render(request,"accesspoints_detail.html", context)
@login_required
def accesspoint_detail(request,id=None):
    accesspoint_res = get_object_or_404(asset_accesspoint,id=id)
    return render(request, "accesspoint-detail.html",{"accesspoint_res": accesspoint_res,})


@login_required
def accesspoints_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    accesspoints_list = asset_accesspoint.objects.all()
    if request.user.id==1:
       accesspoints_list_list = asset_accesspoint.objects.all().order_by('bransh')
    else:
       accesspoints_list_list = asset_accesspoint.objects.all().filter(publisher=request.user)

    paginator = Paginator(accesspoints_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        accesspoints_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        accesspoints_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        accesspoints_list = paginator.page(paginator.num_pages)




    return render(request, "accesspoint-list.html", {"accesspoints_list":accesspoints_list })








# asset management of stick*******************************************************************

@login_required
def add_asset_stick(request):
    form1 = add_stick((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    qs=users.objects.all()
    qslen=users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_stick.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "asset-stick.html", context)


@login_required
def stick_update(request,id=None):
    stick_res = get_object_or_404(asset_stick,id=id)
    form1 = add_stick(request.POST or None,instance=stick_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":stick_res,"form1":form1}
    return render(request,"asset-stick.html",context)
@login_required
def stick_remove1(request,id=None):
    instance = get_object_or_404(asset_stick, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def sticks_detail(request):
        if request.user.id==1:
           sticks_list = asset_stick.objects.all().order_by('bransh')
        else:
           sticks_list = asset_stick.objects.all().filter(publisher=request.user)

        context = {"sticks_list":sticks_list}
        return render(request,"sticks_detail.html", context)
@login_required
def stick_detail(request,id=None):
    stick_res = get_object_or_404(asset_stick,id=id)
    return render(request, "stick-detail.html",{"stick_res": stick_res,})


@login_required
def sticks_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    sticks_list = asset_stick.objects.all()
    if request.user.id==1:
       sticks_list_list = asset_stick.objects.all().order_by('bransh')
    else:
       sticks_list_list = asset_stick.objects.all().filter(publisher=request.user)

    paginator = Paginator(sticks_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        sticks_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sticks_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sticks_list = paginator.page(paginator.num_pages)




    return render(request, "stick-list.html", {"sticks_list":sticks_list })






# asset management of router*******************************************************************


@login_required
def add_asset_router(request):
    form1 = add_router((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_router.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-router.html", context)


@login_required
def router_update(request,id=None):
    router_res = get_object_or_404(asset_router,id=id)
    form1 = add_router(request.POST or None,instance=router_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":router_res,"form1":form1}
    return render(request,"asset-router.html",context)
@login_required
def router_remove1(request,id=None):
    instance = get_object_or_404(asset_router, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def routers_detail(request):
        if request.user.id==1:
           routers_list = asset_router.objects.all().order_by('bransh')
        else:
           routers_list = asset_router.objects.all().filter(publisher=request.user)

        context = {"routers_list":routers_list}
        return render(request,"routers_detail.html", context)
@login_required
def router_detail(request,id=None):
    router_res = get_object_or_404(asset_router,id=id)
    return render(request, "router-detail.html",{"router_res": router_res,})


@login_required
def routers_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    routers_list = asset_router.objects.all()
    if request.user.id ==1:
       routers_list_list = asset_router.objects.all().order_by('bransh')
    else:
       routers_list_list = asset_router.objects.all().filter(publisher=request.user)

    paginator = Paginator(routers_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        routers_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        routers_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        routers_list = paginator.page(paginator.num_pages)




    return render(request, "router-list.html", {"routers_list":routers_list })







# asset management of repeater*******************************************************************

@login_required
def add_asset_repeater(request):
    form1 = add_repeater((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_repeater.id=str(uuid.uuid4())

        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-repeater.html", context)


@login_required
def repeater_update(request,id=None):
    repeater_res = get_object_or_404(asset_repeater,id=id)
    form1 = add_repeater(request.POST or None,instance=repeater_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":repeater_res,"form1":form1}
    return render(request,"asset-repeater.html",context)
@login_required
def repeater_remove1(request,id=None):
    instance = get_object_or_404(asset_repeater, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def repeaters_detail(request):
        if request.user.id==1:
           repeaters_list = asset_repeater.objects.all().order_by('bransh')
        else:
           repeaters_list = asset_repeater.objects.all().filter(publisher=request.user)

        context = {"repeaters_list":repeaters_list}
        return render(request,"repeaters_detail.html", context)
@login_required
def repeater_detail(request,id=None):
    repeater_res = get_object_or_404(asset_repeater,id=id)
    return render(request, "repeater-detail.html",{"repeater_res": repeater_res,})


@login_required
def repeaters_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    repeaters_list = asset_repeater.objects.all()
    if request.user.id==1:
       repeaters_list_list = asset_repeater.objects.all().order_by('bransh')
    else:
       repeaters_list_list = asset_repeater.objects.all().filter(publisher=request.user)

    paginator = Paginator(repeaters_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        repeaters_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        repeaters_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        repeaters_list = paginator.page(paginator.num_pages)




    return render(request, "repeater-list.html", {"repeaters_list":repeaters_list })










# asset management of rack*******************************************************************


@login_required
def add_asset_rack(request):
    form1 = add_rack((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_rack.id=str(uuid.uuid4())

        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-rack.html", context)


@login_required
def rack_update(request,id=None):
    rack_res = get_object_or_404(asset_rack,id=id)
    form1 = add_rack(request.POST or None,instance=rack_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":rack_res,"form1":form1}
    return render(request,"asset-rack.html",context)
@login_required
def rack_remove1(request,id=None):
    instance = get_object_or_404(asset_rack, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def racks_detail(request):
        if request.user.id==1:
           racks_list = asset_rack.objects.all().order_by('bransh')
        else:
           racks_list = asset_rack.objects.all().filter(publisher=request.user)

        context = {"racks_list":racks_list}
        return render(request,"racks_detail.html", context)
@login_required
def rack_detail(request,id=None):
    rack_res = get_object_or_404(asset_rack,id=id)
    return render(request, "rack-detail.html",{"rack_res": rack_res,})


@login_required
def racks_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    racks_list = asset_rack.objects.all()
    if request.user.id==1:
       racks_list_list = asset_rack.objects.all().order_by('bransh')
    else:
       racks_list_list = asset_rack.objects.all().filter(publisher=request.user)

    paginator = Paginator(racks_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        racks_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        racks_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        racks_list = paginator.page(paginator.num_pages)




    return render(request, "rack-list.html", {"racks_list":racks_list })










# asset management of device*******************************************************************


@login_required
def add_asset_device(request):
    form1 = add_device((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_device.id=str(uuid.uuid4())

        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-device.html", context)


@login_required
def device_update(request,id=None):
    device_res = get_object_or_404(asset_device,id=id)
    form1 = add_device(request.POST or None,instance=device_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":device_res,"form1":form1}
    return render(request,"asset-device.html",context)
@login_required
def device_remove1(request,id=None):
    instance = get_object_or_404(asset_device,id=id)
    instance.delete()
    return render(request,"asset_remove_success.html",{})



@login_required
def devices_detail(request):
        if request.user.id==1:
           devices_list = asset_device.objects.all().order_by('bransh')
        else:
           devices_list = asset_device.objects.all().filter(publisher=request.user)

        context = {"devices_list":devices_list}
        return render(request,"devices_detail.html", context)
@login_required
def device_detail(request,id=None):
    device_res = get_object_or_404(asset_device,id=id)
    return render(request, "device-detail.html",{"device_res": device_res,})


@login_required
def devices_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    devices_list = asset_device.objects.all()
    if request.user.id==1:
       devices_list_list = asset_device.objects.all().order_by('bransh')
    else:
       devices_list_list = asset_device.objects.all().filter(publisher=request.user)

    paginator = Paginator(devices_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        devices_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        devices_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        devices_list = paginator.page(paginator.num_pages)




    return render(request, "device-list.html", {"devices_list":devices_list })












# asset management of blueprint*******************************************************************

@login_required
def add_asset_blueprint(request):
    form1 = add_blueprint(request.POST or None, request.FILES or None)
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.created = datetime.now()
        instance1.publisher = request.user
        asset_blueprint.id=str(uuid.uuid4())
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "asset-blueprint.html", context)


@login_required
def blueprint_update(request,id=None):
    blueprint_res = get_object_or_404(asset_blueprint,id=id)
    form1 = add_blueprint(request.POST or None,request.FILES or None,instance=blueprint_res)
    title1 = ""
    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.timestamp = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
    context={"printer_res":blueprint_res,"form1":form1}
    return render(request,"asset-blueprint.html",context)

def blueprint_remove1(request,id=None):
    instance = get_object_or_404(asset_blueprint, id=id)
    instance.delete()
    return render(request,"removed.html",{})



@login_required
def blueprints_detail(request):
        if request.user.id==1:
           blueprints_list = asset_blueprint.objects.all().order_by('bransh')
        else:
           blueprints_list = asset_blueprint.objects.all().filter(publisher=request.user)

        context = {"blueprints_list":blueprints_list}
        return render(request,"blueprints_detail.html", context)
@login_required
def blueprint_detail(request,id=None):
    blueprint_res = get_object_or_404(asset_blueprint,id=id)
    return render(request, "blueprint-detail.html",{"blueprint_res": blueprint_res,})


@login_required
def blueprints_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    blueprints_list = asset_blueprint.objects.all()
    if request.user.id==1:
       blueprints_list_list = asset_blueprint.objects.all().order_by('bransh')
    else:
       blueprints_list_list = asset_blueprint.objects.all().filter(pubisher=request.user)

    paginator = Paginator(blueprints_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        blueprints_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blueprints_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blueprints_list = paginator.page(paginator.num_pages)




    return render(request, "blueprint-list.html", {"blueprints_list":blueprints_list })




@login_required
def reports(request):
    if request.user.id == 1:
        #-----------------computers count-----------------------
        # pclow = asset_pc.objects.get(Q(processor_type__icontains='Pentium')| Q(processor_type__icontains='celeron')).count()
        gpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.62').count()
        gpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.62').count()
        gpclow  =gpclow1 + gpclow2
        mpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.63').count()
        mpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.63').count()
        mpclow  =mpclow1 + mpclow2
        fpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.64').count()
        fpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.64').count()
        fpclow  =fpclow1 + fpclow2
        cpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.67').count()
        cpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.67').count()
        cpclow  =cpclow1 + cpclow2
        kpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.65').count()
        kpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.65').count()
        kpclow  =kpclow1 + kpclow2
        tpclow1 = asset_pc.objects.filter(processor_type__icontains='Pentium',ip__icontains='192.168.105').count()
        tpclow2 = asset_pc.objects.filter(processor_type__icontains='celeron',ip__icontains='192.168.105').count()
        tpclow  =tpclow1 + tpclow2

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        gpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.62').count()
        gpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.62').count()
        gpcmid = gpcmid1 + gpcmid2
        mpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.63').count()
        mpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.63').count()
        mpcmid = mpcmid1 + mpcmid2
        fpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.64').count()
        fpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.64').count()
        fpcmid = fpcmid1 + fpcmid2
        cpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.67').count()
        cpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.67').count()
        cpcmid = cpcmid1 + cpcmid2
        kpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.65').count()
        kpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.65').count()
        kpcmid = kpcmid1 + kpcmid2
        tpcmid1 = asset_pc.objects.filter(processor_type__icontains='Core2',ip__icontains='192.168.105').count()
        tpcmid2 = asset_pc.objects.filter(processor_type__icontains='Dual',ip__icontains='192.168.105').count()
        tpcmid = tpcmid1 + tpcmid2
        #l$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        gpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.62').count()
        mpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.63').count()
        fpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.64').count()
        cpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.67').count()
        kpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.65').count()
        tpchigh = asset_pc.objects.filter(processor_type__icontains='CoreI',ip__icontains='192.168.105').count()

        allpcg = asset_pc.objects.filter(ip__icontains='192.168.62').count()
        allpcm = asset_pc.objects.filter(ip__icontains='192.168.63').count()
        allpcf = asset_pc.objects.filter(ip__icontains='192.168.64').count()
        allpcc = asset_pc.objects.filter(ip__icontains='192.168.67').count()
        allpck = asset_pc.objects.filter(ip__icontains='192.168.65').count()
        allpct = asset_pc.objects.filter(ip__icontains='192.168.105').count()

        #-----------------printers count-----------------------
        gprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.62').count()
        mprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.63').count()
        fprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.64').count()
        cprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.67').count()
        kprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.65').count()
        tprinterlaser = asset_printer.objects.filter(printer_type__icontains='Laser',ip__icontains='192.168.105').count()


        gprinterink = asset_printer.objects.filter(printer_type__icontains='Ink',ip__icontains='192.168.62').count()
        mprinterink = asset_printer.objects.filter(printer_type__icontains='Ink',ip__icontains='192.168.63').count()
        fprinterink = asset_printer.objects.filter(printer_type__icontains='Ink',ip__icontains='192.168.64').count()
        cprinterink = asset_printer.objects.filter(Q(printer_type__icontains='Ink',ip__icontains='192.168.67')|Q(printer_type__icontains='Desk',ip__icontains='192.168.67')).count()
        kprinterink = asset_printer.objects.filter(printer_type__icontains='Ink',ip__icontains='192.168.65').count()
        tprinterink = asset_printer.objects.filter(printer_type__icontains='Ink',ip__icontains='192.168.105').count()




        gprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.62').count()
        mprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.63').count()
        fprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.64').count()
        cprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.67').count()
        kprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.65').count()
        tprintermfp = asset_printer.objects.filter(printer_type__icontains='MFP',ip__icontains='192.168.105').count()




        allprinterg = asset_printer.objects.filter(ip__icontains='192.168.62').count()
        allprinterm = asset_printer.objects.filter(ip__icontains='192.168.63').count()
        allprinterf = asset_printer.objects.filter(ip__icontains='192.168.64').count()
        allprinterc = asset_printer.objects.filter(ip__icontains='192.168.67').count()
        allprinterk = asset_printer.objects.filter(ip__icontains='192.168.65').count()
        allprintert = asset_printer.objects.filter(ip__icontains='192.168.105').count()

        #-----------------scanners count-----------------------
        gscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.62').count()
        mscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.63').count()
        fscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.64').count()
        cscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.67').count()
        kscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.65').count()
        tscannorm = asset_scanner.objects.filter(scanner_type__icontains='LowSpeed',ip__icontains='192.168.105').count()



        gscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.62').count()
        mscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.63').count()
        fscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.64').count()
        cscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.67').count()
        kscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.65').count()
        tscanhigh = asset_scanner.objects.filter(scanner_type__icontains='HighSpeed',ip__icontains='192.168.105').count()



        allscanng = asset_scanner.objects.filter(ip__icontains='192.168.62').count()
        allscannm = asset_scanner.objects.filter(ip__icontains='192.168.63').count()
        allscannf = asset_scanner.objects.filter(ip__icontains='192.168.64').count()
        allscannc = asset_scanner.objects.filter(ip__icontains='192.168.67').count()
        allscannk = asset_scanner.objects.filter(ip__icontains='192.168.65').count()
        allscannt = asset_scanner.objects.filter(ip__icontains='192.168.105').count()

        #-----------------copiers count-----------------------

        gcopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.62').count()
        gcopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.62').count()
        gcopierdata = gcopierdata1 + gcopierdata2
        mcopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.63').count()
        mcopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.63').count()
        mcopierdata = gcopierdata1 + gcopierdata2
        fcopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.64').count()
        fcopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.64').count()
        fcopierdata = gcopierdata1 + gcopierdata2
        ccopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.67').count()
        ccopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.67').count()
        ccopierdata = gcopierdata1 + gcopierdata2
        kcopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.65').count()
        kcopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.65').count()
        kcopierdata = gcopierdata1 + gcopierdata2
        tcopierdata1 = asset_copier.objects.filter(conn_type__icontains='USB',ip__icontains='192.168.105').count()
        tcopierdata2 = asset_copier.objects.filter(conn_type__icontains='ETHERNET',ip__icontains='192.168.105').count()
        tcopierdata = gcopierdata1 + gcopierdata2



        gcopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.62').count()
        mcopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.63').count()
        fcopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.64').count()
        ccopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.67').count()
        kcopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.65').count()
        tcopiernodata = asset_copier.objects.filter(conn_type__icontains='NODATA',ip__icontains='192.168.105').count()



        allcopierg = asset_copier.objects.filter(ip__icontains='192.168.62').count()
        allcopierm = asset_copier.objects.filter(ip__icontains='192.168.63').count()
        allcopierf = asset_copier.objects.filter(ip__icontains='192.168.64').count()
        allcopierc = asset_copier.objects.filter(ip__icontains='192.168.67').count()
        allcopierk = asset_copier.objects.filter(ip__icontains='192.168.65').count()
        allcopiert = asset_copier.objects.filter(ip__icontains='192.168.105').count()
        return render(request,"reports.html",{"gpclow":gpclow,
        "mpclow":mpclow,
        "fpclow":fpclow,
        "cpclow":cpclow,
        "kpclow":kpclow,
        "tpclow":tpclow,
        "gpcmid":gpcmid,
        "mpcmid":mpcmid,
        "fpcmid":fpcmid,
        "cpcmid":cpcmid,
        "kpcmid":kpcmid,
        "tpcmid":tpcmid,
        "gpchigh":gpchigh,
        "mpchigh":mpchigh,
        "fpchigh":fpchigh,
        "cpchigh":cpchigh,
        "kpchigh":kpchigh,
        "tpchigh":tpchigh,
        "allpcg":allpcg,
        "allpcm":allpcm,
        "allpcf":allpcf,
        "allpcc":allpcc,
        "allpck":allpck,
        "allpct":allpct,
        "gprinterlaser":gprinterlaser,
        "mprinterlaser":mprinterlaser,
        "fprinterlaser":fprinterlaser,
        "cprinterlaser":cprinterlaser,
        "kprinterlaser":kprinterlaser,
        "tprinterlaser":tprinterlaser,
        "gprinterink":gprinterink,
        "mprinterink":mprinterink,
        "fprinterink":fprinterink,
        "cprinterink":cprinterink,
        "kprinterink":kprinterink,
        "tprinterink":tprinterink,
        "gprintermfp":gprintermfp,
        "mprintermfp":mprintermfp,
        "fprintermfp":fprintermfp,
        "cprintermfp":cprintermfp,
        "kprintermfp":kprintermfp,
        "tprintermfp":tprintermfp,
        "allprinterg":allprinterg,
        "allprinterm":allprinterm,
        "allprinterf":allprinterf,
        "allprinterc":allprinterc,
        "allprinterk":allprinterk,
        "allprintert":allprintert,
        "gscannorm":gscannorm,
        "mscannorm":mscannorm,
        "fscannorm":fscannorm,
        "cscannorm":cscannorm,
        "kscannorm":kscannorm,
        "tscannorm":tscannorm,
        "gscanhigh":gscanhigh,
        "mscanhigh":mscanhigh,
        "fscanhigh":fscanhigh,
        "cscanhigh":cscanhigh,
        "kscanhigh":kscanhigh,
        "tscanhigh":tscanhigh,
        "allscanng":allscanng,
        "allscannm":allscannm,
        "allscannf":allscannf,
        "allscannc":allscannc,
        "allscannk":allscannk,
        "allscannt":allscannt,
        "gcopierdata":gcopierdata,
        "mcopierdata":mcopierdata,
        "fcopierdata":fcopierdata,
        "ccopierdata":ccopierdata,
        "kcopierdata":kcopierdata,
        "tcopierdata":tcopierdata,
        "gcopiernodata":gcopiernodata,
        "mcopiernodata":mcopiernodata,
        "fcopiernodata":fcopiernodata,
        "ccopiernodata":ccopiernodata,
        "kcopiernodata":kcopiernodata,
        "tcopiernodata":tcopiernodata,
        "allcopierg":allcopierg,
        "allcopierm":allcopierm,
        "allcopierf":allcopierf,
        "allcopierc":allcopierc,
        "allcopierk":allcopierk,
        "allcopiert":allcopiert,
        })
    else:
        return HttpResponseRedirect(reverse('rest'))

#---------------------------------------------------------------------------------------
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


@login_required
def add_new_junk(request):
    form1 = add_junk((request.POST or None))
    title1 = ""
    qs = users.objects.all()
    qslen = users.objects.all().count()
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        junk_parts.id=str(uuid.uuid4())

        # if form1.cleaned_data['cplace'] == 'چهه اخرى':
        #     junk_parts.pstatus = False
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,"qs":qs,"qslen":qslen}
    return render(request, "junk-part.html", context)

def getusercode(request):
    username = request.GET.get("username", None)
    data = serializers.serialize('json', users.objects.filter(user_name__icontains=username).only("user_code"), fields=('user_code',))
    return JsonResponse(data[45:67],safe=False)
@login_required
def junk_update(request,id=None):
    junk_res = get_object_or_404(junk_parts,id=id)
    form1 = add_junk(request.POST or None,instance=junk_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False
    qs = users.objects.all()
    qslen = users.objects.all().count()

    if form1.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
    context={"junk_res":junk_res,"form1":form1,"qs":qs,"qslen":qslen}
    return render(request,"junk-part.html",context)
@login_required
def junk_remove1(request,id=None):
    instance = get_object_or_404(junk_parts, id=id)
    instance.delete()
    return render(request,"removed.html",{})

@login_required
def junks_detail(request):
       if request.user.id==1:
           junks_list = junk_parts.objects.all().order_by('bransh')
       else:
           junks_list = junk_parts.objects.all().filter(publisher=request.user)

       context = {"junks_list":junks_list}
       return render(request,"junks_detail.html", context)
@login_required
def junk_detail(request,id=None):
    junk_res = get_object_or_404(junk_parts,id=id)
    return render(request, "junk-detail.html",{"junk_res": junk_res,})


@login_required
def junks_list(request,id=None):
    if not request.user.is_staff:
            return  HttpResponseRedirect(reverse('rest'))
    today = str(date.today())
    junks_list = junk_parts.objects.all()
    if request.user.id == 1:
       junks_list_list = junk_parts.objects.all().order_by('bransh')
    else:
       junks_list_list = junk_parts.objects.all().filter(publisher=request.user)

    paginator = Paginator(junks_list_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        junks_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        junks_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        junks_list = paginator.page(paginator.num_pages)


     #***************************************************

    return render(request, "junk-list.html", {"junks_list":junks_list })
#ffffffffffffffffff
@login_required
def trans_success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:
        request.session['form-submitted'] = False
        return render(request,"trans_success.html", {})
#====================================
@login_required
def trans_the_junk(request,id=None):
    junk_res = get_object_or_404(junk_parts, id=id)
    form1 = trans_junk(request.POST or None,instance=junk_res)
    title1 = ""
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.pstatus = False
        instance1.save()
        return  HttpResponseRedirect(reverse('trans_success'))
    context = {"form1_title": title1, "form1": form1,"junk_res":junk_res}
    return render(request, "junk-part-trans.html", context)



@login_required
def printer_remove2(request,id=None):
    instance = get_object_or_404(asset_printer, id=id)
    instance.delete()
    return render(request,"removed.html",{})

def adminsrep(request):
    return render(request,"adminsrep.html",{})

#--------------------------------------------------------------------
def asset_search(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('rest'))
    form1 = search1((request.POST or None))
    form2 = search2(request.POST or None)
    form3 = search3(request.POST or None)

    if form1.is_valid() and form2.is_valid() and form3.is_valid():
        sectorname = form1.cleaned_data['select_sector']
        problem = form2.cleaned_data['select_problem']
        username = form3.cleaned_data['select_user']
        if sectorname == '' and problem == '' and username == '':
            title = "there is no search criteria entered"
            res = ""
            context = {"f1": form1, "f2": form2, "f3": form3, "title": title}

        elif sectorname and problem == 'HardWare' and username == '':
            res = hw_malfunction.objects.filter(user_sector__icontains=sectorname)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

        elif sectorname and problem == 'Network' and username == '':
            res = nw_malfunction.objects.filter(user_sector__icontains=sectorname)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

        elif sectorname and problem == 'Printers' and username == '':
            res = print_malfunction.objects.filter(user_sector__icontains=sectorname)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

        elif sectorname and problem == '' and username == '':
            hw_qs = hw_malfunction.objects.filter(user_sector__icontains=sectorname)
            nw_qs = nw_malfunction.objects.filter(user_sector__icontains=sectorname)
            p_qs = print_malfunction.objects.filter(user_sector__icontains=sectorname)
            res = list(chain(hw_qs, nw_qs, p_qs))
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

        elif sectorname and username and problem == '':
            hw_qs = hw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            nw_qs = nw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            p_qs = print_malfunction.objects.filter(user_sector__icontains=sectorname,
                                                    user_fullname__icontains=username)
            res = list(chain(hw_qs, nw_qs, p_qs))
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname and username and problem == 'HardWare':
            res = hw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname and username and problem == 'Network':
            res = nw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname and username and problem == 'Printers':
            res = print_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname == '' and username == '' and problem == 'HardWare':
            res = hw_malfunction.objects.all()
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

        elif sectorname == '' and username == '' and problem == 'Network':
            res = nw_malfunction.objects.all()
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname == '' and username == '' and problem == 'Print':
            res = print_malfunction.objects.all()
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)
        elif sectorname == '' and problem == '' and username:
            hw_qs = hw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            nw_qs = nw_malfunction.objects.filter(user_sector__icontains=sectorname, user_fullname__icontains=username)
            p_qs = print_malfunction.objects.filter(user_sector__icontains=sectorname,
                                                    user_fullname__icontains=username)
            res = list(chain(hw_qs, nw_qs, p_qs))
            cont1 = {"q": res, "f1": form1, "f2": form2, "f3": form3}
            return render(request, "searchc.html", cont1)

    context = {"f1": form1, "f2": form2, "f3": form3, }
    return render(request, "searchc.html", context)
#--------------------------------------------------------------------------------
def searchasst(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('rest'))
    form1 = searchassetmain((request.POST or None))
    form2 = searchassetcomputers(request.POST or None)
    form3 = searchassetlabs(request.POST or None)
    form4 = searchassetprinters(request.POST or None)
    form5 = searchassetscanners(request.POST or None)
    form6 = searchassetcopiers(request.POST or None)
    form7 = selectobj(request.POST or None)




    if form1.is_valid() and form2.is_valid() and form7.is_valid() :

        bransh = form1.cleaned_data['select_bransh']
        hsectors = form1.cleaned_data['select_hsectors']
        sector = form1.cleaned_data['select_sector']
        user = form1.cleaned_data['select_user']
        object = form7.cleaned_data['select_object']

        pcmodel = form2.cleaned_data['pc_model']
        oslicense = form2.cleaned_data['os_license']
        proctype = form2.cleaned_data['processor_type']
        hdds = form2.cleaned_data['harddisk_size']
        joined = form2.cleaned_data['joined']
        montype = form2.cleaned_data['monitor_type']
        # res = asset_pc.objects.filter(bransh__icontains=bransh )

        if  pcmodel=='' and oslicense=='' and proctype=='' and hdds=='' and joined=='' and montype=='':
            title = "there is no search criteria entered"
            res = ""
            context = {"f1": form1, "f2": form2,"title": title,"res":res}
            return render(request, "search_asset.html", context)

        elif user and object=='COMPUTERS' :
             res = asset_pc.objects.filter(user_fullname=user).order_by('-timestamp','processor_type')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif bransh and object=='COMPUTERS':
             res = asset_pc.objects.filter(bransh=bransh).order_by('-timestamp','processor_type')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif hsectors and object=='COMPUTERS':
             res = asset_pc.objects.filter(hsectors=hsectors).order_by('-timestamp','processor_type')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif sector and object=='COMPUTERS':
             res = asset_pc.objects.filter(user_sector=sector).order_by('-timestamp','processor_type')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        #-----------------------------
        elif user and object=='LABTOPS' :
             res = asset_lab.objects.filter(user_fullname=user).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif bransh and object=='LABTOPS':
             res = asset_lab.objects.filter(bransh=bransh).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif hsectors and object=='LABTOPS':
             res = asset_lab.objects.filter(hsectors=hsectors).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif sector and object=='LABTOPS':
             res = asset_lab.objects.filter(user_sector=sector).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        #-----------------------------
        elif user and object=='PRINTERS' :
             res = asset_printer.objects.filter(user_fullname=user).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif bransh and object=='PRINTERS':
             res = asset_printer.objects.filter(bransh=bransh).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif hsectors and object=='PRINTERS':
             res = asset_printer.objects.filter(hsectors=hsectors).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif sector and object=='PRINTERS':
             res = asset_printer.objects.filter(user_sector=sector).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        #-----------------------------
        elif user and object=='SCANNERS' :
             res = asset_scanner.objects.filter(user_fullname=user).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif bransh and object=='SCANNERS':
             res = asset_scanner.objects.filter(bransh=bransh).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif hsectors and object=='SCANNERS':
             res = asset_scanner.objects.filter(hsectors=hsectors).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif sector and object=='SCANNERS':
             res = asset_scanner.objects.filter(user_sector=sector).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        #-----------------------------
        elif user and object=='COPIERS' :
             res = asset_copier.objects.filter(user_fullname=user).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif bransh and object=='COPIERS':
             res = asset_copier.objects.filter(bransh=bransh).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif hsectors and object=='COPIERS':
             res = asset_copier.objects.filter(hsectors=hsectors).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        elif sector and object=='COPIERS':
             res = asset_copier.objects.filter(user_sector=sector).order_by('-timestamp')
             context = {"f1": form1, "f2": form2,"f7":form7,"res":res}
             return render(request, "search_asset.html", context)
        # elif hsectors:
        #      res = asset_pc.objects.filter(hsectors=hsectors)
        #      context = {"f1": form1, "f2": form2,"res":res}
        #      return render(request, "search_asset.html", context)

        # else:
        #      res = asset_pc.objects.filter(bransh=bransh, hsectors=hsectors)
        #      context = {"f1": form1, "f2": form2,"res": res}
        #      return render(request, "search_asset.html", context)
    context = {"f1": form1, "f2": form2,"f7":form7,}
    return render(request,"search_asset.html",context)
#--------------------------------------------------------------------------------
def searchasst2(request):
            if not request.user.is_staff:
                return HttpResponseRedirect(reverse('rest'))
            form1 = searchassetmain((request.POST or None))
            form2 = searchassetcomputers(request.POST or None)
            form3 = searchassetlabs(request.POST or None)
            form4 = searchassetprinters(request.POST or None)
            form5 = searchassetscanners(request.POST or None)
            form6 = searchassetcopiers(request.POST or None)
            form7 = selectobj(request.POST or None)
            qs = users.objects.all()
            qslen = users.objects.all().count()



            if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() :

                bransh = form1.cleaned_data['select_bransh']
                hsectors = form1.cleaned_data['select_hsectors']
                sector = form1.cleaned_data['select_sector']
                user = form1.cleaned_data['select_user']
                object = form7.cleaned_data['select_object']

                pcmodel = form2.cleaned_data['pc_model']
                oslicense = form2.cleaned_data['os_license']
                proctype = form2.cleaned_data['processor_type']
                hdds = form2.cleaned_data['harddisk_size']
                joined = form2.cleaned_data['joined']
                montype = form2.cleaned_data['monitor_type']

                labmodel = form3.cleaned_data['lab_model']
                labvendor = form3.cleaned_data['lab_vendor']


                printertype = form4.cleaned_data['printer_type']
                printermodel = form4.cleaned_data['printer_model']

                scannertype = form5.cleaned_data['scanner_type']
                scannermodel = form5.cleaned_data['scanner_model']

                copiermodel = form6.cleaned_data['copier_model']
                conntype = form6.cleaned_data['conn_type']

                if  pcmodel and oslicense and proctype and hdds=='' and joined=='' and montype=='':
                    title = "there is no search criteria entered"
                    res = ""
                    context = {"f1": form1, "f2": form2,"title": title,"res":res}
                    return render(request, "search_asset2.html", context)

                # ---computers---search--------------------------------------------------------------------------------------
                elif user and object and pcmodel:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,pc_model__icontains=pcmodel).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh and object and pcmodel:
                     res = asset_pc.objects.filter(bransh=bransh,pc_model__icontains=pcmodel).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and object and pcmodel :
                     res = asset_pc.objects.filter(hsectors=hsectors,pc_model__icontains=pcmodel).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector and object and pcmodel:
                     res = asset_pc.objects.filter(user_sector=sector,pc_model__icontains=pcmodel).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)





                elif user and object and oslicense:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,os_license=oslicense).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh and object  and oslicense:
                     res = asset_pc.objects.filter(bransh=bransh,os_license=oslicense).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and object  and oslicense:
                     res = asset_pc.objects.filter(hsectors=hsectors,os_license=oslicense).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and oslicense:
                     res = asset_pc.objects.filter(user_sector=sector,os_license=oslicense).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user and object  and proctype:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,processor_type=proctype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and proctype:
                     res = asset_pc.objects.filter(bransh=bransh,processor_type=proctype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and object  and proctype:
                     res = asset_pc.objects.filter(hsectors=hsectors,processor_type=proctype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector and object  and proctype:
                     res = asset_pc.objects.filter(user_sector=sector,processor_type=proctype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and hdds:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,harddisk_size__icontains=hdds).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and hdds:
                     res = asset_pc.objects.filter(bransh=bransh,harddisk_size__icontains=hdds).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and hdds:
                     res = asset_pc.objects.filter(hsectors=hsectors,harddisk_size__icontains=hdds).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and hdds:
                     res = asset_pc.objects.filter(user_sector=sector,harddisk_size__icontains=hdds).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and joined:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,joined=joined).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and joined:
                     res = asset_pc.objects.filter(bransh=bransh,joined=joined).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and object  and joined:
                     res = asset_pc.objects.filter(hsectors=hsectors,joined=joined).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and joined:
                     res = asset_pc.objects.filter(user_sector=sector,joined=joined).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and montype:
                     res = asset_pc.objects.filter(user_fullname__icontains=user,monitor_type=montype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and hdds:
                     res = asset_pc.objects.filter(bransh=bransh,monitor_type=montype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and hdds:
                     res = asset_pc.objects.filter(hsectors=hsectors,monitor_type=montype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and hdds:
                     res = asset_pc.objects.filter(user_sector=sector,monitor_type=montype).order_by('processor_type')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                # ------labtop--search-----------------------------
                elif user  and object and labmodel:
                     res = asset_lab.objects.filter(user_fullname__icontains=user,lab_model__icontains=labmodel).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and labmodel:
                     res = asset_lab.objects.filter(bransh=bransh,lab_model__icontains=labmodel).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and labmodel:
                     res = asset_lab.objects.filter(hsectors=hsectors,lab_model__icontains=user,lab_model=labmodel).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and labmodel:
                     res = asset_lab.objects.filter(user_sector=sector,lab_model__icontains=labmodel).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and labvendor:
                     res = asset_lab.objects.filter(user_fullname__icontains=user,lab_vendor__icontains=labvendor).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and oslicense:
                     res = asset_lab.objects.filter(bransh=bransh,lab_vendor__icontains=labvendor).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and oslicense:
                     res = asset_lab.objects.filter(hsectors=hsectors,lab_vendor__icontains=labvendor).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and oslicense:
                     res = asset_lab.objects.filter(user_sector=sector,lab_vendor__icontains=labvendor).order_by('lab_vendor')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                # -------search--printer----------------------------------------
                elif user  and object and printertype:
                     res = asset_printer.objects.filter(user_fullname__icontains=user,printer_type=printertype).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and printertype:
                     res = asset_printer.objects.filter(bransh=bransh,printer_type=printertype).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and printertype:
                     res = asset_printer.objects.filter(hsectors=hsectors,printer_type=printertype).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and printertype:
                     res = asset_printer.objects.filter(user_sector=sector,printer_type=printertype).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and printermodel:
                     res = asset_printer.objects.filter(user_fullname__icontains=user,printer_model__icontains=printermodel).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and printermodel:
                     res = asset_printer.objects.filter(bransh=bransh,printer_model__icontains=printermodel).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and printermodel:
                     res = asset_printer.objects.filter(hsectors=hsectors,printer_model__icontains=printermodel).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and printermodel:
                     res = asset_printer.objects.filter(user_sector=sector,printer_model__icontains=printermodel).order_by('printer_model')
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                # ----search --scanner-------------------------
                elif user  and object and scannertype:
                     res = asset_scanner.objects.filter(user_fullname__icontains=user,scanner_type=scannertype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return scannertype(request, "search_asset2.html", context)
                elif bransh  and object and scannertype:
                     res = asset_scanner.objects.filter(bransh=bransh,scanner_type=scannertype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and scannertype:
                     res = asset_scanner.objects.filter(hsectors=hsectors,scanner_type=scannertype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and scannertype:
                     res = asset_scanner.objects.filter(user_sector=sector,scanner_type=scannertype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                elif user  and object and scannermodel:
                     res = asset_scanner.objects.filter(user_fullname__icontains=user,scanner_model__icontains=scannermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and scannermodel:
                     res = asset_scanner.objects.filter(bransh=bransh,scanner_model__icontains=scannermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors and scannermodel:
                     res = asset_scanner.objects.filter(hsectors=hsectors,scanner_model__icontains=scannermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and scannermodel:
                     res = asset_scanner.objects.filter(user_sector=sector,scanner_model__icontains=scannermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)

                # -------search---copiers----------------------
                elif user  and object and copiermodel:
                     res = asset_copier.objects.filter(user_fullname__icontains=user,copier_model__icontains=copiermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif bransh  and object and copiermodel:
                     res = asset_copier.objects.filter(bransh=bransh,copier_model__icontains=copiermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and copiermodel:
                     res = asset_copier.objects.filter(hsectors=hsectors,copier_model__icontains=copiermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and copiermodel:
                     res = asset_copier.objects.filter(user_sector=sector,copier_model__icontains=copiermodel)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)


                elif bransh  and object and conntype:
                     res = asset_copier.objects.filter(bransh=bransh,conn_type=conntype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif hsectors  and object and conntype:
                     res = asset_copier.objects.filter(hsectors=hsectors,conn_type=conntype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)
                elif sector  and object and conntype:
                     res = asset_copier.objects.filter(user_sector=sector,conn_type=conntype)
                     context = {"f1": form1, "f2": form2,"f3": form3,"f4": form4,"f5": form5,"f6": form6, "f7": form7, "res": res}
                     return render(request, "search_asset2.html", context)


        # elif hsectors:
        #      res = asset_pc.objects.filter(hsectors=hsectors)
        #      context = {"f1": form1, "f2": form2,"res":res}
        #      return render(request, "search_asset.html", context)

        # else:
        #      res = asset_pc.objects.filter(bransh=bransh, hsectors=hsectors)
        #      context = {"f1": form1, "f2": form2,"res": res}
        #      return render(request, "search_asset.html", context)
            context = {"f1": form1, "f2": form2,"f7":form7,"f3": form3,"f4": form4,"f5": form5,"f6": form6,"qs":qs,"qslen":qslen}
            return render(request,"search_asset2.html",context)

#---------------------------------------------------------------------------------------------------------------------
@login_required
def add_mission(request):
    form1 = record_mission((request.POST or None))
    title1 = ""
    if form1.is_valid():
        missions.id = str(uuid.uuid4())
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('asset_add_success'))
    context = {"form1_title": title1, "form1": form1,}
    return render(request, "add-missions.html", context)
#---------------------------------------------------------------------------------------------------------------------
@login_required
def list_mission(request):
    aabdelall = missions.objects.filter(publisher__username='aabdelall').order_by('timestamp')
    aebaid = missions.objects.filter(publisher__username='aebaid').order_by('timestamp')
    aesam = missions.objects.filter(publisher__username='aesam').order_by('timestamp')
    ahegazy = missions.objects.filter(publisher__username='ahegazy').order_by('timestamp')
    aibrahim = missions.objects.filter(publisher__username='aibrahim').order_by('timestamp')
    arefaat = missions.objects.filter(publisher__username='arefaat').order_by('timestamp')
    arefky = missions.objects.filter(publisher__username='arefky').order_by('timestamp')
    asalah = missions.objects.filter(publisher__username='asalah').order_by('timestamp')
    asaoud = missions.objects.filter(publisher__username='asaoud').order_by('timestamp')
    dserag = missions.objects.filter(publisher__username='dserag').order_by('timestamp')
    hmostafa = missions.objects.filter(publisher__username='hmostafa').order_by('timestamp')
    iwahab = missions.objects.filter(publisher__username='iwahab').order_by('timestamp')
    mahamed = missions.objects.filter(publisher__username='mahamed').order_by('timestamp')
    mgad = missions.objects.filter(publisher__username='mgad').order_by('timestamp')
    mmohamed = missions.objects.filter(publisher__username='mmohamed').order_by('timestamp')
    mmostafa = missions.objects.filter(publisher__username='mmostafa').order_by('timestamp')
    mnady = missions.objects.filter(publisher__username='mnady').order_by('timestamp')
    mshaban = missions.objects.filter(publisher__username='mshaban').order_by('timestamp')
    ofathy = missions.objects.filter(publisher__username='ofathy').order_by('timestamp')
    rsamir = missions.objects.filter(publisher__username='rsamir').order_by('timestamp')
    wtaweel = missions.objects.filter(publisher__username='wtaweel').order_by('timestamp')
    wtawfaik = missions.objects.filter(publisher__username='wtawfaik').order_by('timestamp')
    ygohary = missions.objects.filter(publisher__username='ygohary').order_by('timestamp')
    mahm = "محمد احمد"
    aref = "عبد المنعم رفعت"
    asid = "أحمد سعيد"
    walaa = "وائل علاء الدين"
    mnad = "مصطفى نادى"
    aref = "احمد رفقى"
    wtaw = "وائل الطويل"
    iwahab = "اسلام عبد الوهاب"
    ahegaz = "أحمد حجازى"
    asala = "أحمد صلاح"
    rsam = "رامز سمير"
    abaid = "أحمد عبيد "
    aibr = "أحمد إبراهيم"
    mgad = "محمد جاد"
    ygoh = "ياسمين الجوهرى"
    aaal = "اميرة عبد العال"
    mmoha = "مها محمد"
    asaod = "أمجد أبو السعود"
    ofat = "أسامة فتحى"
    mmos = "محمد مصطفى"
    dser = "دينا سراج"
    mshab = "محمد شعبان"
    hmost = "هانى مصطفى"
    aesam = "احمد عصام"
    context={ "aabdelall":aabdelall,"aebaid":aebaid,"aesam":aesam,"ahegazy":ahegazy,"aibrahim":aibrahim,"arefaat":arefaat,"arefky":arefky,
     "asalah":asalah,"asaoud":asaoud,"dserag":dserag,"hmostafa":hmostafa,"iwahab":iwahab,"mahamed":mahamed,"mgad":mgad,"mmohamed":mmohamed,
    "mmostafa":mmostafa,"mnady":mnady,"mshaban":mshaban,"ofathy":ofathy,"rsamir":rsamir,"wtaweel":wtaweel,"wtawfaik":wtawfaik,
    "ygohary":ygohary,

              "mahm": mahm,
              "aref": aref,
              "asid": asid,
              "walaa": walaa,
              "mnad": mnad,
              "aref": aref,
              "wtaw": wtaw,
              "iwahab": iwahab,
              "ahegaz": ahegaz,
              "asala": asala,
              "rsam": rsam,
              "abaid": abaid,
              "aibr": aibr,
              "mgad": mgad,
              "ygoh": ygoh,
              "aaal": aaal,
              "mmoha": mmoha,
              "asaod": asaod,
              "ofat": ofat,
              "mmos": mmos,
              "dser": dser,
              "mshab": mshab,
              "hmost": hmost,
              "aesam": aesam,
                  }

    return render(request, "list-missions.html", context)
@login_required
def mission_main(request):

    context = {}
    return render(request, "missions-main.html", context)


@login_required
def mission_add_success(request):
    return render(request,"mission_add_success.html", {})
#________________________________________________________
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#********************************************************************************************************************************
@login_required
def law_affairs(request):
    if not has_group(request.user, "law"):
       return HttpResponseRedirect(reverse('restlaw'))
    form = add_law_note((request.POST or None))
    title2 = ""
    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.ip = request.META['REMOTE_ADDR']
        instance2.publisher = request.user
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))

    context = {"form2_title": title2, "form": form,}
    return render(request, "law_affairs.html", context)
@login_required
def law_affairs_main(request):
    if not has_group(request.user, "law"):
       return HttpResponseRedirect(reverse('restlaw'))
    context = {}
    return render(request, "law_affairs_main.html", context)
@login_required
def law_affairs_list(request):
    if not has_group(request.user, "law"):
       return HttpResponseRedirect(reverse('restlaw'))
    cases_res = LAW.objects.all().order_by('timestamp')
    context = {"cases_res":cases_res}
    return render(request, "law_affairs_list.html", context)
@login_required
def law_affairs_update(request,id=None):
    if not has_group(request.user, "law"):
       return HttpResponseRedirect(reverse('restlaw'))
    law_res = get_object_or_404(LAW,id=id)
    form1 = update_law_note(request.POST or None,instance=law_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"law_affairs_update.html",context)


# -------------------------------------------------------------
def searchcases(request):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))

    form1 = searchlaw((request.POST or None))


    if form1.is_valid():
        case_name = form1.cleaned_data['case_subject']
        court_name = form1.cleaned_data['case_court']
        lawyer_name = form1.cleaned_data['current_lawyer']
        if case_name :
            res = law_cases.objects.filter(case_subject__icontains=case_name)
            cont1 = {"q": res,"f1": form1,}
            return render(request,"search_case.html", cont1)

        elif court_name:
            res = law_cases.objects.filter(case_court__court__icontains=court_name)
            cont1 = {"q": res, "f1": form1,}
            return render(request,"search_case.html", cont1)

        elif lawyer_name:
            res = law_cases.objects.filter(current_lawyer__lawyer__icontains=lawyer_name)
            cont1 = {"q": res, "f1": form1,}
            return render(request, "search_case.html", cont1)


    context = {"f1": form1 }
    return render(request, "search_case.html", context)
#-------------------------------------------------------------------------------
@login_required
def restlaw(request):
    return render(request,"restrictedlaw.html", {})
#===============================================================================================================================
#===============================================================================================================================
@login_required
def law_case_add(request):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    form = add_law_cases((request.POST or None))

    title1 = ""
    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.ip = request.META['REMOTE_ADDR']
        instance2.publisher = request.user

        instance2.save()

        return HttpResponseRedirect(reverse('law_add_success'))

    context = {"title1": title1, "form": form}
    return render(request, "Add_Case.html", context)


@login_required
def law_sitting_add(request):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    form = add_case_sittings((request.POST or None))

    title2 = ""
    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.ip = request.META['REMOTE_ADDR']
        instance2.publisher = request.user
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))

@login_required
def cases(request):
    return render(request,"cases.html", {})



@login_required
def add_master(request):
    return render(request,"Addmaster.html", {})


#****************************************************************************************
@login_required
def addthe_casedep(request):
    form = add_casedep((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_casedep.html", context)


@login_required
def addthe_case_depart_type(request):
    form = add_case_depart_type((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_case_depart_type.html", context)

@login_required
def addthe_case_classification(request):
    form = add_case_classification((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_case_classification.html", context)


@login_required
def addthe_case_category(request):
    form = add_case_category((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_case_category.html", context)

@login_required
def addthe_case_court_name(request):
    form = add_case_court_name((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_case_court_name.html", context)

@login_required
def addthe_case_lawyer(request):
    form = add_case_lawyer((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_case_lawyer.html", context)

@login_required
def addthecase_current_status(request):
    form = add_case_current_status((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthecase_current_status.html", context)

@login_required
def addthe_litigationdeg(request):
    form = add_litigationdeg((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "addthe_litigationdeg.html", context)

@login_required
def caseslisttoaddsitting(request):
    # if request.user.id == 1:
    #    computers_list = asset_pc.objects.all().order_by('bransh')
    # else:
    #cases_list = asset_pc.objects.all().filter(publisher=request.user)
    cases_list = law_cases.objects.all()
    context = {"cases_list":cases_list}
    return render(request,"caseslistforadd.html", context)

@login_required
def casedetforadd(request,id=None):
    form = add_case_sittings((request.POST or None))
    if  form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        #return HttpResponseRedirect(reverse('law_add_success'))
    case_res = get_object_or_404(law_cases,id=id)
    cnums = law_cases.objects.filter().values_list('case_number')
    sitting_list = case_sittings.objects.filter(case_number__in=cnums)
    case_res2 = law_cases.objects.all()
    theurl = request.path
    subs = "casedetforadd"
    resl = theurl.find('subs')



    return render(request, "casedetforadd.html",{"theurl":theurl,"subs":subs,"resl":resl,"case_res": case_res,"form":form,"sitting_list":sitting_list,"case_res2":case_res2})

@login_required
def case_update(request,id=None):
    case_res = get_object_or_404(law_cases,id=id)
    form = add_law_cases(request.POST or None,instance=case_res)
    title1 = ""
    head = "تعديل بيانات الدعوى القضائيه"
    if form.is_valid():
       # request.session['form-submitted'] = True
        instance1 = form.save(commit=False)
        #instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
    theurl = request.path
    subs = "case_update"
    title1 = theurl.find('subs')
    context={"case_res":case_res,"form":form,"title1":title1,"head":head}
    return render(request,"Add_Case.html",context)

@login_required
def cases_detail(request,id=None):
        cases_list = get_object_or_404(law_cases,id=id)
        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        context = {"cases_list":cases_list}
        return render(request,"cases_detail.html", context)

@login_required
def cases_list(request):
        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        cases_list = law_cases.objects.all()
        context = {"cases_list":cases_list}
        return render(request,"cases_list.html", context)






@login_required
def add_the_opponent(request):
    form = add_opponent((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "add_the_opponent.html", context)

@login_required
def add_the_opponent_rep(request):
    form = add_opponent_rep((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "add_the_opponent_rep.html", context)

@login_required
def add_the_gainwtpercent(request):
    form = add_gainwtpercent((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "add_the_gainwtpercent.html", context)


@login_required
def add_the_comprep(request):
    form = add_comprep((request.POST or None))

    if form.is_valid():
        request.session['form-submitted'] = True
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    context = {"form": form}
    return render(request, "add_the_comprep.html", context)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////MEDICAL//////////////////////////////////MEDICAL/////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@login_required
def add_working_pationt_v(request):
    form1 = add_working_pationt((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
@login_required
def add_retired_pationt_v(request):
    form1 = add_retired_pationt((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_hospital_v(request):
    form1 = add_hospital((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_laboratory_v(request):
    form1 = add_laboratory((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_doctor_clinic_v(request):
    form1 = add_doctor_clinic((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_script_v1(request):
    form1 = add_medical_script1((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    qs=midicine.objects.all()
    qslen=midicine.objects.all().count()
    #q= medical_script1.objects.all().order_by('-timestamp')


 #   search_text = request.GET.get("search_text",None)      
 #   q = medical_script1.objects.filter(medical_number = search_text)
    q = medical_script1.objects.filter(publisher=request.user).order_by('-timestamp')

         
       
        #   q= medical_script1.objects.all().order_by('-timestamp')
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form": form1,"source":src,"qs":qs,"qslen":qslen,"q":q}
    return render(request, "add_medical_script_v1.html", context)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_script_v2(request):
    form1 = add_medical_script2((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    q = medical_script2.objects.filter(publisher=request.user).order_by('-timestamp')
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form": form1,"source":src,"q":q}
    return render(request, "add_medical_script_v2.html", context)
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_script_v3(request):
    form1 = add_medical_script3((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    q = medical_script3.objects.filter(publisher=request.user).order_by('-timestamp')

    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form": form1,"source":src}
    return render(request, "add_medical_script_v3.html", context)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_monthly_medical_script_v1(request):
    form1 = add_monthly_medical_script1((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form": form1,"source":src}
    return render(request, "add_monthly_medical_script_v1.html", context)    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_monthly_medical_script_v2(request):
    form1 = add_monthly_medical_script2((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form": form1,"source":src}
    return render(request, "add_monthly_medical_script_v2.html", context)        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_transform_v1(request):
    form1 = add_mdeical_transform1((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_medical_tran_v1.html", context)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_transform_v2(request):
    form1 = add_mdeical_transform2((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_medical_tran_v2.html", context)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_medical_transform_v3(request):
    form1 = add_mdeical_transform3((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_medical_tran_v3.html", context)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def add_midicine_v(request):
    form1 = add_midicine((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, ".html", context)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@login_required
def scripts_main(request):
    return render(request,"scripts_main.html", {})
@login_required
def transforms_main(request):
    return render(request,"transforms_main.html", {})
@login_required
def master_main(request):
    return render(request,"Master_Data.html", {})
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#---------------------------------Master Addition---------------------------------------------------------------
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#------------------hospitals
@login_required
def add_hospital_v(request):
    form1 = add_hospital((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_hospital.html", context)
#------------------------------------------------------
@login_required
def hospital_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    hospital_res = get_object_or_404(hospital,id=id)
    form1 = add_hospital(request.POST or None,instance=hospital_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_hospital.html",context)
#------------------------------------------------------

@login_required
def hospitals_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        hospitals_list = hospital.objects.all()
        context = {"hospitals_list":hospitals_list}
        return render(request,"hospitals_detail.html", context)
@login_required
def hospital_detail(request,id=None):
    hospital_res = get_object_or_404(hospital,id=id)
    return render(request, "hospital-detail.html",{"hospital_res": hospital_res,})


@login_required
def hospitals_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        hospitals_list = hospital.objects.all()
        context = {"hospitals_list":hospitals_list}
        return render(request,"hospitals_detail2.html", context)
@login_required
def hospital_remove_v(request,id=None):
    instance = get_object_or_404(hospital, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("hosp_det/"):
       go='hospitals_detail'
    
    return render(request,"removed.html",{"go":go})
 #----------------------------------------
 # ---------------------------------------
 # -------------------------------------------   
@login_required
def update_success(request):
    t = request.META.get('HTTP_REFERER')
    if t.endswith("hosp-update/"):
       go='hospitals_detail_V'
    elif t.endswith("laboratory-update/"):
       go='laboratorys_detail_V'
    elif t.endswith("doctor_clinic-update/"):
       go='doctor_clinics_detail_V'
    elif t.endswith("midicine-update/"):
       go='midicines_detail_V'
    elif t.endswith("working_pationt-update/"):
       go='working_pationts_detail_V'
    elif t.endswith("retired_pationt-update/"):
       go='retired_pationts_detail_V'
    elif t.endswith("monthly_medical_script1-update/"):
       go='monthly_medical_script1s_detail_V'
    elif t.endswith("monthly_medical_script2-update/"):
       go='monthly_medical_script2s_detail_V'
    elif t.endswith("monthly_medical_script3-update/"):
       go='monthly_medical_script1s_detail_V'                     
    elif t.endswith("add_new_monthly_script1_v/"):
       go='monthlyscript_working_search'            

    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:
        request.session['form-submitted'] = False
        return render(request,"update_success.html", {"go":go})
        # time.sleep(5) 
        # if t.endswith("hosp-update/"):
        #    return HttpResponseRedirect(reverse('hospitals_detail_V'))
    # if t.endswith("hosp-update/"):
    #    return HttpResponseRedirect(reverse('hospitals_detail_V')    

@login_required
def back(request,t):
     # t = request.META.get('HTTP_REFERER')
    if t.endswith("hosp-update/"):
       t= 'hospitals_detail_V'
       back(request,t)
     #  return HttpResponseRedirect(reverse('hospitals_detail_V'))

@login_required
def success(request):
    if  request.session['form-submitted'] == False:
        return  HttpResponseRedirect(reverse('rest'))
    else:    
        return render(request,"success.html", {})       

#--------------------------------------------------------
#---------------------------------------------------------------------------------------------
#=======================================laboratory=============================================
@login_required
def add_laboratory_v(request):
    form1 = add_laboratory((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_laboratory.html", context)
#------------------------------------------------------
@login_required
def laboratorys_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    laboratory_res = get_object_or_404(laboratory,id=id)
    form1 = add_laboratory(request.POST or None,instance=laboratory_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_laboratory.html",context)
#------------------------------------------------------

@login_required
def laboratorys_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        laboratorys_list = laboratory.objects.all()
        context = {"laboratorys_list":laboratorys_list}
        return render(request,"laboratorys_detail.html", context)
@login_required
def laboratory_detail(request,id=None):
    laboratory_res = get_object_or_404(laboratory,id=id)
    return render(request, "laboratory-detail.html",{"laboratory_res": laboratory_res,})


@login_required
def laboratorys_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        laboratorys_list = laboratory.objects.all()
        context = {"laboratorys_list":laboratorys_list}
        return render(request,"laboratorys_detail2.html", context)
@login_required
def laboratory_remove_v(request,id=None):
    instance = get_object_or_404(laboratory, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("laboratory_det/"):
       go='laboratorys_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================clinic=============================================
@login_required
def add_doctor_clinic_v(request):
    form1 = add_doctor_clinic((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_doctor_clinic.html", context)
#------------------------------------------------------
@login_required
def doctor_clinic_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    doctor_clinic_res = get_object_or_404(doctor_clinic,id=id)
    form1 = add_doctor_clinic(request.POST or None,instance=doctor_clinic_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_doctor_clinic.html",context)
#------------------------------------------------------

@login_required
def doctor_clinics_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        doctor_clinics_list = doctor_clinic.objects.all()
        context = {"doctor_clinics_list":doctor_clinics_list}
        return render(request,"doctor_clinics_detail.html", context)
@login_required
def doctor_clinic_detail(request,id=None):
    doctor_clinic_res = get_object_or_404(doctor_clinic,id=id)
    return render(request, "doctor_clinic-detail.html",{"doctor_clinic_res": doctor_clinic_res,})


@login_required
def doctor_clinics_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        doctor_clinics_list = doctor_clinic.objects.all()
        context = {"doctor_clinics_list":doctor_clinics_list}
        return render(request,"doctor_clinics_detail2.html", context)
@login_required
def doctor_clinic_remove_v(request,id=None):
    instance = get_object_or_404(doctor_clinic, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("doctor_clinic_det/"):
       go='doctor_clinics_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================medicine==============================================
@login_required
def add_midicine_v(request):
    form1 = add_midicine((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_midicine.html", context)
#------------------------------------------------------
@login_required
def midicine_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    midicine_res = get_object_or_404(midicine,id=id)
    form1 = add_midicine(request.POST or None,instance=midicine_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_midicine.html",context)
#------------------------------------------------------

@login_required
def midicines_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        midicines_list = midicine.objects.all()
        context = {"midicines_list":midicines_list}
        return render(request,"midicines_detail.html", context)
@login_required
def midicine_detail(request,id=None):
    midicine_res = get_object_or_404(midicine,id=id)
    return render(request, "midicine-detail.html",{"midicine_res": midicine_res,})


@login_required
def midicines_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        midicines_list = midicine.objects.all()
        context = {"midicines_list":midicines_list}
        return render(request,"midicines_detail2.html", context)
@login_required
def midicine_remove_v(request,id=None):
    instance = get_object_or_404(midicine, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("midicine_det/"):
       go='midicines_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================working pation============================================
@login_required
def add_working_pationt_v(request):
    form1 = add_working_pationt((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_working_pationt.html", context)
#------------------------------------------------------
@login_required
def working_pationt_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    working_pationt_res = get_object_or_404(working_pationt,id=id)
    form1 = add_working_pationt(request.POST or None,instance=working_pationt_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_working_pationt.html",context)
#------------------------------------------------------

@login_required
def working_pationts_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        working_pationts_list = working_pationt.objects.all()
        context = {"working_pationts_list":working_pationts_list}
        return render(request,"working_pationts_detail.html", context)
@login_required
def working_pationt_detail(request,id=None):
    working_pationt_res = get_object_or_404(working_pationt,id=id)
    return render(request, "working_pationt-detail.html",{"working_pationt_res": working_pationt_res,})


@login_required
def working_pationts_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        working_pationts_list = working_pationt.objects.all()
        context = {"working_pationts_list":working_pationts_list}
        return render(request,"working_pationts_detail2.html", context)
@login_required
def working_pationt_remove_v(request,id=None):
    instance = get_object_or_404(working_pationt, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("working_pationt_det/"):
       go='working_pationts_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================retired  pationt=====================================
@login_required
def add_retired_pationt_v(request):
    form1 = add_retired_pationt((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_retired_pationt.html", context)
#------------------------------------------------------
@login_required
def retired_pationt_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    retired_pationt_res = get_object_or_404(retired_pationt,id=id)
    form1 = add_retired_pationt(request.POST or None,instance=retired_pationt_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_retired_pationt.html",context)
#------------------------------------------------------

@login_required
def retired_pationts_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        retired_pationts_list = retired_pationt.objects.all()
        context = {"retired_pationts_list":retired_pationts_list}
        return render(request,"retired_pationts_detail.html", context)
@login_required
def retired_pationt_detail(request,id=None):
    retired_pationt_res = get_object_or_404(retired_pationt,id=id)
    return render(request, "retired_pationt-detail.html",{"retired_pationt_res": retired_pationt_res,})


@login_required
def retired_pationts_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        retired_pationts_list = retired_pationt.objects.all()
        context = {"retired_pationts_list":retired_pationts_list}
        return render(request,"retired_pationts_detail2.html", context)
@login_required
def retired_pationt_remove_v(request,id=None):
    instance = get_object_or_404(retired_pationt, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("retired_pationt_det/"):
       go='retired_pationts_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================monthly script for working==============================
@login_required
def add_monthly_medical_script1_v(request):
    form1 = add_monthly_medical_script1((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_monthly_medical_script1.html", context)
#------------------------------------------------------
@login_required
def monthly_medical_script1_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script1_res = get_object_or_404(monthly_medical_script1,id=id)
    form1 = add_monthly_medical_script1(request.POST or None,instance=monthly_medical_script1_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_monthly_medical_script1.html",context)
#------------------------------------------------------

@login_required
def monthly_medical_script1s_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script1s_list = monthly_medical_script1.objects.all().filter(master=True)
        context = {"monthly_medical_script1s_list":monthly_medical_script1s_list}
        return render(request,"monthly_medical_script1s_detail.html", context)
@login_required
def monthly_medical_script1_detail(request,id=None):
    monthly_medical_script1_res = get_object_or_404(monthly_medical_script1,id=id)
    return render(request, "monthly_medical_script1-detail.html",{"monthly_medical_script1_res": monthly_medical_script1_res,})


@login_required
def monthly_medical_script1s_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script1s_list = monthly_medical_script1.objects.all().filter(master=True)
        context = {"monthly_medical_script1s_list":monthly_medical_script1s_list}
        return render(request,"monthly_medical_script1s_detail2.html", context)
@login_required
def monthly_medical_script1_remove_v(request,id=None):
    instance = get_object_or_404(monthly_medical_script1, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("monthly_medical_script1_det/"):
       go='monthly_medical_script1s_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================monthly script for retired==================================================
@login_required
def add_monthly_medical_script2_v(request):
    form1 = add_monthly_medical_script2((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_monthly_medical_script2.html", context)
#------------------------------------------------------
@login_required
def monthly_medical_script2_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script2_res = get_object_or_404(monthly_medical_script2,id=id)
    form1 = add_monthly_medical_script2(request.POST or None,instance=monthly_medical_script2_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_monthly_medical_script2.html",context)
#------------------------------------------------------

@login_required
def monthly_medical_script2s_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script2s_list = monthly_medical_script2.objects.all()
        context = {"monthly_medical_script2s_list":monthly_medical_script2s_list}
        return render(request,"monthly_medical_script2s_detail.html", context)
@login_required
def monthly_medical_script2_detail(request,id=None):
    monthly_medical_script2_res = get_object_or_404(monthly_medical_script2,id=id)
    return render(request, "monthly_medical_script2-detail.html",{"monthly_medical_script2_res": monthly_medical_script2_res,})


@login_required
def monthly_medical_script2s_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script2s_list = monthly_medical_script2.objects.all()
        context = {"monthly_medical_script2s_list":monthly_medical_script2s_list}
        return render(request,"monthly_medical_script2s_detail2.html", context)
@login_required
def monthly_medical_script2_remove_v(request,id=None):
    instance = get_object_or_404(monthly_medical_script2, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("monthly_medical_script2_det/"):
       go='monthly_medical_script2s_detail'
    
    return render(request,"removed.html",{"go":go})
# ======================================monthly script for member========================================================
@login_required
def add_monthly_medical_script3_v(request):
    form1 = add_monthly_medical_script3((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    context = {"form1_title": title1, "form1": form1,"source":src}
    return render(request, "add_monthly_medical_script3.html", context)
#------------------------------------------------------
@login_required
def monthly_medical_script3_update_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script3_res = get_object_or_404(monthly_medical_script3,id=id)
    form1 = add_monthly_medical_script3(request.POST or None,instance=monthly_medical_script3_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate}
    return render(request,"update_monthly_medical_script3.html",context)
#------------------------------------------------------

@login_required
def monthly_medical_script3s_detail(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script3s_list = monthly_medical_script3.objects.all()
        context = {"monthly_medical_script3s_list":monthly_medical_script3s_list}
        return render(request,"monthly_medical_script3s_detail.html", context)
@login_required
def monthly_medical_script3_detail(request,id=None):
    monthly_medical_script3_res = get_object_or_404(monthly_medical_script3,id=id)
    return render(request, "monthly_medical_script3-detail.html",{"monthly_medical_script3_res": monthly_medical_script3_res,})


@login_required
def monthly_medical_script3s_detail_V(request):

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
        monthly_medical_script3s_list = monthly_medical_script3.objects.all()
        context = {"monthly_medical_script3s_list":monthly_medical_script3s_list}
        return render(request,"monthly_medical_script3s_detail2.html", context)
@login_required
def monthly_medical_script3_remove_v(request,id=None):
    instance = get_object_or_404(monthly_medical_script3, id=id)
    instance.delete()
    t = request.META.get('HTTP_REFERER')
    if t.endswith("monthly_medical_script3_det/"):
       go='monthly_medical_script3s_detail'
    
    return render(request,"removed.html",{"go":go})

#&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$-----COST----$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
@login_required
def financial_main(request):
       context = {}
       return render(request,"Financial_medical_Cost_main.html", context)

@login_required
def financial_main1(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = medical_script1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main1.html", context)

@login_required
def financial_main11(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = mdeical_transform1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main11.html", context)
@login_required
def financial_main12(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = monthly_medical_script1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main12.html", context)
@login_required
def financial_main14(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = external_clinic_cure1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main14.html", context)

@login_required
def financial_main13(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = mdeical_script1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main13.html", context)
@login_required
def financial_main14(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = external_clinic_cure1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"Financial_medical_Cost_main14.html", context)









#=========================================================================       
@login_required
def add_medical_script1_cost_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    res1 = get_object_or_404(medical_script1,id=id)
    form0= add_medical_script1(request.POST or None,instance=res1)
    form1 = add_medical_script1_cost(request.POST or None,instance=res1)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        cst1 = form1.cleaned_data['medic1_cost'] 
        cst2 = form1.cleaned_data['medic2_cost'] 
        cst3 = form1.cleaned_data['medic3_cost'] 
        cst4 = form1.cleaned_data['medic4_cost'] 
        cst5 = form1.cleaned_data['medic5_cost'] 
        cst6 = form1.cleaned_data['medic6_cost'] 
        cst7 = form1.cleaned_data['medic7_cost'] 
        if cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 :
           instance1.total_medic_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and  cst7!=' ':
           instance1.total_medic_cost=cst1+cst2+cst3+cst4+cst5+cst6
        elif cst1 and cst2 and cst3 and cst4 and cst5  and cst6!=' ' and cst7!=' ' :
           instance1.total_medic_cost=cst1+cst2+cst3+cst4+cst5
        elif cst1 and cst2 and cst3 and cst4 and cst5!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' :
           instance1.total_medic_cost=cst1+cst2+cst3+cst4
        elif cst1 and cst2 and cst3 and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ':
           instance1.total_medic_cost=cst1+cst2+cst3
        elif cst1 and cst2 and cst3!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ':
           instance1.total_medic_cost=cst1+cst2
        elif cst1 and cst2!=' ' and cst3!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' :
           instance1.total_medic_cost=cst1        
#        instance1.total_medic_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7           
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    cdate = datetime.now()
    context={"form1":form1,"form0":form0,"cdate":cdate,"res1":res1}
    return render(request,"medical_script1_cost_update.html",context)

@login_required
def add_medical_transform1_cost_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    res1 = get_object_or_404(mdeical_transform1,id=id)
    form0= add_mdeical_transform1(request.POST or None,instance=res1)
    form1 = add_medical_transform1_cost(request.POST or None,instance=res1)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    cdate = datetime.now()
    context={"form1":form1,"form0":form0,"cdate":cdate,"res1":res1}
    return render(request,"medical_transform1_cost_update.html",context)    

@login_required
def add_monthly_medical_script1_cost_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    res1 = get_object_or_404(monthly_medical_script1,id=id)
    form0= add_monthly_medical_script1(request.POST or None,instance=res1)
    form1 = add_monthly_medic_cost1(request.POST or None,instance=res1)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        print(type(instance1.total_cost))
        cst1 = form1.cleaned_data['medic1_cost'] 
        cst2 = form1.cleaned_data['medic2_cost'] 
        cst3 = form1.cleaned_data['medic3_cost'] 
        cst4 = form1.cleaned_data['medic4_cost'] 
        cst5 = form1.cleaned_data['medic5_cost'] 
        cst6 = form1.cleaned_data['medic6_cost'] 
        cst7 = form1.cleaned_data['medic7_cost'] 
        cst8 = form1.cleaned_data['medic8_cost'] 
        cst9 = form1.cleaned_data['medic9_cost'] 
        cst10 = form1.cleaned_data['medic10_cost'] 
        cst11 = form1.cleaned_data['medic11_cost'] 
        cst12 = form1.cleaned_data['medic12_cost'] 
        cst13 = form1.cleaned_data['medic13_cost'] 
        cst14 = form1.cleaned_data['medic14_cost'] 
        cst15 = form1.cleaned_data['medic15_cost'] 
        cst16 = form1.cleaned_data['medic16_cost'] 
        cst17 = form1.cleaned_data['medic17_cost'] 
        cst18 = form1.cleaned_data['medic18_cost'] 
        cst19 = form1.cleaned_data['medic19_cost'] 
        cst20 = form1.cleaned_data['medic20_cost'] 
        
        if cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and cst16 and cst17 and cst18 and cst19 and  cst20:
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17+cst18+cst19+cst20
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and cst16 and cst17 and cst18 and cst19  and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17+cst18+cst19
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and cst16 and cst17 and cst18  and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17+cst18
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and cst16 and cst17  and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and cst16 and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15 and  cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14 and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12 and cst13 and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12   and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10 and cst11 and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9 and cst10  and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8 and cst9  and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8  and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and cst7 and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7
        elif cst1 and cst2 and cst3 and cst4 and cst5 and cst6 and  cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6
        elif cst1 and cst2 and cst3 and cst4 and cst5  and cst6!=' ' and cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' '   :
           instance1.total_cost=cst1+cst2+cst3+cst4+cst5
        elif cst1 and cst2 and cst3 and cst4 and cst5!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3+cst4
        elif cst1 and cst2 and cst3 and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2+cst3
        elif cst1 and cst2 and cst3!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1+cst2
        elif cst1 and cst2!=' ' and cst3!=' ' and cst4!=' ' and cst5!=' ' and cst6!=' ' and cst7!=' ' and cst8!=' ' and cst9!=' ' and cst10!=' ' and cst11!=' ' and cst12!=' ' and cst13!=' ' and cst14!=' ' and cst15!=' ' and cst16!=' ' and cst17!=' ' and cst18!=' ' and cst19!=' ' and cst20!=' ' :
           instance1.total_cost=cst1
        # else:
        #    instance1.total_cost=0.000 s
        # champer= Decimal(0.000)
        #instance1.total_cost=instance1.medic1_cost+instance1.medic2_cost+instance1.medic3_cost+instance1.medic4_cost+instance1.medic5_cost+instance1.medic6_cost+instance1.medic7_cost+instance1.medic8_cost+instance1.medic9_cost+instance1.medic10_cost+instance1.medic11_cost+instance1.medic12_cost+instance1.medic13_cost+instance1.medic14_cost+instance1.medic15_cost+instance1.medic16_cost+instance1.medic17_cost+instance1.medic18_cost+instance1.medic19_cost+instance1.medic20_cost           
        # instance1.total_cost=Decimal(0.000)
  #      instance1.total_cost=cst1+cst2+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17+cst18+cst19+cst20+cst3+cst4+cst5+cst6+cst7+cst8+cst9+cst10+cst11+cst12+cst13+cst14+cst15+cst16+cst17+cst18+cst19+cst20)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
        return HttpResponseRedirect(reverse('law_add_success'))
    cdate = datetime.now()
    context={"form1":form1,"form0":form0,"cdate":cdate,"res1":res1}
    return render(request,"monthly_medical_script1_cost_update.html",context)

























































@login_required
def working_records_search(request):
       form4 = searching_frm((request.POST or None))

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name'] 
          res1 = working_pationt.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       retired_pationts_list = retired_pationt.objects.all()
       context = {"q":res1,"retired_pationts_list":retired_pationts_list,"f3":form4}
       return render(request,"working_records_search.html", context)
@login_required
def working_report(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    res1 = get_object_or_404(working_pationt,id=id)
    form0= add_medical_script1(request.POST or None,instance=res1)
    form1 = add_medical_script1_cost(request.POST or None,instance=res1)
    title1 = ""
    emp_code = res1.medical_number

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False
    print(id)

    print(emp_code)
    cdate = datetime.now()
    context={"form1":form1,"form0":form0,"cdate":cdate,"emp_code":emp_code}
    return render(request,"working_report.html",context)





@login_required
def medical_script_report1(request,id=None):
    med1_report = get_object_or_404(medical_script1,id=id)
    return render(request, "medical_script_report1.html",{"med1_report": med1_report,})




























def getmidicineprice(request):
    username = request.GET.get("username", None)
    data = serializers.serialize('json', users.objects.filter(user_name__icontains=username).only("user_code"), fields=('user_code',))
    return JsonResponse(data[45:67],safe=False)

@login_required
def medical_record_main(request):
    context={}
    return render(request,"medical_record_main.html", context)

@login_required
def add_new_monthly_script1_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script1_res = get_object_or_404(monthly_medical_script1,id=id)
    form1 = add_monthly_medical_script1(request.POST or None,instance=monthly_medical_script1_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False
    
    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        if instance1.Added== True:
           return HttpResponseRedirect(reverse('addition_Forbidden')) 
        instance1.id=None
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.Added = True
        instance1.master = False
        instance1.paper_code=str(uuid.uuid4())
        
        instance1.save()
        return HttpResponseRedirect(reverse('add_new_monthly_script1_v',kwargs={"id":instance1.id})) 

    #print_status=instance1.added
     #   return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate,"monthly_medical_script1_res":monthly_medical_script1_res}
    return render(request,"add_new_monthly_script1_v.html",context)   
@login_required
def addition_Forbidden(request):
    return render(request, "addition_Forbidden.html", {})
@login_required
def monthlyscript_working_search(request):
       form4 = searching_frm((request.POST or None))

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name'] 
          res1 = monthly_medical_script1.objects.filter(patient_name__icontains = employee_name,master=True).order_by('-timestamp')#.latest('timestamp')
       else:
           res1=""
       retired_pationts_list = retired_pationt.objects.all()
       context = {"q":res1,"retired_pationts_list":retired_pationts_list,"f3":form4}
       return render(request,"monthlyscript_working_search.html", context)
#--------------------------------------------------------------
@login_required
def add_new_monthly_script2_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script1_res = get_object_or_404(monthly_medical_script2,id=id)
    form1 = add_monthly_medical_script2(request.POST or None,instance=monthly_medical_script1_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.id=None
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate,"monthly_medical_script1_res":monthly_medical_script1_res}
    return render(request,"add_new_monthly_script2_v.html",context)   
 
@login_required
def monthlyscript_retired_search(request):
       form4 = searching_frm((request.POST or None))

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name'] 
          res1 = monthly_medical_script2.objects.filter(patient_name__icontains = employee_name).order_by('-timestamp')#.latest('timestamp')
       else:
           res1=""
       retired_pationts_list = retired_pationt.objects.all()
       context = {"q":res1,"retired_pationts_list":retired_pationts_list,"f3":form4}
       return render(request,"monthlyscript_retired_search.html", context)
#------------------------------------------------------------------------------
@login_required
def add_new_monthly_script3_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    monthly_medical_script1_res = get_object_or_404(monthly_medical_script3,id=id)
    form1 = add_monthly_medical_script3(request.POST or None,instance=monthly_medical_script1_res)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.id=None
        instance1.updated = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return HttpResponseRedirect(reverse('update_success'))
    cdate = datetime.now()
    context={"form1":form1,"cdate":cdate,"monthly_medical_script1_res":monthly_medical_script1_res}
    return render(request,"add_new_monthly_script3_v.html",context)   
 
@login_required
def monthlyscript_member_search(request):
       form4 = searching_frm((request.POST or None))

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name'] 
          res1 = monthly_medical_script3.objects.filter(patient_name__icontains = employee_name).order_by('-timestamp')#.latest('timestamp')
       else:
           res1=""
       retired_pationts_list = retired_pationt.objects.all()
       context = {"q":res1,"retired_pationts_list":retired_pationts_list,"f3":form4}
       return render(request,"monthlyscript_member_search.html", context)


@login_required
def trans_search_toprint(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = mdeical_transform1.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"trans_search_toprint.html", context)       

@login_required
def trans_search_toprint2(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = mdeical_transform2.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"trans_search_toprint2.html", context)       
@login_required
def trans_search_toprint3(request):
       form4 = searching_frm((request.POST or None))
       qs = working_pationt.objects.all()
       qslen=working_pationt.objects.all().count()
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name']           
          res1 = mdeical_transform3.objects.filter(patient_name__icontains = employee_name)
       else:
           res1=""
       context = {"q":res1,"f3":form4,"qs":qs,"qslen":qslen}
       return render(request,"trans_search_toprint3.html", context)              
@login_required
def trans1_forprint(request,id=None):
    med1_report = get_object_or_404(mdeical_transform1,id=id)
    return render(request, "trans1_forprint.html",{"med1_report": med1_report,})
@login_required
def trans1_forprint2(request,id=None):
    med1_report = get_object_or_404(mdeical_transform2,id=id)
    return render(request, "trans1_forprint2.html",{"med1_report": med1_report,})
@login_required
def trans1_forprint3(request,id=None):
    med1_report = get_object_or_404(mdeical_transform3,id=id)
    return render(request, "trans1_forprint3.html",{"med1_report": med1_report,})  

#==========================================rep=======================================
#@login_required
def monthlyscript_member_search(request):
       form4 = searching_frm1((request.POST or None))

        # if request.user.id == 1:
        #    computers_list = asset_pc.objects.all().order_by('bransh')
        # else:
        #    computers_list = asset_pc.objects.all().filter(publisher=request.user)
       if form4.is_valid() :
          employee_name = form4.cleaned_data['employee_name'] 
          res1 = monthly_medical_script3.objects.filter(patient_name__icontains = employee_name).order_by('-timestamp')#.latest('timestamp')
       else:
           res1=""
       retired_pationts_list = retired_pationt.objects.all()

       context = {"q":res1,"retired_pationts_list":retired_pationts_list,"f3":form4}
       return render(request,"monthlyscript_member_search.html", context)          

#================================================================================================================================================================
# ======================================================================EXTERNAL=========================================================================================
@login_required
def add_external_clinic_cure1_v(request):
    form = add_external_clinic_cure1((request.POST or None))
    title1 = ""
    ipaddr = request.META.get('REMOTE_ADDR')
    src = ipaddr
    print(src)
    if form.is_valid():
        request.session['form-submitted'] = True
        instance1 = form.save(commit=False)
        instance1.ip = request.META['REMOTE_ADDR']
        instance1.timestamp = datetime.now()
        instance1.publisher = request.user
        instance1.save()
        return  HttpResponseRedirect(reverse('success'))
    q = external_clinic_cure1.objects.filter(publisher=request.user).order_by('-timestamp')    
    context = {"form1_title": title1, "form": form,"source":src,"q":q}
    return render(request, "add_external_clinic_cure1.html", context)

@login_required
def external_clinic_cure_report1(request,id=None):
    med1_report = get_object_or_404(external_clinic_cure1,id=id)
    return render(request, "external_clinic_cure_report1.html",{"med1_report": med1_report,})















@login_required
def add_cost_external_clinic_cure1_v(request,id=None):
    # if not has_group(request.user, "law"):
    #    return HttpResponseRedirect(reverse('restlaw'))
    res1 = get_object_or_404(external_clinic_cure1,id=id)
    form0= add_external_clinic_cure1(request.POST or None,instance=res1)
    form1 = add_cost_external_clinic_cure1(request.POST or None,instance=res1)
    title1 = ""

    # if form1.cleaned_data['cplace'] == 'چهه اخرى' :
    #    junk_parts.pstatus = False

    if form1.is_valid():
        request.session['form-submitted'] = True
        instance1 = form1.save(commit=False)
        instance1.updated = datetime.now()
        instance1.updater = str(request.user)
        instance1.save()
        return HttpResponseRedirect(reverse('law_add_success'))
        
    cdate = datetime.now()
    context={"form1":form1,"form0":form0,"cdate":cdate,"res1":res1}
    return render(request,"add_cost_external_clinic_cure1_v.html",context)


    