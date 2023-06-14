from django.db import models

# Create your models here.

class staff(models.Model):#人员表
    staff_id=models.CharField(max_length=50,primary_key=True,db_index=True)
    join_id=models.DateTimeField(auto_now=False)
    name=models.CharField(max_length=200,null=True)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
    scenic_plot=models.ForeignKey(to='scenic_plot',on_delete=models.CASCADE)
    class Meta:
        app_label="app" 

class security_personnel(models.Model):#安保人员
    staff_id=models.ForeignKey(to='staff',on_delete=models.CASCADE,primary_key=True)
    grade=models.CharField(max_length=50,null=True)
    class Meta:
        app_label="app" 

class security_view(models.Model):   #视图
    staff_id=models.CharField(max_length=50,primary_key=True,db_index=True)
    join_id=models.DateTimeField(auto_now=False)
    name=models.CharField(max_length=200,null=True)
    class Meta:
        app_label="app" 
        managed = False 
        db_table = "security_view" 

class maintain_view(models.Model):   #视图
    staff_id=models.CharField(max_length=50,primary_key=True,db_index=True)
    join_id=models.DateTimeField(auto_now=False)
    name=models.CharField(max_length=200,null=True)
    class Meta:
        app_label="app" 
        managed = False 
        db_table = "maintain_view" 

class maintain_personnel(models.Model):#运维
    staff_id=models.ForeignKey(to='staff',on_delete=models.CASCADE,primary_key=True)
    professional_field=models.CharField(max_length=50,null=True)
    class Meta:
        app_label="app" 

class scenic_plot(models.Model):#景点
    plot_id=models.IntegerField(primary_key=True)
    plot_name=models.CharField(max_length=50,null=True)
    plot_address=models.CharField(max_length=100,null=True)

class area(models.Model):#区域表
    area_id=models.CharField(max_length=20,primary_key=True)
    area_device=models.CharField(max_length=100,null=True)
    area_name=models.CharField(max_length=50,null=True)
    plot_id=models.ForeignKey(to='scenic_plot',on_delete=models.CASCADE)

class device(models.Model):#设备表
    device_id=models.CharField(max_length=20,primary_key=True)
    device_name=models.CharField(max_length=100,null=True)
    manufacturer=models.CharField(max_length=100,null=True)
    production_date=models.DateTimeField(auto_now=False)
    func=models.CharField(max_length=200,null=True)
    area_id=models.ForeignKey(to="area",on_delete=models.CASCADE)
    

class crowdvis(models.Model):#人流量
    total_count=models.IntegerField()
    vis_count=models.IntegerField()
    in_count=models.IntegerField()
    out_count=models.IntegerField()
    device_id=models.ForeignKey(to="device",on_delete=models.CASCADE,null=True)

class security_report(models.Model):
    staff_id=models.ForeignKey(to="security_personnel",on_delete=models.CASCADE)
    sreport_id=models.AutoField(primary_key=True)
    sreport_date=models.DateTimeField(auto_now=False)
    sreport=models.CharField(max_length=500,null=True)
    area_id=models.ForeignKey(to="area",on_delete=models.CASCADE)


class maintain_report(models.Model):
    staff_id=models.ForeignKey(to="maintain_personnel",on_delete=models.CASCADE)
    mreport_id=models.IntegerField(primary_key=True)
    mreport_date=models.DateTimeField(auto_now=False)
    device_id=models.ForeignKey(to="device",on_delete=models.CASCADE)
    mreport=models.CharField(max_length=500,null=True)



class warning(models.Model):
    device_id=models.ForeignKey(to="device",on_delete=models.CASCADE)
    warn_time = models.DateTimeField(auto_now=False)
    warn_type = models.CharField(max_length=50, null=True)
    warn_area = models.CharField(max_length=50, null=True)
    warn_description = models.CharField(max_length=50, null=True)
    info = models.CharField(max_length=50, null=True)
