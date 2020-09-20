from django.contrib import admin
from django.urls import path, include
from Citizen.views import CitizenAddLogin, CitizenAdd, CitizenEditLogin, CitizenEdit,CitizenSave, CitizenShowLogin, CitizenShowMedicalHistory, UpdradeCitizenData
from Doctor.views import DocEditSave
from MedicalCenter.views import CenterRegisteredSave, CenterUpdate, CenterUpgrade, CenterSignupLogin,  CenterSignUp, CenterEditProfileLogin, AddDoctorinCenter, CenterChooseOption  , CenterAddRemoveDoctor, CenterWorkOnLogin, CenterWorkOnDoctorLogin, CenterPatientIdLogin, CenterSaveReport,RemoveDoctor, CenterPatientPersonalData, CenterMedicalHistory, CenterPatientIdLogin, NewCenterPatient
from Laboratory.views import  LabRegisteredSave
from Doctor.views import AddDoctorLogin, AddAnalystLogin, DoctorEditLogin, AnalystEditLogin, AddDoctor, AnalystEdit, EditAnalystSave, AddDoctorSave, AddAnalyst, AddAnalystSave, DoctorEdit, DoctorWorkOnLogin, SaveReport, PatientLogin, DoctorPatientPersonalData, DoctorWorkOn, NewPatient  
from Laboratory.views import LaboratoryAddBloodGroup, PatientBloodGroupLogin, AddBloodGroupSave, AddBloodGroup, LaboratorySignupLogin, LabSaveReport, LaboratorySignUp, LaboratoryEditProfileLogin, LaboratoryChooseOption, LaboratoryUpdateData, LabUpgradeData,LaboratoryAddRemoveAnalyst, LaboratoryWorkOnLogin, LaboratoryWorkOnAnalystLogin, LaboratoryPatientIdLogin, LaboratoryMedicalHistory, LaboratoryPatientIdLogin, LabRegisteredSave, NewLabPatient, RemoveAnalyst, AddlabAnalyst
from Others.views import  PassportPatientIdLogin, PassportMedicalHistory  
admin.site.site_header = "Medical History App Admin Panel"
admin.site.site_title = "Medical History App Admin Panel"
admin.site.site_index_title = " Welcome To Notes App Admin Panel"
admin.sites.AdminSite.index_title = 'Medical History App'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('home/', include('website.urls')),
    path('index/', include('website.urls')),
    path('test/', include('website.urls')),
    path('GeneraLinstructions/', include('website.urls')),
#---------------------------------------------------------------------------------
    path('DocEditSave/',DocEditSave ,name='DocEditSave' ),
    path('CitizenSave/',CitizenSave ,name='CitizenSave' ),
    path('CenterRegisteredSave/',CenterRegisteredSave ,name='CenterRegisteredSave' ),
    path('LabRegisteredSave/',LabRegisteredSave ,name='LabRegisteredSave' ),
#---------------------------------------------------------------------------------
 
    path('CenterEditProfileLogin/CenterChooseOption/',CenterChooseOption, name='CenterChooseOption'),
    path('CenterEditProfileLogin/CenterChooseOption/CenterUpdate/',CenterUpdate, name='CenterUpdate'),
    path('CenterUpgrade/',CenterUpgrade, name='CenterUpgrade'),
    
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
 
    path('OurTeam/', include('website.urls')),
    path('admin/', include('website.urls')),
