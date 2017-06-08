#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.base
~~~~~~~~~~~~~~~~~~~~

- This file contains Base Class for Notification Viewset.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

# local
from libs import notifyAll as notification


class NotificationViewSet(viewsets.ModelViewSet):
    """Notification Viewset, every notification http request handles by this class

    """
    # TODO : remove AllowAny permission with proper permission class
    permission_classes = (permissions.AllowAny, )

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
        """
        serializer = self.get_serializer_class()
        data = self._validate(serializer, request.data)

        self.notify(data)
        return Response(status=status.HTTP_200_OK)

    def send_sms(self, request):
        """

        :param request:
        :return:
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
