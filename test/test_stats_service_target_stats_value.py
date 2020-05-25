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
from yahoo_ads_display.models.stats_service_target_stats_value import StatsServiceTargetStatsValue  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestStatsServiceTargetStatsValue(unittest.TestCase):
    """StatsServiceTargetStatsValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatsServiceTargetStatsValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.stats_service_target_stats_value.StatsServiceTargetStatsValue()  # noqa: E501
        if include_optional :
            return StatsServiceTargetStatsValue(
                campaign_id = 56,
                campaign_name = '0',
                ad_group_id = 56,
                ad_group_name = '0',
                stats = yahoo_ads_display.models.stats.Stats(
                    imps = 56,
                    imps_prev = 1.337,
                    click_cnt = 56,
                    click_rate = 1.337,
                    click_rate_prev = 1.337,
                    cost = 1.337,
                    avg_cpc = 1.337,
                    conversions = 56,
                    conversion_rate = 1.337,
                    conversions_via_ad_click = 56,
                    conversion_rate_via_ad_click = 1.337,
                    all_conversions = 56,
                    all_conversion_rate = 1.337,
                    cpa = '0',
                    conversion_value = '0',
                    value_per_conversions = '0',
                    conv_value_per_cost = 1.337,
                    all_conv_value_per_cost = 1.337,
                    conv_value_via_ad_click_per_cost = 1.337,
                    all_conversion_value = '0',
                    value_per_all_conversions = '0',
                    conversion_value_via_ad_click = '0',
                    value_per_conversions_via_ad_click = '0',
                    cpa_via_ad_click = '0',
                    all_cpa = '0',
                    cross_device_conversions = 56,
                    avg_deliver_rank = 1.337,
                    measured_imps = 1.337,
                    total_vimps = 56,
                    measured_imps_rate = 1.337,
                    vimps = 56,
                    viewable_imps_rate = 1.337,
                    in_view_rate = 1.337,
                    viewable_clicks = 1.337,
                    in_view_click_cnt = 56,
                    viewable_click_rate = 1.337,
                    in_view_click_rate = 1.337,
                    paid_video_views = 56,
                    paid_video_view_rate = 1.337,
                    average_cpv = 1.337,
                    video_views = 56,
                    video_views_to25 = 56,
                    video_views_to50 = 56,
                    video_views_to75 = 56,
                    video_views_to95 = 56,
                    video_views_to100 = 56,
                    video_views_to3_sec = 56,
                    video_views_to10_sec = 56,
                    average_rate_video_viewed = 1.337,
                    average_duration_video_viewed = 1.337,
                    impression_share = 1.337,
                    budget_impression_share_lost_rate = 1.337,
                    rank_impression_share_lost_rate = 1.337, ),
                target = yahoo_ads_display.models.stats_service_target.StatsServiceTarget(
                    ad_schedule_target = yahoo_ads_display.models.stats_service_ad_schedule_target.StatsServiceAdScheduleTarget(
                        day_of_week = 'MONDAY',
                        end_hour = 56,
                        start_hour = 56, ),
                    age_target = yahoo_ads_display.models.stats_service_age_target.StatsServiceAgeTarget(
                        age = 'GT_RANGE13_14',
                        estimate_flg = 'PAUSED', ),
                    app_target = yahoo_ads_display.models.stats_service_app_target.StatsServiceAppTarget(
                        device_app_type = 'APP', ),
                    audience_category_target = yahoo_ads_display.models.stats_service_audience_category_target.StatsServiceAudienceCategoryTarget(
                        audience_category_type = '0',
                        category_name_en = '0',
                        category_name_ja = '0', ),
                    carrier_target = yahoo_ads_display.models.stats_service_carrier_target.StatsServiceCarrierTarget(
                        carrier_type = 'DOCOMO', ),
                    device_target = yahoo_ads_display.models.stats_service_device_target.StatsServiceDeviceTarget(
                        device_type = 'DESKTOP', ),
                    gender_target = yahoo_ads_display.models.stats_service_gender_target.StatsServiceGenderTarget(
                        gender = 'ST_MALE', ),
                    geo_target = yahoo_ads_display.models.stats_service_geo_target.StatsServiceGeoTarget(
                        geo_name_en = '0',
                        geo_name_ja = '0', ),
                    interest_category_target = yahoo_ads_display.models.stats_service_interest_category_target.StatsServiceInterestCategoryTarget(
                        category_full_name_en = '0',
                        category_full_name_ja = '0', ),
                    os_target = yahoo_ads_display.models.stats_service_os_target.StatsServiceOsTarget(
                        device_os_type = 'IOS', ),
                    os_version_target = yahoo_ads_display.models.stats_service_os_version_target.StatsServiceOsVersionTarget(
                        os_version = '0', ),
                    placement_target = yahoo_ads_display.models.stats_service_placement_target.StatsServicePlacementTarget(
                        placement_url_list_name = '0',
                        placement_url_list_type = 'WHITE_LIST', ),
                    search_target = yahoo_ads_display.models.stats_service_search_target.StatsServiceSearchTarget(
                        search_keyword_list_name = '0', ),
                    site_category_target = yahoo_ads_display.models.stats_service_site_category_target.StatsServiceSiteCategoryTarget(
                        category_full_name_en = '0',
                        category_full_name_ja = '0', ),
                    site_retargeting_target = yahoo_ads_display.models.stats_service_site_retargeting_target.StatsServiceSiteRetargetingTarget(
                        target_list_deliver_type = 'INCLUDE',
                        target_list_name = '0', ),
                    target_id = '0',
                    target_setting = 'NONE',
                    target_type = 'AD_SCHEDULE_TARGET', )
            )
        else :
            return StatsServiceTargetStatsValue(
        )

    def testStatsServiceTargetStatsValue(self):
        """Test StatsServiceTargetStatsValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
