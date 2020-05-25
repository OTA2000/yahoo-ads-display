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


class Label(object):
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
        'color': 'str',
        'description': 'str',
        'label_id': 'int',
        'label_name': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'color': 'color',
        'description': 'description',
        'label_id': 'labelId',
        'label_name': 'labelName'
    }

    def __init__(self, account_id=None, color=None, description=None, label_id=None, label_name=None, local_vars_configuration=None):  # noqa: E501
        """Label - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._color = None
        self._description = None
        self._label_id = None
        self._label_name = None
        self.discriminator = None

        self.account_id = account_id
        self.color = color
        self.description = description
        self.label_id = label_id
        self.label_name = label_name

    @property
    def account_id(self):
        """Gets the account_id of this Label.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The account_id of this Label.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Label.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param account_id: The account_id of this Label.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def color(self):
        """Gets the color of this Label.  # noqa: E501

        <div lang=\"ja\"> カラーです。<br> ADD時およびSET時、このフィールドは省略可能となります。ADD時のデフォルト設定値は#FFFFFFとなります。 </div> <div lang=\"en\"> Color.<br> This field is optional in ADD and SET operation. The default value in ADD operation will be #FFFFFF. </div>   # noqa: E501

        :return: The color of this Label.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Label.

        <div lang=\"ja\"> カラーです。<br> ADD時およびSET時、このフィールドは省略可能となります。ADD時のデフォルト設定値は#FFFFFFとなります。 </div> <div lang=\"en\"> Color.<br> This field is optional in ADD and SET operation. The default value in ADD operation will be #FFFFFF. </div>   # noqa: E501

        :param color: The color of this Label.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def description(self):
        """Gets the description of this Label.  # noqa: E501

        <div lang=\"ja\"> 説明文です。<br> ADD時およびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Description.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The description of this Label.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Label.

        <div lang=\"ja\"> 説明文です。<br> ADD時およびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Description.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param description: The description of this Label.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def label_id(self):
        """Gets the label_id of this Label.  # noqa: E501

        <div lang=\"ja\"> ラベルIDです。<br> SET時およびREMOVE時、このフィールドは必須です。 </div> <div lang=\"en\"> Label ID.<br> This field is required in SET and REMOVE operation. </div>   # noqa: E501

        :return: The label_id of this Label.  # noqa: E501
        :rtype: int
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this Label.

        <div lang=\"ja\"> ラベルIDです。<br> SET時およびREMOVE時、このフィールドは必須です。 </div> <div lang=\"en\"> Label ID.<br> This field is required in SET and REMOVE operation. </div>   # noqa: E501

        :param label_id: The label_id of this Label.  # noqa: E501
        :type: int
        """

        self._label_id = label_id

    @property
    def label_name(self):
        """Gets the label_name of this Label.  # noqa: E501

        <div lang=\"ja\"> ラベル名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Label Name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The label_name of this Label.  # noqa: E501
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this Label.

        <div lang=\"ja\"> ラベル名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Label Name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param label_name: The label_name of this Label.  # noqa: E501
        :type: str
        """

        self._label_name = label_name

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
        if not isinstance(other, Label):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Label):
            return True

        return self.to_dict() != other.to_dict()
