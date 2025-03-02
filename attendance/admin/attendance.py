from django.contrib import admin

from attendance.models.attendance import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass
