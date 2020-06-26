# Generated by Django 3.0.4 on 2020-03-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150)),
                ('category_descp', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='pic_pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_master_id', models.IntegerField()),
                ('pic_path', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='staff_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('desg', models.CharField(max_length=150)),
                ('addr', models.CharField(max_length=1500)),
                ('pin', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=1500)),
                ('pin', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('pic_path', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_test_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('staff_user_id', models.IntegerField()),
                ('pic_path', models.CharField(max_length=500)),
                ('remarks', models.CharField(max_length=1500)),
                ('result', models.CharField(max_length=500)),
                ('dt', models.CharField(max_length=50)),
                ('tm', models.CharField(max_length=50)),
            ],
        ),
    ]