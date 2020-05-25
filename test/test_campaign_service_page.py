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
from yahoo_ads_display.models.campaign_service_page import CampaignServicePage  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestCampaignServicePage(unittest.TestCase):
    """CampaignServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.campaign_service_page.CampaignServicePage()  # noqa: E501
        if include_optional :
            return CampaignServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_display.models.campaign_service_value.CampaignServiceValue(
                        campaign = yahoo_ads_display.models.campaign.Campaign(
                            account_id = 56,
                            ad_product_type = '0',
                            app_id = '0',
                            app_name = '0',
                            bidding_strategy = yahoo_ads_display.models.campaign_service_bidding_strategy.CampaignServiceBiddingStrategy(
                                bidding_strategy_type = 'MANUAL_CPC', ),
                            budget = yahoo_ads_display.models.campaign_service_budget.CampaignServiceBudget(
                                amount = 56,
                                budget_delivery_method = 'STANDARD', ),
                            campaign_bidding_strategy = yahoo_ads_display.models.campaign_service_campaign_bidding_strategy.CampaignServiceCampaignBiddingStrategy(
                                campaign_bidding_strategy_type = 'AUTO',
                                max_cpc_bid_value = 56,
                                max_cpv_bid_value = 56,
                                max_vcpm_bid_value = 56,
                                target_cpa_bid_value = 56, ),
                            campaign_goal = '0',
                            campaign_id = 56,
                            campaign_name = '0',
                            conversion_optimizer = yahoo_ads_display.models.campaign_service_conversion_optimizer.CampaignServiceConversionOptimizer(
                                auto_campaign_conversion_optimizer = yahoo_ads_display.models.campaign_service_auto_campaign_conversion_optimizer.CampaignServiceAutoCampaignConversionOptimizer(
                                    conversion_optimizer_eligibility_flg = 'ENABLE',
                                    target_cpa = 56, ),
                                conversion_optimizer_type = 'MANUAL',
                                manual_campaign_conversion_optimizer = yahoo_ads_display.models.campaign_service_manual_campaign_conversion_optimizer.CampaignServiceManualCampaignConversionOptimizer(
                                    conversion_optimizer_training_status = 'PROCESSING', ), ),
                            device_os_type = 'ANDROID',
                            end_date = '0',
                            feed_id = 56,
                            frequency_cap = yahoo_ads_display.models.campaign_service_frequency_cap.CampaignServiceFrequencyCap(
                                frequency_level = 'CAMPAIGN',
                                frequency_time_unit = 'DAY',
                                impression = 56, ),
                            labels = [
                                yahoo_ads_display.models.campaign_service_label.CampaignServiceLabel(
                                    color = '0',
                                    description = '0',
                                    label_id = 56,
                                    label_name = '0', )
                                ],
                            serving_status = 'SERVING',
                            start_date = '0',
                            type = 'STANDARD',
                            user_status = 'ACTIVE',
                            viewable_frequency_cap = yahoo_ads_display.models.campaign_service_viewable_frequency_cap.CampaignServiceViewableFrequencyCap(
                                v_imps = 56, ), ),
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
            return CampaignServicePage(
        )

    def testCampaignServicePage(self):
        """Test CampaignServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
