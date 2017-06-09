#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.email
~~~~~~~~~~~~~~~~~~~~

- This file contains notification service for email Notifications.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework

# local

# own app
from notification import serializers, base


class GmailViewSet(base.NotificationViewSet):
    """Gmail ViewSet

    """
    serializer_class = serializers.GmailSerilaizer

    def gmail(self, request):
        """

        :param request:
        :return:
        """
        return self.send_email(request)


class SendGridViewSet(base.NotificationViewSet):
    """Sendgrid ViewSet

    """
    serializer_class = serializers.SendGridSerilaizer

    def sendgrid(self, request):
        """

        :param request:
        :return:
        """
        return self.send_email(request)
