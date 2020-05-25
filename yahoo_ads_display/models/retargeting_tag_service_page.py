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


class RetargetingTagServicePage(object):
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
        'total_num_entries': 'int',
        'values': 'list[RetargetingTagServiceValue]'
    }

    attribute_map = {
        'total_num_entries': 'totalNumEntries',
        'values': 'values'
    }

    def __init__(self, total_num_entries=None, values=None, local_vars_configuration=None):  # noqa: E501
        """RetargetingTagServicePage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_num_entries = None
        self._values = None
        self.discriminator = None

        if total_num_entries is not None:
            self.total_num_entries = total_num_entries
        self.values = values

    @property
    def total_num_entries(self):
        """Gets the total_num_entries of this RetargetingTagServicePage.  # noqa: E501

        <div lang=\"ja\">取得される項目の総件数です。</div> <div lang=\"en\">Total number of items to be retrieved.</div>   # noqa: E501

        :return: The total_num_entries of this RetargetingTagServicePage.  # noqa: E501
        :rtype: int
        """
        return self._total_num_entries

    @total_num_entries.setter
    def total_num_entries(self, total_num_entries):
        """Sets the total_num_entries of this RetargetingTagServicePage.

        <div lang=\"ja\">取得される項目の総件数です。</div> <div lang=\"en\">Total number of items to be retrieved.</div>   # noqa: E501

        :param total_num_entries: The total_num_entries of this RetargetingTagServicePage.  # noqa: E501
        :type: int
        """

        self._total_num_entries = total_num_entries

    @property
    def values(self):
        """Gets the values of this RetargetingTagServicePage.  # noqa: E501


        :return: The values of this RetargetingTagServicePage.  # noqa: E501
        :rtype: list[RetargetingTagServiceValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this RetargetingTagServicePage.


        :param values: The values of this RetargetingTagServicePage.  # noqa: E501
        :type: list[RetargetingTagServiceValue]
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
        if not isinstance(other, RetargetingTagServicePage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetargetingTagServicePage):
            return True

        return self.to_dict() != other.to_dict()
