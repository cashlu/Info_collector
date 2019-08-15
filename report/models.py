from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='城市')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['-created']
        verbose_name_plural = '城市'

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='乡镇')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['-created']
        verbose_name_plural = '乡镇'

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='村')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['-created']
        verbose_name_plural = '村'

    def __str__(self):
        return self.name


class SecurityDetail(models.Model):
    """场地安全程度"""

    # 场地安全程度描述choice
    SECURITY_DETAIL_CHOICE = (
        (1, '未发现影响房屋周边安全的不利影响'),
        (2, '房屋周边准在超高土体滑坡'),
        (3, '房屋周边场地存在地质斜坡'),
        (4, '房屋周边存在河流，受河水持续冲刷'),
        (5, '房屋存在沟壑'),
        (6, '房屋周边塌方'),
        (7, '房屋周边下方存在不实空洞'),
    )

    detail = models.IntegerField(choices=SECURITY_DETAIL_CHOICE,
                                 verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '场地安全程度描述'

    def __str__(self):
        return self.get_detail_display()


class GroundsillDetail(models.Model):
    """地基基础"""

    # 地基基础描述choice
    GROUNDSILL_DETAIL_CHOICE = (
        (1, '未发现明显不均匀沉降及滑移'),
        (2, '地基基础轻微不均匀沉降'),
        (3, '地基基础不均匀沉降'),
        (4, '室内地面下陷'),
        (5, '地基基础滑移'),
        (6, '地基基础存在滑移可能'),
        (7, '地基基础被冲毁'),
        (8, '毛石基础粘结砂浆缺失'),
    )

    detail = models.IntegerField(choices=GROUNDSILL_DETAIL_CHOICE,
                                 verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '地基基础描述'

    def __str__(self):
        return self.get_detail_display()


class TiltDetail(models.Model):
    """房屋整体倾斜"""

    # 房屋整体倾斜描述choice
    TILT_DETAIL_CHOICE = (
        (1, '未发现明显倾斜'),
        (2, '房屋墙体局部倾斜'),
        (3, '房屋墙体整体倾斜'),
        (4, '房屋墙体变形'),
        (5, '房屋墙体未发现明显歪闪缺陷')
    )
    detail = models.IntegerField(choices=TILT_DETAIL_CHOICE, verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '房屋整体倾斜描述'

    def __str__(self):
        return self.get_detail_display()


class UponDetail(models.Model):
    """上部承重结构"""

    # 上部承重结构描述choice
    UPON_DETAIL_CHOICE = (
        (1, '未发现结构承载缺陷'),
        (2, '墙体存在裂缝'),
        (3, '墙体轻微裂缝'),
        (4, '墙体贯通缝严重'),
        (5, '墙体风化侵蚀严重'),
        (6, '墙体有效截面积削弱'),
        (7, '内隔墙裂缝'),
        (8, '墙体面层脱落'),
        (9, '墙体变形'),
        (10, '墙体倾斜'),
        (11, '纵横墙连接处松动和开裂'),
        (12, '墙体倒塌'),
        (13, '屋架梁损坏'),
        (14, '屋架檩条损坏'),
        (15, '屋架梁下墙体开裂损坏'),
        (16, '屋架梁下墙体变形'),
        (17, '地基基础不均匀沉降引起的裂缝'),
        (18, '房屋墙体、屋盖无明显受力裂缝和变形'),
        (19, '墙体严重破坏，无法正常使用'),
        (20, '屋架损坏'),
    )
    detail = models.IntegerField(choices=UPON_DETAIL_CHOICE, verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '房上部承重结构描述'

    def __str__(self):
        return self.get_detail_display()


class FenceDetail(models.Model):
    """围护结构"""

    # 围护结构描述choice
    FENCE_DETAIL_CHOICE = (
        (1, '未发现围护缺损'),
        (2, '同上'),
        (3, '墙体存在裂缝'),
        (4, '屋面坍塌'),
        (5, '屋面下陷'),
        (6, '墙体面层脱落'),
        (7, '墙体裂缝'),
        (8, '室内地面下陷'),
        (9, '内隔墙裂缝'),
        (10, '纵横墙多处裂缝'),
    )
    detail = models.IntegerField(choices=FENCE_DETAIL_CHOICE, verbose_name='描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '围护结构描述'

    def __str__(self):
        return self.get_detail_display()


class Advice(models.Model):
    ADVICE_CHOICE = (
        (1, '修缮'),
        (2, '加固危险点'),
        (3, '建议重建'),
        (4, '重建，停止使用，马上搬出'),
        (5, '取消鉴定'),
    )
    advice = models.IntegerField(choices=ADVICE_CHOICE, verbose_name='处理意见')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '处理意见'

    def __str__(self):
        return self.get_advice_display()


class Reviewer(models.Model):
    """审核人"""
    name = models.CharField(max_length=50, verbose_name='审核人')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = '审核人'

    def __str__(self):
        return self.name


class Report(models.Model):
    # 年代choice
    DECADE_CHOICE = (
        ('0000', '未知'),
        ('1900', '1900'),
        ('1910', '1910'),
        ('1920', '1920'),
        ('1930', '1930'),
        ('1940', '1940'),
        ('1950', '1950'),
        ('1960', '1960'),
        ('1970', '1970'),
        ('1980', '1980'),
        ('1990', '1990'),
        ('2000', '2000'),
        ('2010', '2010'),
    )

    # 房屋用途choice
    PURPOSE_CHOICE = (
        (1, '住宅'),
        (2, '厂房'),
        (3, '公共建筑'),
    )

    STRUCTURE_CHOICE = (
        (1, '混凝土结构'),
        (2, '砌体结构'),
        (3, '木结构'),
        (4, '钢结构'),
        (5, '石结构'),
        (6, '生土结构'),
    )

    # 结构得分choice
    DEGREE_CHOICE = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )

    # 场地安全程度描述choice
    SECURITY_DETAIL_CHOICE = (
        (1, '未发现影响房屋周边安全的不利影响'),
        (2, '房屋周边准在超高土体滑坡'),
        (3, '房屋周边场地存在地质斜坡'),
        (4, '房屋周边存在河流，受河水持续冲刷'),
        (5, '房屋存在沟壑'),
        (6, '房屋周边塌方'),
        (7, '房屋周边下方存在不实空洞'),
    )

    # 地基基础描述choice
    GROUNDSILL_DETAIL_CHOICE = (
        (1, '未发现明显不均匀沉降及滑移'),
        (2, '地基基础轻微不均匀沉降'),
        (3, '地基基础不均匀沉降'),
        (4, '室内地面下陷'),
        (5, '地基基础滑移'),
        (6, '地基基础存在滑移可能'),
        (7, '地基基础被冲毁'),
        (8, '毛石基础粘结砂浆缺失'),
    )

    # 房屋整体倾斜描述choice
    TILT_DETAIL_CHOICE = (
        (1, '未发现明显倾斜'),
        (2, '房屋墙体局部倾斜'),
        (3, '房屋墙体整体倾斜'),
        (4, '房屋墙体变形'),
        (5, '房屋墙体未发现明显歪闪缺陷')
    )

    # 上部承重结构描述choice
    UPON_DETAIL_CHOICE = (
        (1, '未发现结构承载缺陷'),
        (2, '墙体存在裂缝'),
        (3, '墙体轻微裂缝'),
        (4, '墙体贯通缝严重'),
        (5, '墙体风化侵蚀严重'),
        (6, '墙体有效截面积削弱'),
        (7, '内隔墙裂缝'),
        (8, '墙体面层脱落'),
        (9, '墙体变形'),
        (10, '墙体倾斜'),
        (11, '纵横墙连接处松动和开裂'),
        (12, '墙体倒塌'),
        (13, '屋架梁损坏'),
        (14, '屋架檩条损坏'),
        (15, '屋架梁下墙体开裂损坏'),
        (16, '屋架梁下墙体变形'),
        (17, '地基基础不均匀沉降引起的裂缝'),
        (18, '房屋墙体、屋盖无明显受力裂缝和变形'),
        (19, '墙体严重破坏，无法正常使用'),
        (20, '屋架损坏'),
    )

    # 围护结构描述choice
    FENCE_DETAIL_CHOICE = (
        (1, '未发现围护缺损'),
        (2, '同上'),
        (3, '墙体存在裂缝'),
        (4, '屋面坍塌'),
        (5, '屋面下陷'),
        (6, '墙体面层脱落'),
        (7, '墙体裂缝'),
        (8, '室内地面下陷'),
        (9, '内隔墙裂缝'),
        (10, '纵横墙多处裂缝'),
    )

    # 评定等级choice
    ASSESS_LEVEL_CHOICE = (
        ('a', 'A 完好无损'),
        ('b', 'B 轻微破损，可以使用'),
        ('c', 'C 破损经修缮后可以使用'),
        ('d', 'D 严重破坏，不能使用'),
        ('e', '倒塌'),
    )

    # 填表人
    # todo: 名单要修改
    CREATOR_CHOICE = (
        (1, '杨军魁'),
        (2, '芦满'),
        (3, '关萌'),
        (4, '黄波'),
    )
    bid = models.CharField(max_length=100, null=True, blank=True,
                           verbose_name='建鉴编号')
    name = models.CharField(max_length=250, verbose_name='姓名')
    identity = models.CharField(max_length=50, verbose_name='身份证号', unique=True)
    decade = models.CharField(choices=DECADE_CHOICE, max_length=10,
                              default='0000', verbose_name='建成年代')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, default=1,
                             verbose_name='城市')
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING, default=1,
                             verbose_name='镇')
    village = models.ForeignKey(Village, on_delete=models.DO_NOTHING, default=1,
                                verbose_name='村')
    purpose = models.IntegerField(choices=PURPOSE_CHOICE, default=1,
                                  verbose_name='用途')
    comment = models.TextField(max_length=250, verbose_name='备注')
    structure = models.IntegerField(choices=STRUCTURE_CHOICE,
                                    default=1, verbose_name='结构形式')
    # 结构情况打分
    security = models.CharField(max_length=10, choices=DEGREE_CHOICE,
                                default='a', verbose_name='场地安全程度')
    groundsill = models.CharField(max_length=10, choices=DEGREE_CHOICE,
                                  default='a', verbose_name='地基基础')
    tilt = models.CharField(max_length=10, choices=DEGREE_CHOICE, default='a',
                            verbose_name='房屋整体倾斜')
    upon = models.CharField(max_length=10, choices=DEGREE_CHOICE, default='a',
                            verbose_name='上部承重结构')
    fence = models.CharField(max_length=10, choices=DEGREE_CHOICE, default='a',
                             verbose_name='围护结构')

    # 下面五个结构描述，每一户可能有1-3条，所以用ManyToMany。
    security_detail = models.ManyToManyField(SecurityDetail,
                                             verbose_name='场地安全程度说明')
    groundsill_detail = models.ManyToManyField(GroundsillDetail,
                                               verbose_name='地基基础说明')
    tilt_detail = models.ManyToManyField(TiltDetail, verbose_name='房屋整体倾斜说明')
    upon_detail = models.ManyToManyField(UponDetail, verbose_name='上部承重结构说明')
    fence_detail = models.ManyToManyField(FenceDetail, verbose_name='围护结构说明')

    assess_level = models.CharField(max_length=10, choices=ASSESS_LEVEL_CHOICE,
                                    default='a', verbose_name='评定等级')
    advice = models.ManyToManyField(Advice, verbose_name='处理建议')
    street_contract = models.CharField(max_length=50, verbose_name='镇（街道）联系人')
    street_contract_phone = models.CharField(max_length=50,
                                             verbose_name='镇（街道）联系人电话')
    village_contract = models.CharField(max_length=50, verbose_name='村联系人')
    village_contract_phone = models.CharField(max_length=50,
                                              verbose_name='村联系人电话')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.DO_NOTHING,
                                 default=1, verbose_name='审核人')
    created = models.DateField(auto_now_add=True, verbose_name='添加日期')
    updated = models.DateTimeField(auto_now=True, verbose_name='修改日期')
    appraiser = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                  verbose_name='鉴定人')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '报告'

    def __str__(self):
        return str(self.pk) + ' - ' + self.name + '(' + self.identity + ')'



class Picture(models.Model):
    file = models.ImageField(upload_to='%Y%m%d')
    report = models.ForeignKey(Report, on_delete=models.DO_NOTHING,
                               related_name='report_pics')
    created = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '图片'
