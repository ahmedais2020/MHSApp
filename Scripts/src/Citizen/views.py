from django.shortcuts import render, redirect
from website import models
from django.contrib import messages

def CitizenAddLogin(request):  
  return render(request,'Citizen/CitizenAddLogin.html', {})

def CitizenAdd(request):  
  GetCitizenCode= request.POST['PersonalNationalID'] 
  request.session['GetCitizenCode_se'] = GetCitizenCode
  try:
    Fetch_data= models.Citizen.objects.get(PerNationalId = GetCitizenCode)    
    GetPersonalData = models.PersonalData.objects.get(PerNationalId= GetCitizenCode)   
    print('---------------You Are Already Exist On SyStem---------------Your UserName Is:'+str(Fetch_data.UserName)+'---------------')
    messages.success(request, 'You Are Already Exist On SyStem!')
    return render(request,'Citizen/CitizenEditLogin.html', {})
  except:

    print('Citizen id after add form CitizenAdd-------->' + (GetCitizenCode))
    return render(request,'Citizen/CitizenAdd.html', {'PerNationalId':GetCitizenCode})

def CitizenSave(request):
  Fname = request.POST['Fname']
  Gender= request.POST['Gender']
  Jop= request.POST['Jop']
  BrthGov = request.POST['BrthGov']
  CurrentGov= request.POST['CurrentGov']
  CurrentAdd= request.POST['CurrentAdd']
  FNo = request.POST['FNo']
  SNo= request.POST['SNo']
  Email= request.POST['Email']
  FRelName = request.POST['FRelName']
  FRelNo= request.POST['FRelNo']
  SRelName= request.POST['SRelName']
  SRelNo= request.POST['SRelNo']
  Passport = request.POST['Passport']
  PerID = request.POST['PerID']
  BirthDate = request.POST['BirthDate']
  PerID= request.POST['PerID']
  UserName= request.POST['UserName']
  Pass= request.POST['Pass']

  newCit = models.Citizen(
    PerNationalId = PerID,
    UserName =  UserName,
    Password =  Pass,
  )
  newCit.save()
  newPer = models.PersonalData(
    FullName = Fname,
    Gender  =   Gender,
    Job     =    Jop,
    BirthGov   = BrthGov,
    CurrentGov  = CurrentGov,
    CurrentAddress = CurrentAdd,
    FirstPhone =  FNo,
    SecoundPhone = SNo,
    Email    =      Email,
    FirstRelName  = FRelName,
    FirstRelPhone = FRelNo,
    SecoundRelName =  SRelName,
    SecoundRelPhone = SRelNo,
    PassportNo =   Passport,
    PerNationalId_id = PerID,
    BirthDate  = BirthDate,
  )
  newPer.save()
  messages.success(request, 'Your Data Saved Successfully')
  return render(request,'home.html', {})

def CitizenEditLogin(request):
  return render(request,'Citizen/CitizenEditLogin.html', {})

def CitizenEdit(request):
  GetCitizenUsername = request.POST['username'] 
  request.session['GetCitizenCode_se'] = GetCitizenUsername
  GetPasswordLogin = request.POST['password']
  request.session['GetPasswordLogin_se'] = GetPasswordLogin
  print ('UserName from login--------------->>>'+str(GetCitizenUsername))
  print ('Password from login--------------->>>'+str(GetPasswordLogin))
  try:
    Fetch_data = models.Citizen.objects.get(UserName=GetCitizenUsername , Password=GetPasswordLogin)   
    print('Fetched Data for citizen Done ------> '+ str(Fetch_data.PerNationalId))
    GetPersonalData = models.PersonalData.objects.get(PerNationalId_id = Fetch_data.PerNationalId)                             
    print('Citizen Username after add form CitizenEdit-------->' + str(GetCitizenUsername))  
    return render(request,'Citizen/CitizenEdit.html', {'PersonalData':GetPersonalData, 'DBPass':Fetch_data.Password,'GetUsername':Fetch_data})
  except:
    print('---------------Wrong UserName Or Passwod!---------------')
    messages.success(request, 'Login Failed !')
    return render (request, 'home.html')

