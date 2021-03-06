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


class StatsServicePeriodCustomDate(object):
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
        'stats_end_date': 'str',
        'stats_start_date': 'str'
    }

    attribute_map = {
        'stats_end_date': 'statsEndDate',
        'stats_start_date': 'statsStartDate'
    }

    def __init__(self, stats_end_date=None, stats_start_date=None, local_vars_configuration=None):  # noqa: E501
        """StatsServicePeriodCustomDate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stats_end_date = None
        self._stats_start_date = None
        self.discriminator = None

        self.stats_end_date = stats_end_date
        self.stats_start_date = stats_start_date

    @property
    def stats_end_date(self):
        """Gets the stats_end_date of this StatsServicePeriodCustomDate.  # noqa: E501

        <div lang=\"ja\"> 統計情報取得終了日時<br> ※フォーマット：yyyyMMdd </div> <div lang=\"en\"> Acquisition end date of stats information<br> ∗ Format: yyyyMMdd </div>   # noqa: E501

        :return: The stats_end_date of this StatsServicePeriodCustomDate.  # noqa: E501
        :rtype: str
        """
        return self._stats_end_date

    @stats_end_date.setter
    def stats_end_date(self, stats_end_date):
        """Sets the stats_end_date of this StatsServicePeriodCustomDate.

        <div lang=\"ja\"> 統計情報取得終了日時<br> ※フォーマット：yyyyMMdd </div> <div lang=\"en\"> Acquisition end date of stats information<br> ∗ Format: yyyyMMdd </div>   # noqa: E501

        :param stats_end_date: The stats_end_date of this StatsServicePeriodCustomDate.  # noqa: E501
        :type: str
        """

        self._stats_end_date = stats_end_date

    @property
    def stats_start_date(self):
        """Gets the stats_start_date of this StatsServicePeriodCustomDate.  # noqa: E501

        <div lang=\"ja\"> 統計情報取得開始日時<br> ※フォーマット：yyyyMMdd </div> <div lang=\"en\"> Acquisition start date of stats information<br> ∗ Format: yyyyMMdd </div>   # noqa: E501

        :return: The stats_start_date of this StatsServicePeriodCustomDate.  # noqa: E501
        :rtype: str
        """
        return self._stats_start_date

    @stats_start_date.setter
    def stats_start_date(self, stats_start_date):
        """Sets the stats_start_date of this StatsServicePeriodCustomDate.

        <div lang=\"ja\"> 統計情報取得開始日時<br> ※フォーマット：yyyyMMdd </div> <div lang=\"en\"> Acquisition start date of stats information<br> ∗ Format: yyyyMMdd </div>   # noqa: E501

        :param stats_start_date: The stats_start_date of this StatsServicePeriodCustomDate.  # noqa: E501
        :type: str
        """

        self._stats_start_date = stats_start_date

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
        if not isinstance(other, StatsServicePeriodCustomDate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsServicePeriodCustomDate):
            return True

        return self.to_dict() != other.to_dict()
