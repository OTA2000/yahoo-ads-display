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


class CampaignServiceSelector(object):
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
        'campaign_goal_filter_type': 'CampaignServiceGoalFilterType',
        'campaign_ids': 'list[int]',
        'campaign_type': 'CampaignServiceType',
        'contains_label_id_flg': 'bool',
        'feed_ids': 'list[int]',
        'label_ids': 'list[int]',
        'number_results': 'int',
        'start_index': 'int',
        'user_statuses': 'list[CampaignServiceUserStatus]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'campaign_goal_filter_type': 'campaignGoalFilterType',
        'campaign_ids': 'campaignIds',
        'campaign_type': 'campaignType',
        'contains_label_id_flg': 'containsLabelIdFlg',
        'feed_ids': 'feedIds',
        'label_ids': 'labelIds',
        'number_results': 'numberResults',
        'start_index': 'startIndex',
        'user_statuses': 'userStatuses'
    }

    def __init__(self, account_id=None, campaign_goal_filter_type=None, campaign_ids=None, campaign_type=None, contains_label_id_flg=None, feed_ids=None, label_ids=None, number_results=500, start_index=1, user_statuses=None, local_vars_configuration=None):  # noqa: E501
        """CampaignServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._campaign_goal_filter_type = None
        self._campaign_ids = None
        self._campaign_type = None
        self._contains_label_id_flg = None
        self._feed_ids = None
        self._label_ids = None
        self._number_results = None
        self._start_index = None
        self._user_statuses = None
        self.discriminator = None

        self.account_id = account_id
        self.campaign_goal_filter_type = campaign_goal_filter_type
        self.campaign_ids = campaign_ids
        self.campaign_type = campaign_type
        self.contains_label_id_flg = contains_label_id_flg
        self.feed_ids = feed_ids
        self.label_ids = label_ids
        self.number_results = number_results
        self.start_index = start_index
        self.user_statuses = user_statuses

    @property
    def account_id(self):
        """Gets the account_id of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">検索条件 : アカウントID</div> <div lang=\"en\">Search Condition: Account ID</div>   # noqa: E501

        :return: The account_id of this CampaignServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CampaignServiceSelector.

        <div lang=\"ja\">検索条件 : アカウントID</div> <div lang=\"en\">Search Condition: Account ID</div>   # noqa: E501

        :param account_id: The account_id of this CampaignServiceSelector.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def campaign_goal_filter_type(self):
        """Gets the campaign_goal_filter_type of this CampaignServiceSelector.  # noqa: E501


        :return: The campaign_goal_filter_type of this CampaignServiceSelector.  # noqa: E501
        :rtype: CampaignServiceGoalFilterType
        """
        return self._campaign_goal_filter_type

    @campaign_goal_filter_type.setter
    def campaign_goal_filter_type(self, campaign_goal_filter_type):
        """Sets the campaign_goal_filter_type of this CampaignServiceSelector.


        :param campaign_goal_filter_type: The campaign_goal_filter_type of this CampaignServiceSelector.  # noqa: E501
        :type: CampaignServiceGoalFilterType
        """

        self._campaign_goal_filter_type = campaign_goal_filter_type

    @property
    def campaign_ids(self):
        """Gets the campaign_ids of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">検索条件 : キャンペーンID</div> <div lang=\"en\">Search Condition: Campaign ID</div>   # noqa: E501

        :return: The campaign_ids of this CampaignServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, campaign_ids):
        """Sets the campaign_ids of this CampaignServiceSelector.

        <div lang=\"ja\">検索条件 : キャンペーンID</div> <div lang=\"en\">Search Condition: Campaign ID</div>   # noqa: E501

        :param campaign_ids: The campaign_ids of this CampaignServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._campaign_ids = campaign_ids

    @property
    def campaign_type(self):
        """Gets the campaign_type of this CampaignServiceSelector.  # noqa: E501


        :return: The campaign_type of this CampaignServiceSelector.  # noqa: E501
        :rtype: CampaignServiceType
        """
        return self._campaign_type

    @campaign_type.setter
    def campaign_type(self, campaign_type):
        """Sets the campaign_type of this CampaignServiceSelector.


        :param campaign_type: The campaign_type of this CampaignServiceSelector.  # noqa: E501
        :type: CampaignServiceType
        """

        self._campaign_type = campaign_type

    @property
    def contains_label_id_flg(self):
        """Gets the contains_label_id_flg of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">ラベルID取得フラグ</div> <div lang=\"en\">Flag of contains label ID</div>   # noqa: E501

        :return: The contains_label_id_flg of this CampaignServiceSelector.  # noqa: E501
        :rtype: bool
        """
        return self._contains_label_id_flg

    @contains_label_id_flg.setter
    def contains_label_id_flg(self, contains_label_id_flg):
        """Sets the contains_label_id_flg of this CampaignServiceSelector.

        <div lang=\"ja\">ラベルID取得フラグ</div> <div lang=\"en\">Flag of contains label ID</div>   # noqa: E501

        :param contains_label_id_flg: The contains_label_id_flg of this CampaignServiceSelector.  # noqa: E501
        :type: bool
        """

        self._contains_label_id_flg = contains_label_id_flg

    @property
    def feed_ids(self):
        """Gets the feed_ids of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">検索条件 : フィードID</div> <div lang=\"en\">Search Condition: Feed ID</div>   # noqa: E501

        :return: The feed_ids of this CampaignServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._feed_ids

    @feed_ids.setter
    def feed_ids(self, feed_ids):
        """Sets the feed_ids of this CampaignServiceSelector.

        <div lang=\"ja\">検索条件 : フィードID</div> <div lang=\"en\">Search Condition: Feed ID</div>   # noqa: E501

        :param feed_ids: The feed_ids of this CampaignServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._feed_ids = feed_ids

    @property
    def label_ids(self):
        """Gets the label_ids of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">検索条件 : ラベルID</div> <div lang=\"en\">Search Condition: Label ID</div>   # noqa: E501

        :return: The label_ids of this CampaignServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this CampaignServiceSelector.

        <div lang=\"ja\">検索条件 : ラベルID</div> <div lang=\"en\">Search Condition: Label ID</div>   # noqa: E501

        :param label_ids: The label_ids of this CampaignServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._label_ids = label_ids

    @property
    def number_results(self):
        """Gets the number_results of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this CampaignServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this CampaignServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this CampaignServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results > 500):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value less than or equal to `500`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_results = number_results

    @property
    def start_index(self):
        """Gets the start_index of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this CampaignServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this CampaignServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this CampaignServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_index is not None and start_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._start_index = start_index

    @property
    def user_statuses(self):
        """Gets the user_statuses of this CampaignServiceSelector.  # noqa: E501

        <div lang=\"ja\">検索条件 : 取得範囲</div> <div lang=\"en\">Search Condition: Delivery status of user settings</div>   # noqa: E501

        :return: The user_statuses of this CampaignServiceSelector.  # noqa: E501
        :rtype: list[CampaignServiceUserStatus]
        """
        return self._user_statuses

    @user_statuses.setter
    def user_statuses(self, user_statuses):
        """Sets the user_statuses of this CampaignServiceSelector.

        <div lang=\"ja\">検索条件 : 取得範囲</div> <div lang=\"en\">Search Condition: Delivery status of user settings</div>   # noqa: E501

        :param user_statuses: The user_statuses of this CampaignServiceSelector.  # noqa: E501
        :type: list[CampaignServiceUserStatus]
        """

        self._user_statuses = user_statuses

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
        if not isinstance(other, CampaignServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignServiceSelector):
            return True

        return self.to_dict() != other.to_dict()