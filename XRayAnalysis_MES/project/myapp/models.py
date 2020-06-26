from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=50)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    addr = models.CharField(max_length=1500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class category_master(models.Model):
    category_name = models.CharField(max_length=150)
    category_descp = models.CharField(max_length=1500)

    def __str__(self):
        return self.category_name

class pic_pool(models.Model):
    category_master_id = models.IntegerField()
    pic_path = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

    def __str__(self):
        return self.pic_path

class user_test_master(models.Model):
    user_id = models.IntegerField()
    staff_user_id = models.IntegerField()
    pic_path = models.CharField(max_length=500)
    remarks = models.CharField(max_length=1500)
    result = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

    def __str__(self):
        return self.pic_path

class staff_master(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    desg = models.CharField(max_length=150)
    addr = models.CharField(max_length=1500)
    pin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class user_pic(models.Model):
    user_id = models.IntegerField()
    pic_path = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

    def __str__(self):
        return self.pic_path
