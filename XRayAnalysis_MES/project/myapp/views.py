from django.shortcuts import render
from .models import user_login,category_master,user_details,pic_pool,staff_master,user_pic,user_test_master
from django.db.models import Max
from django.core.files.storage import FileSystemStorage
from .algo_impl import orb_compute,selfile
import os

# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request,'./myapp/about.html')

def contact(request):
    return render(request,'./myapp/contact.html')

def admin_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd)

        if len(ul) == 1:
            request.session['user_id'] = ul[0].uname
            context = {'uname': request.session['user_id']}
            return render(request, 'myapp/admin_home.html',
                          context)
        else:
            return render(request, 'myapp/admin_login.html')
    else:
        return render(request, 'myapp/admin_login.html')

def admin_home(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_home.html',context)

def admin_settings(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings.html',context)

def admin_settings_404(request):

    context = {'uname':request.session['user_id']}
    return render(request,'./myapp/admin_settings_404.html',context)

def admin_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_id']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/admin_settings.html')
            else:
                return render(request, './myapp/admin_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/admin_changepassword.html')
    else:
        return render(request, './myapp/admin_changepassword.html')

def admin_category_master_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category_descp = request.POST.get('category_descp')

        cm = category_master(category_name=category_name,category_descp=category_descp)
        cm.save()
        return render(request, 'myapp/admin_category_master_add.html')

    else:
        return render(request, 'myapp/admin_category_master_add.html')

def admin_category_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = category_master.objects.get(id=int(id))
    nm.delete()

    nm_l = category_master.objects.all()
    context ={'category_list':nm_l}
    return render(request,'myapp/admin_category_master_view.html',context)

def admin_category_master_view(request):
    nm_l = category_master.objects.all()
    context = {'category_list': nm_l}
    return render(request, 'myapp/admin_category_master_view.html', context)

def admin_staff_master_add(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        desg = request.POST.get('desg')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname = email
        status = "new"

        ul = user_login(uname=uname, password=password, utype='staff')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        sm = staff_master(user_id=user_id, fname=fname, lname=lname, desg=desg, addr=addr, pin=pin, contact=contact,
                          status=status, email=email)
        sm.save()

        return render(request, 'myapp/admin_staff_master_add.html')

    else:
        return render(request, 'myapp/admin_staff_master_add.html')

def admin_staff_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    nm = staff_master.objects.get(id=int(id))
    nm.delete()

    nm_l = staff_master.objects.all()
    context ={'staff_list':nm_l}
    return render(request,'myapp/admin_staff_master_view.html',context)

def admin_staff_master_view(request):
    nm_l = staff_master.objects.all()
    context = {'staff_list': nm_l}
    return render(request, 'myapp/admin_staff_master_view.html', context)

def admin_pic_pool_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(uploaded_file.name, uploaded_file)
        category_master_id = int(request.POST.get('category_master_id'))
        dt = datetime.today().strftime('%Y-%m-%d')

        tm = datetime.today().strftime('%H:%M:%S')
        pic_obj = pic_pool(pic_path=pic_path,category_master_id=category_master_id,dt=dt,tm=tm)
        pic_obj.save()
        category_list = category_master.objects.all()
        context = {'category_list': category_list }
        return render(request, 'myapp/admin_pic_pool_add.html',context)
    else:
        category_list = category_master.objects.all()
        context = {'category_list': category_list}
        return render(request, 'myapp/admin_pic_pool_add.html',context)


def admin_pic_pool_delete(request):
    id = request.GET.get('id')
    print("id="+id)
    lm = pic_pool.objects.get(id=int(id))
    lm.delete()
    pp_l = pic_pool.objects.all()
    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name
    context = {'pic_list':pp_l,'category_list':cmd}
    return render(request,'myapp/admin_pic_pool_view.html',context)

def admin_pic_pool_view(request):
    pp_l = pic_pool.objects.all()
    cm_l = category_master.objects.all()
    cmd = {}
    for nm in cm_l:
        cmd[nm.id] = nm.category_name
    context = {'pic_list': pp_l,  'category_list': cmd}
    return render(request, 'myapp/admin_pic_pool_view.html', context)

def admin_user_test_master_view(request):
    pp_l = user_test_master.objects.all()
    ud_l = user_details.objects.all()
    cmd = {}
    for nm in ud_l:
        cmd[nm.user_id] = f'{nm.fname} {nm.lname}'
    context = {'test_list': pp_l, 'user_list': cmd}
    return render(request, 'myapp/admin_user_test_master_view.html', context)
########staff###########
def staff_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='staff')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/staff_home.html',context)
        else:
            return render(request, 'myapp/staff_login.html')
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)
from datetime import datetime
def staff_user_test_master_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()

        pic_path = fs.save(randomString(10)+uploaded_file.name, uploaded_file)
        print(pic_path)

        pic_list = pic_pool.objects.all()
        cnt = 0
        cnt1= 0
        selfile=''
        selcat=0
        for pic in pic_list:
            file1 = f'./myapp/static/myapp/media/{pic.pic_path}'
            file2 = f'./myapp/static/myapp/media/{pic_path}'
            cnt1 = orb_compute(file1,file2,cnt)
            if cnt1 >= cnt:
                selfile=file1
                selcat=pic.category_master_id
            	cnt = cnt1
            print(f"{file1},{file2},{cnt}")

        print(selfile)
        print(selcat)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        remarks = request.POST.get('remarks')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname = email
        status = "new"
        ul = user_login.objects.filter(uname=uname, password=password, utype='user')
        print(len(ul))
        if len(ul) == 1:
            user_id = ul[0].id
        else:
            ul = user_login(uname=uname, password=password, utype='user')
            ul.save()
            user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

            ud = user_details(user_id=user_id, fname=fname, lname=lname, dob=dob,gender=gender, addr=addr, pin=pin, contact=contact,
                          status=status, email=email)
            ud.save()

        cm = category_master.objects.get(id=int(selcat))

        staff_user_id = int(request.session['user_id'])
        result = cm.category_name
        dt = datetime.today().strftime('%Y-%m-%d')

        tm = datetime.today().strftime('%H:%M:%S')


        utm = user_test_master(user_id=user_id, pic_path=pic_path, result=result, dt=dt, tm=tm,
                               remarks=remarks,staff_user_id=staff_user_id)
        utm.save()

        context = {'category_name': cm.category_name}
        return render(request, 'myapp/staff_user_test_result.html',context)
    else:
        context = {}

        return render(request, 'myapp/staff_user_test_master_add.html',context)

