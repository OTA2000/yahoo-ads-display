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
from yahoo_ads_display.models.stats_service_target import StatsServiceTarget  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestStatsServiceTarget(unittest.TestCase):
    """StatsServiceTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatsServiceTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.stats_service_target.StatsServiceTarget()  # noqa: E501
        if include_optional :
            return StatsServiceTarget(
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
                    estimate_flg = 'PAUSED',
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
                target_type = 'AD_SCHEDULE_TARGET'
            )
        else :
            return StatsServiceTarget(
        )

    def testStatsServiceTarget(self):
        """Test StatsServiceTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
