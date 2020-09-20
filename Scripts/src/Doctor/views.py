from django.shortcuts import render, redirect
from website import models
from django.core.exceptions import ValidationError
import datetime 
from dateutil.relativedelta import *
from django.contrib import messages

def AddAnalystLogin(request):
  return render(request,'Doctor/AnalystAddLogin.html', {})

def AddAnalyst(request):
  GetAnalystCode = request.POST['AnalystCode']
  GetPasswordLogin = request.POST['password']
  request.session['GetAnalystCode__se'] = GetAnalystCode
  print('-------------<<GetAnalystCode>>----------'+str(GetAnalystCode))
  print('-------------<<GetPasswordLogin>>----------'+str(GetPasswordLogin))
  try:
    Fetch_data = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalystCode)
    try:
      CheckPass = models.Analyst.objects.get(AnalystCode=GetAnalystCode, Password=GetPasswordLogin)
      print('Analyst Exist in Ministry------------->>')
      try:
        CheckifExist = models.Analyst.objects.get(AnalystCode=GetAnalystCode)
        print('-------------<< Analyst Already Added Before >>---------------------')
        messages.success(request, 'You Are Exist As Analyst in System!')
        return render(request,'Doctor/AnalystEditLogin.html', {})
      except:
        print('-------------<< Analyst Not Exist in Analyst table Login Done >>---------------------')
        National_ID_From_PersonalData = models.PersonalData.objects.get(PerNationalId=Fetch_data.NationalId)
        print('-------------<< Analyst Not Exist in Analyst table Login Done >>---------------------')
        return render(request,'Doctor/AnalystAdd.html', {'Show_data':Fetch_data, 'DBPass':Fetch_data.Password ,'Show_Name':National_ID_From_PersonalData})
    except:
      messages.success(request, 'Login Field !')
      return render(request,'Doctor/AnalystAddLogin.html', {})
  except:
    print('------------------------You Are Not Alowed Not Exist in Ministry------------------------')
    messages.success(request, 'Login Field !')
    return render(request,'Doctor/AnalystAddLogin.html', {})


def AddAnalystSave(request):
  GetPass = request.POST['Pass1']
  
  GetAnalystCode = request.session['GetAnalystCode__se']
  print('-----------<< New Analyst Data >>------Pass------>>'+str(GetPass))
  new = models.Analyst(Password=GetPass, AnalystCode=GetAnalystCode)
  new.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request,'Doctor/DoctorAddLogin.html', {})

def AddDoctorLogin(request):
  return render(request,'Doctor/DoctorAddLogin.html', {})

def AddDoctor(request):
  GetSyndicateCode= request.POST['Syndicate_Code'] 
  GetPasswordLogin = request.POST['password']  
  try:
    Fetch_data= models.MedicalSyndicateLicense.objects.get(SynCode=GetSyndicateCode, Password=GetPasswordLogin)
    request.session['GetSyndicateCode_AddDoctor_se'] = GetSyndicateCode  
    print('-------------<< Doctor Exist In Ministry >>-----------Ntional Id------>>'+str(Fetch_data.SynCode))
    try:
      CheckifExist= models.Doctor.objects.get(SynCode=GetSyndicateCode)
      
      print('-------------<< Doctor Already Added Before >>---------------------')
      messages.success(request, 'You Are Exist As A Doctor in The System!')
      return render(request,'Doctor/DoctorEditLogin.html', {})
    except:
      National_ID_From_PersonalData = models.PersonalData.objects.get(PerNationalId=Fetch_data.NationalId)
      print('-------------<< Doctor Not Exist in doctor table Login Done >>---------------------')
      print('-------------<< Doctor Nname >>---------------------'+str(National_ID_From_PersonalData.FullName))
      return render(request,'Doctor/DoctorAdd.html',{'Show_data':Fetch_data, 'Show_Name':National_ID_From_PersonalData})
  except:
    print('-------------<< Doctor Doesnt Exist In Ministry >>-----------')
    messages.success(request, 'Login Field !')
    return render(request,'Doctor/DoctorAddLogin.html', {})

