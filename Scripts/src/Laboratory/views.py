from django.shortcuts import render, redirect
from website import models
from django.contrib import messages
# LaboratoryCode
#--------------------------------------------------------------------------------------#
def LaboratorySignupLogin(request):
  return render(request,'Laboratory/LaboratorySignupLogin.html', {})

def LaboratorySignUp(request):
  GetLaboratoryCode= request.POST['LaboratoryCode'] 
  GetLaboratoryPass= request.POST['password'] 
  try:
    Checkifexist = models.HealthMinistryLicenseLab.objects.get(MinLabCode=GetLaboratoryCode, Password=GetLaboratoryPass)
    try:
      CheckLabCodeinLabModel = models.Laboratory.objects.get(LabCode=GetLaboratoryCode)
      print('---------------<< Laboratory Exist in Laboratory Model >>----------------')
      return render(request,'Laboratory/LaboratorySignupLogin.html', {})
    except:
      request.session['GetLaboratoryCode_se'] = GetLaboratoryCode
      print('Laboratory id after add form LaboratorySignUp-------->' + (GetLaboratoryCode))
      return render(request,'Laboratory/LaboratorySignUp.html', {'LabData':Checkifexist})
  except:
    print('----------<< Laboratory Doesnt Exist in Ministry Lab Or Check Your Password >>-------------')
    messages.success(request, 'UserName OR PAssword Wrong !')
    return render(request,'Laboratory/LaboratorySignupLogin.html', {})


def LabRegisteredSave(request):
  LabCode  = request.POST['LabCode']
  LabPassword = request.POST['Pass1']
  LabName = request.POST['LabName']
  LabType = request.POST['LabType']
  LabGov = request.POST['LabGov']
  CurrentAddress= request.POST['CurrentAddress']
  FirstPhone= request.POST['FirstPhone']
  SecoundPhone= request.POST['SecoundPhone']
  newLab = models.Laboratory(
    LabCode =  LabCode,
    LabPassword	= LabPassword ,  
    LabName	=  LabName,
    LabType=LabType,
    LabGov	=   LabGov,
    CurrentAddress	=  CurrentAddress,
    FirstPhone	= FirstPhone ,
    SecoundPhone	=  SecoundPhone,
  )
  newLab.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request,'home.html', {})
#-------------------------------------------------------------
def LaboratoryEditProfileLogin(request):
  return render(request,'Laboratory/LaboratoryEditProfileLogin.html', {})



#---------------------------  DisplayData= models.Test.objects.all() --------LabCode-----------------------
def LaboratoryChooseOption(request):
  GetLaboratoryCode= request.POST['LabCode'] 
  GetLaboratoryPass= request.POST['password']
  try:
    CheckifexisttinMinistry = models.HealthMinistryLicenseLab.objects.get(MinLabCode=GetLaboratoryCode)
    try:
      CheckLabEditLogin = models.Laboratory.objects.get(LabCode=GetLaboratoryCode, LabPassword=GetLaboratoryPass) 
      request.session['GetLaboratoryPass_se'] = GetLaboratoryPass
      request.session['GetLabCode_se'] = GetLaboratoryCode
      print('Laboratory id after add form LaboratoryChooseOption-------->' + (GetLaboratoryCode)) 
      return render(request,'Laboratory/LaboratoryChooseOption.html', {})
    except:
      print('NOTEXISt----------- in Laboratory Model----- Or Check Your PassWord ------NOTEXISt')
      messages.success(request, 'Login Field !')
      return render(request,'Laboratory/LaboratoryEditProfileLogin.html', {})
  except:
    print('---------------------<< This Lab Doesnt exist in Ministry!! >>---------------')
    messages.success(request, 'Login Field !')
    return render(request,'Laboratory/LaboratoryEditProfileLogin.html', {})

#-------------------------------------------------------------------------------------



