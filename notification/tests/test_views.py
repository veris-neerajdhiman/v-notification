#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notification.tests.test_views
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes Test cases for Notification Views .

"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.test import TestCase
from django.core.urlresolvers import reverse


class SMSNotificationTestCase(TestCase):
    """Handles SMS Notification Test Cases

    """

    def setUp(self):
        pass

    def test_plivo_notification(self):
        """Test Plivio notification.

        """
        url = reverse('notification-urls:plivo-notification')

        # FixMe : Authid & Auth_token are fake, lib don't valdate auth_id & token so in case of
        # FixMe : (contd. ) wrong tokens were used, Lib will not raise nay error of wrong credentials.
        data = {
            "to": "+919818887844",
            "from_": "plivo",
            "provider": "plivo",
            "auth_id": "test-auth-id",
            "auth_token": "test-auth-token",
            "body": "Plivo micro service message"
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)

    def test_twilio_notification(self):
        """Test Twilio Notification.

        """
        url = reverse('notification-urls:twilio-notification')

        print("you need to specify Twilio credentials.")

        data = {
            "to": "+919818887844",
            "from_": "<phone number needed>",
            "provider": "twilio",
            "account_sid": "<account-sid>",
            "auth_token": "<auth token>",
            "body": "Twilio micro service message"
        }
        pass
        # response = self.client.post(url, data=data)
        # self.assertEqual(response.status_code, 200)


class EmailNotificationTestCase(TestCase):
    """Handles Email Notification Test Cases

    """

    def setUp(self):
        pass

    def test_gmail_notification(self):
        """Test Gmail notification.

        """
        url = reverse('notification-urls:gmail-notification')

        # FixMe : Gmail credentials are fake, lib don't validate credentials so in case of
        # FixMe : (contd. ) wrong tokens were used, Lib will not raise nay error of wrong credentials.
        data = {
            "to": "akki.inforian@gmail.com",
            "from_email":"admin@qq.com",
            "subject": "micro service integration",
            "provider": "gmail",
            "body": "<h1>['Thisfieldisrequired.']</h1>",
            "html_message":"true",
            "username": "<username>",
            "host": "<host>",
            "password": "<password>"
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)

    def test_sendgrid_notification(self):
        """Test Sendgrid notification.

        """
        url = reverse('notification-urls:gmail-notification')

        # FixMe : Sendgrid credentials are fake, lib don't validate credentials so in case of
        # FixMe : (contd. ) wrong tokens were used, Lib will not raise nay error of wrong credentials.
        data = {
            "to": "akki.inforian@gmail.com",
            "from_email":"admin@qq.com",
            "subject": "micro service integration",
            "provider": "gmail",
            "body": "<h1>['Thisfieldisrequired.']</h1>",
            "html_message":"true",
            "username": "<username>",
            "host": "<host>",
            "password": "<password>"
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 200)


class PushNotificationTestCase(TestCase):
    """Handles Push Notification Test Cases

    """

    def setUp(self):
        pass

    def test_push_notification(self):
        """Test Push Notification.

        """
        # ToDo : Add push notification test case , when ever push feature is added in this micro-service.
        pass

