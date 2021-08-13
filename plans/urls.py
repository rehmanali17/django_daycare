from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('contact', views.contact, name = 'contact'),
    path('user/plans', views.plans, name = 'plans'),
    path('user/delete_plan', views.deletePlan, name = 'deletePlan'),
    path('user/update_profile', views.updateProfile, name = 'updateProfile'),
    path('user/buy_plan/<int:id>', views.buyPlan, name = 'buyPlan'),
    path('user/planBought', views.planBought, name = 'planBought'),
    path('view_plan/<int:id>/<str:time>', views.plan, name = 'plan'),
    path('user/logout', views.logout, name = 'logout')
]

