from django.db import models
from datetime import datetime
from django.utils import timezone



class Citizen(models.Model):
    PerNationalId= models.BigIntegerField(
        primary_key=True,        
        )
    UserName= models.CharField(
        max_length=50,
        null=True,
    )
    Password= models.CharField(
        max_length=60,
        null=False,
    )

class PersonalData(models.Model):
    FullName=models.CharField(
        max_length=60,
        null=False,
    )
    Gender= models.CharField(
        max_length=10,
        null=False,
    )
    Job = models.CharField(
        max_length=50,
        null=False,
    )
    BirthGov= models.CharField(
        null=False,
        max_length=40,
    )
    BirthDate= models.DateField(
        null=True,
        
    )
    CurrentGov= models.CharField(
        null=False,
        max_length=40,
    )
    CurrentAddress=models.CharField(
        null=False,
        max_length=120, 
    )
    FirstPhone=models.BigIntegerField(
        null=False,
        
        )
    SecoundPhone= models.BigIntegerField(
        null=False,
        
    )
    Email= models.EmailField(
        null=False,
        max_length=60,
    )
    FirstRelName=models.CharField(
        max_length=60,
        null=False,
    )
    FirstRelPhone=models.BigIntegerField(
        null=False,
        
        )
    SecoundRelName=models.CharField(
        max_length=60,
        null=False,
    )
    SecoundRelPhone= models.BigIntegerField(
        null=False,
        
    )
    PassportNo=models.BigIntegerField(
        null=True,
        
    )
    BloodGroup=models.CharField(
        null=True,
        max_length=5,
    )
    PerNationalId=models.ForeignKey(Citizen,
     on_delete=models.PROTECT,null=True)
     
    Date=models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    LabCode=models.CharField(
        max_length=30,        
        null=True,
    )

    LabName=models.CharField(
        max_length=60,
        null=True,
    )

    
class Doctor(models.Model):
    SynCode=models.BigIntegerField(        
        primary_key=True,
    )
    DoctorNationalId=models.CharField(
        max_length=30,
        null=True,
    )
    
    Password=models.CharField(
        max_length=60,
        null=True,
    )    
    Date=models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

class MedicalCenter(models.Model):
    CenterCode= models.BigIntegerField(
        primary_key=True,
        
    )    
    CenterType= models.CharField(
        max_length=20,
        null=True,
    )
    Password=models.CharField(
        max_length=60,
        null=False,
    )  
    CenterName=models.CharField(
        max_length=60,
        null=False,
    )
    CenterGov= models.CharField(
        null=False,
        max_length=40,
    )
    CurrentAddress=models.CharField(
        null=False,
        max_length=120, 
    )
    FirstPhone=models.BigIntegerField(
        null=False,        
    )
    SecoundPhone= models.BigIntegerField(
        null=False,        
    )
    RegisteredDate=models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    UpdateDate=models.DateTimeField(
        auto_now=True,
        null=True,
    )

class DocWorkOnCenter(models.Model):
    SynCode=models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)
    DoctorName=models.CharField(max_length=60,null=True)
    DoctorNationalId=models.CharField(max_length=30,null=True)
    CenterCode=models.ForeignKey(MedicalCenter, on_delete=models.PROTECT, null=True)
    Specialization1=models.CharField(max_length=50,null=True)
    Specialization2=models.CharField(max_length=50,null=True)
    WorkOnDate=models.DateTimeField(auto_now_add=True, null=False)


class DocWorkOnCenterHistory(models.Model):
    SynCode=models.CharField(
        max_length=30,
        null=False,
    )
    DoctorName=models.CharField(max_length=60,null=True)
    DoctorNationalId=models.CharField(max_length=30,null=True)
    Specialization1=models.CharField(max_length=50,null=True)
    Specialization2=models.CharField(max_length=50,null=True)
    CenterCode=models.CharField(
        max_length=30,
        null=True,
    )

    WorkOnDate=models.DateTimeField(
        auto_now_add=True,
        null=False,
    )
    RemoveDate=models.DateTimeField(
        null=True,
    )

class DoctorPerson(models.Model):    
    SynCode=models.ForeignKey(Doctor,
     on_delete=models.PROTECT)
    
    PerNationalId=models.ForeignKey(Citizen,
     on_delete=models.PROTECT,null=True)

    CurrentTime=models.DateTimeField(        
        auto_now_add=True,
        null=False,
    )
class PersonMedicalCenter(models.Model):    
    CenterCode=models.ForeignKey(MedicalCenter,
     on_delete=models.PROTECT)
    
    PerNationalId=models.ForeignKey(Citizen,
     on_delete=models.PROTECT,null=True)

    CurrentTime=models.DateTimeField(        
        auto_now_add=True,
        null=False,
    )

