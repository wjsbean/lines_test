# Generated by Django 2.1.1 on 2018-11-11 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria_Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_trait', models.CharField(max_length=20, verbose_name='性状')),
                ('criteria_record', models.TextField(verbose_name='记载标准')),
            ],
            options={
                'verbose_name': '性状记载标准',
                'verbose_name_plural': '性状记载标准',
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=20, verbose_name='试验名称')),
            ],
            options={
                'verbose_name': '试验名称',
                'verbose_name_plural': '试验名称',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_group', models.CharField(max_length=20, verbose_name='试验组别')),
                ('test_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Experiment', verbose_name='试验名称')),
            ],
            options={
                'verbose_name': '试验组别',
                'verbose_name_plural': '试验组别',
            },
        ),
        migrations.CreateModel(
            name='Info_EcoCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_high', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='低荚高')),
                ('weight_HGrain', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='百粒重')),
                ('rate_PurpleSpot', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='紫斑率')),
                ('rate_BrownSpot', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='褐斑率')),
                ('rate_Insect', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='虫食率')),
                ('rate_others', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='其他粒率')),
                ('remarks', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name': '经济性状',
                'verbose_name_plural': '经济性状',
            },
        ),
        migrations.CreateModel(
            name='Info_ExperiLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_unit', models.CharField(max_length=40, verbose_name='承试单位')),
                ('testPoint_name', models.CharField(max_length=40, verbose_name='试点名称')),
                ('testPoint_loc', models.CharField(max_length=20, verbose_name='所在地')),
                ('testLoc_longitude', models.CharField(max_length=10, verbose_name='经度')),
                ('testLoc_latitude', models.CharField(max_length=10, verbose_name='纬度')),
                ('testLoc_altitude', models.CharField(max_length=10, verbose_name='海拔')),
                ('address', models.TextField(verbose_name='通讯地址')),
                ('contacts', models.CharField(max_length=10, verbose_name='联系人')),
                ('contact_num', models.CharField(max_length=15, verbose_name='联系电话')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('group', models.ManyToManyField(to='summary.Group', verbose_name='试验组别')),
            ],
            options={
                'verbose_name': '承试点信息',
                'verbose_name_plural': '承试点信息',
            },
        ),
        migrations.CreateModel(
            name='Info_FieldCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeding_date', models.DateField(verbose_name='播种期')),
                ('seeding_state', models.DateField(verbose_name='出苗期')),
                ('flowering_period', models.DateField(verbose_name='开花期')),
                ('mature_period', models.DateField(verbose_name='成熟期')),
                ('harvest_period', models.DateField(verbose_name='收获期')),
                ('No_GrowDays', models.PositiveIntegerField(verbose_name='生育日数')),
                ('leaf_shape', models.CharField(choices=[('圆叶', '圆叶'), ('卵圆', '卵圆'), ('椭圆', '椭圆'), ('披针形', '披针形')], max_length=5, verbose_name='叶形')),
                ('flower_color', models.CharField(choices=[('白花', '白花'), ('紫花', '紫花')], max_length=5, verbose_name='花色')),
                ('hairy_color', models.CharField(choices=[('无茸毛', '无茸毛'), ('灰色', '灰色'), ('棕色', '棕色')], max_length=5, verbose_name='茸毛色')),
                ('pod_BearHabit', models.CharField(choices=[('有限', '有限'), ('亚有限', '亚有限'), ('无限', '无限')], max_length=8, verbose_name='结荚习性')),
                ('plant_architecture', models.CharField(choices=[('收敛', '收敛'), ('开张', '开张'), ('半开张', '半开张')], max_length=8, verbose_name='株型')),
                ('pod_dehiscence', models.CharField(choices=[('不裂', '不裂'), ('中裂', '中裂'), ('易裂', '易裂')], max_length=5, verbose_name='裂荚性')),
                ('deciduous', models.CharField(choices=[('落叶', '落叶'), ('半落', '半落'), ('不落', '不落')], max_length=5, verbose_name='落叶性')),
                ('lodging', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=2, verbose_name='倒伏性')),
                ('root_rot', models.CharField(max_length=5, verbose_name='根腐病')),
                ('smv', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=5, verbose_name='花叶病')),
                ('in_green', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='症青')),
                ('virus_other', models.CharField(max_length=50, verbose_name='其他病毒病')),
            ],
            options={
                'verbose_name': '田间性状',
                'verbose_name_plural': '田间性状',
            },
        ),
        migrations.CreateModel(
            name='Info_TestLines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=50, verbose_name='品系名称')),
                ('line_institute', models.CharField(max_length=50, verbose_name='选育单位')),
                ('line_owner', models.CharField(max_length=10, verbose_name='选育人')),
                ('line_contactor', models.CharField(max_length=10, verbose_name='联系人')),
                ('line_type', models.CharField(max_length=10, verbose_name='品种类型')),
                ('line_maleParent', models.CharField(max_length=30, verbose_name='父本')),
                ('line_femaleParent', models.CharField(max_length=30, verbose_name='母本')),
                ('line_target_date', models.DateField(verbose_name='育成日期')),
                ('line_phone', models.CharField(max_length=15, verbose_name='联系电话')),
                ('line_email', models.EmailField(max_length=254, verbose_name='联系邮箱')),
                ('line_year', models.DateField(verbose_name='参试年份')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Group', verbose_name='试验信息')),
            ],
            options={
                'verbose_name': '参试品种',
                'verbose_name_plural': '参试品种',
            },
        ),
        migrations.CreateModel(
            name='Info_Yield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_rep1', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='重复1')),
                ('test_rep2', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='重复2')),
                ('test_rep3', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='重复3')),
                ('avg_yield', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='平均值')),
                ('line_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_TestLines', verbose_name='参试品系')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_ExperiLocation', verbose_name='试验点')),
            ],
            options={
                'verbose_name': '产量信息表',
                'verbose_name_plural': '产量信息表',
            },
        ),
        migrations.CreateModel(
            name='PurposeRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_purpose', models.TextField(verbose_name='试验目的')),
                ('test_request', models.TextField(verbose_name='试验要求')),
                ('test_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Group', verbose_name='试验组别')),
            ],
            options={
                'verbose_name': '试验目的',
                'verbose_name_plural': '试验目的',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.TextField()),
                ('organization', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '注册用户',
                'verbose_name_plural': '注册用户',
            },
        ),
        migrations.AddField(
            model_name='info_fieldcharacter',
            name='line_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_TestLines', verbose_name='参试品系'),
        ),
        migrations.AddField(
            model_name='info_fieldcharacter',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_ExperiLocation', verbose_name='试验点'),
        ),
        migrations.AddField(
            model_name='info_ecocharacter',
            name='line_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_TestLines', verbose_name='参试品系'),
        ),
        migrations.AddField(
            model_name='info_ecocharacter',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Info_ExperiLocation', verbose_name='试验点'),
        ),
    ]
