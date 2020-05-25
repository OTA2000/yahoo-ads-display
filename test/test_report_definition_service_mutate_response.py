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
from yahoo_ads_display.models.report_definition_service_mutate_response import ReportDefinitionServiceMutateResponse  # noqa: E501
from yahoo_ads_display.rest import ApiException

class TestReportDefinitionServiceMutateResponse(unittest.TestCase):
    """ReportDefinitionServiceMutateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportDefinitionServiceMutateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = yahoo_ads_display.models.report_definition_service_mutate_response.ReportDefinitionServiceMutateResponse()  # noqa: E501
        if include_optional :
            return ReportDefinitionServiceMutateResponse(
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
                rval = yahoo_ads_display.models.report_definition_service_return_value.ReportDefinitionServiceReturnValue(
                    values = [
                        yahoo_ads_display.models.report_definition_service_value.ReportDefinitionServiceValue(
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
                            report_definition = yahoo_ads_display.models.report_definition.ReportDefinition(
                                account_id = 56,
                                complete_time = '0',
                                date_range = yahoo_ads_display.models.report_definition_service_date_range.ReportDefinitionServiceDateRange(
                                    end_date = '0',
                                    start_date = '0', ),
                                date_range_type = 'CUSTOM_DATE',
                                download_encode = 'UTF-8',
                                download_format = 'CSV',
                                fields = [
                                    '0'
                                    ],
                                filters = [
                                    yahoo_ads_display.models.report_definition_service_filter.ReportDefinitionServiceFilter(
                                        field = '0',
                                        filter_operator = 'EQUALS', )
                                    ],
                                frequency_range = 'DAILY',
                                job_status = 'ACCEPTED',
                                lang = 'JA',
                                report_job_error_detail = '0',
                                report_job_id = 56,
                                report_name = '0',
                                request_time = '0',
                                sort_fields = [
                                    yahoo_ads_display.models.report_definition_service_report_sort_field.ReportDefinitionServiceReportSortField(
                                        field = '0',
                                        report_sort_type = 'ASC', )
                                    ],
                                zip = 'ON', ), )
                        ], )
            )
        else :
            return ReportDefinitionServiceMutateResponse(
        )

    def testReportDefinitionServiceMutateResponse(self):
        """Test ReportDefinitionServiceMutateResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
