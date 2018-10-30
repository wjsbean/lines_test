from django.contrib import admin
from .models import Info_TestLines, Info_Experiment, Info_ExperiLocation, Info_EcoCharacter
from .models import Info_FieldCharacter, Info_Yield, PurposeRequirement, Criteria_Character

# Register your models here.

class Info_ExperiLocationAdmin(admin.ModelAdmin):
    list_display = ('test_unit', 'testPoint_name', 'testPoint_loc', 'testLoc_longitude',
                    'testLoc_latitude', 'testLoc_altitude', 'address', 'contacts',
                    'contact_num', 'contact_email')
    ordering = ('test_unit',)

    list_filter = ('test_unit', 'testPoint_loc', 'contacts')
    search_fields = ('test_unit', 'contacts')


class Info_TestLinesAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'line_institute', 'line_owner', 'line_contactor', 'line_type',
                    'line_parents', 'line_target_date', 'line_phone', 'line_email')
    ordering = ('line_name',)

    list_filter = ('line_name', 'line_institute', 'line_owner', 'line_type', 'line_parents')
    search_fields = ('line_name', 'line_owner')


class PurposeRequirementAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'test_group', 'test_purpose', 'test_request')
    ordering = ('test_name',)

    list_filter = ('test_name', 'test_group')
    search_fields = ('test_name', 'test_group')


class Info_ExperimentAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'test_group', 'test_name', 'test_unit')
    ordering = ('line_name', 'test_group')


class Info_EcoCharacterAdmin(admin.ModelAdmin):
    list_display = ('info_testLines', 'line_name', 'pod_high', 'weight_HGrain',
                    'rate_PurpleSpot', 'rate_BrownSpot', 'rate_Insect',
                    'rate_others', 'remarks')
    ordering = ('info_testLines',)


class Info_FieldCharacterAdmin(admin.ModelAdmin):
    list_display = ('info_testLines', 'line_name', 'seeding_date', 'seeding_state',
                    'flowering_period', 'mature_period', 'harvest_period',
                    'No_GrowDays', 'leaf_shape', 'flower_color', 'hairy_color',
                    'pod_BearHabit', 'plant_architecture', 'pod_dehiscence',
                    'deciduous', 'lodging', 'root_rot', 'smv', 'in_green',
                    'virus_other')
    ordering = ('info_testLines',)


class Criteria_CharacterAdmin(admin.ModelAdmin):
    list_display = ('line_trait', 'criteria_record')
    ordering = ('line_trait',)


class Info_YieldAdmin(admin.ModelAdmin):
    list_display = ('info_testLines', 'test_name', 'line_name',
                    'test_rep1', 'test_rep2', 'test_rep3', 'avg_yield')
    ordering = ('info_testLines',)


admin.site.register(Info_ExperiLocation, Info_ExperiLocationAdmin)
admin.site.register(Info_TestLines, Info_TestLinesAdmin)
admin.site.register(PurposeRequirement, PurposeRequirementAdmin)
admin.site.register(Info_Experiment, Info_ExperimentAdmin)
admin.site.register(Info_EcoCharacter, Info_EcoCharacterAdmin)
admin.site.register(Info_FieldCharacter, Info_FieldCharacterAdmin)
admin.site.register(Criteria_Character, Criteria_CharacterAdmin)
admin.site.register(Info_Yield, Info_YieldAdmin)
