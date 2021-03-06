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
from yahoo_ads_display.models.feed_ftp_service_operation import FeedFtpServiceOperation  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestFeedFtpServiceOperation(unittest.TestCase):
    """FeedFtpServiceOperation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeedFtpServiceOperation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.feed_ftp_service_operation.FeedFtpServiceOperation()  # noqa: E501
        if include_optional :
            return FeedFtpServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_display.models.feed_ftp.FeedFtp(
                        account_id = 56,
                        active_status = 'INACTIVE',
                        feed_id = 56,
                        feed_url = '0',
                        item_list_upload_type = 'UPDATE_PART',
                        schedule = yahoo_ads_display.models.feed_ftp_service_schedule.FeedFtpServiceSchedule(
                            schedule_daily = yahoo_ads_display.models.feed_ftp_service_schedule_daily.FeedFtpServiceScheduleDaily(
                                time = 56, ),
                            schedule_hourly = yahoo_ads_display.models.feed_ftp_service_schedule_hourly.FeedFtpServiceScheduleHourly(
                                interval = 56, ),
                            schedule_type = 'HOURLY',
                            schedule_weekly = yahoo_ads_display.models.feed_ftp_service_schedule_weekly.FeedFtpServiceScheduleWeekly(
                                schedule_week = 'SUN',
                                time = 56, ), ),
                        user_name = '0',
                        user_password = '0', )
                    ]
            )
        else :
            return FeedFtpServiceOperation(
                account_id = 56,
                operand = [
                    yahoo_ads_display.models.feed_ftp.FeedFtp(
                        account_id = 56,
                        active_status = 'INACTIVE',
                        feed_id = 56,
                        feed_url = '0',
                        item_list_upload_type = 'UPDATE_PART',
                        schedule = yahoo_ads_display.models.feed_ftp_service_schedule.FeedFtpServiceSchedule(
                            schedule_daily = yahoo_ads_display.models.feed_ftp_service_schedule_daily.FeedFtpServiceScheduleDaily(
                                time = 56, ),
                            schedule_hourly = yahoo_ads_display.models.feed_ftp_service_schedule_hourly.FeedFtpServiceScheduleHourly(
                                interval = 56, ),
                            schedule_type = 'HOURLY',
                            schedule_weekly = yahoo_ads_display.models.feed_ftp_service_schedule_weekly.FeedFtpServiceScheduleWeekly(
                                schedule_week = 'SUN',
                                time = 56, ), ),
                        user_name = '0',
                        user_password = '0', )
                    ],
        )

    def testFeedFtpServiceOperation(self):
        """Test FeedFtpServiceOperation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