def staff_user_test_master_view(request):
    pp_l = user_test_master.objects.all()
    ud_l = user_details.objects.all()
    cmd = {}
    for nm in ud_l:
        cmd[nm.user_id] = f'{nm.fname} {nm.lname}'
    context = {'test_list': pp_l, 'user_list': cmd}
    return render(request, 'myapp/staff_user_test_master_view.html', context)

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/staff_settings.html')
            else:
                return render(request, './myapp/staff_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/staff_changepassword.html')
    else:
        return render(request, './myapp/staff_changepassword.html')

def staff_settings(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_settings.html',context)


###########################################
def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, password=passwd,utype='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            context = {'uname': request.session['user_name']}
            return render(request, 'myapp/user_home.html',context)
        else:
            return render(request, 'myapp/user_login.html')
    else:
        return render(request, 'myapp/user_login.html')

def user_home(request):
    context = {'uname': request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)

def user_test_master_view(request):
    user_id=int(request.session['user_id'])
    pp_l = user_test_master.objects.filter(user_id=user_id)
    ud_l = user_details.objects.all()
    cmd = {}
    for nm in ud_l:
        cmd[nm.user_id] = f'{nm.fname} {nm.lname}'
    context = {'test_list': pp_l, 'user_list': cmd}
    return render(request, 'myapp/user_test_master_view.html', context)

def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                return render(request, './myapp/user_settings.html')
            else:
                return render(request, './myapp/user_settings.html')
        except user_login.DoesNotExist:
            return render(request, './myapp/user_changepassword.html')
    else:
        return render(request, './myapp/user_changepassword.html')

def user_settings(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_settings.html',context)

###########################################
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


