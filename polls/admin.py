
from django.contrib import admin

from .models import Question
from .models import RSVP
from .models import InvitedGuest

admin.site.register(Question)
admin.site.register(RSVP)
admin.site.register(InvitedGuest)