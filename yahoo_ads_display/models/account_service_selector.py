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


class AccountServiceSelector(object):
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
        'account_ids': 'list[int]',
        'account_name': 'str',
        'account_statuses': 'list[AccountServiceStatus]',
        'account_types': 'list[AccountServiceType]',
        'auth_type': 'AccountServiceAuthType',
        'include_test_account': 'AccountServiceIncludeTestAccount',
        'number_results': 'int',
        'start_index': 'int'
    }

    attribute_map = {
        'account_ids': 'accountIds',
        'account_name': 'accountName',
        'account_statuses': 'accountStatuses',
        'account_types': 'accountTypes',
        'auth_type': 'authType',
        'include_test_account': 'includeTestAccount',
        'number_results': 'numberResults',
        'start_index': 'startIndex'
    }

    def __init__(self, account_ids=None, account_name=None, account_statuses=None, account_types=None, auth_type=None, include_test_account=None, number_results=500, start_index=1, local_vars_configuration=None):  # noqa: E501
        """AccountServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_ids = None
        self._account_name = None
        self._account_statuses = None
        self._account_types = None
        self._auth_type = None
        self._include_test_account = None
        self._number_results = None
        self._start_index = None
        self.discriminator = None

        self.account_ids = account_ids
        self.account_name = account_name
        self.account_statuses = account_statuses
        self.account_types = account_types
        self.auth_type = auth_type
        self.include_test_account = include_test_account
        self.number_results = number_results
        self.start_index = start_index

    @property
    def account_ids(self):
        """Gets the account_ids of this AccountServiceSelector.  # noqa: E501

        <div lang=\"ja\">指定しない場合は紐づくアカウントをすべて取得します。</div> <div lang=\"en\">If nothing is selected, all accounts are retrieved.</div>   # noqa: E501

        :return: The account_ids of this AccountServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this AccountServiceSelector.

        <div lang=\"ja\">指定しない場合は紐づくアカウントをすべて取得します。</div> <div lang=\"en\">If nothing is selected, all accounts are retrieved.</div>   # noqa: E501

        :param account_ids: The account_ids of this AccountServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._account_ids = account_ids

    @property
    def account_name(self):
        """Gets the account_name of this AccountServiceSelector.  # noqa: E501

        <div lang=\"ja\">アカウント名です。</div> <div lang=\"en\">Account name.</div>   # noqa: E501

        :return: The account_name of this AccountServiceSelector.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this AccountServiceSelector.

        <div lang=\"ja\">アカウント名です。</div> <div lang=\"en\">Account name.</div>   # noqa: E501

        :param account_name: The account_name of this AccountServiceSelector.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_statuses(self):
        """Gets the account_statuses of this AccountServiceSelector.  # noqa: E501


        :return: The account_statuses of this AccountServiceSelector.  # noqa: E501
        :rtype: list[AccountServiceStatus]
        """
        return self._account_statuses

    @account_statuses.setter
    def account_statuses(self, account_statuses):
        """Sets the account_statuses of this AccountServiceSelector.


        :param account_statuses: The account_statuses of this AccountServiceSelector.  # noqa: E501
        :type: list[AccountServiceStatus]
        """

        self._account_statuses = account_statuses

    @property
    def account_types(self):
        """Gets the account_types of this AccountServiceSelector.  # noqa: E501


        :return: The account_types of this AccountServiceSelector.  # noqa: E501
        :rtype: list[AccountServiceType]
        """
        return self._account_types

    @account_types.setter
    def account_types(self, account_types):
        """Sets the account_types of this AccountServiceSelector.


        :param account_types: The account_types of this AccountServiceSelector.  # noqa: E501
        :type: list[AccountServiceType]
        """

        self._account_types = account_types

    @property
    def auth_type(self):
        """Gets the auth_type of this AccountServiceSelector.  # noqa: E501


        :return: The auth_type of this AccountServiceSelector.  # noqa: E501
        :rtype: AccountServiceAuthType
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this AccountServiceSelector.


        :param auth_type: The auth_type of this AccountServiceSelector.  # noqa: E501
        :type: AccountServiceAuthType
        """

        self._auth_type = auth_type

    @property
    def include_test_account(self):
        """Gets the include_test_account of this AccountServiceSelector.  # noqa: E501


        :return: The include_test_account of this AccountServiceSelector.  # noqa: E501
        :rtype: AccountServiceIncludeTestAccount
        """
        return self._include_test_account

    @include_test_account.setter
    def include_test_account(self, include_test_account):
        """Sets the include_test_account of this AccountServiceSelector.


        :param include_test_account: The include_test_account of this AccountServiceSelector.  # noqa: E501
        :type: AccountServiceIncludeTestAccount
        """

        self._include_test_account = include_test_account

    @property
    def number_results(self):
        """Gets the number_results of this AccountServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this AccountServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this AccountServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this AccountServiceSelector.  # noqa: E501
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
        """Gets the start_index of this AccountServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this AccountServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this AccountServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this AccountServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_index is not None and start_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._start_index = start_index

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
        if not isinstance(other, AccountServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountServiceSelector):
            return True

        return self.to_dict() != other.to_dict()
