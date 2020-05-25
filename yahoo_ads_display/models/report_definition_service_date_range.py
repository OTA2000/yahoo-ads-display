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


class ReportDefinitionServiceDateRange(object):
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
        'end_date': 'str',
        'start_date': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'start_date': 'startDate'
    }

    def __init__(self, end_date=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """ReportDefinitionServiceDateRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_date = None
        self._start_date = None
        self.discriminator = None

        self.end_date = end_date
        self.start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ReportDefinitionServiceDateRange.  # noqa: E501

        <div lang=\"ja\"> 集計終了日です。<br> このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> The compilation end date. <br> This field is required in ADD operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The end_date of this ReportDefinitionServiceDateRange.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportDefinitionServiceDateRange.

        <div lang=\"ja\"> 集計終了日です。<br> このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> The compilation end date. <br> This field is required in ADD operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param end_date: The end_date of this ReportDefinitionServiceDateRange.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this ReportDefinitionServiceDateRange.  # noqa: E501

        <div lang=\"ja\"> 集計開始日です。<br> このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> The compilation start date.<br> This field is required in ADD operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The start_date of this ReportDefinitionServiceDateRange.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReportDefinitionServiceDateRange.

        <div lang=\"ja\"> 集計開始日です。<br> このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> The compilation start date.<br> This field is required in ADD operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param start_date: The start_date of this ReportDefinitionServiceDateRange.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if not isinstance(other, ReportDefinitionServiceDateRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportDefinitionServiceDateRange):
            return True

        return self.to_dict() != other.to_dict()
