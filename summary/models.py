from django.db import models

# Create your models here.
class Info_TestLines(models.Model):
    # information for each lines tested
    line_name = models.CharField(verbose_name="品系名称", max_length=50)
    line_institute = models.CharField(verbose_name="选育单位", max_length=50)
    line_owner = models.CharField(verbose_name="选育人", max_length=10)
    line_contactor = models.CharField(verbose_name="联系人", max_length=10)
    line_type = models.CharField(verbose_name="品种类型", max_length=10)
    line_parents = models.CharField(verbose_name="亲本组合", max_length=50)
    line_target_date = models.DateField(verbose_name="育成日期")
    line_phone = models.CharField(verbose_name="联系电话", max_length=15)
    line_Email = models.EmailField(verbose_name="联系邮箱")
    exp_name = models.CharField(verbose_name="试验名称", max_length=20)
    exp_group = models.CharField(verbose_name="试验组别", max_length=20)


class Info_EcoCharacter(models.Model):
    # information for economic characters
    line_name = models.CharField(verbose_name="品种名称", max_length=50)


class Info_FieldCharacter(models.Model):
    # information for field characters
    pass


class Info_ExperiLocation(models.Model):
    pass


class Info_Experiment(models.Model):
    pass


class Criteria_Character(models.Model):
    pass


class PurposeRequirement(models.Model):
    pass


class Info_Yield(models.Model):
    pass