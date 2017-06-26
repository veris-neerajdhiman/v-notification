#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- micro_services.libs.notifyAll
~~~~~~~~~~~~~~

-   This file contains the notifyAll third party library classes/functions which we are going to use in Notification.
    micro-service, so every request to third party will goes from here so in future if we replace any lib with another
    our core code will not be changed , we just needs to update this file.

-   Here we will create a proxy class for actual lib which will reverse proxy the request to that lib.
 """


# future
from __future__ import unicode_literals

# 3rd party libs
from notifyAll.services import notifier

# rest-framework
from rest_framework.exceptions import ValidationError

# local
from notification import config as notification_settings


class NotifyAllLib(object):
    """A Proxy class of notifyAll library

    ref : https://github.com/inforian/django-notifyAll
    """

    def _prepare_notification_message(self, *args, **kwargs):
        """

        :return: notification message as per notification_type
        """
        if kwargs.get('notification_type') == notification_settings.EMAIL:
            return self._email_message(*args, **kwargs)
        elif kwargs.get('notification_type') == notification_settings.SMS:
            return self._sms_message(*args, **kwargs)
        elif kwargs.get('notification_type') == notification_settings.PUSH:
            return self._push_message(*args, **kwargs)
        else:
            raise ValidationError({'detail': 'Unknown notification service.'})

    def _email_message(self, *args, **kwargs):
        """

        :return: message and remaining kwargs (if exists they may be configuration keys)
        """
        context = {
            'subject': kwargs.pop('subject', ''),
            'body': kwargs.pop('body', ''),
            'html_message': kwargs.pop('body', '') if kwargs.pop('html_message') is True else None
        }

        return (
            {
                'source': kwargs.pop('from_email'),
                'destination': kwargs.pop('to'),
                'notification_type': notification_settings.EMAIL,
                'provider': kwargs.pop('provider'),
                'context': context,
            },
            kwargs
        )

    def _sms_message(self, *args, **kwargs):
        """

        :return:
        """
        return (
            {
                'source': kwargs.pop('from_', 'plivo'),
                'destination': kwargs.pop('to'),
                'notification_type': notification_settings.SMS,
                'provider': kwargs.pop('provider'),
                'context': {
                    'body': kwargs.pop('body')
                }
            },
            kwargs
        )

    def _push_message(self, *args, **kwargs):
        """

        :return:
        """
        pass

    def send_notification(self, *args, **kwargs):
        """

        :return: error if any otherwise send notification to respective destination
        """
        message, extra_kwargs = self._prepare_notification_message(*args, **kwargs)

        notification = notifier.Notifier(**message)

        try:
            notification.notify(**extra_kwargs)
        except Exception as e:
            raise ValidationError(e)

