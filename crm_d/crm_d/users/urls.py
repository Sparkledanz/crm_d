from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
     path("travel/",views.Travelview,name="travel"),
     path("auth/",views.Auth,name="auth"),
     path("home/",views.home,name="home"),
     path("employee/",views.Employeeview,name="employee"),
     path("employer/",views.Employerview,name="employer"),
     path("partner/",views.Partnerview,name="partner"),
     path("settlement/",views.Settlementview,name="settlement"),
     path("documents/",views.Documentview,name="documents"),
     path('logout/', auth_views.LogoutView.as_view(next_page='auth'), name='logout'),
     path('notification/', views.notification_page, name='notification'),
     path('profile/<str:username>/', views.partner_profile, name='profile'),
     #path('message/<str:username>/', views.send_message, name='message'),
     path("search/",views.search,name="search"),
     path('update/<int:partner_id>/', views.update_partner, name='update_partner'),
     path('delete/<int:partner_id>/', views.delete_partner, name='delete_partner'),
    path('update<int:settlement_id>/',views.update_settlement,name='update_settlement'),
    path('delete<int:settlement_id>/',views.delete_settlement,name='delete_settlement'),
    path('update/<int:employer_id>/', views.update_employer, name='update_employer'),
    path('delete/<int:employer_id>/', views.delete_employer, name='delete_employer'),
    path('update/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
   path('message/<str:username>/', views.send_message, name='message'),

]