def AddDoctorSave(request):
  GetPass = request.POST['Pass1']
  
  GetSyndicateCode  =  request.session['GetSyndicateCode_AddDoctor_se']
  print('-----------<< New Doctor Data >>------Pass------>>'+str(GetPass))
  new = models.Doctor( Password=GetPass, SynCode=GetSyndicateCode)
  new.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request,'Doctor/DoctorAddLogin.html', {})

def DoctorEditLogin(request):
  return render(request,'Doctor/DoctorEditLogin.html', {})
  
def AnalystEditLogin(request):
  return render(request,'Doctor/AnalystEditLogin.html', {})

def AnalystEdit(request):
  GetAnalystCode= request.POST['Analyst__Code']  
  GetPasswordLogin = request.POST['password'] 
  Fetch_Pass = models.Analyst.objects.get(AnalystCode=GetAnalystCode).Password
  try:
    Fetch_data = models.Analyst.objects.get(AnalystCode=GetAnalystCode, Password=GetPasswordLogin)
    request.session['GetAnalystCode_AnalystEdit_se'] = GetAnalystCode
    Fetch_id =  models.Analyst.objects.get(AnalystCode=GetAnalystCode)
    print('Analyst id after add form DoctorEdit-------->' + (GetAnalystCode))
    print('Database Pass from Analyst Edit-------->' + str(Fetch_data))
    return render(request,'Doctor/AnalystEdit.html', {'Show':Fetch_id ,'DBPass': Fetch_Pass, 'AnalystCode':GetAnalystCode})
  except:
    print('------------------------You Are Not Alowed------------------------')
    messages.success(request, 'Login Field !')
    return render(request, 'home.html')
 

def EditAnalystSave(request):
  GetAnalystCode = request.session['GetAnalystCode_AnalystEdit_se']
  OldPass= request.POST['OldPass']
  Pass1= request.POST['Pass1']
  Pass2 = request.POST['Pass2']
  Fetch_id =  models.Analyst.objects.get(AnalystCode=GetAnalystCode)  
  try:
    Fetch_Pass = models.Analyst.objects.get(AnalystCode=GetAnalystCode).Password
    new = models.Analyst( Password=Pass1, AnalystCode=GetAnalystCode, RegisterDate=Fetch_id.RegisterDate)
    print('-------------OldPass True-------------'+str(OldPass))
    print('-------------OldPass db-------------'+str(Fetch_Pass))
  except:    
    print('----------Not Allowed To Edit DATA Check Your Old Pass----------')
    print('---------Old Pass-->>>'+str(OldPass)+'<<<---------')
    print('-------------OldPass db-------------'+str(Fetch_Pass))
    return render(request,'Doctor/DoctorEdit.html', {'Show':Fetch_id , 'DBPass': Fetch_Pass, 'AnalystCode':GetAnalystCode})
  print('---------Old Pass-->>>'+str(OldPass)+'<<<---------')
  print('----------pass1--------->>' + str(Pass1))
  print('----------pass2--------->>' + str(Pass2))
  new.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request, 'home.html')


def DoctorEdit(request):
  GetSyndicateCode= request.POST['Syndicate_Code'] 
  SynCode = request.POST['Syndicate_Code']
  GetPasswordLogin = request.POST['password'] 
  Fetch_Pass = models.Doctor.objects.get(SynCode=SynCode).Password
  try:
    Fetch_data = models.Doctor.objects.get(SynCode=GetSyndicateCode, Password=GetPasswordLogin)
    request.session['GetSyndicateCode_DoctorEdit_se'] = GetSyndicateCode
    Fetch_id =  models.Doctor.objects.get(SynCode=GetSyndicateCode)
    print('Doctor id after add form DoctorEdit-------->' + (GetSyndicateCode))
    print('Database Pass from DoctorEdit-------->' + str(Fetch_data))
    return render(request,'Doctor/DoctorEdit.html', {'Show':Fetch_id ,'DBPass': Fetch_Pass, 'SynCode':GetSyndicateCode})
  except:
    print('------------------------You Are Not Alowed------------------------')
    messages.success(request, 'Login Field !')
    return render(request, 'home.html')
  

