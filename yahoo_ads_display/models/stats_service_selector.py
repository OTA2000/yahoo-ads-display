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


class StatsServiceSelector(object):
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
        'campaign_ids': 'list[int]',
        'ad_group_ids': 'list[int]',
        'ad_ids': 'list[int]',
        'media_ids': 'list[int]',
        'stats_period': 'StatsServiceStatsPeriod',
        'period_custom_date': 'StatsServicePeriodCustomDate',
        'target_types': 'list[StatsServiceTargetType]',
        'type': 'StatsServiceType',
        'start_index': 'int',
        'number_results': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'campaign_ids': 'campaignIds',
        'ad_group_ids': 'adGroupIds',
        'ad_ids': 'adIds',
        'media_ids': 'mediaIds',
        'stats_period': 'statsPeriod',
        'period_custom_date': 'periodCustomDate',
        'target_types': 'targetTypes',
        'type': 'type',
        'start_index': 'startIndex',
        'number_results': 'numberResults'
    }

    def __init__(self, account_id=None, campaign_ids=None, ad_group_ids=None, ad_ids=None, media_ids=None, stats_period=None, period_custom_date=None, target_types=None, type=None, start_index=1, number_results=500, local_vars_configuration=None):  # noqa: E501
        """StatsServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._campaign_ids = None
        self._ad_group_ids = None
        self._ad_ids = None
        self._media_ids = None
        self._stats_period = None
        self._period_custom_date = None
        self._target_types = None
        self._type = None
        self._start_index = None
        self._number_results = None
        self.discriminator = None

        self.account_id = account_id
        self.campaign_ids = campaign_ids
        self.ad_group_ids = ad_group_ids
        self.ad_ids = ad_ids
        self.media_ids = media_ids
        self.stats_period = stats_period
        self.period_custom_date = period_custom_date
        self.target_types = target_types
        self.type = type
        self.start_index = start_index
        self.number_results = number_results

    @property
    def account_id(self):
        """Gets the account_id of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\">アカウントID</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :return: The account_id of this StatsServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this StatsServiceSelector.

        <div lang=\"ja\">アカウントID</div> <div lang=\"en\">Account ID.</div>   # noqa: E501

        :param account_id: The account_id of this StatsServiceSelector.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def campaign_ids(self):
        """Gets the campaign_ids of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\"> キャンペーンID<br> typeで「CAMPAIGN」または「ADGROUP」または「AD」または「TARGET」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Campaign ID.<br> Available only when &#34;CAMPAIGN&#34; or &#34;ADGROUP&#34; or &#34;AD&#34; or &#34;TARGET&#34; is specified for type. </div>   # noqa: E501

        :return: The campaign_ids of this StatsServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, campaign_ids):
        """Sets the campaign_ids of this StatsServiceSelector.

        <div lang=\"ja\"> キャンペーンID<br> typeで「CAMPAIGN」または「ADGROUP」または「AD」または「TARGET」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Campaign ID.<br> Available only when &#34;CAMPAIGN&#34; or &#34;ADGROUP&#34; or &#34;AD&#34; or &#34;TARGET&#34; is specified for type. </div>   # noqa: E501

        :param campaign_ids: The campaign_ids of this StatsServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._campaign_ids = campaign_ids

    @property
    def ad_group_ids(self):
        """Gets the ad_group_ids of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 広告グループID<br> typeで「ADGROUP」または「AD」または「TARGET」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Ad group ID.<br> Available only when &#34;ADGROUP&#34; or &#34;AD&#34; or &#34;TARGET&#34; is specified for type. </div>   # noqa: E501

        :return: The ad_group_ids of this StatsServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_group_ids

    @ad_group_ids.setter
    def ad_group_ids(self, ad_group_ids):
        """Sets the ad_group_ids of this StatsServiceSelector.

        <div lang=\"ja\"> 広告グループID<br> typeで「ADGROUP」または「AD」または「TARGET」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Ad group ID.<br> Available only when &#34;ADGROUP&#34; or &#34;AD&#34; or &#34;TARGET&#34; is specified for type. </div>   # noqa: E501

        :param ad_group_ids: The ad_group_ids of this StatsServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._ad_group_ids = ad_group_ids

    @property
    def ad_ids(self):
        """Gets the ad_ids of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 広告ID<br> typeで「AD」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Ad ID.<br> Available only when &#34;AD&#34; is specified for type. </div>   # noqa: E501

        :return: The ad_ids of this StatsServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_ids

    @ad_ids.setter
    def ad_ids(self, ad_ids):
        """Sets the ad_ids of this StatsServiceSelector.

        <div lang=\"ja\"> 広告ID<br> typeで「AD」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Ad ID.<br> Available only when &#34;AD&#34; is specified for type. </div>   # noqa: E501

        :param ad_ids: The ad_ids of this StatsServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._ad_ids = ad_ids

    @property
    def media_ids(self):
        """Gets the media_ids of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 画像ID<br> typeで「MEDIA」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Media ID.<br> Available only when &#34;MEDIA&#34; is specified for type. </div>   # noqa: E501

        :return: The media_ids of this StatsServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._media_ids

    @media_ids.setter
    def media_ids(self, media_ids):
        """Sets the media_ids of this StatsServiceSelector.

        <div lang=\"ja\"> 画像ID<br> typeで「MEDIA」を指定した場合のみ有効です。 </div> <div lang=\"en\"> Media ID.<br> Available only when &#34;MEDIA&#34; is specified for type. </div>   # noqa: E501

        :param media_ids: The media_ids of this StatsServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._media_ids = media_ids

    @property
    def stats_period(self):
        """Gets the stats_period of this StatsServiceSelector.  # noqa: E501


        :return: The stats_period of this StatsServiceSelector.  # noqa: E501
        :rtype: StatsServiceStatsPeriod
        """
        return self._stats_period

    @stats_period.setter
    def stats_period(self, stats_period):
        """Sets the stats_period of this StatsServiceSelector.


        :param stats_period: The stats_period of this StatsServiceSelector.  # noqa: E501
        :type: StatsServiceStatsPeriod
        """

        self._stats_period = stats_period

    @property
    def period_custom_date(self):
        """Gets the period_custom_date of this StatsServiceSelector.  # noqa: E501


        :return: The period_custom_date of this StatsServiceSelector.  # noqa: E501
        :rtype: StatsServicePeriodCustomDate
        """
        return self._period_custom_date

    @period_custom_date.setter
    def period_custom_date(self, period_custom_date):
        """Sets the period_custom_date of this StatsServiceSelector.


        :param period_custom_date: The period_custom_date of this StatsServiceSelector.  # noqa: E501
        :type: StatsServicePeriodCustomDate
        """

        self._period_custom_date = period_custom_date

    @property
    def target_types(self):
        """Gets the target_types of this StatsServiceSelector.  # noqa: E501


        :return: The target_types of this StatsServiceSelector.  # noqa: E501
        :rtype: list[StatsServiceTargetType]
        """
        return self._target_types

    @target_types.setter
    def target_types(self, target_types):
        """Sets the target_types of this StatsServiceSelector.


        :param target_types: The target_types of this StatsServiceSelector.  # noqa: E501
        :type: list[StatsServiceTargetType]
        """

        self._target_types = target_types

    @property
    def type(self):
        """Gets the type of this StatsServiceSelector.  # noqa: E501


        :return: The type of this StatsServiceSelector.  # noqa: E501
        :rtype: StatsServiceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatsServiceSelector.


        :param type: The type of this StatsServiceSelector.  # noqa: E501
        :type: StatsServiceType
        """

        self._type = type

    @property
    def start_index(self):
        """Gets the start_index of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this StatsServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this StatsServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this StatsServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_index is not None and start_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._start_index = start_index

    @property
    def number_results(self):
        """Gets the number_results of this StatsServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this StatsServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this StatsServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this StatsServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results > 500):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_results = number_results

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
        if not isinstance(other, StatsServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsServiceSelector):
            return True

        return self.to_dict() != other.to_dict()
