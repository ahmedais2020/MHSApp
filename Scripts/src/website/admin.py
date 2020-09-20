from django.contrib import admin
from .models import Citizen
from.models import PersonalData
from.models import Doctor
from.models import MedicalCenter
from.models import DocWorkOnCenter
from.models import DocWorkOnCenterHistory
from.models import DoctorPerson
from.models import PersonMedicalCenter
from.models import MedicalHistory
from.models import Laboratory
from.models import AnalystLabHistory
from.models import PersonLab
from.models import Analyst
from.models import AnalystWorkOnLab
from.models import HealthMinistryLicenseLab
from.models import HealthMinistryLicenseCenter
from.models import MedicalSyndicateLicense
from.models import MedicalAnalystLicense
# Register your models here.
admin.site.register(Citizen)
admin.site.register(PersonalData)
admin.site.register(Doctor)
admin.site.register(MedicalCenter)
admin.site.register(DocWorkOnCenter)
admin.site.register(DocWorkOnCenterHistory)
admin.site.register(DoctorPerson)
admin.site.register(PersonMedicalCenter)
admin.site.register(MedicalHistory)
admin.site.register(Laboratory)
admin.site.register(AnalystLabHistory)
admin.site.register(PersonLab)
admin.site.register(Analyst)
admin.site.register(AnalystWorkOnLab)
admin.site.register(HealthMinistryLicenseLab)
admin.site.register(HealthMinistryLicenseCenter)
admin.site.register(MedicalSyndicateLicense)
admin.site.register(MedicalAnalystLicense)











