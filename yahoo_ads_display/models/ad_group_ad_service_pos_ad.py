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


class AdGroupAdServicePosAd(object):
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
        'description': 'str',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'url': 'url'
    }

    def __init__(self, description=None, url=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAdServicePosAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._url = None
        self.discriminator = None

        self.description = description
        self.url = url

    @property
    def description(self):
        """Gets the description of this AdGroupAdServicePosAd.  # noqa: E501

        <div lang=\"ja\"> 説明文です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Descriptive text.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The description of this AdGroupAdServicePosAd.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdGroupAdServicePosAd.

        <div lang=\"ja\"> 説明文です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Descriptive text.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param description: The description of this AdGroupAdServicePosAd.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """Gets the url of this AdGroupAdServicePosAd.  # noqa: E501

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The url of this AdGroupAdServicePosAd.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AdGroupAdServicePosAd.

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param url: The url of this AdGroupAdServicePosAd.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, AdGroupAdServicePosAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAdServicePosAd):
            return True

        return self.to_dict() != other.to_dict()
