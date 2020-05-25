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
from yahoo_ads_display.models.placement_url_list_service_mutate_response import PlacementUrlListServiceMutateResponse  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestPlacementUrlListServiceMutateResponse(unittest.TestCase):
    """PlacementUrlListServiceMutateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PlacementUrlListServiceMutateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.placement_url_list_service_mutate_response.PlacementUrlListServiceMutateResponse()  # noqa: E501
        if include_optional :
            return PlacementUrlListServiceMutateResponse(
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
                rid = '0',
                rval = yahoo_ads_display.models.placement_url_list_service_return_value.PlacementUrlListServiceReturnValue(
                    values = [
                        yahoo_ads_display.models.placement_url_list_service_value.PlacementUrlListServiceValue(
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
                            url_list = yahoo_ads_display.models.placement_url_list.PlacementUrlList(
                                account_id = 56,
                                description = '0',
                                unknown_domain_flg = 'TRUE',
                                url_list_id = 56,
                                url_list_name = '0',
                                urls = [
                                    yahoo_ads_display.models.placement_url_list_service_url_list.PlacementUrlListServiceUrlList(
                                        placement_url = '0',
                                        url_active_flg = 'PAUSED', )
                                    ], ), )
                        ], )
            )
        else :
            return PlacementUrlListServiceMutateResponse(
        )

    def testPlacementUrlListServiceMutateResponse(self):
        """Test PlacementUrlListServiceMutateResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