def LaboratoryUpdateData(request):
  GetLaboratoryCode  =  request.session['GetLabCode_se']
  GetLaboratoryPass = request.session['GetLaboratoryPass_se']
  try:
    CheckToOpenUpdateForm = models.Laboratory.objects.get(LabCode=GetLaboratoryCode, LabPassword=GetLaboratoryPass)
    print('Laboratory id after add form LaboratoryUpdateData-------->' + (GetLaboratoryCode))
    return render(request,'Laboratory/LaboratoryUpdateData.html', {'LabData': CheckToOpenUpdateForm})
  except:
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})
  






def LabUpgradeData(request):
  GetLaboratoryCode  =  request.session['GetLabCode_se']
  GetLaboratoryPass = request.session['GetLaboratoryPass_se']
  GetLabName = request.POST['LabName']
  GetLabType= request.POST['LabType']
  GetLabGov= request.POST['LabGov']
  GetLabfirstnumber = request.POST['firstnumber']
  GetLabsecondnumber = request.POST['secondnumber']
  GetLabaddress= request.POST['address']
  GetLabOldPass= request.POST['OldPass']
  GetLabPass= request.POST['Pass1']
  CheckToOpenUpdateForm = models.Laboratory.objects.get(LabCode=GetLaboratoryCode, LabPassword=GetLaboratoryPass)
  try:
    print('-------------Try-------------'+ str(GetLabOldPass))
    CheckToUpdateForm = models.Laboratory.objects.get(LabCode=GetLaboratoryCode, LabPassword=GetLabOldPass)
    print('-------------Try-------------'+ str(GetLabOldPass))
    newData = models.Laboratory(
      LabCode=GetLaboratoryCode,
      LabPassword= GetLabPass,
      LabName=GetLabName,
      LabType=GetLabType,
      LabGov=GetLabGov,
      CurrentAddress=GetLabaddress,
      FirstPhone=GetLabfirstnumber,
      SecoundPhone=GetLabsecondnumber,
      Date=CheckToUpdateForm.Date
    )
    newData.save()
    print('-------------SAVE DONE-------------')
    messages.success(request, 'Your Data Saved Successfully')
    return render(request,'Laboratory/LaboratoryUpdateData.html', {'LabData': CheckToOpenUpdateForm})
  except:
    print('----------Not Allowed To Edit DATA Check Your Old Pass----------')
    messages.success(request, 'Edit Data Field !')
    print('---------Old Pass-->>>'+str(CheckToOpenUpdateForm.LabPassword)+'<<<---------')    
    return render(request,'home.html', {})


def LaboratoryAddRemoveAnalyst(request):
  GetLaboratoryCode  =  request.session['GetLabCode_se']
  print('Laboratory id after add form LaboratoryAddRemoveAnalyst-------->' + (GetLaboratoryCode))
  getLabData = models.Laboratory.objects.get(LabCode=GetLaboratoryCode)
  getTableData = models.AnalystWorkOnLab.objects.filter(LabCode=GetLaboratoryCode) 
  return render(request,'Laboratory/LaboratoryAddRemoveAnalyst.html', {'LabData': getLabData, 'TableData' : getTableData})

