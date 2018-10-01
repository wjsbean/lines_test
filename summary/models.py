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
    line_name = models.ForeignKey(Info_TestLines, on_delete=models.CASCADE)
    #line_period = models.PositiveIntegerField(verbose_name="生育期", default=0)
    pod_high = models.DecimalField(verbose_name="低荚高", max_digits=2, decimal_places=2, default=0.0)
    weight_HGrain = models.DecimalField(verbose_name="百粒重", max_digits=2, decimal_places=2, default=0.0)
    rate_PurpleSpot = models.DecimalField(verbose_name="紫斑率", max_digits=2, decimal_places=2, default=0.0)
    rate_BrownSpot = models.DecimalField(verbose_name="褐斑率", max_digits=2, decimal_places=2, default=0.0)
    rate_Insect = models.DecimalField(verbose_name="虫食率", max_digits=2, decimal_places=2, default=0.0)
    rate_others = models.DecimalField(verbose_name="其他粒率", max_digits=2, decimal_places=2, default=0.0)
    remarks = models.TextField(verbose_name="备注")


class Info_FieldCharacter(models.Model):
    # information for field characters
    shape = (
        ('圆叶', '圆叶'),
        ('卵圆', '卵圆'),
        ('椭圆', '椭圆'),
        ('披针形', '披针形'),
    )
    fcolor = (
        ('白花', '白花'),
        ('紫花', '紫花'),
    )
    hcolor = (
        ('灰色', '灰色'),
        ('灰色', '灰色'),
    )
    habit = (
        ('有限', '有限'),
        ('亚有限', '亚有限'),
        ('无限', '无限'),
    )
    architecture = (
        ('收敛' , '收敛'),
        ('开张', '开张'),
        ('半开张', '半开张'),
    )
    pod = (
        ('不裂', '不裂'),
        ('中裂', '中裂'),
        ('易裂', '易裂'),
    )
    deci = (
        ('落叶', '落叶'),
        ('半落', '半落'),
        ('不落', '不落'),
    )
    lodg = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    SMV = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    line_name = models.ForeignKey(Info_TestLines, on_delete=models.CASCADE)
    seeding_date = models.DateField(verbose_name='播种期')
    seeding_state = models.DateField(verbose_name='出苗期')
    flowering_period = models.DateField(verbose_name="开花期")
    mature_period = models.DateField(verbose_name="成熟期")
    harvest_period = models.DateField(verbose_name="收获期")
    No_GrowDays = models.PositiveIntegerField("生育日数")
    leaf_shape = models.CharField(verbose_name="叶形", max_length=5, choices=shape)
    flower_color = models.CharField(verbose_name="花色", max_length=5, choices=fcolor)
    hairy_color = models.CharField(verbose_name="茸毛色", max_length=5, choices=hcolor)
    pod_BearHabit = models.CharField(verbose_name="结荚习性", max_length=8, choices=habit)
    plant_architecture = models.CharField(verbose_name="株型", max_length=8, choices=architecture)
    pod_dehiscence = models.CharField(verbose_name="裂荚性", max_length=5, choices=pod)
    deciduous = models.CharField(verbose_name="落叶性", max_length=5, choices=deci)
    lodging = models.CharField(verbose_name="倒伏性", max_length=2, choices=lodg)
    root_rot = models.CharField(verbose_name="根腐病", max_length=5)
    smv = models.CharField(verbose_name="花叶病", max_length=5, choices=SMV)
    in_green = models.DecimalField(verbose_name="症青", max_digits=2, decimal_places=2, default=0.0)
    virus_other = models.CharField(verbose_name="其他病毒病", max_length=50)


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