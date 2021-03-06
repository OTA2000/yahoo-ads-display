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


class PlacementUrlIdeaServiceSelector(object):
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
        'keyword': 'str',
        'site_categories': 'list[str]',
        'ad_formats': 'list[PlacementUrlIdeaServiceAdFormatConditions]',
        'start_index': 'int',
        'number_results': 'int'
    }

    attribute_map = {
        'keyword': 'keyword',
        'site_categories': 'siteCategories',
        'ad_formats': 'adFormats',
        'start_index': 'startIndex',
        'number_results': 'numberResults'
    }

    def __init__(self, keyword=None, site_categories=None, ad_formats=None, start_index=1, number_results=500, local_vars_configuration=None):  # noqa: E501
        """PlacementUrlIdeaServiceSelector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keyword = None
        self._site_categories = None
        self._ad_formats = None
        self._start_index = None
        self._number_results = None
        self.discriminator = None

        self.keyword = keyword
        self.site_categories = site_categories
        self.ad_formats = ad_formats
        self.start_index = start_index
        self.number_results = number_results

    @property
    def keyword(self):
        """Gets the keyword of this PlacementUrlIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\"> 検索キーワードの配列です。<br> ・URLを検索するためのキーワードです。<br> ・部分一致です。<br> ・スペース区切りでAND検索です。<br> ・最大文字数250です。<br> ・スペース区切りでの単語数は最大10個です。 </div> <div lang=\"en\"> Array of Search keyword.<br> ・Keyword to search the URL<br> ・Broad match<br> ・Search all keywords (AND), separated by spaces<br> ・Maximum of 250 characters<br> ・Maximum of 10 spaces to separate the words </div>   # noqa: E501

        :return: The keyword of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this PlacementUrlIdeaServiceSelector.

        <div lang=\"ja\"> 検索キーワードの配列です。<br> ・URLを検索するためのキーワードです。<br> ・部分一致です。<br> ・スペース区切りでAND検索です。<br> ・最大文字数250です。<br> ・スペース区切りでの単語数は最大10個です。 </div> <div lang=\"en\"> Array of Search keyword.<br> ・Keyword to search the URL<br> ・Broad match<br> ・Search all keywords (AND), separated by spaces<br> ・Maximum of 250 characters<br> ・Maximum of 10 spaces to separate the words </div>   # noqa: E501

        :param keyword: The keyword of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

    @property
    def site_categories(self):
        """Gets the site_categories of this PlacementUrlIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\"> カテゴリの配列です。<br> ・URLのカテゴリです。<br> ・完全一致です。<br> ・複数指定でOR検索です。<br> ・TC-SC-xxxxxxで現される規定値です。<br> ・DicitonaryServiceから返ってくるTC-SC-xxxxxxをそのまま指定です。<br> ・最大50件です。 </div> <div lang=\"en\"> Array of categories.<br> ・Category of URL<br> ・Exact match<br> ・Search multiple specific keywords (OR)<br> ・From value: TC-SC-xxxxxx<br> ・Choose the TC-SC-xxxxxx value from DictionaryService<br> ・Maximum of 50 cases </div>   # noqa: E501

        :return: The site_categories of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :rtype: list[str]
        """
        return self._site_categories

    @site_categories.setter
    def site_categories(self, site_categories):
        """Sets the site_categories of this PlacementUrlIdeaServiceSelector.

        <div lang=\"ja\"> カテゴリの配列です。<br> ・URLのカテゴリです。<br> ・完全一致です。<br> ・複数指定でOR検索です。<br> ・TC-SC-xxxxxxで現される規定値です。<br> ・DicitonaryServiceから返ってくるTC-SC-xxxxxxをそのまま指定です。<br> ・最大50件です。 </div> <div lang=\"en\"> Array of categories.<br> ・Category of URL<br> ・Exact match<br> ・Search multiple specific keywords (OR)<br> ・From value: TC-SC-xxxxxx<br> ・Choose the TC-SC-xxxxxx value from DictionaryService<br> ・Maximum of 50 cases </div>   # noqa: E501

        :param site_categories: The site_categories of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :type: list[str]
        """

        self._site_categories = site_categories

    @property
    def ad_formats(self):
        """Gets the ad_formats of this PlacementUrlIdeaServiceSelector.  # noqa: E501


        :return: The ad_formats of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :rtype: list[PlacementUrlIdeaServiceAdFormatConditions]
        """
        return self._ad_formats

    @ad_formats.setter
    def ad_formats(self, ad_formats):
        """Sets the ad_formats of this PlacementUrlIdeaServiceSelector.


        :param ad_formats: The ad_formats of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :type: list[PlacementUrlIdeaServiceAdFormatConditions]
        """

        self._ad_formats = ad_formats

    @property
    def start_index(self):
        """Gets the start_index of this PlacementUrlIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :return: The start_index of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this PlacementUrlIdeaServiceSelector.

        <div lang=\"ja\">ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Index of the first result to return in this page. This field must be greater than or equal to 1.</div>   # noqa: E501

        :param start_index: The start_index of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                start_index is not None and start_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `start_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._start_index = start_index

    @property
    def number_results(self):
        """Gets the number_results of this PlacementUrlIdeaServiceSelector.  # noqa: E501

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :return: The number_results of this PlacementUrlIdeaServiceSelector.  # noqa: E501
        :rtype: int
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this PlacementUrlIdeaServiceSelector.

        <div lang=\"ja\">ページの最大件数です。このフィールドは、1以上を指定する必要があります。</div> <div lang=\"en\">Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.</div>   # noqa: E501

        :param number_results: The number_results of this PlacementUrlIdeaServiceSelector.  # noqa: E501
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
        if not isinstance(other, PlacementUrlIdeaServiceSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlacementUrlIdeaServiceSelector):
            return True

        return self.to_dict() != other.to_dict()
