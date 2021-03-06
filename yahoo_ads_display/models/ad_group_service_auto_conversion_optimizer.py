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


class AdGroupServiceAutoConversionOptimizer(object):
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
        'eligibility_flg': 'AdGroupServiceEligibilityFlg',
        'target_cpa': 'int'
    }

    attribute_map = {
        'eligibility_flg': 'eligibilityFlg',
        'target_cpa': 'targetCpa'
    }

    def __init__(self, eligibility_flg=None, target_cpa=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupServiceAutoConversionOptimizer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eligibility_flg = None
        self._target_cpa = None
        self.discriminator = None

        self.eligibility_flg = eligibility_flg
        self.target_cpa = target_cpa

    @property
    def eligibility_flg(self):
        """Gets the eligibility_flg of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501


        :return: The eligibility_flg of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501
        :rtype: AdGroupServiceEligibilityFlg
        """
        return self._eligibility_flg

    @eligibility_flg.setter
    def eligibility_flg(self, eligibility_flg):
        """Sets the eligibility_flg of this AdGroupServiceAutoConversionOptimizer.


        :param eligibility_flg: The eligibility_flg of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501
        :type: AdGroupServiceEligibilityFlg
        """

        self._eligibility_flg = eligibility_flg

    @property
    def target_cpa(self):
        """Gets the target_cpa of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501

        <div lang=\"ja\"> コンバージョン単価の目標値です。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ※設定範囲は1 - 9,999,999,999です。<br> ※コンバージョン最適化機能が動作している場合には、手動で設定されている入札設定は無効になります。 </div> <div lang=\"en\"> Target cost per conversion.<br> This field is optional in ADD and SET operation.<br> ∗Settable range is 1 - 9,999,999,999.<br> ∗If function of conversion optimization is running, manual bid settings is invalid. </div>   # noqa: E501

        :return: The target_cpa of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501
        :rtype: int
        """
        return self._target_cpa

    @target_cpa.setter
    def target_cpa(self, target_cpa):
        """Sets the target_cpa of this AdGroupServiceAutoConversionOptimizer.

        <div lang=\"ja\"> コンバージョン単価の目標値です。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ※設定範囲は1 - 9,999,999,999です。<br> ※コンバージョン最適化機能が動作している場合には、手動で設定されている入札設定は無効になります。 </div> <div lang=\"en\"> Target cost per conversion.<br> This field is optional in ADD and SET operation.<br> ∗Settable range is 1 - 9,999,999,999.<br> ∗If function of conversion optimization is running, manual bid settings is invalid. </div>   # noqa: E501

        :param target_cpa: The target_cpa of this AdGroupServiceAutoConversionOptimizer.  # noqa: E501
        :type: int
        """

        self._target_cpa = target_cpa

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
        if not isinstance(other, AdGroupServiceAutoConversionOptimizer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupServiceAutoConversionOptimizer):
            return True

        return self.to_dict() != other.to_dict()
