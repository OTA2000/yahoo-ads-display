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


class SearchKeywordIdeaServiceSelector(object):
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
        'keyword_frequency': 'SearchKeywordIdeaServiceKeywordFrequency',
        'keyword_ids': 'list[int]',
        'keyword_recency': 'SearchKeywordIdeaServiceKeywordRecency',
        'keywords': 'list[str]',
        'match_type': 'SearchKeywordIdeaServiceMatchType',
        'number_results': 'int',
        'sort_field': 'SearchKeywordIdeaServiceSortField',
        'sort_type': 'SearchKeywordIdeaServiceSortType',
        'start_index': 'int'
    }

    attribute_map = {
        'keyword_frequency': 'keywordFrequency',
        'keyword_ids': 'keywordIds',
        'keyword_recency': 'keywordRecency',
        'keywords': 'keywords',
        'match_type': 'matchType',
        'number_results': 'numberResults',
        'sort_field': 'sortField',
        'sort_type': 'sortType',
        'start_index': 'startIndex'
    }

    def __init__(self, keyword_frequency=None, keyword_ids=None, keyword_recency=None, keywords=None, match_type=None, number_results=1000, sort_field=None, sort_type=None, start_index=1, local_vars_configuration=None):  # noqa: E501
        """SearchKeywordIdeaServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keyword_frequency = None
        self._keyword_ids = None
        self._keyword_recency = None
        self._keywords = None
        self._match_type = None
        self._number_results = None
        self._sort_field = None
        self._sort_type = None
        self._start_index = None
        self.discriminator = None

        self.keyword_frequency = keyword_frequency
        self.keyword_ids = keyword_ids
        self.keyword_recency = keyword_recency
        self.keywords = keywords
        self.match_type = match_type
        self.number_results = number_results
        self.sort_field = sort_field
        self.sort_type = sort_type
        self.start_index = start_index

    @property
    def keyword_frequency(self):
        """Gets the keyword_frequency of this SearchKeywordIdeaServiceSelector.  # noqa: E501


        :return: The keyword_frequency of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: SearchKeywordIdeaServiceKeywordFrequency
        """
        return self._keyword_frequency

    @keyword_frequency.setter
    def keyword_frequency(self, keyword_frequency):
        """Sets the keyword_frequency of this SearchKeywordIdeaServiceSelector.


        :param keyword_frequency: The keyword_frequency of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: SearchKeywordIdeaServiceKeywordFrequency
        """

        self._keyword_frequency = keyword_frequency

    @property
    def keyword_ids(self):
        """Gets the keyword_ids of this SearchKeywordIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 検索条件：キーワードID<br> ※キーワード検索用<br> ※キーワード、キーワードIDの同時指定はできません。 </div> <div lang=\"en\">Search condition : Keyword ID.<br> *Keyword for searching.<br> *Can not specify Keyword and Keyword ID at the same time. </div>   # noqa: E501

        :return: The keyword_ids of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: list[int]
        """
        return self._keyword_ids

    @keyword_ids.setter
    def keyword_ids(self, keyword_ids):
        """Sets the keyword_ids of this SearchKeywordIdeaServiceSelector.

        <div lang=\"ja\"> 検索条件：キーワードID<br> ※キーワード検索用<br> ※キーワード、キーワードIDの同時指定はできません。 </div> <div lang=\"en\">Search condition : Keyword ID.<br> *Keyword for searching.<br> *Can not specify Keyword and Keyword ID at the same time. </div>   # noqa: E501

        :param keyword_ids: The keyword_ids of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: list[int]
        """

        self._keyword_ids = keyword_ids

    @property
    def keyword_recency(self):
        """Gets the keyword_recency of this SearchKeywordIdeaServiceSelector.  # noqa: E501


        :return: The keyword_recency of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: SearchKeywordIdeaServiceKeywordRecency
        """
        return self._keyword_recency

    @keyword_recency.setter
    def keyword_recency(self, keyword_recency):
        """Sets the keyword_recency of this SearchKeywordIdeaServiceSelector.


        :param keyword_recency: The keyword_recency of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: SearchKeywordIdeaServiceKeywordRecency
        """

        self._keyword_recency = keyword_recency

    @property
    def keywords(self):
        """Gets the keywords of this SearchKeywordIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 検索条件：キーワード<br> ※キーワード提案用<br> ※キーワード、キーワードIDの同時指定はできません。 </div> <div lang=\"en\"> Search condition : Keyword.<br> *Keyword for suggesting.<br> *Can not specify Keyword and Keyword ID at the same time. </div>   # noqa: E501

        :return: The keywords of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this SearchKeywordIdeaServiceSelector.

        <div lang=\"ja\"> 検索条件：キーワード<br> ※キーワード提案用<br> ※キーワード、キーワードIDの同時指定はできません。 </div> <div lang=\"en\"> Search condition : Keyword.<br> *Keyword for suggesting.<br> *Can not specify Keyword and Keyword ID at the same time. </div>   # noqa: E501

        :param keywords: The keywords of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def match_type(self):
        """Gets the match_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501


        :return: The match_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: SearchKeywordIdeaServiceMatchType
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this SearchKeywordIdeaServiceSelector.


        :param match_type: The match_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: SearchKeywordIdeaServiceMatchType
        """

        self._match_type = match_type

    @property
    def number_results(self):
        """Gets the number_results of this SearchKeywordIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this SearchKeywordIdeaServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results > 1000):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_results is not None and number_results < 1):  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_results = number_results

    @property
    def sort_field(self):
        """Gets the sort_field of this SearchKeywordIdeaServiceSelector.  # noqa: E501


        :return: The sort_field of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: SearchKeywordIdeaServiceSortField
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this SearchKeywordIdeaServiceSelector.


        :param sort_field: The sort_field of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: SearchKeywordIdeaServiceSortField
        """

        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501


        :return: The sort_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: SearchKeywordIdeaServiceSortType
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this SearchKeywordIdeaServiceSelector.


        :param sort_type: The sort_type of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :type: SearchKeywordIdeaServiceSortType
        """

        self._sort_type = sort_type

    @property
    def start_index(self):
        """Gets the start_index of this SearchKeywordIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this SearchKeywordIdeaServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this SearchKeywordIdeaServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this SearchKeywordIdeaServiceSelector.  # noqa: E501
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
        if not isinstance(other, SearchKeywordIdeaServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SearchKeywordIdeaServiceSelector):
            return True

        return self.to_dict() != other.to_dict()