def DocEditSave(request):
  SynCode = request.POST['SyCode']
  
  OldPass= request.POST['OldPass']
  Pass1= request.POST['Pass1']
  Pass2 = request.POST['Pass2']
  GetSyndicateCode = request.session['GetSyndicateCode_DoctorEdit_se']
  Fetch_id =  models.Doctor.objects.get(SynCode=GetSyndicateCode)  
  GetSyndicateCode2 =  request.session['GetSyndicateCode_AddDoctor_se']
  try:
    Fetch_Pass = models.Doctor.objects.get(SynCode=SynCode)
    new = models.Doctor(SynCode = SynCode, Password = Pass1, Date=Fetch_Pass.Date)  
    print('-------------OldPass True-------------'+str(OldPass))
    print('-------------OldPass db-------------'+str(Fetch_Pass))
  except:    
    print('----------Not Allowed To Edit DATA Check Your Old Pass----------')
    print('---------Old Pass-->>>'+str(OldPass)+'<<<---------')
    print('-------------OldPass db-------------'+str(Fetch_Pass))
    messages.success(request, 'Edit Data Field !')
    return render(request,'Doctor/DoctorEdit.html', {'Show':Fetch_id , 'DBPass': Fetch_Pass.Password, 'SynCode':GetSyndicateCode2})
  print('---------Old Pass-->>>'+str(OldPass)+'<<<---------')
  print('----------pass1--------->>' + str(Pass1))
  print('----------pass2--------->>' + str(Pass2))
  new.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request, 'home.html')

def DoctorWorkOnLogin(request):
  return render(request,'Doctor/DoctorWorkOnLogin.html', {})

def PatientLogin(request):
  GetSyndicateCode= request.POST['Syndicate_Code'] 
  request.session['GetDocSynCode_se'] = GetSyndicateCode
  request.session['GetSyndicateCode_PatientIdLogin_se']  = GetSyndicateCode
  GetPassLogin = request.POST['password'] 
  try:
    GetData= models.MedicalSyndicateLicense.objects.get(SynCode=GetSyndicateCode)
    print('-------------<< Doctor Exist in Ministry >>------------------')
    GetDataSynCode=GetData.SynCode
    GetDoctorNationalId=GetData.NationalId
    print('----------------<< Doctor national id >>--------'+str(GetDoctorNationalId))
    try:
      GetallDoctorData=  models.PersonalData.objects.get(PerNationalId=GetDoctorNationalId)
      print('-----------<< Doctor Data >>----------------'+str(GetallDoctorData))
      GetDoctorName = models.PersonalData.objects.get(id=GetDoctorNationalId).FullName
      request.session['GetDoctorName_se'] = GetDoctorName
      print('-----------<< Get Doctor Data Works >>----------------'+str(GetDoctorName))
    except:
      print('-----------<< Get Doctor Data Doesnt Work >>----------------')
      return render(request,'Doctor/DoctorWorkOnLogin.html', {})
    request.session['GetSyndicateCode_se']=GetDataSynCode
    request.session['GetDoctorId_se']=GetDoctorNationalId
    print('-------------<< Doctor Syndicate Code from PatientLogin>>------------------>>'+str(GetData.SynCode))
    print('-------------<< Doctor National Id from PatientLogin>>>------------------>>'+str(GetData.NationalId))
    try:
      Check_Doctory_Pass= models.Doctor.objects.get(SynCode=GetSyndicateCode, Password=GetPassLogin)
      print('-------------<< Doctor Password True login Done >>------------------')
      return render(request,'Doctor/PatientIdLogin.html', {})
    except:
      print('-------------<< Doctor Password Doesnt True login Failed >>------------------')
      messages.success(request, 'Login Field !')
      return render(request,'Doctor/DoctorWorkOnLogin.html', {})
  except:
    print('-------------<< Doctor Doesnt Exist in Ministry >>------------------')
    messages.success(request, 'Login Field !')
    return render(request,'Doctor/DoctorWorkOnLogin.html', {})

