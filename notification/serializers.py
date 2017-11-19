#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.serializers
~~~~~~~~~~~~~~

- This file contains the Notification (email, sms, push) Serializers.
 """

# future
from __future__ import unicode_literals

# DRF
from rest_framework import serializers

# local

# own app
from notification import config


class NoneSerializer(serializers.Serializer):
    """
    """
    pass


class EmailNotificationSerializer(serializers.Serializer):
    """Email Notification Serializer

    """
    host = serializers.CharField(required=True, help_text="Email host")
    to = serializers.EmailField(required=True)
    from_email = serializers.EmailField(required=False)
    subject = serializers.CharField(required=True)
    body = serializers.CharField(required=True)
    html_message = serializers.BooleanField(default=False)
    provider = serializers.ChoiceField(required=True, choices=config.EMAIL_NOTIFICATION_PROVIDER)
    notification_type = serializers.CharField(default=config.EMAIL)

    def validate_from_email(self, from_email):
        """
        :param from_email: from_email value send by client
        :return:
        """
        if not from_email:
            return config.DEFAULT_FROM_EMAIL
        return from_email


class SMSNotificationSerializer(serializers.Serializer):
    """SMS Notification Serializer

    """
    to = serializers.CharField(required=True)
    from_ = serializers.CharField(required=False)
    body = serializers.CharField(required=True)
    provider = serializers.ChoiceField(required=True, choices=config.SMS_NOTIFICATION_PROVIDER)
    notification_type = serializers.CharField(default=config.SMS)


class GmailSerilaizer(EmailNotificationSerializer):
    """Gamil Serializer

    """
    username = serializers.CharField(required=True, help_text="Gmail Account Username")
    password = serializers.CharField(required=True, help_text="Gmail Account Password")


class SendGridSerilaizer(EmailNotificationSerializer):
    """Sendgrid Serializer

    """
    # sendgrid_api_key = serializers.CharField(required=True, help_text="SendGrid API key.")
    username = serializers.CharField(required=True, help_text="Sendgrid Account Username")
    password = serializers.CharField(required=True, help_text="Sendgrid Account Password")

class PlivoSerilaizer(SMSNotificationSerializer):
    """Plivo Serializer

    """
    auth_id = serializers.CharField(required=True, help_text="Plivo Auth ID.")
    auth_token = serializers.CharField(required=True, help_text="Plivo Auth Token.")


class TwilioSerilaizer(SMSNotificationSerializer):
    """Twilio Serializer

    """
    account_sid = serializers.CharField(required=True, help_text="Twilio Account SID.")
    auth_token = serializers.CharField(required=True, help_text="Twilio Auth Token.")


class Msg91Serilaizer(SMSNotificationSerializer):
    """Msg91 Serializer

    """
    auth_key = serializers.CharField(required=True, help_text="Msg91 Auth key.")
