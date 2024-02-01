# MainApp/stream/admin.py

from django.contrib import admin

from MainApp.stream.models.live_stream import LiveStream


@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'is_active')
    list_filter = ('is_active', 'start_time')
