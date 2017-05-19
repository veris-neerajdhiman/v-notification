#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.views
~~~~~~~~~~~~~~~~~~~~

- This file contains notification service actions like sed sms, email, push notifications.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

# local
from libs import notifyAll as notification

# own app
from notification import serializers


class NotificationViewSet(viewsets.ModelViewSet):
    """Notification Viewset, every notification http request handles by this class

    """
    # TODO : remove AllowAny permission with proper permission class
    permission_classes = (permissions.AllowAny, )

    def get_serializer_class(self):
        if self.action == 'send_email':
            return serializers.EmailNotificationSerializer
        elif self.action == 'send_sms':
            return serializers.SMSNotificationSerializer
        elif self.action == 'send_push':
            return serializers.NoneSerializer
        return serializers.NoneSerializer

    def _validate(self, serializer, data):
        """

        :param serializer: serializer against which data to ve validated
        :param data: data to ve validated
        :return: validated data.
        """

        serializer_instance = serializer(data=data)
        serializer_instance.is_valid(raise_exception=True)
        return serializer_instance.data

    def send_email(self, request):
        """

        :param request:
        :return:

        POST Example :
        {
            "to": "example@gmail.com",
            "from_email":"admin@example.com",
            "subject": "micro service integration",
            "provider": "gmail",
            "body": "<h1>email Body comes here</h1>",
            "html_message":"true"
        }
        """
        serializer = self.get_serializer_class()
        data = self._validate(serializer, request.data)

        self.notify(data)
        return Response(status=status.HTTP_200_OK)

    def send_sms(self, request):
        """

        :param request:
        :return:

        POST EXAMPLE :
        {
            "to": "+9198********",
            "from_": "plivo",
            "provider": "plivo",
            "body": "micro service message"
        }
        """
        serializer = self.get_serializer_class()
        data = self._validate(serializer, request.data)

        self.notify(data)
        return Response(status=status.HTTP_200_OK)

    def send_push(self, request):
        """

        :param request:
        :return:
        """
        pass

    def notify(self, data):
        """

        :param data: Notification data
        """
        notify_lib = notification.NotifyAllLib()
        notify_lib.send_notification(**data)

