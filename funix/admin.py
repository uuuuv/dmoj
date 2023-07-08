from django.contrib import admin
from funix.models import ProblemTestCaseData, SuspiciousSubmissionBehavior
# Register your models here.
admin.site.register(ProblemTestCaseData)
admin.site.register(SuspiciousSubmissionBehavior)