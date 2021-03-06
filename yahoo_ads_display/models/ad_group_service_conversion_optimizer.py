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


class AdGroupServiceConversionOptimizer(object):
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
        'auto_conversion_optimizer': 'AdGroupServiceAutoConversionOptimizer',
        'manual_conversion_optimizer': 'AdGroupServiceManualConversionOptimizer',
        'none_conversion_optimizer': 'AdGroupServiceNoneConversionOptimizer',
        'optimizer_type': 'AdGroupServiceOptimizerType'
    }

    attribute_map = {
        'auto_conversion_optimizer': 'autoConversionOptimizer',
        'manual_conversion_optimizer': 'manualConversionOptimizer',
        'none_conversion_optimizer': 'noneConversionOptimizer',
        'optimizer_type': 'optimizerType'
    }

    def __init__(self, auto_conversion_optimizer=None, manual_conversion_optimizer=None, none_conversion_optimizer=None, optimizer_type=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupServiceConversionOptimizer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_conversion_optimizer = None
        self._manual_conversion_optimizer = None
        self._none_conversion_optimizer = None
        self._optimizer_type = None
        self.discriminator = None

        self.auto_conversion_optimizer = auto_conversion_optimizer
        self.manual_conversion_optimizer = manual_conversion_optimizer
        self.none_conversion_optimizer = none_conversion_optimizer
        self.optimizer_type = optimizer_type

    @property
    def auto_conversion_optimizer(self):
        """Gets the auto_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501


        :return: The auto_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :rtype: AdGroupServiceAutoConversionOptimizer
        """
        return self._auto_conversion_optimizer

    @auto_conversion_optimizer.setter
    def auto_conversion_optimizer(self, auto_conversion_optimizer):
        """Sets the auto_conversion_optimizer of this AdGroupServiceConversionOptimizer.


        :param auto_conversion_optimizer: The auto_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :type: AdGroupServiceAutoConversionOptimizer
        """

        self._auto_conversion_optimizer = auto_conversion_optimizer

    @property
    def manual_conversion_optimizer(self):
        """Gets the manual_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501


        :return: The manual_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :rtype: AdGroupServiceManualConversionOptimizer
        """
        return self._manual_conversion_optimizer

    @manual_conversion_optimizer.setter
    def manual_conversion_optimizer(self, manual_conversion_optimizer):
        """Sets the manual_conversion_optimizer of this AdGroupServiceConversionOptimizer.


        :param manual_conversion_optimizer: The manual_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :type: AdGroupServiceManualConversionOptimizer
        """

        self._manual_conversion_optimizer = manual_conversion_optimizer

    @property
    def none_conversion_optimizer(self):
        """Gets the none_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501


        :return: The none_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :rtype: AdGroupServiceNoneConversionOptimizer
        """
        return self._none_conversion_optimizer

    @none_conversion_optimizer.setter
    def none_conversion_optimizer(self, none_conversion_optimizer):
        """Sets the none_conversion_optimizer of this AdGroupServiceConversionOptimizer.


        :param none_conversion_optimizer: The none_conversion_optimizer of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :type: AdGroupServiceNoneConversionOptimizer
        """

        self._none_conversion_optimizer = none_conversion_optimizer

    @property
    def optimizer_type(self):
        """Gets the optimizer_type of this AdGroupServiceConversionOptimizer.  # noqa: E501


        :return: The optimizer_type of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :rtype: AdGroupServiceOptimizerType
        """
        return self._optimizer_type

    @optimizer_type.setter
    def optimizer_type(self, optimizer_type):
        """Sets the optimizer_type of this AdGroupServiceConversionOptimizer.


        :param optimizer_type: The optimizer_type of this AdGroupServiceConversionOptimizer.  # noqa: E501
        :type: AdGroupServiceOptimizerType
        """

        self._optimizer_type = optimizer_type

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
        if not isinstance(other, AdGroupServiceConversionOptimizer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupServiceConversionOptimizer):
            return True

        return self.to_dict() != other.to_dict()
