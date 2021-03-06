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


class Feed(object):
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
        'feed_id': 'int',
        'feed_name': 'str',
        'item_count': 'int',
        'approved_item_count': 'int',
        'dis_approved_item_count': 'int'
    }

    attribute_map = {
        'account_id': 'accountId',
        'feed_id': 'feedId',
        'feed_name': 'feedName',
        'item_count': 'itemCount',
        'approved_item_count': 'approvedItemCount',
        'dis_approved_item_count': 'disApprovedItemCount'
    }

    def __init__(self, account_id=None, feed_id=None, feed_name=None, item_count=None, approved_item_count=None, dis_approved_item_count=None, local_vars_configuration=None):  # noqa: E501
        """Feed - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._feed_id = None
        self._feed_name = None
        self._item_count = None
        self._approved_item_count = None
        self._dis_approved_item_count = None
        self.discriminator = None

        self.account_id = account_id
        self.feed_id = feed_id
        self.feed_name = feed_name
        self.item_count = item_count
        self.approved_item_count = approved_item_count
        self.dis_approved_item_count = dis_approved_item_count

    @property
    def account_id(self):
        """Gets the account_id of this Feed.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Account ID.<br> This field is required in requests. </div>   # noqa: E501

        :return: The account_id of this Feed.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Feed.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> Account ID.<br> This field is required in requests. </div>   # noqa: E501

        :param account_id: The account_id of this Feed.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def feed_id(self):
        """Gets the feed_id of this Feed.  # noqa: E501

        <div lang=\"ja\"> Feedを識別するIDです。<br> SET時およびREMOVE時、このフィールドは必須です。 </div> <div lang=\"en\"> ID for identifying Feed.<br> This field is required in SET and REMOVE operation. </div>   # noqa: E501

        :return: The feed_id of this Feed.  # noqa: E501
        :rtype: int
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this Feed.

        <div lang=\"ja\"> Feedを識別するIDです。<br> SET時およびREMOVE時、このフィールドは必須です。 </div> <div lang=\"en\"> ID for identifying Feed.<br> This field is required in SET and REMOVE operation. </div>   # noqa: E501

        :param feed_id: The feed_id of this Feed.  # noqa: E501
        :type: int
        """

        self._feed_id = feed_id

    @property
    def feed_name(self):
        """Gets the feed_name of this Feed.  # noqa: E501

        <div lang=\"ja\"> Feedを識別する名称です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Name for identifying Feed.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The feed_name of this Feed.  # noqa: E501
        :rtype: str
        """
        return self._feed_name

    @feed_name.setter
    def feed_name(self, feed_name):
        """Sets the feed_name of this Feed.

        <div lang=\"ja\"> Feedを識別する名称です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Name for identifying Feed.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param feed_name: The feed_name of this Feed.  # noqa: E501
        :type: str
        """

        self._feed_name = feed_name

    @property
    def item_count(self):
        """Gets the item_count of this Feed.  # noqa: E501

        <div lang=\"ja\"> アイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The item_count of this Feed.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this Feed.

        <div lang=\"ja\"> アイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param item_count: The item_count of this Feed.  # noqa: E501
        :type: int
        """

        self._item_count = item_count

    @property
    def approved_item_count(self):
        """Gets the approved_item_count of this Feed.  # noqa: E501

        <div lang=\"ja\"> 審査済みアイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of approved items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The approved_item_count of this Feed.  # noqa: E501
        :rtype: int
        """
        return self._approved_item_count

    @approved_item_count.setter
    def approved_item_count(self, approved_item_count):
        """Sets the approved_item_count of this Feed.

        <div lang=\"ja\"> 審査済みアイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of approved items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param approved_item_count: The approved_item_count of this Feed.  # noqa: E501
        :type: int
        """

        self._approved_item_count = approved_item_count

    @property
    def dis_approved_item_count(self):
        """Gets the dis_approved_item_count of this Feed.  # noqa: E501

        <div lang=\"ja\"> 審査否認アイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of disapproved items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The dis_approved_item_count of this Feed.  # noqa: E501
        :rtype: int
        """
        return self._dis_approved_item_count

    @dis_approved_item_count.setter
    def dis_approved_item_count(self, dis_approved_item_count):
        """Sets the dis_approved_item_count of this Feed.

        <div lang=\"ja\"> 審査否認アイテム数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Number of disapproved items.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param dis_approved_item_count: The dis_approved_item_count of this Feed.  # noqa: E501
        :type: int
        """

        self._dis_approved_item_count = dis_approved_item_count

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
        if not isinstance(other, Feed):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Feed):
            return True

        return self.to_dict() != other.to_dict()
