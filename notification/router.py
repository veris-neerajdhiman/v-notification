#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.router
~~~~~~~~~~~~~~~~~

- This file contains Notification service routers.
"""

# future
from __future__ import unicode_literals

# Django
from django.conf.urls import url

# own app
from notification import email, sms


gmail_notification = email.GmailViewSet.as_view({
    'post': 'gmail',
})

sendgrid_notification = email.SendGridViewSet.as_view({
    'post': 'sendgrid',
})

plivo_notification = sms.PlivoViewSet.as_view({
    'post': 'plivo',
})

twilio_notification = sms.TwilioViewSet.as_view({
    'post': 'twilio',
})

# push_notification = views.NotificationViewSet.as_view({
#     'post': 'send_push',
# })

urlpatterns = [
        url(r'^email/gmail/$',
            gmail_notification,
            name='gmail-notification'),
        url(r'^email/sendgrid/$',
            sendgrid_notification,
            name='sendgrid-notification'),
        url(r'^sms/plivo/$',
            plivo_notification,
            name='plivo-notification'),
        url(r'^sms/twilio/$',
            twilio_notification,
            name='twilio-notification'),
        # url(r'^push/$',
        #     push_notification,
        #     name='push-notification'),
]
