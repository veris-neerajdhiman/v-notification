#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.sms
~~~~~~~~~~~~~~~~~~~~

- This file contains notification service for SMS Notifications.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework

# local

# own app
from notification import serializers, base


class PlivoViewSet(base.NotificationViewSet):
    """Plivo ViewSet

    """
    serializer_class = serializers.PlivoSerilaizer

    def plivo(self, request):
        """

        :param request:
        :return:
        """
        return self.send_sms(request)


class TwilioViewSet(base.NotificationViewSet):
    """Twilio ViewSet

    """
    serializer_class = serializers.TwilioSerilaizer

    def twilio(self, request):
        """

        :param request:
        :return:
        """
        return self.send_sms(request)