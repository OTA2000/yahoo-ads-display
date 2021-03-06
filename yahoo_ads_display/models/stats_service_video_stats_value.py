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


class StatsServiceVideoStatsValue(object):
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
        'media_id': 'int',
        'video_name': 'str',
        'video_title': 'str',
        'stats': 'Stats'
    }

    attribute_map = {
        'media_id': 'mediaId',
        'video_name': 'videoName',
        'video_title': 'videoTitle',
        'stats': 'stats'
    }

    def __init__(self, media_id=None, video_name=None, video_title=None, stats=None, local_vars_configuration=None):  # noqa: E501
        """StatsServiceVideoStatsValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._media_id = None
        self._video_name = None
        self._video_title = None
        self._stats = None
        self.discriminator = None

        self.media_id = media_id
        self.video_name = video_name
        self.video_title = video_title
        self.stats = stats

    @property
    def media_id(self):
        """Gets the media_id of this StatsServiceVideoStatsValue.  # noqa: E501

        <div lang=\"ja\">メディアID</div> <div lang=\"en\">Media ID</div>   # noqa: E501

        :return: The media_id of this StatsServiceVideoStatsValue.  # noqa: E501
        :rtype: int
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id):
        """Sets the media_id of this StatsServiceVideoStatsValue.

        <div lang=\"ja\">メディアID</div> <div lang=\"en\">Media ID</div>   # noqa: E501

        :param media_id: The media_id of this StatsServiceVideoStatsValue.  # noqa: E501
        :type: int
        """

        self._media_id = media_id

    @property
    def video_name(self):
        """Gets the video_name of this StatsServiceVideoStatsValue.  # noqa: E501

        <div lang=\"ja\">実ファイル名</div> <div lang=\"en\">File name</div>   # noqa: E501

        :return: The video_name of this StatsServiceVideoStatsValue.  # noqa: E501
        :rtype: str
        """
        return self._video_name

    @video_name.setter
    def video_name(self, video_name):
        """Sets the video_name of this StatsServiceVideoStatsValue.

        <div lang=\"ja\">実ファイル名</div> <div lang=\"en\">File name</div>   # noqa: E501

        :param video_name: The video_name of this StatsServiceVideoStatsValue.  # noqa: E501
        :type: str
        """

        self._video_name = video_name

    @property
    def video_title(self):
        """Gets the video_title of this StatsServiceVideoStatsValue.  # noqa: E501

        <div lang=\"ja\">ビデオ名</div> <div lang=\"en\">Video title</div>   # noqa: E501

        :return: The video_title of this StatsServiceVideoStatsValue.  # noqa: E501
        :rtype: str
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        """Sets the video_title of this StatsServiceVideoStatsValue.

        <div lang=\"ja\">ビデオ名</div> <div lang=\"en\">Video title</div>   # noqa: E501

        :param video_title: The video_title of this StatsServiceVideoStatsValue.  # noqa: E501
        :type: str
        """

        self._video_title = video_title

    @property
    def stats(self):
        """Gets the stats of this StatsServiceVideoStatsValue.  # noqa: E501


        :return: The stats of this StatsServiceVideoStatsValue.  # noqa: E501
        :rtype: Stats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this StatsServiceVideoStatsValue.


        :param stats: The stats of this StatsServiceVideoStatsValue.  # noqa: E501
        :type: Stats
        """

        self._stats = stats

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
        if not isinstance(other, StatsServiceVideoStatsValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsServiceVideoStatsValue):
            return True

        return self.to_dict() != other.to_dict()
