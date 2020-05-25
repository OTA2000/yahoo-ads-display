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
from yahoo_ads_display.models.feed_data_service_selector import FeedDataServiceSelector  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestFeedDataServiceSelector(unittest.TestCase):
    """FeedDataServiceSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeedDataServiceSelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.feed_data_service_selector.FeedDataServiceSelector()  # noqa: E501
        if include_optional :
            return FeedDataServiceSelector(
                account_id = 56,
                feed_ids = [
                    56
                    ],
                file_upload_date_range = yahoo_ads_display.models.feed_data_service_file_upload_date_range.FeedDataServiceFileUploadDateRange(
                    end_date = '0',
                    start_date = '0', ),
                item_list_upload_ids = [
                    56
                    ],
                number_results = 1,
                start_index = 1,
                upload_statuses = [
                    'UPLOADED'
                    ]
            )
        else :
            return FeedDataServiceSelector(
                account_id = 56,
        )

    def testFeedDataServiceSelector(self):
        """Test FeedDataServiceSelector"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()