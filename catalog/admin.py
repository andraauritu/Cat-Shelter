from django.contrib import admin

from .models import Cat, MedicalRecord, UserProfile, Adoption, Visit

admin.site.register(Cat)
admin.site.register(MedicalRecord)
admin.site.register(UserProfile)
admin.site.register(Adoption)
admin.site.register(Visit)
