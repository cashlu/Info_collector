from django.contrib import admin
from django.contrib.auth.models import User

from .models import Report, Picture, SecurityDetail, GroundsillDetail, \
    TiltDetail, UponDetail, FenceDetail, City, Town, Village, Advice, Reviewer


class PictureAdmin(admin.StackedInline):
    model = Picture


@admin.register(Report)
class InfoAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Report._meta.get_fields()]
    list_display = (
        'name', 'identity', 'decade', 'purpose', 'assess_level', 'reviewer',
        'appraiser',)

    fieldsets = (
        ('基本信息',
         {'fields': [
             ('name', 'identity'),
             ('decade', 'purpose'),
             ('city', 'town', 'village'),
             'comment',
         ]}),
        ('结构形式',
         {'fields': ['structure']}),
        ('结构组成部分检查结果', {'fields': [
            ('security', 'security_detail'),
            ('groundsill', 'groundsill_detail'),
            ('tilt', 'tilt_detail'),
            ('upon', 'upon_detail'),
            ('fence', 'fence_detail')
        ]}),
        ('房屋综合评定', {'fields': [
            'assess_level',
            'advice'
        ]}),
        ('表尾', {'fields': [
            ('street_contract', 'street_contract_phone'),
            ('village_contract', 'village_contract_phone'),
            ('reviewer',)
        ]})
    )
    inlines = (PictureAdmin,)

    search_fields = ('name', 'identity', 'comment',)  # advice__advice
    list_filter = (
        'structure', 'security', 'groundsill', 'tilt', 'upon', 'fence',
        'assess_level')

    # filter_horizontal = (
    #     'security_detail', 'groundsill_detail', 'tilt_detail', 'upon_detail',
    #     'fence_detail', 'advice')

    def save_model(self, request, obj, form, change):
        obj.appraiser = request.user
        obj.save()


# @admin.register(Picture)
# class PictureAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Picture._meta.get_fields()]


@admin.register(SecurityDetail)
class SecurityDetailAdmin(admin.ModelAdmin):
    list_display = ('detail',)


@admin.register(GroundsillDetail)
class GroundsillDetailAdmin(admin.ModelAdmin):
    list_display = ('detail',)


@admin.register(TiltDetail)
class TiltDetailAdmin(admin.ModelAdmin):
    list_display = ('detail',)


@admin.register(UponDetail)
class UponDetailAdmin(admin.ModelAdmin):
    list_display = ('detail',)


@admin.register(FenceDetail)
class FenceDetailAdmin(admin.ModelAdmin):
    list_display = ('detail',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    list_display = ('advice',)


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('name',)