def AddlabAnalyst(request):
  GetAnalystCodeForAddAnalyst = request.POST['AddAnalystId']
  GetAnalystId = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalystCodeForAddAnalyst)
  print('AnalystNationalId---------------------->>'+str(GetAnalystId.NationalId))
  print('GetAnalystId---------------------->>'+str(GetAnalystId))
  GetLaboratoryCode  =  request.session['GetLabCode_se']
  try:
    CheckAnalystifExist = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalystCodeForAddAnalyst)
    try:
      CheckIfSignedUpBefore =models.Analyst.objects.get(AnalystCode=GetAnalystCodeForAddAnalyst)
      print('-------<< Analyst Exist In Analyst Model >>--------')
      try:
        CheckifexistinLab = models.AnalystWorkOnLab.objects.get(AnalystCode=GetAnalystCodeForAddAnalyst, LabCode=GetLaboratoryCode)
        print('Analyst Already Works In This Lab!')
        
        messages.success(request, 'Login Field !')
        return render(request,'home.html', {})

      except:
        LabData = models.Laboratory.objects.get(LabCode=GetLaboratoryCode)
        GetAnalystPerData = models.PersonalData.objects.get(PerNationalId=GetAnalystId.NationalId)
        GetAnalystSpec = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalystCodeForAddAnalyst)
        print('Get Lab Data Done------------------>>>'+str (LabData))
        SaveData = models.AnalystWorkOnLab(
          LabCode_id=LabData.LabCode,
          AnalystCode_id=GetAnalystCodeForAddAnalyst,
          AnalystName=GetAnalystPerData.FullName,
          AnalystNationalId=GetAnalystPerData.PerNationalId.PerNationalId,
          Specialization1=GetAnalystSpec.Specialization1,
          Specialization2=GetAnalystSpec.Specialization2
        )
        SaveData.save()
        SaveDataHistory = models.AnalystLabHistory(
          LabCode_id=LabData.LabCode,
          AnalystCode=GetAnalystCodeForAddAnalyst,
          AnalystName=GetAnalystPerData.FullName,
          AnalystNationalId=GetAnalystPerData.PerNationalId.PerNationalId,
          Specialization1=GetAnalystSpec.Specialization1,
          Specialization2=GetAnalystSpec.Specialization2
        )
        SaveDataHistory.save()
        print('Data Saved Done!')
        messages.success(request, 'Your Data Saved Successfully')
        return render(request,'Laboratory/LaboratoryChooseOption.html', {})
    except:
      messages.success(request, 'Login Field !')
      return render(request,'home.html', {})
  except:
      messages.success(request, 'Login Field !')
      return render(request,'home.html', {})
      


        
def RemoveAnalyst(request):
  RemoveAnalystCode = request.POST['ShowDocId']
  GetLaboratoryCode  =  request.session['GetLabCode_se']
  try:
    ShowLabData= models.Laboratory.objects.get(LabCode=GetLaboratoryCode)
    getTableData = models.AnalystWorkOnLab.objects.filter(LabCode=GetLaboratoryCode)
    Get_Removable_ID = models.AnalystWorkOnLab.objects.get(AnalystNationalId=RemoveAnalystCode, LabCode=GetLaboratoryCode)
    RemoveAnalyst = models.AnalystWorkOnLab(id = Get_Removable_ID.id)
    RemoveAnalyst.delete() 
    return render(request,'Laboratory/LaboratoryChooseOption.html', {})
  except:
    messages.success(request, 'Select Analyst To Remove !')
    return render(request,'Laboratory/LaboratoryAddRemoveAnalyst.html', {'LabData': ShowLabData, 'TableData' : getTableData})

def LaboratoryWorkOnLogin(request):
  return render(request,'Laboratory/LaboratoryWorkOnLogin.html', {})

def LaboratoryWorkOnAnalystLogin(request):# Keda ana khadt el code bta3 el center
  
  GetLaboratoryCode  =  request.POST['Laboratory_Code']
  request.session['GetLaboratoryCode___SE'] = GetLaboratoryCode
  GetLaboratoryPass = request.POST['password']
  request.session['GetLaboratoryPass___SE'] = GetLaboratoryCode
  print(str(GetLaboratoryCode))
  print(str(GetLaboratoryPass))
  try:
    Checkifexistt = models.HealthMinistryLicenseLab.objects.get(MinLabCode=GetLaboratoryCode, Password=GetLaboratoryPass)
    print('Laboratory id after add form LaboratoryWorkOnAnalystLogin-------->' + (GetLaboratoryCode))
    print('Laboratory Exist In Ministry')
    return render(request,'Laboratory/LaboratoryWorkOnAnalystLogin.html', {})
  except:
    print('Laboratory NOT Exist In Ministry OR Check Password')
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})

