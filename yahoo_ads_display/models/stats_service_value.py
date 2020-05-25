# coding: utf-8

"""
    Yahoo!広告 ディスプレイ広告 API リファレンス / Yahoo! Ads Display Ads API Reference

    <div lang=\"ja\">Yahoo!広告 ディスプレイ広告 APIのWebサービスについて説明します。<br> 「Try it out」のご利用には、事前にアプリケーションの登録が必要です。また、アプリケーションのリダイレクトURIの1つに<br> https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.htmlを登録してください。 </div> <div lang=\"en\">Display Ads API Web Services supported in Yahoo! Ads API.<br> When you use \"Try it out\", you need to register your application in advance.<br> As one of redirect URI for application, you need to set \"https://yahoojp-marketing.github.io/ads-display-api-documents/oauth2-redirect.html\". </div>   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yahoo_ads_display.configuration import Configuration


class StatsServiceValue(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_id': 'int',
        'ad_group_stats_value': 'StatsServiceAdGroupStatsValue',
        'ad_stats_value': 'StatsServiceAdStatsValue',
        'campaign_stats_value': 'StatsServiceCampaignStatsValue',
        'errors': 'list[Error]',
        'image_stats_value': 'StatsServiceImageStatsValue',
        'operation_succeeded': 'bool',
        'period_custom_date': 'StatsServicePeriodCustomDate',
        'stats_period': 'StatsServiceStatsPeriod',
        'target_stats_value': 'StatsServiceTargetStatsValue',
        'type': 'StatsServiceType',
        'video_stats_value': 'StatsServiceVideoStatsValue'
    }

    attribute_map = {
        'account_id': 'accountId',
        'ad_group_stats_value': 'adGroupStatsValue',
        'ad_stats_value': 'adStatsValue',
        'campaign_stats_value': 'campaignStatsValue',
        'errors': 'errors',
        'image_stats_value': 'imageStatsValue',
        'operation_succeeded': 'operationSucceeded',
        'period_custom_date': 'periodCustomDate',
        'stats_period': 'statsPeriod',
        'target_stats_value': 'targetStatsValue',
        'type': 'type',
        'video_stats_value': 'videoStatsValue'
    }

    def __init__(self, account_id=None, ad_group_stats_value=None, ad_stats_value=None, campaign_stats_value=None, errors=None, image_stats_value=None, operation_succeeded=None, period_custom_date=None, stats_period=None, target_stats_value=None, type=None, video_stats_value=None, local_vars_configuration=None):  # noqa: E501
        """StatsServiceValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ad_group_stats_value = None
        self._ad_stats_value = None
        self._campaign_stats_value = None
        self._errors = None
        self._image_stats_value = None
        self._operation_succeeded = None
        self._period_custom_date = None
        self._stats_period = None
        self._target_stats_value = None
        self._type = None
        self._video_stats_value = None
        self.discriminator = None

        self.account_id = account_id
        self.ad_group_stats_value = ad_group_stats_value
        self.ad_stats_value = ad_stats_value
        self.campaign_stats_value = campaign_stats_value
        self.errors = errors
        self.image_stats_value = image_stats_value
        self.operation_succeeded = operation_succeeded
        self.period_custom_date = period_custom_date
        self.stats_period = stats_period
        self.target_stats_value = target_stats_value
        self.type = type
        self.video_stats_value = video_stats_value

    @property
    def account_id(self):
        """Gets the account_id of this StatsServiceValue.  # noqa: E501

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :return: The account_id of this StatsServiceValue.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this StatsServiceValue.

        <div lang=\"ja\">アカウントIDです。</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :param account_id: The account_id of this StatsServiceValue.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def ad_group_stats_value(self):
        """Gets the ad_group_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The ad_group_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceAdGroupStatsValue
        """
        return self._ad_group_stats_value

    @ad_group_stats_value.setter
    def ad_group_stats_value(self, ad_group_stats_value):
        """Sets the ad_group_stats_value of this StatsServiceValue.


        :param ad_group_stats_value: The ad_group_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceAdGroupStatsValue
        """

        self._ad_group_stats_value = ad_group_stats_value

    @property
    def ad_stats_value(self):
        """Gets the ad_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The ad_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceAdStatsValue
        """
        return self._ad_stats_value

    @ad_stats_value.setter
    def ad_stats_value(self, ad_stats_value):
        """Sets the ad_stats_value of this StatsServiceValue.


        :param ad_stats_value: The ad_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceAdStatsValue
        """

        self._ad_stats_value = ad_stats_value

    @property
    def campaign_stats_value(self):
        """Gets the campaign_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The campaign_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceCampaignStatsValue
        """
        return self._campaign_stats_value

    @campaign_stats_value.setter
    def campaign_stats_value(self, campaign_stats_value):
        """Sets the campaign_stats_value of this StatsServiceValue.


        :param campaign_stats_value: The campaign_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceCampaignStatsValue
        """

        self._campaign_stats_value = campaign_stats_value

    @property
    def errors(self):
        """Gets the errors of this StatsServiceValue.  # noqa: E501


        :return: The errors of this StatsServiceValue.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this StatsServiceValue.


        :param errors: The errors of this StatsServiceValue.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def image_stats_value(self):
        """Gets the image_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The image_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceImageStatsValue
        """
        return self._image_stats_value

    @image_stats_value.setter
    def image_stats_value(self, image_stats_value):
        """Sets the image_stats_value of this StatsServiceValue.


        :param image_stats_value: The image_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceImageStatsValue
        """

        self._image_stats_value = image_stats_value

    @property
    def operation_succeeded(self):
        """Gets the operation_succeeded of this StatsServiceValue.  # noqa: E501

        <div lang=\"ja\">処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。</div> <div lang=\"en\">The process results. If true, the process succeeded. If false, the process failed.</div>   # noqa: E501

        :return: The operation_succeeded of this StatsServiceValue.  # noqa: E501
        :rtype: bool
        """
        return self._operation_succeeded

    @operation_succeeded.setter
    def operation_succeeded(self, operation_succeeded):
        """Sets the operation_succeeded of this StatsServiceValue.

        <div lang=\"ja\">処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。</div> <div lang=\"en\">The process results. If true, the process succeeded. If false, the process failed.</div>   # noqa: E501

        :param operation_succeeded: The operation_succeeded of this StatsServiceValue.  # noqa: E501
        :type: bool
        """

        self._operation_succeeded = operation_succeeded

    @property
    def period_custom_date(self):
        """Gets the period_custom_date of this StatsServiceValue.  # noqa: E501


        :return: The period_custom_date of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServicePeriodCustomDate
        """
        return self._period_custom_date

    @period_custom_date.setter
    def period_custom_date(self, period_custom_date):
        """Sets the period_custom_date of this StatsServiceValue.


        :param period_custom_date: The period_custom_date of this StatsServiceValue.  # noqa: E501
        :type: StatsServicePeriodCustomDate
        """

        self._period_custom_date = period_custom_date

    @property
    def stats_period(self):
        """Gets the stats_period of this StatsServiceValue.  # noqa: E501


        :return: The stats_period of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceStatsPeriod
        """
        return self._stats_period

    @stats_period.setter
    def stats_period(self, stats_period):
        """Sets the stats_period of this StatsServiceValue.


        :param stats_period: The stats_period of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceStatsPeriod
        """

        self._stats_period = stats_period

    @property
    def target_stats_value(self):
        """Gets the target_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The target_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceTargetStatsValue
        """
        return self._target_stats_value

    @target_stats_value.setter
    def target_stats_value(self, target_stats_value):
        """Sets the target_stats_value of this StatsServiceValue.


        :param target_stats_value: The target_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceTargetStatsValue
        """

        self._target_stats_value = target_stats_value

    @property
    def type(self):
        """Gets the type of this StatsServiceValue.  # noqa: E501


        :return: The type of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatsServiceValue.


        :param type: The type of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceType
        """

        self._type = type

    @property
    def video_stats_value(self):
        """Gets the video_stats_value of this StatsServiceValue.  # noqa: E501


        :return: The video_stats_value of this StatsServiceValue.  # noqa: E501
        :rtype: StatsServiceVideoStatsValue
        """
        return self._video_stats_value

    @video_stats_value.setter
    def video_stats_value(self, video_stats_value):
        """Sets the video_stats_value of this StatsServiceValue.


        :param video_stats_value: The video_stats_value of this StatsServiceValue.  # noqa: E501
        :type: StatsServiceVideoStatsValue
        """

        self._video_stats_value = video_stats_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatsServiceValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsServiceValue):
            return True

        return self.to_dict() != other.to_dict()
