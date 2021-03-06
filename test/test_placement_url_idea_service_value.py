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
from yahoo_ads_display.models.placement_url_idea_service_value import PlacementUrlIdeaServiceValue  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestPlacementUrlIdeaServiceValue(unittest.TestCase):
    """PlacementUrlIdeaServiceValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlacementUrlIdeaServiceValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.placement_url_idea_service_value.PlacementUrlIdeaServiceValue()  # noqa: E501
        if include_optional :
            return PlacementUrlIdeaServiceValue(
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
                operation_succeeded = True,
                placement_url_idea = yahoo_ads_display.models.placement_url_idea.PlacementUrlIdea(
                    keyword = '0',
                    site_category = [
                        '0'
                        ],
                    search_url = '0',
                    ad_format = [
                        yahoo_ads_display.models.placement_url_idea_service_ad_format.PlacementUrlIdeaServiceAdFormat(
                            ad_style = '0',
                            ad_type = '0',
                            width = 56,
                            height = 56, )
                        ],
                    desktop_reaches = 56,
                    desktop_ad_requests = 56,
                    smart_phone_reaches = 56,
                    smart_phone_ad_requests = 56,
                    tablet_reaches = 56,
                    tablet_ad_requests = 56, )
            )
        else :
            return PlacementUrlIdeaServiceValue(
        )

    def testPlacementUrlIdeaServiceValue(self):
        """Test PlacementUrlIdeaServiceValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
