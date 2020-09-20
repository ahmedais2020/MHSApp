from django.shortcuts import render, redirect
from website import models
import datetime 
from dateutil.relativedelta import *
from django.contrib import messages

def CenterSignupLogin(request):
  return render(request,'MedicalCenter/CenterSignupLogin.html', {})

def CenterSignUp(request):
  GetCenter_Code= request.POST['Center_Code'] 
  GetCenter_pass = request.POST['password']
  try:
    Checkifexist = models.HealthMinistryLicenseCenter.objects.get(CenterCode=GetCenter_Code, Password=GetCenter_pass)
    try:
      CheckCenterCodeinMCenterModel = models.MedicalCenter.objects.get(CenterCode=GetCenter_Code )
      print('---------------<< Medical Center Exist in Medical Center Model >>----------------')
      return render(request,'MedicalCenter/CenterSignupLogin.html', {'Message' : message})
    except:
      request.session['GetCenter_Code_se'] = GetCenter_Code
      print('------------<< Center Code >>----------------'+str(GetCenter_Code))
      print('--------------<< Center Name >>--------------'+str(Checkifexist.CenterName))
      print('------------< Center Type >----------------'+Checkifexist.CenterType)
      print('------------< Center Governorate >----------------'+Checkifexist.CenterGov)
      print('Center id  from CenterSignupLogin-------->' + (GetCenter_Code))
      return render(request,'MedicalCenter/CenterSignUp.html', {'CenterCode':GetCenter_Code,  'CenterData':Checkifexist})
  except:
    messages.success(request, 'Login Field !')
    print('----------<< Center Doesnt Exist in Ministry Centers Or Check Your Password >>-------------')
    return render(request,'MedicalCenter/CenterSignupLogin.html', {})

def CenterRegisteredSave(request):
  CenterCode = request.POST['CenterCode']
  Password = request.POST['Pass1']
  CenterName = request.POST['CenterName']
  CenterType = request.POST['CenterType']
  CenterGov = request.POST['CenterGov']
  CurrentAddress = request.POST['CurrentAddress']
  FirstPhone = request.POST['FirstPhone']
  SecoundPhone = request.POST['SecoundPhone']
  newCenter = models.MedicalCenter(
    CenterCode =  CenterCode,
    Password  =  Password,
    CenterName  =   CenterName,
    CenterType= CenterType,
    CenterGov  =  CenterGov,
    CurrentAddress  =  CurrentAddress,
    FirstPhone  =  FirstPhone,
    SecoundPhone  =  SecoundPhone,
  )
  newCenter.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request,'home.html', {})


 # GetCenterCode  =  request.session['GetCenterCode_se']
def CenterEditProfileLogin(request):
  return render(request,'MedicalCenter/CenterEditProfileLogin.html', {})

def CenterChooseOption(request):  
  GetCenterCode= request.POST['MCentercode'] 
  GetCenterPass = request.POST['MCenterpassword'] 
  try:
    CheckCenterEditLogin = models.MedicalCenter.objects.get(CenterCode = GetCenterCode, Password=GetCenterPass)
    request.session['GetCenterCode_se'] = GetCenterCode
    request.session['GetCenterPasse_se'] = GetCenterPass
    print('center id after from CenterEditProfileLogin-------->' + (GetCenterCode))
    return render(request,'MedicalCenter/CenterChooseOption.html', {})
  except:
    print('NOTEXISt----------- in Medical Center Model----- Or Check Your PassWord ------NOTEXISt')
    return render(request,'MedicalCenter/CenterEditProfileLogin.html', {})





def CenterUpdate(request):
  GetCenterCode  =  request.session['GetCenterCode_se']
  GetCenterPass = request.session['GetCenterPasse_se']
  try:
    CheckToOpenUpdateForm = models.MedicalCenter.objects.get(CenterCode=GetCenterCode, Password=GetCenterPass)
    print('center id after add form CenterUpdate-------->' + (GetCenterCode))
    return render(request,'MedicalCenter/CenterUpdateData.html', {'CenterData' : CheckToOpenUpdateForm})
  except:
    return render(request,'MedicalCenter/CenterEditProfileLogin.html', {})
  
