# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class IpAccessControlListTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sip \
                                 .ip_access_control_lists.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0",
                "ip_access_control_lists": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                        "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                        "friendly_name": "aaaa",
                        "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "subresource_uris": {
                            "ip_addresses": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAddresses.json"
                        },
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    }
                ],
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0",
                "ip_access_control_lists": [],
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json?PageSize=50&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists.list()
        
        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sip \
                                 .ip_access_control_lists.create(friendly_name="friendly_name")
        
        values = {
            'FriendlyName': "friendly_name",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                "friendly_name": "aaaa",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subresource_uris": {
                    "ip_addresses": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAddresses.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists.create(friendly_name="friendly_name")
        
        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sip \
                                 .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                "friendly_name": "aaaa",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subresource_uris": {
                    "ip_addresses": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAddresses.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sip \
                                 .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(friendly_name="friendly_name")
        
        values = {
            'FriendlyName': "friendly_name",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Fri, 17 Jul 2015 21:25:15 +0000",
                "date_updated": "Fri, 17 Jul 2015 21:25:15 +0000",
                "friendly_name": "aaaa",
                "sid": "ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subresource_uris": {
                    "ip_addresses": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAddresses.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(friendly_name="friendly_name")
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sip \
                                 .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SIP/IpAccessControlLists/ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sip \
                                      .ip_access_control_lists(sid="ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)
