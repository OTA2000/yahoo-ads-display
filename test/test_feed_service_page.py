# coding: utf-8

"""
    Yahoo!広告 ディスプレイ広告 API リファレンス / Yahoo! Ads Display Ads API Reference

    <div lang=\"ja\">Yahoo!広告 ディスプレイ広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Display Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import yahoo_ads_display
from yahoo_ads_display.models.feed_service_page import FeedServicePage  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestFeedServicePage(unittest.TestCase):
    """FeedServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeedServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.feed_service_page.FeedServicePage()  # noqa: E501
        if include_optional :
            return FeedServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_display.models.feed_service_value.FeedServiceValue(
                        feed = yahoo_ads_display.models.feed.Feed(
                            account_id = 56,
                            feed_id = 56,
                            feed_name = '0',
                            item_count = 56,
                            approved_item_count = 56,
                            dis_approved_item_count = 56, ),
                        upload_limits = [
                            yahoo_ads_display.models.feed_service_upload_limit.FeedServiceUploadLimit(
                                source_type = 'FTP_SCHEDULE',
                                control_type = 'UPLOAD_COUNT_LIMIT',
                                limit_value = 56, )
                            ],
                        errors = [
                            yahoo_ads_display.models.error.Error(
                                code = '0',
                                message = '0',
                                details = [
                                    yahoo_ads_display.models.error_detail.ErrorDetail(
                                        request_key = '0',
                                        request_value = '0', )
                                    ], )
                            ],
                        operation_succeeded = True, )
                    ]
            )
        else :
            return FeedServicePage(
        )

    def testFeedServicePage(self):
        """Test FeedServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