class  MedicalHistory (models.Model):
    CurrentTime=models.DateTimeField(        
        auto_now_add=True,
        null=False,
    )

    PerNationalId=models.ForeignKey(Citizen,
     on_delete=models.PROTECT,
     null=True,
     )
     
    SynCode=models.CharField(
        max_length=30,
        null=True,
    )
    DoctorName=models.CharField(
        max_length=60,
        null=True,
    )
    CenterCode=models.CharField(
        max_length=30,
        null=True,
    )
    DoctorNationalId=models.CharField(
        max_length=30,
        null=True,
    )
    AnalystNationalId=models.CharField(
        max_length=30,
        null=True,
    )
    CenterName=models.CharField(
        max_length=60,
        null=True,
    )

    RecordDate=models.DateTimeField(        
        auto_now_add=True,
        null=False,
    )
    MedicalReport=models.TextField(
        null=True,
    )

    Treatment=models.TextField(
        null=True,
    )

    LabCode=models.CharField(
        max_length=30,        
        null=True,
    )

    LabName=models.CharField(
        max_length=60,
        null=True,
    )

    AnalysisReport=models.TextField(
        null=True,
    )

    RaysReport=models.TextField(
        null=True,
    )

class Laboratory(models.Model):
    LabCode=models.BigIntegerField(
        
        primary_key=True,
    )

    LabName=models.CharField(
        max_length=60,
        null=False,
    )

    LabType= models.CharField(
        max_length=50,
        null=True,
    )
    LabPassword=models.CharField(
        max_length=60,
        null=False,
    )

    LabGov= models.CharField(
        null=False,
        max_length=40,
    )

    CurrentAddress=models.CharField(
        null=False,
        max_length=120, 
    )

    FirstPhone=models.BigIntegerField(
        null=False,
        
    )

    SecoundPhone= models.BigIntegerField(
        null=False,
        
    )

    Date=models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

class AnalystLabHistory (models.Model):
    LabCode=models.ForeignKey(Laboratory,
     on_delete=models.PROTECT)

    AnalystCode=models.CharField(
        max_length=30,
        null=False,
    )
    AnalystName=models.CharField(max_length=60,null=True)
    AnalystNationalId=models.CharField(max_length=30,null=True)
    Specialization1=models.CharField(max_length=50,null=True)
    Specialization2=models.CharField(max_length=50,null=True)
    AnalystAddDate=models.DateTimeField(
        auto_now_add=True,
        null=False,
    )
    
    RemoveAnalystDate=models.DateTimeField(
        null=True,
    )

class PersonLab(models.Model):
    PerNationalId=models.ForeignKey(Citizen,
     on_delete=models.PROTECT,null=True)

    LabCode=models.ForeignKey(Laboratory,
     on_delete=models.PROTECT)

    Date=models.DateTimeField(
     auto_now_add=True,
     null=True,
    )

class Analyst(models.Model):
    AnalystCode=models.BigIntegerField(
        primary_key=True,
    )

    UserName= models.CharField(
        max_length=50,
        null=True,
    )

    Password=models.CharField(
        max_length=60,
        null=False,
    )

    RegisterDate=models.DateTimeField(
     auto_now_add=True,
     null=True,
    )

class AnalystWorkOnLab (models.Model):
    LabCode=models.ForeignKey(Laboratory,on_delete=models.PROTECT)
    AnalystCode=models.ForeignKey(Analyst,on_delete=models.PROTECT)
    AnalystName=models.CharField(max_length=60,null=True)
    AnalystNationalId=models.CharField(max_length=30,null=True)
    Specialization1=models.CharField(max_length=50,null=True)
    Specialization2=models.CharField(max_length=50,null=True)
    WorkOnDate=models.DateTimeField(auto_now_add=True,null=False)
  
class HealthMinistryLicenseLab(models.Model):
    MinLabCode=models.BigIntegerField(
        primary_key=True,
        null=False,
    )

    LabName=models.CharField(
        max_length=60,
        null=True,
    )

    LabType=models.CharField(
        max_length=20,
        null=True,
    )

    LabGov=models.CharField(
        max_length=40,
        null=True,
    )
    Password= models.CharField(
        max_length=60,
        null=True,
    )
class HealthMinistryLicenseCenter(models.Model):
    CenterCode=models.BigIntegerField(
        primary_key=True,
    )

    CenterName=models.CharField(
        max_length=60,
        null=False,
    )

    CenterType=models.CharField(
        max_length=20,
        null=False,
    )

    CenterGov=models.CharField(
        max_length=40,
        null=False,
    )
    Password= models.CharField(
        max_length=60,
        null=True,
    )
class MedicalSyndicateLicense(models.Model):
    SynCode=models.BigIntegerField(
        primary_key=True,
        
    )
    Password= models.CharField(
        max_length=60,
        null=True,
    )
    NationalId=models.CharField(
        max_length=30,
        null=False,        
    )

    Specialization1=models.CharField(
        max_length=50,
        null=False,
    )

    Specialization2=models.CharField(
        max_length=50,
        null=False,
    )

class MedicalAnalystLicense(models.Model):
    AnalystCode=models.BigIntegerField(
        primary_key=True,
        
    )
    Password= models.CharField(
        max_length=60,
        null=True,
    )
    NationalId=models.CharField(
        max_length=30,
        null=False,        
    )

    Specialization1=models.CharField(
        max_length=50,
        null=False,
    )

    Specialization2=models.CharField(
        max_length=50,
        null=True,
    )
