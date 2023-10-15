from django.db import models

# Create your models here.

class 物料表(models.Model):
    物料号 = models.IntegerField(primary_key=True)
    名称 = models.CharField(max_length=45, blank=True, null=True)
    单位 = models.CharField(max_length=45, blank=True, null=True)
    调配方式 = models.CharField(max_length=45, blank=True, null=True)
    损耗率 = models.FloatField(blank=True, null=True)
    作业提前期 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '物料表'

class 库存表(models.Model):
    物料号 = models.OneToOneField(物料表, models.DO_NOTHING, db_column='物料号', primary_key=True)
    物料名称 = models.CharField(max_length=45, blank=True, null=True)
    工序库存 = models.IntegerField(blank=True, null=True)
    资材库存 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '库存表'

class 调配构成表(models.Model):
    调配基准编号 = models.CharField(max_length=45, blank=True, null=True)
    调配区代码 = models.CharField(max_length=45, blank=True, null=True)
    父物料号 = models.OneToOneField(物料表, models.DO_NOTHING, db_column='父物料号', related_name="father", primary_key=True)
    父物料名称 = models.CharField(max_length=45, blank=True, null=True)
    子物料号 = models.ForeignKey(物料表, models.DO_NOTHING, db_column='子物料号', related_name="son")
    子物料名称 = models.CharField(max_length=45, blank=True, null=True)
    构成数 = models.IntegerField(blank=True, null=True)
    配料提前期 = models.IntegerField(blank=True, null=True)
    供应商提前期 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '调配构成表'
        unique_together = (('父物料号', '子物料号'),)