def DoctorPatientPersonalData(request):
  GetPatientNationalId= request.POST['Patient_National_Id']
  GetDataSynCode = request.session['GetSyndicateCode_se']
  GetDoctorNationalId = request.session['GetDoctorId_se']    
  GetDoctorName = request.session['GetDoctorName_se']
  try:
    Fetch_Patient= models.Citizen.objects.get(PerNationalId=GetPatientNationalId)
    request.session['GetPatientNationalId_se'] = GetPatientNationalId     
    GetPatiientData = models.PersonalData.objects.get(PerNationalId=GetPatientNationalId)    
    print('------<< Patient Exist in Citizen Login Done >>--------------')    
    print('-----<< Patient National ID from Template>>-------------->>'+ (GetPatientNationalId))    
    print('-----<< Doctor Syndicate Code from DoctorPatientPersonalData>>---->>'+str(GetDataSynCode))
    print('-----<< Doctor National Id from DoctorPatientPersonalData>>------>>'+str(GetDoctorNationalId))
    PatientDOB = GetPatiientData.BirthDate
    print('---------------------->>>>>Patient BirthDate'+str(PatientDOB))
    CurrentDate = datetime.datetime.now().date() 
    print('---------------------->>>>>Current Date '+str(CurrentDate))
    Patient_age = relativedelta(CurrentDate, PatientDOB)
    print('-------------------<< DOB .YEARS>>-------------------------'+str(Patient_age.years))
    print('-------------------<< DOB .Months>>-------------------------'+str(Patient_age.months))
    print('-------------------<< DOB .Days>>-------------------------'+str(Patient_age.days))
    return render(request,'Doctor/DoctorPatientPersonalData.html', {'DoctorName':GetDoctorName,'Age':Patient_age, 'PatientData':GetPatiientData})
  except:
    print('----------------<< This Patient Doesnt Exist in the System As Citizen >>---------------')
    messages.success(request, 'This Patient Doesnt Exist in the System As Citizen !')
    return render(request,'Doctor/PatientIdLogin.html', {})

def DoctorWorkOn(request):
  GetDoctorName = request.session['GetDoctorName_se']
  GetPatientNationalId =  request.session['GetPatientNationalId_se']  
  TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatientNationalId)
  GetPatiientData = models.PersonalData.objects.get(PerNationalId=GetPatientNationalId)   
  print('Patient id after add form DoctorEdit-------->' + (GetPatientNationalId))
  return render(request,'Doctor/DoctorWorkOn.html', {'DoctorName':GetDoctorName, 'TableData':TableData,  'PatientData':GetPatiientData})

def SaveReport(request):
  GetSyndicateCode = request.session['GetDocSynCode_se']
  GetDoctorName = request.session['GetDoctorName_se']
  GetPatientNationalId =  request.session['GetPatientNationalId_se']  
  GetDoctorNationalId = request.session['GetDoctorId_se']  
  GetSpecialDoctor = 'Special Doctor'
  GetMedicalReport= request.POST['AddMReport']
  GetTreatment= request.POST['AddTreatment']
  TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatientNationalId)
  GetPatiientData = models.PersonalData.objects.get(PerNationalId=GetPatientNationalId)    
  Patient__ID=GetPatiientData.PerNationalId.PerNationalId
  GetDoctorData = models.PersonalData.objects.get(PerNationalId=GetDoctorNationalId)
  print ('TableData --------<<>>'+str(TableData))
  print ('Doctor Syndicate Code --------<<>>'+str(GetSyndicateCode))
  print ('Doctor Name --------<<>>'+str(GetDoctorData.FullName))
  print ('Doctor Personal Id --------<<>>'+str(GetDoctorData.PerNationalId))
  print ('Patient Name --------<<>'+str(GetPatiientData.FullName))
  print ('GetPatientNationalId --------<<>>'+str(Patient__ID))
  SaveData = models.MedicalHistory(
    DoctorNationalId=GetDoctorData.PerNationalId.PerNationalId,
    PerNationalId_id= Patient__ID,
    SynCode=GetSyndicateCode,
    MedicalReport=GetMedicalReport,
    Treatment=GetTreatment,
    CenterName=GetSpecialDoctor,
    DoctorName=GetDoctorName,
    
  )
  SaveData.save()
  
  print('--------------<< Patient Doesnt exist in Citizrn Model >>----------------')
  messages.success(request, 'Report Saved Successfully')
  return render(request,'Doctor/PatientIdLogin.html', {})

def NewPatient(request):
  SessionGetDrCode =  request.session['GetSyndicateCode_PatientIdLogin_se']  
  print('Patient id after add form PatientIdLogin-------->' + (SessionGetDrCode))
  del request.session['GetPatientNationalId_se']
  messages.success(request, 'Sign Another Patient')
  return render(request,'Doctor/PatientIdLogin.html', {})

