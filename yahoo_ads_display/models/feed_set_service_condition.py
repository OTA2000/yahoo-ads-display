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


class FeedSetServiceCondition(object):
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
        'compare_operator': 'FeedSetServiceCompareOperator',
        'value': 'str'
    }

    attribute_map = {
        'compare_operator': 'compareOperator',
        'value': 'value'
    }

    def __init__(self, compare_operator=None, value=None, local_vars_configuration=None):  # noqa: E501
        """FeedSetServiceCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._compare_operator = None
        self._value = None
        self.discriminator = None

        self.compare_operator = compare_operator
        self.value = value

    @property
    def compare_operator(self):
        """Gets the compare_operator of this FeedSetServiceCondition.  # noqa: E501


        :return: The compare_operator of this FeedSetServiceCondition.  # noqa: E501
        :rtype: FeedSetServiceCompareOperator
        """
        return self._compare_operator

    @compare_operator.setter
    def compare_operator(self, compare_operator):
        """Sets the compare_operator of this FeedSetServiceCondition.


        :param compare_operator: The compare_operator of this FeedSetServiceCondition.  # noqa: E501
        :type: FeedSetServiceCompareOperator
        """

        self._compare_operator = compare_operator

    @property
    def value(self):
        """Gets the value of this FeedSetServiceCondition.  # noqa: E501

        <div lang=\"ja\"> 値です。<br> ADD時、このフィールドは必須です。<br> 設定可能な値はFeedSetServiceConditionTypeをご参照ください。<br> </div> <div lang=\"en\"> Value.<br> This field is required in ADD operation.<br> Refer to FeedSetServiceConditionType for possible values. </div>   # noqa: E501

        :return: The value of this FeedSetServiceCondition.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FeedSetServiceCondition.

        <div lang=\"ja\"> 値です。<br> ADD時、このフィールドは必須です。<br> 設定可能な値はFeedSetServiceConditionTypeをご参照ください。<br> </div> <div lang=\"en\"> Value.<br> This field is required in ADD operation.<br> Refer to FeedSetServiceConditionType for possible values. </div>   # noqa: E501

        :param value: The value of this FeedSetServiceCondition.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, FeedSetServiceCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedSetServiceCondition):
            return True

        return self.to_dict() != other.to_dict()