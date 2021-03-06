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


class CampaignServiceViewableFrequencyCap(object):
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
        'frequency_level': 'CampaignServiceFrequencyLevel',
        'frequency_time_unit': 'CampaignServiceFrequencyTimeUnit',
        'v_imps': 'int'
    }

    attribute_map = {
        'frequency_level': 'frequencyLevel',
        'frequency_time_unit': 'frequencyTimeUnit',
        'v_imps': 'vImps'
    }

    def __init__(self, frequency_level=None, frequency_time_unit=None, v_imps=None, local_vars_configuration=None):  # noqa: E501
        """CampaignServiceViewableFrequencyCap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frequency_level = None
        self._frequency_time_unit = None
        self._v_imps = None
        self.discriminator = None

        self.frequency_level = frequency_level
        self.frequency_time_unit = frequency_time_unit
        self.v_imps = v_imps

    @property
    def frequency_level(self):
        """Gets the frequency_level of this CampaignServiceViewableFrequencyCap.  # noqa: E501


        :return: The frequency_level of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :rtype: CampaignServiceFrequencyLevel
        """
        return self._frequency_level

    @frequency_level.setter
    def frequency_level(self, frequency_level):
        """Sets the frequency_level of this CampaignServiceViewableFrequencyCap.


        :param frequency_level: The frequency_level of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :type: CampaignServiceFrequencyLevel
        """

        self._frequency_level = frequency_level

    @property
    def frequency_time_unit(self):
        """Gets the frequency_time_unit of this CampaignServiceViewableFrequencyCap.  # noqa: E501


        :return: The frequency_time_unit of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :rtype: CampaignServiceFrequencyTimeUnit
        """
        return self._frequency_time_unit

    @frequency_time_unit.setter
    def frequency_time_unit(self, frequency_time_unit):
        """Sets the frequency_time_unit of this CampaignServiceViewableFrequencyCap.


        :param frequency_time_unit: The frequency_time_unit of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :type: CampaignServiceFrequencyTimeUnit
        """

        self._frequency_time_unit = frequency_time_unit

    @property
    def v_imps(self):
        """Gets the v_imps of this CampaignServiceViewableFrequencyCap.  # noqa: E501

        <div lang=\"ja\"> 同一ユーザに対する広告の最大ビューアブルインプレッション数です。<br> このフィールドは、ADDおよびSET時に省略可能となります。 </div> <div lang=\"en\"> Maximum number of ad viewable impressions to same user.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The v_imps of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :rtype: int
        """
        return self._v_imps

    @v_imps.setter
    def v_imps(self, v_imps):
        """Sets the v_imps of this CampaignServiceViewableFrequencyCap.

        <div lang=\"ja\"> 同一ユーザに対する広告の最大ビューアブルインプレッション数です。<br> このフィールドは、ADDおよびSET時に省略可能となります。 </div> <div lang=\"en\"> Maximum number of ad viewable impressions to same user.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param v_imps: The v_imps of this CampaignServiceViewableFrequencyCap.  # noqa: E501
        :type: int
        """

        self._v_imps = v_imps

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
        if not isinstance(other, CampaignServiceViewableFrequencyCap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignServiceViewableFrequencyCap):
            return True

        return self.to_dict() != other.to_dict()
