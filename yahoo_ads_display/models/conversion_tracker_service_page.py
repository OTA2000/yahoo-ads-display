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


class ConversionTrackerServicePage(object):
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
        'period': 'ConversionTrackerServicePeriod',
        'total_all_conversion_value': 'str',
        'total_all_conversions': 'int',
        'total_conversion_value': 'str',
        'total_conversion_value_via_ad_click': 'str',
        'total_conversions': 'int',
        'total_conversions_via_ad_click': 'int',
        'total_cross_device_conversions': 'int',
        'total_num_entries': 'int',
        'values': 'list[ConversionTrackerServiceValue]'
    }

    attribute_map = {
        'period': 'period',
        'total_all_conversion_value': 'totalAllConversionValue',
        'total_all_conversions': 'totalAllConversions',
        'total_conversion_value': 'totalConversionValue',
        'total_conversion_value_via_ad_click': 'totalConversionValueViaAdClick',
        'total_conversions': 'totalConversions',
        'total_conversions_via_ad_click': 'totalConversionsViaAdClick',
        'total_cross_device_conversions': 'totalCrossDeviceConversions',
        'total_num_entries': 'totalNumEntries',
        'values': 'values'
    }

    def __init__(self, period=None, total_all_conversion_value=None, total_all_conversions=None, total_conversion_value=None, total_conversion_value_via_ad_click=None, total_conversions=None, total_conversions_via_ad_click=None, total_cross_device_conversions=None, total_num_entries=None, values=None, local_vars_configuration=None):  # noqa: E501
        """ConversionTrackerServicePage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._period = None
        self._total_all_conversion_value = None
        self._total_all_conversions = None
        self._total_conversion_value = None
        self._total_conversion_value_via_ad_click = None
        self._total_conversions = None
        self._total_conversions_via_ad_click = None
        self._total_cross_device_conversions = None
        self._total_num_entries = None
        self._values = None
        self.discriminator = None

        self.period = period
        self.total_all_conversion_value = total_all_conversion_value
        self.total_all_conversions = total_all_conversions
        self.total_conversion_value = total_conversion_value
        self.total_conversion_value_via_ad_click = total_conversion_value_via_ad_click
        self.total_conversions = total_conversions
        self.total_conversions_via_ad_click = total_conversions_via_ad_click
        self.total_cross_device_conversions = total_cross_device_conversions
        if total_num_entries is not None:
            self.total_num_entries = total_num_entries
        self.values = values

    @property
    def period(self):
        """Gets the period of this ConversionTrackerServicePage.  # noqa: E501


        :return: The period of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: ConversionTrackerServicePeriod
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ConversionTrackerServicePage.


        :param period: The period of this ConversionTrackerServicePage.  # noqa: E501
        :type: ConversionTrackerServicePeriod
        """

        self._period = period

    @property
    def total_all_conversion_value(self):
        """Gets the total_all_conversion_value of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョンの価値（全て）の合計です。</div> <div lang=\"en\">Total of conv. value (all).</div>   # noqa: E501

        :return: The total_all_conversion_value of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: str
        """
        return self._total_all_conversion_value

    @total_all_conversion_value.setter
    def total_all_conversion_value(self, total_all_conversion_value):
        """Sets the total_all_conversion_value of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョンの価値（全て）の合計です。</div> <div lang=\"en\">Total of conv. value (all).</div>   # noqa: E501

        :param total_all_conversion_value: The total_all_conversion_value of this ConversionTrackerServicePage.  # noqa: E501
        :type: str
        """

        self._total_all_conversion_value = total_all_conversion_value

    @property
    def total_all_conversions(self):
        """Gets the total_all_conversions of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョン数（全て）の合計です。</div> <div lang=\"en\">Total of conversions (all).</div>   # noqa: E501

        :return: The total_all_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_all_conversions

    @total_all_conversions.setter
    def total_all_conversions(self, total_all_conversions):
        """Sets the total_all_conversions of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョン数（全て）の合計です。</div> <div lang=\"en\">Total of conversions (all).</div>   # noqa: E501

        :param total_all_conversions: The total_all_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :type: int
        """

        self._total_all_conversions = total_all_conversions

    @property
    def total_conversion_value(self):
        """Gets the total_conversion_value of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョンの価値の合計です。</div> <div lang=\"en\">Total of conv. value.</div>   # noqa: E501

        :return: The total_conversion_value of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: str
        """
        return self._total_conversion_value

    @total_conversion_value.setter
    def total_conversion_value(self, total_conversion_value):
        """Sets the total_conversion_value of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョンの価値の合計です。</div> <div lang=\"en\">Total of conv. value.</div>   # noqa: E501

        :param total_conversion_value: The total_conversion_value of this ConversionTrackerServicePage.  # noqa: E501
        :type: str
        """

        self._total_conversion_value = total_conversion_value

    @property
    def total_conversion_value_via_ad_click(self):
        """Gets the total_conversion_value_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョンの価値の合計（クリック経由）です。</div> <div lang=\"en\">Total of conv. value (via click).</div>   # noqa: E501

        :return: The total_conversion_value_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: str
        """
        return self._total_conversion_value_via_ad_click

    @total_conversion_value_via_ad_click.setter
    def total_conversion_value_via_ad_click(self, total_conversion_value_via_ad_click):
        """Sets the total_conversion_value_via_ad_click of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョンの価値の合計（クリック経由）です。</div> <div lang=\"en\">Total of conv. value (via click).</div>   # noqa: E501

        :param total_conversion_value_via_ad_click: The total_conversion_value_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501
        :type: str
        """

        self._total_conversion_value_via_ad_click = total_conversion_value_via_ad_click

    @property
    def total_conversions(self):
        """Gets the total_conversions of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョン数の合計です。</div> <div lang=\"en\">Total of conversions.</div>   # noqa: E501

        :return: The total_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_conversions

    @total_conversions.setter
    def total_conversions(self, total_conversions):
        """Sets the total_conversions of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョン数の合計です。</div> <div lang=\"en\">Total of conversions.</div>   # noqa: E501

        :param total_conversions: The total_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :type: int
        """

        self._total_conversions = total_conversions

    @property
    def total_conversions_via_ad_click(self):
        """Gets the total_conversions_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">コンバージョン数の合計（クリック経由）です。</div> <div lang=\"en\">Total of conversions (via click).</div>   # noqa: E501

        :return: The total_conversions_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_conversions_via_ad_click

    @total_conversions_via_ad_click.setter
    def total_conversions_via_ad_click(self, total_conversions_via_ad_click):
        """Sets the total_conversions_via_ad_click of this ConversionTrackerServicePage.

        <div lang=\"ja\">コンバージョン数の合計（クリック経由）です。</div> <div lang=\"en\">Total of conversions (via click).</div>   # noqa: E501

        :param total_conversions_via_ad_click: The total_conversions_via_ad_click of this ConversionTrackerServicePage.  # noqa: E501
        :type: int
        """

        self._total_conversions_via_ad_click = total_conversions_via_ad_click

    @property
    def total_cross_device_conversions(self):
        """Gets the total_cross_device_conversions of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">クロスデバイスコンバージョン数の合計です。</div> <div lang=\"en\">Total of cross-device conv.</div>   # noqa: E501

        :return: The total_cross_device_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_cross_device_conversions

    @total_cross_device_conversions.setter
    def total_cross_device_conversions(self, total_cross_device_conversions):
        """Sets the total_cross_device_conversions of this ConversionTrackerServicePage.

        <div lang=\"ja\">クロスデバイスコンバージョン数の合計です。</div> <div lang=\"en\">Total of cross-device conv.</div>   # noqa: E501

        :param total_cross_device_conversions: The total_cross_device_conversions of this ConversionTrackerServicePage.  # noqa: E501
        :type: int
        """

        self._total_cross_device_conversions = total_cross_device_conversions

    @property
    def total_num_entries(self):
        """Gets the total_num_entries of this ConversionTrackerServicePage.  # noqa: E501

        <div lang=\"ja\">取得される項目の総件数です。です。</div> <div lang=\"en\">Total number of items to be retrieved.</div>   # noqa: E501

        :return: The total_num_entries of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_num_entries

    @total_num_entries.setter
    def total_num_entries(self, total_num_entries):
        """Sets the total_num_entries of this ConversionTrackerServicePage.

        <div lang=\"ja\">取得される項目の総件数です。です。</div> <div lang=\"en\">Total number of items to be retrieved.</div>   # noqa: E501

        :param total_num_entries: The total_num_entries of this ConversionTrackerServicePage.  # noqa: E501
        :type: int
        """

        self._total_num_entries = total_num_entries

    @property
    def values(self):
        """Gets the values of this ConversionTrackerServicePage.  # noqa: E501


        :return: The values of this ConversionTrackerServicePage.  # noqa: E501
        :rtype: list[ConversionTrackerServiceValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ConversionTrackerServicePage.


        :param values: The values of this ConversionTrackerServicePage.  # noqa: E501
        :type: list[ConversionTrackerServiceValue]
        """

        self._values = values

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
        if not isinstance(other, ConversionTrackerServicePage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversionTrackerServicePage):
            return True

        return self.to_dict() != other.to_dict()
