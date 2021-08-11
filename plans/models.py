from django.db import models

# Create your models here.

# class User(models.Model):
#     email = models.CharField(max_length=70)
#     password = models.CharField(max_length=70)
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=70)
#     phone = models.CharField(max_length=12)
    
#     def __str__(self):
#         return self.email

# class Plan(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=70)
#     duration = models.CharField(max_length=30)
#     trial = models.CharField(max_length=30)
#     time_duration = models.CharField(max_length=30)
#     price = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.title
    
# class Plans_Bought(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
#     time = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.user  + ': ' + self.plan


class Messages(models.Model):
    m_email = models.CharField(max_length=100, blank=True, null=True)
    m_phone = models.TextField(blank=True, null=True)
    m_address = models.TextField(blank=True, null=True)
    m_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'
        
    def __str__(self):
            return self.m_message


class Plan(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    trial = models.CharField(max_length=100, blank=True, null=True)
    time_duration = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan'
    
    def __str__(self):
            return self.title


class PlansBought(models.Model):
    p = models.ForeignKey(Plan, models.DO_NOTHING, blank=True, null=True)
    u_email = models.ForeignKey('Users', models.DO_NOTHING, db_column='u_email', blank=True, null=True)
    p_time = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans_bought'
    


class Users(models.Model):
    u_email = models.CharField(primary_key=True, max_length=100)
    u_password = models.TextField(blank=True, null=True)
    u_name = models.TextField(blank=True, null=True)
    u_address = models.TextField(blank=True, null=True)
    u_phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        
    def __str__(self):
            return self.u_name
    
    