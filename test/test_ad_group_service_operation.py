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
from yahoo_ads_display.models.ad_group_service_operation import AdGroupServiceOperation  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestAdGroupServiceOperation(unittest.TestCase):
    """AdGroupServiceOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AdGroupServiceOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.ad_group_service_operation.AdGroupServiceOperation()  # noqa: E501
        if include_optional :
            return AdGroupServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_display.models.ad_group.AdGroup(
                        account_id = 56,
                        ad_group_bidding_strategy = yahoo_ads_display.models.ad_group_service_bidding_strategy.AdGroupServiceBiddingStrategy(
                            campaign_bidding_strategy_type = 'AUTO',
                            max_cpc_bid_value = 56,
                            max_cpv_bid_value = 56,
                            max_vcpm_bid_value = 56,
                            target_cpa_bid_value = 56, ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        bid = yahoo_ads_display.models.ad_group_service_bid.AdGroupServiceBid(
                            manual_cpc_bid = yahoo_ads_display.models.ad_group_service_manual_cpc_bid.AdGroupServiceManualCPCBid(
                                max_cpc = 56, ),
                            manual_cpv_bid = yahoo_ads_display.models.ad_group_service_manual_cpv_bid.AdGroupServiceManualCPVBid(
                                max_cpv = 56, ),
                            type = 'MANUAL_CPC', ),
                        campaign_id = 56,
                        campaign_name = '0',
                        conversion_optimizer = yahoo_ads_display.models.ad_group_service_conversion_optimizer.AdGroupServiceConversionOptimizer(
                            auto_conversion_optimizer = yahoo_ads_display.models.ad_group_service_auto_conversion_optimizer.AdGroupServiceAutoConversionOptimizer(
                                eligibility_flg = 'ENABLE',
                                target_cpa = 56, ),
                            manual_conversion_optimizer = yahoo_ads_display.models.ad_group_service_manual_conversion_optimizer.AdGroupServiceManualConversionOptimizer(),
                            none_conversion_optimizer = yahoo_ads_display.models.ad_group_service_none_conversion_optimizer.AdGroupServiceNoneConversionOptimizer(),
                            optimizer_type = 'NONE', ),
                        device = [
                            'DESKTOP'
                            ],
                        device_app = [
                            'APP'
                            ],
                        device_os = [
                            'IOS'
                            ],
                        device_os_version = '0',
                        dynamic_image_extensions = 'ACTIVE',
                        feed_set_id = 56,
                        is_remove_feed_set_id = True,
                        labels = [
                            yahoo_ads_display.models.ad_group_service_label.AdGroupServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        smart_device_carriers = [
                            'DOCOMO'
                            ],
                        user_status = 'ACTIVE', )
                    ]
            )
        else :
            return AdGroupServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_display.models.ad_group.AdGroup(
                        account_id = 56,
                        ad_group_bidding_strategy = yahoo_ads_display.models.ad_group_service_bidding_strategy.AdGroupServiceBiddingStrategy(
                            campaign_bidding_strategy_type = 'AUTO',
                            max_cpc_bid_value = 56,
                            max_cpv_bid_value = 56,
                            max_vcpm_bid_value = 56,
                            target_cpa_bid_value = 56, ),
                        ad_group_id = 56,
                        ad_group_name = '0',
                        bid = yahoo_ads_display.models.ad_group_service_bid.AdGroupServiceBid(
                            manual_cpc_bid = yahoo_ads_display.models.ad_group_service_manual_cpc_bid.AdGroupServiceManualCPCBid(
                                max_cpc = 56, ),
                            manual_cpv_bid = yahoo_ads_display.models.ad_group_service_manual_cpv_bid.AdGroupServiceManualCPVBid(
                                max_cpv = 56, ),
                            type = 'MANUAL_CPC', ),
                        campaign_id = 56,
                        campaign_name = '0',
                        conversion_optimizer = yahoo_ads_display.models.ad_group_service_conversion_optimizer.AdGroupServiceConversionOptimizer(
                            auto_conversion_optimizer = yahoo_ads_display.models.ad_group_service_auto_conversion_optimizer.AdGroupServiceAutoConversionOptimizer(
                                eligibility_flg = 'ENABLE',
                                target_cpa = 56, ),
                            manual_conversion_optimizer = yahoo_ads_display.models.ad_group_service_manual_conversion_optimizer.AdGroupServiceManualConversionOptimizer(),
                            none_conversion_optimizer = yahoo_ads_display.models.ad_group_service_none_conversion_optimizer.AdGroupServiceNoneConversionOptimizer(),
                            optimizer_type = 'NONE', ),
                        device = [
                            'DESKTOP'
                            ],
                        device_app = [
                            'APP'
                            ],
                        device_os = [
                            'IOS'
                            ],
                        device_os_version = '0',
                        dynamic_image_extensions = 'ACTIVE',
                        feed_set_id = 56,
                        is_remove_feed_set_id = True,
                        labels = [
                            yahoo_ads_display.models.ad_group_service_label.AdGroupServiceLabel(
                                color = '0',
                                description = '0',
                                label_id = 56,
                                label_name = '0', )
                            ],
                        smart_device_carriers = [
                            'DOCOMO'
                            ],
                        user_status = 'ACTIVE', )
                    ],
        )

    def testAdGroupServiceOperation(self):
        """Test AdGroupServiceOperation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