def UpdradeCitizenData(request):    
  GetCitizenUsername  =  request.session['GetCitizenCode_se']
  GetPasswordLogin  =  request.session['GetPasswordLogin_se']
  print('Citizen Username after add form GetCitizenUsername-------->' + (GetCitizenUsername))
  print('Citizen Password after add form GetPasswordLogin-------->' + (GetPasswordLogin))
  Gett_data = models.Citizen.objects.get(UserName=GetCitizenUsername , Password=GetPasswordLogin)   
  GetPersonalData = models.PersonalData.objects.get(PerNationalId_id = Gett_data.PerNationalId)                             
  GetDjangoid= GetPersonalData.id
  Fname = request.POST['fullname']  
  Jop= request.POST['Jop']  
  CurrentGov= request.POST['CurrentGov']
  CurrentAdd= request.POST['CurrentAdd']
  FNo = request.POST['FNo']
  SNo= request.POST['SNo']  
  Email= request.POST['Email']
  FRelName = request.POST['FRelName']
  FRelNo= request.POST['FRelNo']
  SRelName= request.POST['SRelName']
  SRelNo= request.POST['SRelNo']
  Passport = request.POST['Passport']
  PerID = request.POST['NationalID']  
  UserName= request.POST['username']
  OldPass= request.POST['OldPass']
  Pass1= request.POST['Pass1']
  Pass2 = request.POST['Pass2']
  print('Citizen PerID -------->' + (PerID))
  try:
    citizenn = models.Citizen(
      UserName = UserName,
      Password= Pass1,
      PerNationalId=PerID
    )
    citizenn.save()
    SaveData = models.PersonalData(   
      id = GetDjangoid,
      FullName = Fname,
      Job     =    Jop,
      Gender= GetPersonalData.Gender,
      Date=GetPersonalData.Date,
      CurrentGov  = CurrentGov,
      BirthGov=GetPersonalData.BirthGov,
      BirthDate=GetPersonalData.BirthDate,
      CurrentAddress = CurrentAdd,
      FirstPhone =  FNo,
      SecoundPhone = SNo,
      Email    =      Email,
      FirstRelName  = FRelName,
      FirstRelPhone = FRelNo,
      SecoundRelName =  SRelName,
      SecoundRelPhone = SRelNo,
      PassportNo =   Passport,
      PerNationalId_id = PerID,
    )
    SaveData.save()
    messages.success(request, 'Data Saved Successfully')
    return render (request, 'home.html')
  except:    
    Fetch_Pass = models.Citizen.objects.get(UserName=GetCitizenUsername , Password=GetPasswordLogin)   
    print('----------Not Allowed To Edit DATA Check Your Old Pass----------')
    print('---------Old Pass-->>>'+str(OldPass)+'<<<---------')
    print('-------------OldPass db-------------'+str(Fetch_Pass.Password))
    return render(request,'Citizen/CitizenEditLogin.html', {})

def CitizenShowLogin(request):
  return render(request,'Citizen/CitizenShowLogin.html', {})

def CitizenShowMedicalHistory(request):
  GetCitizenUsername= request.POST['username'] 
  request.session['GetCitizenCode_se'] = GetCitizenUsername
  GetPasswordLogin=request.POST['password']
  try:
    Fetch_data = models.Citizen.objects.get(UserName=GetCitizenUsername , Password=GetPasswordLogin) #  PerNational Id
    GetPatientdata = models.PersonalData.objects.get(PerNationalId=Fetch_data.PerNationalId)
    GetTableData = models.MedicalHistory.objects.filter(PerNationalId=Fetch_data.PerNationalId)
    print('Citizen Username after add form CitizenEdit-------->' + str(GetCitizenUsername)) 
    return render(request,'Citizen/CitizenShowMedicalHistory.html', {'TableData':GetTableData, 'PatientData':GetPatientdata})
  except:
    print('---------------Wrong UserName Or Passwod!---------------')
    messages.success(request, 'Login Failed !')
    return render(request,'Citizen/CitizenShowLogin.html', {})

