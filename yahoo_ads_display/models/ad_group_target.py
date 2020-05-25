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


class AdGroupTarget(object):
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
        'account_id': 'int',
        'ad_group_id': 'int',
        'bid_multiplier': 'float',
        'campaign_id': 'int',
        'target': 'AdGroupTargetServiceTarget'
    }

    attribute_map = {
        'account_id': 'accountId',
        'ad_group_id': 'adGroupId',
        'bid_multiplier': 'bidMultiplier',
        'campaign_id': 'campaignId',
        'target': 'target'
    }

    def __init__(self, account_id=None, ad_group_id=None, bid_multiplier=None, campaign_id=None, target=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupTarget - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ad_group_id = None
        self._bid_multiplier = None
        self._campaign_id = None
        self._target = None
        self.discriminator = None

        self.account_id = account_id
        self.ad_group_id = ad_group_id
        self.bid_multiplier = bid_multiplier
        self.campaign_id = campaign_id
        self.target = target

    @property
    def account_id(self):
        """Gets the account_id of this AdGroupTarget.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The account_id of this AdGroupTarget.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AdGroupTarget.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param account_id: The account_id of this AdGroupTarget.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this AdGroupTarget.  # noqa: E501

        <div lang=\"ja\"> 広告グループIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Ad group ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The ad_group_id of this AdGroupTarget.  # noqa: E501
        :rtype: int
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this AdGroupTarget.

        <div lang=\"ja\"> 広告グループIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Ad group ID.<br> This field is required in requests. </div>   # noqa: E501

        :param ad_group_id: The ad_group_id of this AdGroupTarget.  # noqa: E501
        :type: int
        """

        self._ad_group_id = ad_group_id

    @property
    def bid_multiplier(self):
        """Gets the bid_multiplier of this AdGroupTarget.  # noqa: E501

        <div lang=\"ja\"> 入札価格調整率です。<br> このフィールドは、ADD、SETおよびREPLACE時は省略可能となり、REMOVE時は無視されます。<br> ※入札価格調整率が設定できないターゲティングの場合は返却されません。 </div> <div lang=\"en\"> Bid adjustment.<br> This field is optional in ADD, SET and REPLACE operation, and will be ignored in REMOVE operation.<br> ∗If bid adjustment is unable to set targeting, not returned. </div>   # noqa: E501

        :return: The bid_multiplier of this AdGroupTarget.  # noqa: E501
        :rtype: float
        """
        return self._bid_multiplier

    @bid_multiplier.setter
    def bid_multiplier(self, bid_multiplier):
        """Sets the bid_multiplier of this AdGroupTarget.

        <div lang=\"ja\"> 入札価格調整率です。<br> このフィールドは、ADD、SETおよびREPLACE時は省略可能となり、REMOVE時は無視されます。<br> ※入札価格調整率が設定できないターゲティングの場合は返却されません。 </div> <div lang=\"en\"> Bid adjustment.<br> This field is optional in ADD, SET and REPLACE operation, and will be ignored in REMOVE operation.<br> ∗If bid adjustment is unable to set targeting, not returned. </div>   # noqa: E501

        :param bid_multiplier: The bid_multiplier of this AdGroupTarget.  # noqa: E501
        :type: float
        """

        self._bid_multiplier = bid_multiplier

    @property
    def campaign_id(self):
        """Gets the campaign_id of this AdGroupTarget.  # noqa: E501

        <div lang=\"ja\"> キャンペーンIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Campaign ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The campaign_id of this AdGroupTarget.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this AdGroupTarget.

        <div lang=\"ja\"> キャンペーンIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Campaign ID.<br> This field is required in requests. </div>   # noqa: E501

        :param campaign_id: The campaign_id of this AdGroupTarget.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def target(self):
        """Gets the target of this AdGroupTarget.  # noqa: E501


        :return: The target of this AdGroupTarget.  # noqa: E501
        :rtype: AdGroupTargetServiceTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this AdGroupTarget.


        :param target: The target of this AdGroupTarget.  # noqa: E501
        :type: AdGroupTargetServiceTarget
        """

        self._target = target

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
        if not isinstance(other, AdGroupTarget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupTarget):
            return True

        return self.to_dict() != other.to_dict()
