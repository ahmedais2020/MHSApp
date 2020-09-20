from django.shortcuts import render
from website import models

#--------------------------------------------------------------------------------------#
def PassportPatientIdLogin(request):
  return render(request,'Passport/PassportPatientIdLogin.html', {})

def PassportMedicalHistory(request):   
  GetPassportNumber= request.POST['PassportNumber'] 
  try:
    checkifexist = models.PersonalData.objects.get(PassportNo=GetPassportNumber)
    getdata = models.MedicalHistory.objects.filter(PerNationalId_id=checkifexist.PerNationalId)
    print('Passport id after add form PassportPatientIdLogin-------->' + (GetPassportNumber))
    return render(request,'Passport/PassportMedicalHistory.html', {'TableData' : getdata, 'PassportNo':GetPassportNumber})
  except:
    print('This Passport Not Exist in MedicalHistory Or Personal Data')
    return render(request,'Passport/PassportPatientIdLogin.html', {})