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
from yahoo_ads_display.models.media_service_page import MediaServicePage  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestMediaServicePage(unittest.TestCase):
    """MediaServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MediaServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.media_service_page.MediaServicePage()  # noqa: E501
        if include_optional :
            return MediaServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_display.models.media_service_value.MediaServiceValue(
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
                        media_record = yahoo_ads_display.models.media_service_record.MediaServiceRecord(
                            account_id = 56,
                            approval_status = 'APPROVED',
                            campaign_banner_flg = 'FALSE',
                            creation_time = '0',
                            disapproval_reason_codes = [
                                '0'
                                ],
                            logo_flg = 'FALSE',
                            image_media = yahoo_ads_display.models.media_service_image_media.MediaServiceImageMedia(
                                media_type = 'IMAGE',
                                aspect_ratio = '0',
                                data = 'YQ==',
                                file_size = 56,
                                height = 56,
                                media_ad_format = '0',
                                media_file_type = 'JPEG',
                                width = 56, ),
                            media_id = 56,
                            media_name = '0',
                            media_title = '0',
                            thumbnail_flg = 'FALSE',
                            user_status = 'ACTIVE', ), )
                    ]
            )
        else :
            return MediaServicePage(
        )

    def testMediaServicePage(self):
        """Test MediaServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
