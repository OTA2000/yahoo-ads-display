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


class FeedFtp(object):
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
        'active_status': 'FeedFtpServiceActiveStatus',
        'feed_id': 'int',
        'feed_url': 'str',
        'item_list_upload_type': 'FeedFtpServiceItemListUploadType',
        'schedule': 'FeedFtpServiceSchedule',
        'user_name': 'str',
        'user_password': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'active_status': 'activeStatus',
        'feed_id': 'feedId',
        'feed_url': 'feedUrl',
        'item_list_upload_type': 'itemListUploadType',
        'schedule': 'schedule',
        'user_name': 'userName',
        'user_password': 'userPassword'
    }

    def __init__(self, account_id=None, active_status=None, feed_id=None, feed_url=None, item_list_upload_type=None, schedule=None, user_name=None, user_password=None, local_vars_configuration=None):  # noqa: E501
        """FeedFtp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._active_status = None
        self._feed_id = None
        self._feed_url = None
        self._item_list_upload_type = None
        self._schedule = None
        self._user_name = None
        self._user_password = None
        self.discriminator = None

        self.account_id = account_id
        self.active_status = active_status
        self.feed_id = feed_id
        self.feed_url = feed_url
        self.item_list_upload_type = item_list_upload_type
        self.schedule = schedule
        self.user_name = user_name
        self.user_password = user_password

    @property
    def account_id(self):
        """Gets the account_id of this FeedFtp.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The account_id of this FeedFtp.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this FeedFtp.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param account_id: The account_id of this FeedFtp.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def active_status(self):
        """Gets the active_status of this FeedFtp.  # noqa: E501


        :return: The active_status of this FeedFtp.  # noqa: E501
        :rtype: FeedFtpServiceActiveStatus
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this FeedFtp.


        :param active_status: The active_status of this FeedFtp.  # noqa: E501
        :type: FeedFtpServiceActiveStatus
        """

        self._active_status = active_status

    @property
    def feed_id(self):
        """Gets the feed_id of this FeedFtp.  # noqa: E501

        <div lang=\"ja\"> Feedを識別するIdです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Feed ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The feed_id of this FeedFtp.  # noqa: E501
        :rtype: int
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this FeedFtp.

        <div lang=\"ja\"> Feedを識別するIdです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Feed ID.<br> This field is required in requests. </div>   # noqa: E501

        :param feed_id: The feed_id of this FeedFtp.  # noqa: E501
        :type: int
        """

        self._feed_id = feed_id

    @property
    def feed_url(self):
        """Gets the feed_url of this FeedFtp.  # noqa: E501

        <div lang=\"ja\"> 商品リストファイルのURLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> URL of item list file.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The feed_url of this FeedFtp.  # noqa: E501
        :rtype: str
        """
        return self._feed_url

    @feed_url.setter
    def feed_url(self, feed_url):
        """Sets the feed_url of this FeedFtp.

        <div lang=\"ja\"> 商品リストファイルのURLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> URL of item list file.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param feed_url: The feed_url of this FeedFtp.  # noqa: E501
        :type: str
        """

        self._feed_url = feed_url

    @property
    def item_list_upload_type(self):
        """Gets the item_list_upload_type of this FeedFtp.  # noqa: E501


        :return: The item_list_upload_type of this FeedFtp.  # noqa: E501
        :rtype: FeedFtpServiceItemListUploadType
        """
        return self._item_list_upload_type

    @item_list_upload_type.setter
    def item_list_upload_type(self, item_list_upload_type):
        """Sets the item_list_upload_type of this FeedFtp.


        :param item_list_upload_type: The item_list_upload_type of this FeedFtp.  # noqa: E501
        :type: FeedFtpServiceItemListUploadType
        """

        self._item_list_upload_type = item_list_upload_type

    @property
    def schedule(self):
        """Gets the schedule of this FeedFtp.  # noqa: E501


        :return: The schedule of this FeedFtp.  # noqa: E501
        :rtype: FeedFtpServiceSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this FeedFtp.


        :param schedule: The schedule of this FeedFtp.  # noqa: E501
        :type: FeedFtpServiceSchedule
        """

        self._schedule = schedule

    @property
    def user_name(self):
        """Gets the user_name of this FeedFtp.  # noqa: E501

        <div lang=\"ja\"> ユーザー名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> User name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The user_name of this FeedFtp.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this FeedFtp.

        <div lang=\"ja\"> ユーザー名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> User name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param user_name: The user_name of this FeedFtp.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_password(self):
        """Gets the user_password of this FeedFtp.  # noqa: E501

        <div lang=\"ja\"> パスワードです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Password.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The user_password of this FeedFtp.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this FeedFtp.

        <div lang=\"ja\"> パスワードです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Password.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param user_password: The user_password of this FeedFtp.  # noqa: E501
        :type: str
        """

        self._user_password = user_password

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
        if not isinstance(other, FeedFtp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeedFtp):
            return True

        return self.to_dict() != other.to_dict()
