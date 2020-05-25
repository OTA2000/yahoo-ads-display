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
from yahoo_ads_display.models.feed_set import FeedSet  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestFeedSet(unittest.TestCase):
    """FeedSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeedSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.feed_set.FeedSet()  # noqa: E501
        if include_optional :
            return FeedSet(
                account_id = 56,
                condition_sets = [
                    yahoo_ads_display.models.feed_set_service_condition_set.FeedSetServiceConditionSet(
                        condition_type = 'CATEGORY_ID',
                        or_conditions = [
                            yahoo_ads_display.models.feed_set_service_condition.FeedSetServiceCondition(
                                compare_operator = 'EQUAL',
                                value = '0', )
                            ], )
                    ],
                feed_id = 56,
                feed_set_id = 56,
                feed_set_name = '0',
                is_default_set = True,
                item_count = 56
            )
        else :
            return FeedSet(
        )

    def testFeedSet(self):
        """Test FeedSet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
