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
from yahoo_ads_display.models.campaign_migration_service_upload_return_value import CampaignMigrationServiceUploadReturnValue  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestCampaignMigrationServiceUploadReturnValue(unittest.TestCase):
    """CampaignMigrationServiceUploadReturnValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignMigrationServiceUploadReturnValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.campaign_migration_service_upload_return_value.CampaignMigrationServiceUploadReturnValue()  # noqa: E501
        if include_optional :
            return CampaignMigrationServiceUploadReturnValue(
                values = [
                    yahoo_ads_display.models.campaign_migration_service_job_value.CampaignMigrationServiceJobValue(
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
                        migration_job = yahoo_ads_display.models.campaign_migration_service_job.CampaignMigrationServiceJob(
                            account_id = 56,
                            failed_count = 56,
                            in_progress_count = 56,
                            job_status = 'NOT_STARTED',
                            migration_job_end_date = '0',
                            migration_job_id = 56,
                            migration_job_submit_date = '0',
                            scope = 'SINGLE_ACCOUNT',
                            succeeded_count = 56,
                            total_count = 56, ),
                        operation_succeeded = True, )
                    ]
            )
        else :
            return CampaignMigrationServiceUploadReturnValue(
        )

    def testCampaignMigrationServiceUploadReturnValue(self):
        """Test CampaignMigrationServiceUploadReturnValue"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()