def CenterUpgrade(request):    
  GetCenterCode  =  request.session['GetCenterCode_se']
  Password = request.POST['Password']
  OldPassword= request.POST['OldPassword']
  GetCenterType = request.POST['CenterType']
  CenterName = request.POST['CenterName']
  CenterGov = request.POST['CenterGov']
  CurrentAddress= request.POST['CurrentAddress']
  FirstPhone= request.POST['FirstPhone']
  SecoundPhone= request.POST['SecoundPhone']
  
  
  try:
    getMedicalCenterData = models.MedicalCenter.objects.get(CenterCode=GetCenterCode) 
    newCenter = models.MedicalCenter(    
        CenterCode = GetCenterCode,
        Password  =  Password,
        CenterName  =   CenterName,
        CenterType = GetCenterType,
        CenterGov  =  CenterGov,
        CurrentAddress  =  CurrentAddress,
        FirstPhone  =  FirstPhone,
        SecoundPhone  =  SecoundPhone,
        RegisteredDate=getMedicalCenterData.RegisteredDate
    )
    newCenter.save()
    print('-------------SAVE DONE-------------')
    print('-------------OldPass True-------------'+str(OldPassword))
    
    messages.success(request, 'Your Data Saved Successfully')
    return render(request,'MedicalCenter/CenterChooseOption.html', {})
  except:    
    print('----------Not Allowed To Edit DATA Check Your Old Pass----------')
    print('---------Old Pass-->>>'+str(OldPassword)+'<<<---------')    
    messages.success(request, 'Saved Data Field !')
    return render(request,'home.html', {})


def CenterAddRemoveDoctor(request):
  GetCenterCode  =  request.session['GetCenterCode_se']
  ShowCenterData = models.MedicalCenter.objects.get(CenterCode=GetCenterCode)
  getTableData = models.DocWorkOnCenter.objects.filter(CenterCode_id=GetCenterCode)
  print('center id after add form CenterUpdate-------->' + (GetCenterCode))
  return render(request,'MedicalCenter/CenterAddRemoveDoctor.html', {'CenterData' : ShowCenterData, 'TableData':getTableData})


def AddDoctorinCenter(request):
  GetSynCodForAddedDoc = request.POST['SynCodeAdd']  
  print('SynCodeAdd>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'+ str(GetSynCodForAddedDoc))
  GetCenterCode  =  request.session['GetCenterCode_se']    
  try:
    CheckifDocExist = models.MedicalSyndicateLicense.objects.get(SynCode=GetSynCodForAddedDoc)
    try:
      GetDocID = models.Doctor.objects.get(SynCode=GetSynCodForAddedDoc)
      
      try:
        Checkifexist = models.DocWorkOnCenter.objects.get(SynCode=GetSynCodForAddedDoc, CenterCode=GetCenterCode)
        print('Doctor Already Works In This Center!')
        messages.success(request, 'Doctor Already Works In This Center!')
        return render(request,'MedicalCenter/CenterChooseOption.html', {})
      except:
        CenterData = models.MedicalCenter.objects.get(CenterCode=GetCenterCode) 
        GetDocPerData = models.PersonalData.objects.get(PerNationalId=GetDocID.DoctorNationalId)
        GetDocSpec = models.MedicalSyndicateLicense.objects.get(SynCode=GetSynCodForAddedDoc)
        print('Get Center Data Done------------------>>>'+str(CenterData.CenterCode))
        CheckifSignedUpBefore = models.Doctor.objects.get(SynCode=GetSynCodForAddedDoc)
        print('-------<< Doctor Exist In Doctor Model >>--------')
        print('-------<< GetCenterCode >>-------->>>>>>>>>>>>>>>>'+ str(GetCenterCode))  
        SaveData = models.DocWorkOnCenter(
          CenterCode_id=CenterData.CenterCode,
          SynCode_id=GetSynCodForAddedDoc,
          DoctorName=GetDocPerData.FullName,
          DoctorNationalId=GetDocPerData.PerNationalId.PerNationalId,
          Specialization1=GetDocSpec.Specialization1,
          Specialization2=GetDocSpec.Specialization2
        )
        SaveData.save()
        SaveinHistory = models.DocWorkOnCenterHistory(
          CenterCode=CenterData.CenterCode,
          SynCode=GetSynCodForAddedDoc,
          DoctorName=GetDocPerData.FullName,
          DoctorNationalId=GetDocPerData.PerNationalId.PerNationalId,
          Specialization1=GetDocSpec.Specialization1,
          Specialization2=GetDocSpec.Specialization2
        )
        SaveinHistory.save()
        getTableData = models.DocWorkOnCenter.objects.filter(CenterCode_id=GetCenterCode)
        print('-------<< Doctor Saved in doc workon center>>--------')
        messages.success(request, 'Doctor Added in Center')
        return render(request,'MedicalCenter/CenterChooseOption.html', {})
    except:
      print('Doctor Doesn\'t Exist in Doctor model')
      messages.success(request, 'Doctor Add Field !')
      return render(request,'MedicalCenter/CenterChooseOption.html', {})
  except:
    print('Doctor Doesn\'t Exist in Ministry')
    messages.success(request, 'Doctor Add Field !')
    return render(request,'MedicalCenter/CenterChooseOption.html', {})
    
    