#---------------------------------------------------------------------------------
    path('CitizenAddLogin/',CitizenAddLogin, name='CitizenAddLogin'),
    path('CitizenAddLogin/CitizenAdd/',CitizenAdd, name='CitizenAdd'),
    path('CitizenEditLogin/',CitizenEditLogin, name='CitizenEditLogin'),
    path('CitizenEditLogin/CitizenEdit/',CitizenEdit, name='CitizenEdit'),
    path('CitizenEditLogin/CitizenEdit/UpdradeCitizenData',UpdradeCitizenData, name='UpdradeCitizenData'),
    path('CitizenShowLogin/', CitizenShowLogin, name='CitizenShowLogin'),
    path('CitizenShowLogin/CitizenShowMedicalHistory/',  CitizenShowMedicalHistory, name='CitizenShowMedicalHistory'),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('AddDoctorLogin/',AddDoctorLogin, name='AddDoctorLogin'),
    path('AddDoctorLogin/AddDoctor',AddDoctor, name='AddDoctor'),
    path('AddDoctorLogin/AddDoctor/AddDoctorSave',AddDoctorSave, name='AddDoctorSave'),
    path('AddAnalystLogin/AddAnalyst',AddAnalyst, name='AddAnalyst'),
    path('AddAnalystLogin/AddAnalyst/AddAnalystSave',AddAnalystSave, name='AddAnalystSave'),
    path('AddAnalystLogin/',AddAnalystLogin, name='AddAnalystLogin'),
    path('DoctorEditLogin/',DoctorEditLogin, name='DoctorEditLogin'),
    path('AnalystEditLogin/',AnalystEditLogin, name='AnalystEditLogin'),
    path('AnalystEditLogin/AnalystEdit/', AnalystEdit, name='AnalystEdit'),
    path('AnalystEditLogin/AnalystEdit/EditAnalystSave', EditAnalystSave, name='EditAnalystSave'),
    path('DoctorEditLogin/DoctorEdit/', DoctorEdit, name='DoctorEdit'),
    path('DoctorWorkOnLogin/', DoctorWorkOnLogin, name='DoctorWorkOnLogin'),
    path('DoctorWorkOnLogin/PatientLogin/', PatientLogin, name='PatientLogin'),
    path('DoctorWorkOnLogin/PatientIdLogin/DoctorPatientPersonalData', DoctorPatientPersonalData, name='DoctorPatientPersonalData'),
    path('DoctorWorkOnLogin/PatientIdLogin/DoctorWorkOn/',  DoctorWorkOn, name='DoctorWorkOn'),
    path('DoctorWorkOnLogin/PatientIdLogin/DoctorWorkOn/SaveReport',  SaveReport, name='SaveReport'),
    path('DoctorWorkOnLogin/PatientIdLogin/DoctorWorkOn/NewPatient',  NewPatient, name='NewPatient'),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('CenterSignupLogin/',CenterSignupLogin, name='CenterSignupLogin'),
    path('CenterSignupLogin/CenterSignUp/', CenterSignUp, name='CenterSignUp'),
    path('CenterEditProfileLogin/',CenterEditProfileLogin, name='CenterEditProfileLogin'), 
    path('CenterEditProfileLogin/CenterChooseOption/AddDoctorinCenter',AddDoctorinCenter, name='AddDoctorinCenter'), 
    path('CenterEditProfileLogin/CenterChooseOption/CenterAddRemoveDoctor',CenterAddRemoveDoctor, name='CenterAddRemoveDoctor'),
    path('CenterWorkOnLogin/', CenterWorkOnLogin, name='CenterWorkOnLogin'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/', CenterWorkOnDoctorLogin, name='CenterWorkOnDoctorLogin'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/CenterPatientIdLogin/',CenterPatientIdLogin, name='CenterPatientIdLogin'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/CenterPatientPersonalData', CenterPatientPersonalData, name='CenterPatientPersonalData'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/CenterMedicalHistory',CenterMedicalHistory, name='CenterMedicalHistory'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/CenterPatientIdLogin',CenterPatientIdLogin, name='CenterPatientIdLogin'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/SaveReport',CenterSaveReport, name='CenterSaveReport'),
    path('CenterEditProfileLogin/CenterChooseOption/RemoveDoctor',RemoveDoctor, name='RemoveDoctor'),
    path('CenterWorkOnLogin/CenterWorkOnDoctorLogin/CenterMedicalHistory/NewCenterPatient',NewCenterPatient, name='NewCenterPatient'),
   

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('LaboratorySignupLogin/',LaboratorySignupLogin, name='LaboratorySignupLogin'),
    path('LaboratorySignupLogin/LaboratorySignUp/', LaboratorySignUp, name='LaboratorySignUp'),
    path('LaboratoryEditProfileLogin/', LaboratoryEditProfileLogin, name='LaboratoryEditProfileLogin'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/', LaboratoryChooseOption, name='LaboratoryChooseOption'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/LaboratoryUpdateData',LaboratoryUpdateData, name='LaboratoryUpdateData'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/LabUpgradeData',LabUpgradeData, name='LabUpgradeData'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/LaboratoryAddRemoveAnalyst', LaboratoryAddRemoveAnalyst, name='LaboratoryAddRemoveAnalyst'),
    path('LaboratoryWorkOnLogin/', LaboratoryWorkOnLogin, name='LaboratoryWorkOnLogin'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/',LaboratoryWorkOnAnalystLogin, name='LaboratoryWorkOnAnalystLogin'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/LaboratoryPatientIdLogin/', LaboratoryPatientIdLogin, name='LaboratoryPatientIdLogin'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/LaboratoryMedicalHistory', LaboratoryMedicalHistory, name='LaboratoryMedicalHistory'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/LaboratoryPatientIdLogin',LaboratoryPatientIdLogin, name='LaboratoryPatientIdLogin'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/LabSaveReport',LabSaveReport, name='LabSaveReport'),
    path('LaboratoryWorkOnLogin/LaboratoryWorkOnAnalystLogin/LaboratoryMedicalHistory/NewLabPatient',NewLabPatient, name='NewLabPatient'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/RemoveAnalyst',RemoveAnalyst, name='RemoveAnalyst'),
    path('LaboratoryEditProfileLogin/LaboratoryChooseOption/AddlabAnalyst',AddlabAnalyst, name='AddlabAnalyst'),
    path('LaboratoryAddBloodGroup',LaboratoryAddBloodGroup, name='LaboratoryAddBloodGroup'),
    path('LaboratoryAddBloodGroup/PatientBloodGroupLogin',PatientBloodGroupLogin, name='PatientBloodGroupLogin'),
    path('LaboratoryAddBloodGroup/PatientBloodGroupLogin/AddBloodGroup',AddBloodGroup, name='AddBloodGroup'),
    path('LaboratoryAddBloodGroup/PatientBloodGroupLogin/AddBloodGroup/AddBloodGroupSave',AddBloodGroupSave, name='AddBloodGroupSave'),
    

   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
    path('PassportPatientIdLogin/',PassportPatientIdLogin, name='PassportPatientIdLogin'),
    path('PassportPatientIdLogin/PassportMedicalHistory',PassportMedicalHistory, name='PassportMedicalHistory'),
]
