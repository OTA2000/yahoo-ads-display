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


class StatsServiceAudienceCategoryTarget(object):
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
        'audience_category_type': 'str',
        'category_name_en': 'str',
        'category_name_ja': 'str'
    }

    attribute_map = {
        'audience_category_type': 'audienceCategoryType',
        'category_name_en': 'categoryNameEn',
        'category_name_ja': 'categoryNameJa'
    }

    def __init__(self, audience_category_type=None, category_name_en=None, category_name_ja=None, local_vars_configuration=None):  # noqa: E501
        """StatsServiceAudienceCategoryTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._audience_category_type = None
        self._category_name_en = None
        self._category_name_ja = None
        self.discriminator = None

        self.audience_category_type = audience_category_type
        self.category_name_en = category_name_en
        self.category_name_ja = category_name_ja

    @property
    def audience_category_type(self):
        """Gets the audience_category_type of this StatsServiceAudienceCategoryTarget.  # noqa: E501

        <div lang=\"ja\">提供されるカテゴリの種別を表します。</div> <div lang=\"en\">Audience category information.</div>   # noqa: E501

        :return: The audience_category_type of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._audience_category_type

    @audience_category_type.setter
    def audience_category_type(self, audience_category_type):
        """Sets the audience_category_type of this StatsServiceAudienceCategoryTarget.

        <div lang=\"ja\">提供されるカテゴリの種別を表します。</div> <div lang=\"en\">Audience category information.</div>   # noqa: E501

        :param audience_category_type: The audience_category_type of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :type: str
        """

        self._audience_category_type = audience_category_type

    @property
    def category_name_en(self):
        """Gets the category_name_en of this StatsServiceAudienceCategoryTarget.  # noqa: E501

        <div lang=\"ja\">カテゴリ名（英語）です。</div> <div lang=\"en\">Category name (English)</div>   # noqa: E501

        :return: The category_name_en of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._category_name_en

    @category_name_en.setter
    def category_name_en(self, category_name_en):
        """Sets the category_name_en of this StatsServiceAudienceCategoryTarget.

        <div lang=\"ja\">カテゴリ名（英語）です。</div> <div lang=\"en\">Category name (English)</div>   # noqa: E501

        :param category_name_en: The category_name_en of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :type: str
        """

        self._category_name_en = category_name_en

    @property
    def category_name_ja(self):
        """Gets the category_name_ja of this StatsServiceAudienceCategoryTarget.  # noqa: E501

        <div lang=\"ja\">カテゴリ名（日本語）です。</div> <div lang=\"en\">Category name (Japanese)</div>   # noqa: E501

        :return: The category_name_ja of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :rtype: str
        """
        return self._category_name_ja

    @category_name_ja.setter
    def category_name_ja(self, category_name_ja):
        """Sets the category_name_ja of this StatsServiceAudienceCategoryTarget.

        <div lang=\"ja\">カテゴリ名（日本語）です。</div> <div lang=\"en\">Category name (Japanese)</div>   # noqa: E501

        :param category_name_ja: The category_name_ja of this StatsServiceAudienceCategoryTarget.  # noqa: E501
        :type: str
        """

        self._category_name_ja = category_name_ja

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
        if not isinstance(other, StatsServiceAudienceCategoryTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsServiceAudienceCategoryTarget):
            return True

        return self.to_dict() != other.to_dict()