def RemoveDoctor(request):  
  RemovedDocCode = request.POST['ShowDocId']
  print(RemovedDocCode)
  GetCenterCode  =  request.session['GetCenterCode_se']
  try:
    GetCenterCode  =  request.session['GetCenterCode_se']
    ShowCenterData = models.MedicalCenter.objects.get(CenterCode=GetCenterCode)
    getTableData = models.DocWorkOnCenter.objects.filter(CenterCode_id=GetCenterCode)
    GetRemovableID = models.DocWorkOnCenter.objects.get(DoctorNationalId=RemovedDocCode, CenterCode_id=GetCenterCode)
    RemovedDoc = models.DocWorkOnCenter( id = GetRemovableID.id)
    RemovedDoc.delete()  
    return render(request,'MedicalCenter/CenterChooseOption.html', {})
  except:
    messages.success(request, 'Select Doctor To Remove !')
    return render(request,'MedicalCenter/CenterAddRemoveDoctor.html', {'CenterData' : ShowCenterData, 'TableData':getTableData})


def CenterWorkOnLogin(request):
  return render(request,'MedicalCenter/CenterWorkOnLogin.html', {})

def CenterWorkOnDoctorLogin(request):
  GetMCenterCode= request.POST['MCenterCode'] 
  GetMCenterPass = request.POST['password']  
  try:
    CHECK_IF_EXIST = models.HealthMinistryLicenseCenter.objects.get(CenterCode=GetMCenterCode, Password=GetMCenterPass)
    request.session['GetMCenterCode_se'] = GetMCenterCode
    print('Center id after add form CenterWorkOnDoctorLogin-------->' + (GetMCenterCode))  
    print('Center Exist In Ministry')
    return render(request,'MedicalCenter/CenterWorkOnDoctorLogin.html', {})
  except:
    print('Center NOT Exist In Ministry')
    messages.success(request, 'Login Field !')
    return render(request,'MedicalCenter/CenterWorkOnLogin.html', {})


def CenterPatientIdLogin(request):
  GetSyndicate_Code = request.POST['Syndicate_Code']
  GetSyndicate_Pass = request.POST['password']
  GetMCenterCode = request.session['GetMCenterCode_se']
  try:
    CheckDoctorNCenter = models.DocWorkOnCenter.objects.get(SynCode=GetSyndicate_Code, CenterCode=GetMCenterCode)
    try:
      CheckDocPass = models.Doctor.objects.get(SynCode=GetSyndicate_Code, Password=GetSyndicate_Pass)
      request.session['GetSyndicate_Code_se'] = GetSyndicate_Code
      print('Syndicate id after add form CenterPatientIdLogin-------->' + (GetSyndicate_Code))
      print('Center id after add form CenterPatientIdLogin-------->' + (GetMCenterCode))
      return render(request,'MedicalCenter/CenterPatientIdLogin.html', {})
    except:
      print('Check If YOu Exist In Doctor Model Or Check Your Password')
      return render(request,'MedicalCenter/CenterWorkOnDoctorLogin.html', {})
  except:
    print('!!!!!! Doctor Doesnt Allowed To Work In This Center !!!!!!')
    messages.success(request, 'Login Field !')
    return render(request,'MedicalCenter/CenterWorkOnLogin.html', {})

