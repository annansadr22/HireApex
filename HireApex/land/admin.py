from django.contrib import admin
from .models import UserProfile, JobProfile, Language, SkillSet

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(JobProfile)
admin.site.register(Language)
admin.site.register(SkillSet)
