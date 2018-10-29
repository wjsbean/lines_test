from django.db import models

# Create your models here.

class Info_ExperiLocation(models.Model):  #承试点信息
    test_unit = models.CharField(verbose_name="承试单位", max_length=40)
    testPoint_name = models.CharField(verbose_name="试点名称", max_length=40)
    testPoint_loc = models.CharField(verbose_name="所在地", max_length=20)
    testLoc_longitude = models.CharField(verbose_name="经度", max_length=10)
    testLoc_latitude = models.CharField(verbose_name="纬度", max_length=10)
    testLoc_altitude = models.CharField(verbose_name="海拔", max_length=10)
    address = models.TextField(verbose_name="通讯地址")
    contacts = models.CharField(verbose_name="联系人", max_length=10)
    contact_num = models.CharField(verbose_name="联系电话", max_length=15)
    contact_email = models.EmailField(verbose_name="电子邮箱")

    def __str__(self):
        return self.test_unit


class Info_TestLines(models.Model):  #参试品种
    # information for each lines tested
    line_name = models.CharField(verbose_name="品系名称", max_length=50)
    line_institute = models.CharField(verbose_name="选育单位", max_length=50)
    line_owner = models.CharField(verbose_name="选育人", max_length=10)
    line_contactor = models.CharField(verbose_name="联系人", max_length=10)
    line_type = models.CharField(verbose_name="品种类型", max_length=10)
    line_parents = models.CharField(verbose_name="亲本组合", max_length=50)
    line_target_date = models.DateField(verbose_name="育成日期")
    line_phone = models.CharField(verbose_name="联系电话", max_length=15)
    line_email = models.EmailField(verbose_name="联系邮箱")

    def __str__(self):
        return self.line_name


class PurposeRequirement(models.Model):  #试验目的
    test_name = models.CharField(verbose_name="试验名称", max_length=40)
    test_group = models.CharField(verbose_name="试验组别", max_length=20)
    test_purpose = models.TextField(verbose_name="试验目的")
    test_request = models.TextField(verbose_name="试验要求")

    def __str__(self):
        return self.test_name


class Info_Experiment(models.Model):  #试验信息表
    line_name = models.ForeignKey(Info_TestLines, verbose_name="参试品系", on_delete=models.CASCADE)
    test_group = models.ForeignKey(PurposeRequirement, verbose_name="试验组别", on_delete=models.CASCADE)
    test_name = models.CharField(verbose_name="试验名称", max_length=40)
    test_unit = models.ForeignKey(Info_ExperiLocation, verbose_name="承试单位", on_delete=models.CASCADE)
    #test_name = models.CharField(verbose_name="试验名称", max_length=40)
    #test_group = models.CharField(verbose_name="试验组别", max_length=20)
    #line_name = models.CharField(verbose_name="品系名称", max_length=50)
    #test_unit = models.CharField(verbose_name="承试单位", max_length=40)

    def __str__(self):
       return self.test_name


class Info_EcoCharacter(models.Model):  #经济性状
    # information for economic characters
    info_testLines = models.ForeignKey(Info_TestLines, on_delete=models.CASCADE)
    #line_period = models.PositiveIntegerField(verbose_name="生育期", default=0)
    line_name = models.CharField(verbose_name="品系名称", max_length=50)
    pod_high = models.DecimalField(verbose_name="低荚高", max_digits=2, decimal_places=2, default=0.0)
    weight_HGrain = models.DecimalField(verbose_name="百粒重", max_digits=2, decimal_places=2, default=0.0)
    rate_PurpleSpot = models.DecimalField(verbose_name="紫斑率", max_digits=2, decimal_places=2, default=0.0)
    rate_BrownSpot = models.DecimalField(verbose_name="褐斑率", max_digits=2, decimal_places=2, default=0.0)
    rate_Insect = models.DecimalField(verbose_name="虫食率", max_digits=2, decimal_places=2, default=0.0)
    rate_others = models.DecimalField(verbose_name="其他粒率", max_digits=2, decimal_places=2, default=0.0)
    remarks = models.TextField(verbose_name="备注")

    def __str__(self):
        return self.line_name


class Info_FieldCharacter(models.Model):  #田间性状
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

    info_testLines = models.ForeignKey(Info_TestLines, on_delete=models.CASCADE)
    line_name = models.CharField(verbose_name="品系名称", max_length=50)
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

    def __str__(self):
        return self.line_name


class Criteria_Character(models.Model):  #性状记载标准
    line_trait = models.CharField(verbose_name="性状", max_length=20)
    criteria_record = models.TextField(verbose_name="记载标准")

    def __str__(self):
        return self.line_trait


class Info_Yield(models.Model):  #产量信息表
    info_testLines = models.ForeignKey(Info_TestLines, on_delete=models.CASCADE)
    test_name = models.CharField(verbose_name="试验名称", max_length=40)
    line_name = models.CharField(verbose_name="品系名称", max_length=50)
    test_rep1 = models.DecimalField(verbose_name="重复1", max_digits=4, decimal_places=2, default=0.0)
    test_rep2 = models.DecimalField(verbose_name="重复2", max_digits=4, decimal_places=2, default=0.0)
    test_rep3 = models.DecimalField(verbose_name="重复3", max_digits=4, decimal_places=2, default=0.0)
    avg_yield = models.DecimalField(verbose_name="平均值", max_digits=4, decimal_places=2, default=0.0)

    def __str__(self):
        return self.line_name