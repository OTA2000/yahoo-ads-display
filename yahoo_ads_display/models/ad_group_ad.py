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


class AdGroupAd(object):
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
        'ad': 'AdGroupAdServiceAd',
        'ad_group_id': 'int',
        'ad_group_name': 'str',
        'ad_id': 'int',
        'ad_name': 'str',
        'ad_style': 'AdGroupAdServiceAdStyle',
        'approval_status': 'AdGroupAdServiceApprovalStatus',
        'bid': 'AdGroupAdServiceBid',
        'campaign_id': 'int',
        'campaign_name': 'str',
        'disapproval_reason_codes': 'list[str]',
        'impression_beacon_urls': 'list[str]',
        'is_remove_beacon_urls': 'AdGroupAdServiceIsRemoveFlg',
        'is_remove_third_party_tracking_script_url': 'AdGroupAdServiceIsRemoveFlg',
        'labels': 'list[AdGroupAdServiceLabel]',
        'media_id': 'int',
        'third_party_tracking_script_url': 'str',
        'third_party_tracking_vendor': 'str',
        'user_status': 'AdGroupAdServiceUserStatus'
    }

    attribute_map = {
        'account_id': 'accountId',
        'ad': 'ad',
        'ad_group_id': 'adGroupId',
        'ad_group_name': 'adGroupName',
        'ad_id': 'adId',
        'ad_name': 'adName',
        'ad_style': 'adStyle',
        'approval_status': 'approvalStatus',
        'bid': 'bid',
        'campaign_id': 'campaignId',
        'campaign_name': 'campaignName',
        'disapproval_reason_codes': 'disapprovalReasonCodes',
        'impression_beacon_urls': 'impressionBeaconUrls',
        'is_remove_beacon_urls': 'isRemoveBeaconUrls',
        'is_remove_third_party_tracking_script_url': 'isRemoveThirdPartyTrackingScriptUrl',
        'labels': 'labels',
        'media_id': 'mediaId',
        'third_party_tracking_script_url': 'thirdPartyTrackingScriptUrl',
        'third_party_tracking_vendor': 'thirdPartyTrackingVendor',
        'user_status': 'userStatus'
    }

    def __init__(self, account_id=None, ad=None, ad_group_id=None, ad_group_name=None, ad_id=None, ad_name=None, ad_style=None, approval_status=None, bid=None, campaign_id=None, campaign_name=None, disapproval_reason_codes=None, impression_beacon_urls=None, is_remove_beacon_urls=None, is_remove_third_party_tracking_script_url=None, labels=None, media_id=None, third_party_tracking_script_url=None, third_party_tracking_vendor=None, user_status=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._ad = None
        self._ad_group_id = None
        self._ad_group_name = None
        self._ad_id = None
        self._ad_name = None
        self._ad_style = None
        self._approval_status = None
        self._bid = None
        self._campaign_id = None
        self._campaign_name = None
        self._disapproval_reason_codes = None
        self._impression_beacon_urls = None
        self._is_remove_beacon_urls = None
        self._is_remove_third_party_tracking_script_url = None
        self._labels = None
        self._media_id = None
        self._third_party_tracking_script_url = None
        self._third_party_tracking_vendor = None
        self._user_status = None
        self.discriminator = None

        self.account_id = account_id
        self.ad = ad
        self.ad_group_id = ad_group_id
        self.ad_group_name = ad_group_name
        self.ad_id = ad_id
        self.ad_name = ad_name
        self.ad_style = ad_style
        self.approval_status = approval_status
        self.bid = bid
        self.campaign_id = campaign_id
        self.campaign_name = campaign_name
        self.disapproval_reason_codes = disapproval_reason_codes
        self.impression_beacon_urls = impression_beacon_urls
        self.is_remove_beacon_urls = is_remove_beacon_urls
        self.is_remove_third_party_tracking_script_url = is_remove_third_party_tracking_script_url
        self.labels = labels
        self.media_id = media_id
        self.third_party_tracking_script_url = third_party_tracking_script_url
        self.third_party_tracking_vendor = third_party_tracking_vendor
        self.user_status = user_status

    @property
    def account_id(self):
        """Gets the account_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Account ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The account_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AdGroupAd.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Account ID.<br> This field is required in requests. </div>   # noqa: E501

        :param account_id: The account_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def ad(self):
        """Gets the ad of this AdGroupAd.  # noqa: E501


        :return: The ad of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceAd
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """Sets the ad of this AdGroupAd.


        :param ad: The ad of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceAd
        """

        self._ad = ad

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 広告グループIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Ad group ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The ad_group_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this AdGroupAd.

        <div lang=\"ja\"> 広告グループIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Ad group ID.<br> This field is required in requests. </div>   # noqa: E501

        :param ad_group_id: The ad_group_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_group_id = ad_group_id

    @property
    def ad_group_name(self):
        """Gets the ad_group_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 広告グループ名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Ad group name.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The ad_group_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, ad_group_name):
        """Sets the ad_group_name of this AdGroupAd.

        <div lang=\"ja\"> 広告グループ名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Ad group name.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param ad_group_name: The ad_group_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._ad_group_name = ad_group_name

    @property
    def ad_id(self):
        """Gets the ad_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 広告IDです。<br> このフィールドは、ADD時は無視され、SETおよびREMOVE時に必須となります。 </div> <div lang=\"en\"> Ad ID.<br> This field will be ignored in ADD operation, and will be required in SET and REMOVE operation. </div>   # noqa: E501

        :return: The ad_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this AdGroupAd.

        <div lang=\"ja\"> 広告IDです。<br> このフィールドは、ADD時は無視され、SETおよびREMOVE時に必須となります。 </div> <div lang=\"en\"> Ad ID.<br> This field will be ignored in ADD operation, and will be required in SET and REMOVE operation. </div>   # noqa: E501

        :param ad_id: The ad_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._ad_id = ad_id

    @property
    def ad_name(self):
        """Gets the ad_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 広告名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Ad name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The ad_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._ad_name

    @ad_name.setter
    def ad_name(self, ad_name):
        """Sets the ad_name of this AdGroupAd.

        <div lang=\"ja\"> 広告名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Ad name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param ad_name: The ad_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._ad_name = ad_name

    @property
    def ad_style(self):
        """Gets the ad_style of this AdGroupAd.  # noqa: E501


        :return: The ad_style of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceAdStyle
        """
        return self._ad_style

    @ad_style.setter
    def ad_style(self, ad_style):
        """Sets the ad_style of this AdGroupAd.


        :param ad_style: The ad_style of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceAdStyle
        """

        self._ad_style = ad_style

    @property
    def approval_status(self):
        """Gets the approval_status of this AdGroupAd.  # noqa: E501


        :return: The approval_status of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceApprovalStatus
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """Sets the approval_status of this AdGroupAd.


        :param approval_status: The approval_status of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceApprovalStatus
        """

        self._approval_status = approval_status

    @property
    def bid(self):
        """Gets the bid of this AdGroupAd.  # noqa: E501


        :return: The bid of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceBid
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this AdGroupAd.


        :param bid: The bid of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceBid
        """

        self._bid = bid

    @property
    def campaign_id(self):
        """Gets the campaign_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> キャンペーンIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Campaign ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The campaign_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this AdGroupAd.

        <div lang=\"ja\"> キャンペーンIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Campaign ID.<br> This field is required in requests. </div>   # noqa: E501

        :param campaign_id: The campaign_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> キャンペーン名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Campaign name.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The campaign_name of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this AdGroupAd.

        <div lang=\"ja\"> キャンペーン名です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Campaign name.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param campaign_name: The campaign_name of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._campaign_name = campaign_name

    @property
    def disapproval_reason_codes(self):
        """Gets the disapproval_reason_codes of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 掲載拒否の理由です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Reject reason on editorial review.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The disapproval_reason_codes of this AdGroupAd.  # noqa: E501
        :rtype: list[str]
        """
        return self._disapproval_reason_codes

    @disapproval_reason_codes.setter
    def disapproval_reason_codes(self, disapproval_reason_codes):
        """Sets the disapproval_reason_codes of this AdGroupAd.

        <div lang=\"ja\"> 掲載拒否の理由です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Reject reason on editorial review.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param disapproval_reason_codes: The disapproval_reason_codes of this AdGroupAd.  # noqa: E501
        :type: list[str]
        """

        self._disapproval_reason_codes = disapproval_reason_codes

    @property
    def impression_beacon_urls(self):
        """Gets the impression_beacon_urls of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> インプレッションビーコンURLです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Impression beacon URL.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The impression_beacon_urls of this AdGroupAd.  # noqa: E501
        :rtype: list[str]
        """
        return self._impression_beacon_urls

    @impression_beacon_urls.setter
    def impression_beacon_urls(self, impression_beacon_urls):
        """Sets the impression_beacon_urls of this AdGroupAd.

        <div lang=\"ja\"> インプレッションビーコンURLです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Impression beacon URL.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param impression_beacon_urls: The impression_beacon_urls of this AdGroupAd.  # noqa: E501
        :type: list[str]
        """

        self._impression_beacon_urls = impression_beacon_urls

    @property
    def is_remove_beacon_urls(self):
        """Gets the is_remove_beacon_urls of this AdGroupAd.  # noqa: E501


        :return: The is_remove_beacon_urls of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceIsRemoveFlg
        """
        return self._is_remove_beacon_urls

    @is_remove_beacon_urls.setter
    def is_remove_beacon_urls(self, is_remove_beacon_urls):
        """Sets the is_remove_beacon_urls of this AdGroupAd.


        :param is_remove_beacon_urls: The is_remove_beacon_urls of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceIsRemoveFlg
        """

        self._is_remove_beacon_urls = is_remove_beacon_urls

    @property
    def is_remove_third_party_tracking_script_url(self):
        """Gets the is_remove_third_party_tracking_script_url of this AdGroupAd.  # noqa: E501


        :return: The is_remove_third_party_tracking_script_url of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceIsRemoveFlg
        """
        return self._is_remove_third_party_tracking_script_url

    @is_remove_third_party_tracking_script_url.setter
    def is_remove_third_party_tracking_script_url(self, is_remove_third_party_tracking_script_url):
        """Sets the is_remove_third_party_tracking_script_url of this AdGroupAd.


        :param is_remove_third_party_tracking_script_url: The is_remove_third_party_tracking_script_url of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceIsRemoveFlg
        """

        self._is_remove_third_party_tracking_script_url = is_remove_third_party_tracking_script_url

    @property
    def labels(self):
        """Gets the labels of this AdGroupAd.  # noqa: E501


        :return: The labels of this AdGroupAd.  # noqa: E501
        :rtype: list[AdGroupAdServiceLabel]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AdGroupAd.


        :param labels: The labels of this AdGroupAd.  # noqa: E501
        :type: list[AdGroupAdServiceLabel]
        """

        self._labels = labels

    @property
    def media_id(self):
        """Gets the media_id of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> メディアIDです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Media ID.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The media_id of this AdGroupAd.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this AdGroupAd.

        <div lang=\"ja\"> メディアIDです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Media ID.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param media_id: The media_id of this AdGroupAd.  # noqa: E501
        :type: int
        """

        self._media_id = media_id

    @property
    def third_party_tracking_script_url(self):
        """Gets the third_party_tracking_script_url of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 第三者計測スクリプトURLです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Third party tracking script URL.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The third_party_tracking_script_url of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._third_party_tracking_script_url

    @third_party_tracking_script_url.setter
    def third_party_tracking_script_url(self, third_party_tracking_script_url):
        """Sets the third_party_tracking_script_url of this AdGroupAd.

        <div lang=\"ja\"> 第三者計測スクリプトURLです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Third party tracking script URL.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param third_party_tracking_script_url: The third_party_tracking_script_url of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._third_party_tracking_script_url = third_party_tracking_script_url

    @property
    def third_party_tracking_vendor(self):
        """Gets the third_party_tracking_vendor of this AdGroupAd.  # noqa: E501

        <div lang=\"ja\"> 第三者計測ベンダー（ReadOnly）です。<br> thirdPartyTrackingScriptUrlのドメインに基づく第三者計測ベンダーが設定されます。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Third party tracking vendor (Read only).<br> Third party tracking vendor based on domain of thirdPartyTrackingScriptUrl is set.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The third_party_tracking_vendor of this AdGroupAd.  # noqa: E501
        :rtype: str
        """
        return self._third_party_tracking_vendor

    @third_party_tracking_vendor.setter
    def third_party_tracking_vendor(self, third_party_tracking_vendor):
        """Sets the third_party_tracking_vendor of this AdGroupAd.

        <div lang=\"ja\"> 第三者計測ベンダー（ReadOnly）です。<br> thirdPartyTrackingScriptUrlのドメインに基づく第三者計測ベンダーが設定されます。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Third party tracking vendor (Read only).<br> Third party tracking vendor based on domain of thirdPartyTrackingScriptUrl is set.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param third_party_tracking_vendor: The third_party_tracking_vendor of this AdGroupAd.  # noqa: E501
        :type: str
        """

        self._third_party_tracking_vendor = third_party_tracking_vendor

    @property
    def user_status(self):
        """Gets the user_status of this AdGroupAd.  # noqa: E501


        :return: The user_status of this AdGroupAd.  # noqa: E501
        :rtype: AdGroupAdServiceUserStatus
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        """Sets the user_status of this AdGroupAd.


        :param user_status: The user_status of this AdGroupAd.  # noqa: E501
        :type: AdGroupAdServiceUserStatus
        """

        self._user_status = user_status

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
        if not isinstance(other, AdGroupAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAd):
            return True

        return self.to_dict() != other.to_dict()
