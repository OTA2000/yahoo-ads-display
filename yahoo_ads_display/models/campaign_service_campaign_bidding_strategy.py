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


class CampaignServiceCampaignBiddingStrategy(object):
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
        'campaign_bidding_strategy_type': 'CampaignServiceCampaignBiddingStrategyType',
        'max_cpc_bid_value': 'int',
        'max_cpv_bid_value': 'int',
        'max_vcpm_bid_value': 'int',
        'target_cpa_bid_value': 'int'
    }

    attribute_map = {
        'campaign_bidding_strategy_type': 'campaignBiddingStrategyType',
        'max_cpc_bid_value': 'maxCpcBidValue',
        'max_cpv_bid_value': 'maxCpvBidValue',
        'max_vcpm_bid_value': 'maxVcpmBidValue',
        'target_cpa_bid_value': 'targetCpaBidValue'
    }

    def __init__(self, campaign_bidding_strategy_type=None, max_cpc_bid_value=None, max_cpv_bid_value=None, max_vcpm_bid_value=None, target_cpa_bid_value=None, local_vars_configuration=None):  # noqa: E501
        """CampaignServiceCampaignBiddingStrategy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_bidding_strategy_type = None
        self._max_cpc_bid_value = None
        self._max_cpv_bid_value = None
        self._max_vcpm_bid_value = None
        self._target_cpa_bid_value = None
        self.discriminator = None

        self.campaign_bidding_strategy_type = campaign_bidding_strategy_type
        self.max_cpc_bid_value = max_cpc_bid_value
        self.max_cpv_bid_value = max_cpv_bid_value
        self.max_vcpm_bid_value = max_vcpm_bid_value
        self.target_cpa_bid_value = target_cpa_bid_value

    @property
    def campaign_bidding_strategy_type(self):
        """Gets the campaign_bidding_strategy_type of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501


        :return: The campaign_bidding_strategy_type of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :rtype: CampaignServiceCampaignBiddingStrategyType
        """
        return self._campaign_bidding_strategy_type

    @campaign_bidding_strategy_type.setter
    def campaign_bidding_strategy_type(self, campaign_bidding_strategy_type):
        """Sets the campaign_bidding_strategy_type of this CampaignServiceCampaignBiddingStrategy.


        :param campaign_bidding_strategy_type: The campaign_bidding_strategy_type of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :type: CampaignServiceCampaignBiddingStrategyType
        """

        self._campaign_bidding_strategy_type = campaign_bidding_strategy_type

    @property
    def max_cpc_bid_value(self):
        """Gets the max_cpc_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501

        <div lang=\"ja\"> キャンペーン最大入札価格(CPC)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (CPC). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The max_cpc_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._max_cpc_bid_value

    @max_cpc_bid_value.setter
    def max_cpc_bid_value(self, max_cpc_bid_value):
        """Sets the max_cpc_bid_value of this CampaignServiceCampaignBiddingStrategy.

        <div lang=\"ja\"> キャンペーン最大入札価格(CPC)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (CPC). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param max_cpc_bid_value: The max_cpc_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :type: int
        """

        self._max_cpc_bid_value = max_cpc_bid_value

    @property
    def max_cpv_bid_value(self):
        """Gets the max_cpv_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501

        <div lang=\"ja\"> キャンペーン最大入札価格(CPV)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (CPV). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The max_cpv_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._max_cpv_bid_value

    @max_cpv_bid_value.setter
    def max_cpv_bid_value(self, max_cpv_bid_value):
        """Sets the max_cpv_bid_value of this CampaignServiceCampaignBiddingStrategy.

        <div lang=\"ja\"> キャンペーン最大入札価格(CPV)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (CPV). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param max_cpv_bid_value: The max_cpv_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :type: int
        """

        self._max_cpv_bid_value = max_cpv_bid_value

    @property
    def max_vcpm_bid_value(self):
        """Gets the max_vcpm_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501

        <div lang=\"ja\"> キャンペーン最大入札価格(vCPM)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (vCPM).<br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The max_vcpm_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._max_vcpm_bid_value

    @max_vcpm_bid_value.setter
    def max_vcpm_bid_value(self, max_vcpm_bid_value):
        """Sets the max_vcpm_bid_value of this CampaignServiceCampaignBiddingStrategy.

        <div lang=\"ja\"> キャンペーン最大入札価格(vCPM)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Max bid of campaign (vCPM).<br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param max_vcpm_bid_value: The max_vcpm_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :type: int
        """

        self._max_vcpm_bid_value = max_vcpm_bid_value

    @property
    def target_cpa_bid_value(self):
        """Gets the target_cpa_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501

        <div lang=\"ja\"> キャンペーン目標単価(tCPA)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Target bid of campaign (tCPA). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :return: The target_cpa_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._target_cpa_bid_value

    @target_cpa_bid_value.setter
    def target_cpa_bid_value(self, target_cpa_bid_value):
        """Sets the target_cpa_bid_value of this CampaignServiceCampaignBiddingStrategy.

        <div lang=\"ja\"> キャンペーン目標単価(tCPA)です。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> Target bid of campaign (tCPA). <br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. </div>   # noqa: E501

        :param target_cpa_bid_value: The target_cpa_bid_value of this CampaignServiceCampaignBiddingStrategy.  # noqa: E501
        :type: int
        """

        self._target_cpa_bid_value = target_cpa_bid_value

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
        if not isinstance(other, CampaignServiceCampaignBiddingStrategy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignServiceCampaignBiddingStrategy):
            return True

        return self.to_dict() != other.to_dict()
