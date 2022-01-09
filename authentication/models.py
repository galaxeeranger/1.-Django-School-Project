from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()



# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length = 50)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    describe = models.TextField(default = 'Image Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# #Creating Django Signals

# # It's like trigger in database. It will run only when Data is Added in CustomUser model

# @receiver(post_save, sender=CustomUser)
# # Now Creating a Function which will automatically insert data in HOD, Staff or Student
# def create_user_profile(sender, instance, created, **kwargs):
#     # if Created is true (Means Data Inserted)
#     if created:
#         # Check the user_type and insert the data in respective tables
#         if instance.user_type == 1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type == 2:
#             Staffs.objects.create(admin=instance)
#         if instance.user_type == 3:
#             Students.objects.create(admin=instance, image_id=Images.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 1:
#         instance.adminhod.save()
#     if instance.user_type == 2:
#         instance.staffs.save()
#     if instance.user_type == 3:
#         instance.students.save()