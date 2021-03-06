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
from yahoo_ads_display.models.retargeting_list_service_page import RetargetingListServicePage  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestRetargetingListServicePage(unittest.TestCase):
    """RetargetingListServicePage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RetargetingListServicePage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.retargeting_list_service_page.RetargetingListServicePage()  # noqa: E501
        if include_optional :
            return RetargetingListServicePage(
                total_num_entries = 56,
                values = [
                    yahoo_ads_display.models.retargeting_list_service_value.RetargetingListServiceValue(
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
                        retargeting_list = yahoo_ads_display.models.retargeting_list.RetargetingList(
                            account_id = 56,
                            delivery_status = 'ACTIVE',
                            description = '0',
                            reach = 56,
                            target_list = yahoo_ads_display.models.retargeting_list_service_target_list.RetargetingListServiceTargetList(
                                combination_target_list = yahoo_ads_display.models.retargeting_list_service_combination_target_list.RetargetingListServiceCombinationTargetList(
                                    combinations = [
                                        yahoo_ads_display.models.retargeting_list_service_combination.RetargetingListServiceCombination(
                                            logical_operator = 'OR',
                                            target_lists = [
                                                yahoo_ads_display.models.retargeting_list_service_target_list_data.RetargetingListServiceTargetListData(
                                                    target_list_id = 56,
                                                    target_list_name = '0', )
                                                ], )
                                        ], ),
                                custom_audience_target_list = yahoo_ads_display.models.retargeting_list_service_custom_audience_target_list.RetargetingListServiceCustomAudienceTargetList(
                                    custom_audience_id = '0',
                                    reach_period = 56, ),
                                rule_target_list = yahoo_ads_display.models.retargeting_list_service_rule_target_list.RetargetingListServiceRuleTargetList(
                                    is_open = 'TRUE',
                                    is_preset = 'TRUE',
                                    reach_period = 56,
                                    retargeting_tag_id = '0',
                                    rules = [
                                        yahoo_ads_display.models.retargeting_list_service_rule.RetargetingListServiceRule(
                                            rule_conditions = [
                                                yahoo_ads_display.models.retargeting_list_service_rule_condition.RetargetingListServiceRuleCondition(
                                                    compare_operator = 'EQUAL',
                                                    rule_type = 'URL',
                                                    value = '0', )
                                                ], )
                                        ], ),
                                similarity_target_list = yahoo_ads_display.models.retargeting_list_service_similarity_target_list.RetargetingListServiceSimilarityTargetList(
                                    target_list_id = 56,
                                    target_list_size = 'RATE_1',
                                    target_list_size_reaches = [
                                        yahoo_ads_display.models.retargeting_list_service_target_list_size_reaches.RetargetingListServiceTargetListSizeReaches(
                                            reach = 56, )
                                        ], ),
                                target_list_type = 'DEFAULT_LIST', ),
                            target_list_id = 56,
                            target_list_name = '0', ), )
                    ]
            )
        else :
            return RetargetingListServicePage(
        )

    def testRetargetingListServicePage(self):
        """Test RetargetingListServicePage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
