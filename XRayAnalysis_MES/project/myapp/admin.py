from django.contrib import admin
from .models import user_login,category_master,user_details,pic_pool,staff_master,user_pic,user_test_master
# Register your models here.
admin.site.register(user_login)
admin.site.register(category_master)
admin.site.register(user_details)
admin.site.register(pic_pool)
admin.site.register(staff_master)
admin.site.register(user_pic)
admin.site.register(user_test_master)