def LaboratoryPatientIdLogin(request):# Code El Center// Code El Analyst  
  GetAnalyst_Code= request.POST['Analyst_Code'] 
  GetAnalyst_Pass= request.POST['password'] 
  GetLaboratoryCode  =  request.session['GetLaboratoryCode___SE']
  GetLaboratoryPass = request.session['GetLaboratoryPass___SE']
  try:
    CheckAnalystNLaboratory= models.AnalystWorkOnLab.objects.get(AnalystCode=GetAnalyst_Code, LabCode=GetLaboratoryCode)
    try:
      CheckAnalystPass = models.Analyst.objects.get(AnalystCode=GetAnalyst_Code, Password=GetAnalyst_Pass)
      request.session['GetAnalyst_Code_se'] = GetAnalyst_Code
      print('Laboratory id after add form LaboratoryPatientIdLogin-------->' + (GetLaboratoryCode))
      print('Analyst id after add form LaboratoryPatientIdLogin-------->' + (GetAnalyst_Code))
      return render(request,'Laboratory/LaboratoryPatientIdLogin.html', {})
    except:
      messages.success(request, 'Login Field !')
      return render(request,'home.html', {})
  except:
    print('!!!!!! Analyst Doesnt Allowed To Work In This Laboratory !!!!!!')
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})



def LaboratoryMedicalHistory(request):# Code El Center// Code El Analyst// code el Patient
  GetPatient_National_ID= request.POST['Patient_National_ID'] 
  GetLaboratory_Code = request.session['GetLaboratoryCode___SE']
  GetAnalyst_Code  =  request.session['GetAnalyst_Code_se']
  print(str(GetAnalyst_Code))
  print(str(GetLaboratory_Code)) 
  request.session['Patient_National_ID__se'] = GetPatient_National_ID
  try:
    LabData = models.Laboratory.objects.get(LabCode=GetLaboratory_Code)
    AnalystGetData = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalyst_Code)
    AnalystData = models.PersonalData.objects.get(id = AnalystGetData.NationalId)
    TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatient_National_ID)  
  except:
    print('Make Sure Analyst Exist  in MedicalAnalystLicense')
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})
  try:
    PatinetData = models.PersonalData.objects.get(PerNationalId=GetPatient_National_ID)
    request.session['GetPatient_National_ID_se'] = GetPatient_National_ID
    print('Analyst id after add form LaboratoryMedicalHistory-------->' + (GetAnalyst_Code))
    print('Laboratory id after add form LaboratoryMedicalHistory-------->' + (GetLaboratory_Code))
    print('Patient id after add form LaboratoryMedicalHistory-------->' + (GetPatient_National_ID))
    return render(request,'Laboratory/LaboratoryMedicalHistory.html', {'TableData':TableData,'LabData': LabData, 'PatientData': PatinetData, 'AnalystData':AnalystData})
  except:        
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})


def LabSaveReport(request):
  GetAnalysisReport= request.POST['AnalysisReport']
  GetRaysReport= request.POST['RaysReport']
  GetPatient_National_ID = request.session['Patient_National_ID__se']
  PatinetData = models.PersonalData.objects.get(PerNationalId=GetPatient_National_ID)
  GetAnalyst_Code  =  request.session['GetAnalyst_Code_se']
  GetLaboratory_Code = request.session['GetLabCode_se']
  LabData = models.Laboratory.objects.get(LabCode=GetLaboratory_Code)
  AnalystGetData = models.MedicalAnalystLicense.objects.get(AnalystCode=GetAnalyst_Code)
  AnalystData = models.PersonalData.objects.get(id = AnalystGetData.NationalId)
  TableData = models.MedicalHistory.objects.filter(PerNationalId=GetPatient_National_ID)  
  HistoryData = models.MedicalHistory(
    PerNationalId_id= GetPatient_National_ID,
    LabCode= GetLaboratory_Code,
    LabName= LabData.LabName,
    SynCode=GetAnalyst_Code,
    AnalystNationalId=AnalystData.PerNationalId.PerNationalId,
    DoctorName=AnalystData.FullName,
    AnalysisReport= GetAnalysisReport,
    RaysReport=GetRaysReport,
    PassportNo=PatinetData.PassportNo
  )
  HistoryData.save()
  messages.success(request, 'Report Saved Successfully')
  return render(request,'Laboratory/LaboratoryPatientIdLogin.html', {})

def NewLabPatient(request):
  GetLaboratory_Code = request.session['GetLaboratory_Code_se']
  GetAnalyst_Code  =  request.session['GetAnalyst_Code_se']
  print('Analyst id after add form LaboratoryMedicalHistory-------->' + (GetAnalyst_Code))
  print('Laboratory id after add form LaboratoryMedicalHistory-------->' + (GetLaboratory_Code))
  del request.session['GetPatient_National_ID_se']
  return render(request,'Laboratory/LaboratoryPatientIdLogin.html', {})

