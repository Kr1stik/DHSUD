from django.contrib import admin
from .models import HoaProfile, NoticeOfViolation, OrderToPerform, OrderForInvestigation

# We use @admin.register to customize how the tables look in the admin panel
@admin.register(HoaProfile)
class HoaProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_municipality', 'status', 'total_members')
    list_filter = ('status', 'city_municipality')
    search_fields = ('name', 'contact_person')

@admin.register(NoticeOfViolation)
class NoticeOfViolationAdmin(admin.ModelAdmin):
    list_display = ('control_no', 'hoa', 'date_issued', 'evaluator')
    search_fields = ('control_no', 'hoa__name')

@admin.register(OrderToPerform)
class OrderToPerformAdmin(admin.ModelAdmin):
    list_display = ('control_no', 'hoa', 'date_issued', 'mr_status')

@admin.register(OrderForInvestigation)
class OrderForInvestigationAdmin(admin.ModelAdmin):
    list_display = ('control_no', 'hoa', 'penalties', 'date_issued')
    list_filter = ('penalties',)