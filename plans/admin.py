from django.contrib import admin
# from .models import User,Plan,Plans_Bought
from .models import Messages, Plan, PlansBought, Users
# Register your models here.

# admin.site.register(User)
# admin.site.register(Plan)
# admin.site.register(Plans_Bought)

admin.site.register(Messages)
admin.site.register(Plan)
admin.site.register(PlansBought)
admin.site.register(Users)