def LaboratoryAddBloodGroup(request):
  return render(request,'Laboratory/LaboratoryBloodGroupLogin.html', {})
  
def PatientBloodGroupLogin(request):
  GetLabCode = request.POST['LaboratoryCode']
  request.session['GetLabCode____Se'] = GetLabCode
  GetLabPass = request.POST['password'] 
  try:
    CheckifExistinMinistry = models.HealthMinistryLicenseLab.objects.get(MinLabCode=GetLabCode)
    try:
      CheckUserAndPass= models.Laboratory.objects.get(LabCode=GetLabCode, LabPassword=GetLabPass)
      return render(request,'Laboratory/BloodGroupPatientLogin.html', {})
    except:
      print('Lab Doesnt Exist in Laboratory Model Or Check UR PAss')
      messages.success(request, 'Login Field !')
      return render(request,'home.html', {})
  except:
    print('Lab Doesnt Exist in Ministry')
    messages.success(request, 'Login Field !')
    return render(request,'home.html', {})

def AddBloodGroup(request):
  GetPAtientID= request.POST['Patient_National_ID']
  request.session['PatientData_SSEE'] = GetPAtientID
  try:
    Checkifexist = models.PersonalData.objects.get(PerNationalId_id=GetPAtientID)
    try:
      CheckBloodGroup = models.PersonalData.objects.get(PerNationalId_id=GetPAtientID).BloodGroup
      try:
        CheckBloodGroupVal = models.PersonalData.objects.get(PerNationalId_id=GetPAtientID, BloodGroup=None)         
        return render(request,'Laboratory/AddBloodGroup.html', {'PatientData':Checkifexist})
      except:
        print('This Patient Has BLoodGroup')
        messages.success(request, 'This Patient Has BLoodGroup: '+ str(CheckBloodGroup))
        return render(request,'Laboratory/BloodGroupPatientLogin.html', {})
    except:
      return render(request,'Laboratory/AddBloodGroup.html', {'PatientData':Checkifexist})
  except:
    print('Patient Not Exist in System')
    messages.success(request, 'Login Field !')
    return render(request,'Laboratory/BloodGroupPatientLogin.html', {})

def AddBloodGroupSave(request):
  getBloodGroup = request.POST['Add_Blood_Group']
  GetPAtientID = request.session['PatientData_SSEE']
  GetLaboratoryCode = request.session['GetLabCode____Se']
  GetLabData = models.Laboratory.objects.get(LabCode=GetLaboratoryCode)
  GetDatta = models.PersonalData.objects.get(PerNationalId_id=GetPAtientID)  
  new = models.PersonalData(
    id = GetDatta.PerNationalId.PerNationalId,
    FullName = GetDatta.FullName,
    Gender  =   GetDatta.Gender,
    Job     =    GetDatta.Job,
    BirthGov   = GetDatta.BirthGov,
    CurrentGov  = GetDatta.CurrentGov,
    CurrentAddress = GetDatta.CurrentAddress,
    FirstPhone =  GetDatta.FirstPhone,
    SecoundPhone = GetDatta.SecoundPhone,
    Email    =      GetDatta.Email,
    FirstRelName  = GetDatta.FirstRelName,
    FirstRelPhone = GetDatta.FirstRelPhone,
    SecoundRelName =  GetDatta.SecoundRelName,
    SecoundRelPhone = GetDatta.SecoundPhone,
    PassportNo =   GetDatta.PassportNo,
    PerNationalId_id = GetDatta.PerNationalId.PerNationalId,
    BirthDate  = GetDatta.BirthDate,
    BloodGroup= getBloodGroup,
    Date=GetDatta.Date,
    LabCode=GetLaboratoryCode,
    LabName=GetLabData.LabName
  )
  new.save()
  messages.success(request, 'BLoodGroup Added To This Patient: '+ str(getBloodGroup))
  return render(request,'Laboratory/BloodGroupPatientLogin.html', {})
  