def CenterPatientPersonalData(request):
  GetPatient_National_ID= request.POST['Patient_National_ID'] 
  GetSyndicate_Code = request.session['GetSyndicate_Code_se']
  GetMCenterCode = request.session['GetMCenterCode_se']
  CenterDatta = models.MedicalCenter.objects.get(CenterCode=GetMCenterCode)
  DocGetData  = models.MedicalSyndicateLicense.objects.get(SynCode=GetSyndicate_Code)
  DocData     = models.PersonalData.objects.get(id = DocGetData.NationalId)
  try:
    PatientData = models.PersonalData.objects.get(PerNationalId=GetPatient_National_ID)
    request.session['GetPatient_National_ID_se'] = GetPatient_National_ID
    PatientDOB = PatientData.BirthDate
    print('---------------------->>>>>Patient BirthDate'+str(PatientDOB))
    CurrentDate = datetime.datetime.now().date() 
    print('---------------------->>>>>Current Date '+str(CurrentDate))
    Patient_age = relativedelta(CurrentDate, PatientDOB)
    print('-------------------<< DOB .YEARS>>-------------------------'+str(Patient_age.years))
    print('-------------------<< DOB .Months>>-------------------------'+str(Patient_age.months))
    print('-------------------<< DOB .Days>>-------------------------'+str(Patient_age.days))
    print('Center id after add form CenterPatientPersonalData-------->' + (GetMCenterCode))
    print('Syndicate id after add form CenterPatientPersonalData-------->' + (GetSyndicate_Code))
    print('Patient id after add form CenterPatientPersonalData-------->' + (GetPatient_National_ID))
    return render(request,'MedicalCenter/CenterPatientPersonalData.html', {'CenterData':CenterDatta,'Age':Patient_age, 'PatientData': PatientData, 'DoctorData':DocData})
  except:
    print('Patient Doesnt Siogned Up Before')
    messages.success(request, 'Login Field !')
    return render(request,'MedicalCenter/CenterPatientIdLogin.html', {})

def CenterMedicalHistory(request):
  GetPatient_National_ID = request.session['GetPatient_National_ID_se']
  GetSyndicate_Code = request.session['GetSyndicate_Code_se']
  GetMCenterCode = request.session['GetMCenterCode_se']
  CenterDatta = models.MedicalCenter.objects.get(CenterCode=GetMCenterCode)
  DocGetData  = models.MedicalSyndicateLicense.objects.get(SynCode=GetSyndicate_Code)
  DocData     = models.PersonalData.objects.get(id = DocGetData.NationalId)
  PatientData = models.PersonalData.objects.get(PerNationalId=GetPatient_National_ID)
  TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatient_National_ID)  
  print('Center id after add form CenterMedicalHistory-------->' + (GetMCenterCode))
  print('Syndicate id after add form CenterMedicalHistory-------->' + (GetSyndicate_Code))
  print('Patient id after add form CenterMedicalHistory-------->' + (GetPatient_National_ID))
  return render(request,'MedicalCenter/CenterMedicalHistory.html', {'DoctorData':DocData, 'TableData':TableData, 'PatientData':PatientData, 'CenterData':CenterDatta})

def CenterSaveReport(request):  
  GetMedicalReport= request.POST['AddMReport']
  GetTreatment= request.POST['AddTreatment']
  GetPatient_National_ID = request.session['GetPatient_National_ID_se']
  GetSyndicate_Code = request.session['GetSyndicate_Code_se']
  GetMCenterCode = request.session['GetMCenterCode_se']
  CenterDatta = models.MedicalCenter.objects.get(CenterCode=GetMCenterCode)
  DocGetData  = models.MedicalSyndicateLicense.objects.get(SynCode=GetSyndicate_Code)
  DocData     = models.PersonalData.objects.get(id = DocGetData.NationalId)
  PatientData = models.PersonalData.objects.get(PerNationalId=GetPatient_National_ID)
  TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatient_National_ID)
  PatientDOB = PatientData.BirthDate
  CurrentDate = datetime.datetime.now().date() 
  Patient_age = relativedelta(CurrentDate, PatientDOB)
  
  SaveData = models.MedicalHistory(
    PerNationalId_id= GetPatient_National_ID,
    CenterCode=GetMCenterCode,
    CenterName=CenterDatta.CenterName,
    SynCode=GetSyndicate_Code,
    DoctorNationalId=DocData.PerNationalId.PerNationalId,
    DoctorName=DocData.FullName,
    MedicalReport=GetMedicalReport,
    Treatment=GetTreatment,    
    
  )
  SaveData.save()  
  messages.success(request, 'Report Saved Successfully')
  return render(request,'MedicalCenter/CenterPatientPersonalData.html', {'CenterData':CenterDatta,'Age':Patient_age, 'PatientData': PatientData, 'DoctorData':DocData})


def NewCenterPatient(request):
  GetSyndicate_Code = request.session['GetSyndicate_Code_se']
  GetMCenterCode = request.session['GetMCenterCode_se']
  print('Center id after add form CenterMedicalHistory-------->' + (GetMCenterCode))
  print('Syndicate id after add form CenterMedicalHistory-------->' + (GetSyndicate_Code))
  del request.session['GetPatient_National_ID_se']
  return render(request,'MedicalCenter/CenterPatientIdLogin.html', {})