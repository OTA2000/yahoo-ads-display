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


class FeedSetServiceValue(object):
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
        'errors': 'list[Error]',
        'feed_set': 'FeedSet',
        'operation_succeeded': 'bool'
    }

    attribute_map = {
        'errors': 'errors',
        'feed_set': 'feedSet',
        'operation_succeeded': 'operationSucceeded'
    }

    def __init__(self, errors=None, feed_set=None, operation_succeeded=None, local_vars_configuration=None):  # noqa: E501
        """FeedSetServiceValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._feed_set = None
        self._operation_succeeded = None
        self.discriminator = None

        self.errors = errors
        self.feed_set = feed_set
        self.operation_succeeded = operation_succeeded

    @property
    def errors(self):
        """Gets the errors of this FeedSetServiceValue.  # noqa: E501


        :return: The errors of this FeedSetServiceValue.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this FeedSetServiceValue.


        :param errors: The errors of this FeedSetServiceValue.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def feed_set(self):
        """Gets the feed_set of this FeedSetServiceValue.  # noqa: E501


        :return: The feed_set of this FeedSetServiceValue.  # noqa: E501
        :rtype: FeedSet
        """
        return self._feed_set

    @feed_set.setter
    def feed_set(self, feed_set):
        """Sets the feed_set of this FeedSetServiceValue.


        :param feed_set: The feed_set of this FeedSetServiceValue.  # noqa: E501
        :type: FeedSet
        """

        self._feed_set = feed_set

    @property
    def operation_succeeded(self):
        """Gets the operation_succeeded of this FeedSetServiceValue.  # noqa: E501

        <div lang=\"ja\">処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。</div> <div lang=\"en\">The process results. If true, the process succeeded. If false, the process failed.</div>   # noqa: E501

        :return: The operation_succeeded of this FeedSetServiceValue.  # noqa: E501
        :rtype: bool
        """
        return self._operation_succeeded

    @operation_succeeded.setter
    def operation_succeeded(self, operation_succeeded):
        """Sets the operation_succeeded of this FeedSetServiceValue.

        <div lang=\"ja\">処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。</div> <div lang=\"en\">The process results. If true, the process succeeded. If false, the process failed.</div>   # noqa: E501

        :param operation_succeeded: The operation_succeeded of this FeedSetServiceValue.  # noqa: E501
        :type: bool
        """

        self._operation_succeeded = operation_succeeded

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
        if not isinstance(other, FeedSetServiceValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedSetServiceValue):
            return True

        return self.to_dict() != other.to_dict()
