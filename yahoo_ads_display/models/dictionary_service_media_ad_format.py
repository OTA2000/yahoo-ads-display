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


class DictionaryServiceMediaAdFormat(object):
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
        'ad_format': 'str',
        'aspect': 'bool',
        'aspect_height': 'int',
        'aspect_ratio': 'str',
        'aspect_width': 'int',
        'campaign_banner': 'bool',
        'height': 'int',
        'logo': 'bool',
        'max_height': 'int',
        'max_width': 'int',
        'size': 'int',
        'size_to': 'int',
        'static_image': 'bool',
        'thumbnail': 'bool',
        'transparent': 'bool',
        'width': 'int'
    }

    attribute_map = {
        'ad_format': 'adFormat',
        'aspect': 'aspect',
        'aspect_height': 'aspectHeight',
        'aspect_ratio': 'aspectRatio',
        'aspect_width': 'aspectWidth',
        'campaign_banner': 'campaignBanner',
        'height': 'height',
        'logo': 'logo',
        'max_height': 'maxHeight',
        'max_width': 'maxWidth',
        'size': 'size',
        'size_to': 'sizeTo',
        'static_image': 'staticImage',
        'thumbnail': 'thumbnail',
        'transparent': 'transparent',
        'width': 'width'
    }

    def __init__(self, ad_format=None, aspect=None, aspect_height=None, aspect_ratio=None, aspect_width=None, campaign_banner=None, height=None, logo=None, max_height=None, max_width=None, size=None, size_to=None, static_image=None, thumbnail=None, transparent=None, width=None, local_vars_configuration=None):  # noqa: E501
        """DictionaryServiceMediaAdFormat - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ad_format = None
        self._aspect = None
        self._aspect_height = None
        self._aspect_ratio = None
        self._aspect_width = None
        self._campaign_banner = None
        self._height = None
        self._logo = None
        self._max_height = None
        self._max_width = None
        self._size = None
        self._size_to = None
        self._static_image = None
        self._thumbnail = None
        self._transparent = None
        self._width = None
        self.discriminator = None

        self.ad_format = ad_format
        self.aspect = aspect
        self.aspect_height = aspect_height
        self.aspect_ratio = aspect_ratio
        self.aspect_width = aspect_width
        self.campaign_banner = campaign_banner
        self.height = height
        self.logo = logo
        self.max_height = max_height
        self.max_width = max_width
        self.size = size
        self.size_to = size_to
        self.static_image = static_image
        self.thumbnail = thumbnail
        self.transparent = transparent
        self.width = width

    @property
    def ad_format(self):
        """Gets the ad_format of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">ディスプレイ（画像）広告のフォーマットです。</div> <div lang=\"en\">Format of display (image) ads</div>   # noqa: E501

        :return: The ad_format of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: str
        """
        return self._ad_format

    @ad_format.setter
    def ad_format(self, ad_format):
        """Sets the ad_format of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">ディスプレイ（画像）広告のフォーマットです。</div> <div lang=\"en\">Format of display (image) ads</div>   # noqa: E501

        :param ad_format: The ad_format of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: str
        """

        self._ad_format = ad_format

    @property
    def aspect(self):
        """Gets the aspect of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">アスペクト比対応かどうかを示します。</div> <div lang=\"en\">This field indicates whether the aspect ratio is supported.</div>   # noqa: E501

        :return: The aspect of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._aspect

    @aspect.setter
    def aspect(self, aspect):
        """Sets the aspect of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">アスペクト比対応かどうかを示します。</div> <div lang=\"en\">This field indicates whether the aspect ratio is supported.</div>   # noqa: E501

        :param aspect: The aspect of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._aspect = aspect

    @property
    def aspect_height(self):
        """Gets the aspect_height of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">画像アスペクト比：高さ [ratio]です。</div> <div lang=\"en\">Image aspect ratio: height [ratio]</div>   # noqa: E501

        :return: The aspect_height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._aspect_height

    @aspect_height.setter
    def aspect_height(self, aspect_height):
        """Sets the aspect_height of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">画像アスペクト比：高さ [ratio]です。</div> <div lang=\"en\">Image aspect ratio: height [ratio]</div>   # noqa: E501

        :param aspect_height: The aspect_height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._aspect_height = aspect_height

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">アスペクト比です。</div> <div lang=\"en\">Aspect ratio.</div>   # noqa: E501

        :return: The aspect_ratio of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: str
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">アスペクト比です。</div> <div lang=\"en\">Aspect ratio.</div>   # noqa: E501

        :param aspect_ratio: The aspect_ratio of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: str
        """

        self._aspect_ratio = aspect_ratio

    @property
    def aspect_width(self):
        """Gets the aspect_width of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">画像アスペクト比：幅 [ratio]です。</div> <div lang=\"en\">Image aspect ratio: width [ratio]</div>   # noqa: E501

        :return: The aspect_width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._aspect_width

    @aspect_width.setter
    def aspect_width(self, aspect_width):
        """Sets the aspect_width of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">画像アスペクト比：幅 [ratio]です。</div> <div lang=\"en\">Image aspect ratio: width [ratio]</div>   # noqa: E501

        :param aspect_width: The aspect_width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._aspect_width = aspect_width

    @property
    def campaign_banner(self):
        """Gets the campaign_banner of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">キャンペーンバナー画像である/キャンペーンバナー画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a campaign banner image or not.</div>   # noqa: E501

        :return: The campaign_banner of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._campaign_banner

    @campaign_banner.setter
    def campaign_banner(self, campaign_banner):
        """Sets the campaign_banner of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">キャンペーンバナー画像である/キャンペーンバナー画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a campaign banner image or not.</div>   # noqa: E501

        :param campaign_banner: The campaign_banner of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._campaign_banner = campaign_banner

    @property
    def height(self):
        """Gets the height of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">最小画像サイズ：高さ [pixel]です。</div> <div lang=\"en\">Minimum image size: height [pixel]</div>   # noqa: E501

        :return: The height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">最小画像サイズ：高さ [pixel]です。</div> <div lang=\"en\">Minimum image size: height [pixel]</div>   # noqa: E501

        :param height: The height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def logo(self):
        """Gets the logo of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">ロゴ画像である/ロゴ画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a logo image or not.</div>   # noqa: E501

        :return: The logo of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">ロゴ画像である/ロゴ画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a logo image or not.</div>   # noqa: E501

        :param logo: The logo of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._logo = logo

    @property
    def max_height(self):
        """Gets the max_height of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">サイズ上限：高さ [pixel]です。</div> <div lang=\"en\">Size limit: height [pixel]</div>   # noqa: E501

        :return: The max_height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">サイズ上限：高さ [pixel]です。</div> <div lang=\"en\">Size limit: height [pixel]</div>   # noqa: E501

        :param max_height: The max_height of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._max_height = max_height

    @property
    def max_width(self):
        """Gets the max_width of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">サイズ上限：幅 [pixel]です。</div> <div lang=\"en\">Size limit: width [pixel]</div>   # noqa: E501

        :return: The max_width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">サイズ上限：幅 [pixel]です。</div> <div lang=\"en\">Size limit: width [pixel]</div>   # noqa: E501

        :param max_width: The max_width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._max_width = max_width

    @property
    def size(self):
        """Gets the size of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">画像の最大容量：[byte]です。</div> <div lang=\"en\">Maximum image capacity: [byte]</div>   # noqa: E501

        :return: The size of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">画像の最大容量：[byte]です。</div> <div lang=\"en\">Maximum image capacity: [byte]</div>   # noqa: E501

        :param size: The size of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def size_to(self):
        """Gets the size_to of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">画像圧縮後の容量：[byte]です。</div> <div lang=\"en\">Image compression capacity: [byte]</div>   # noqa: E501

        :return: The size_to of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._size_to

    @size_to.setter
    def size_to(self, size_to):
        """Sets the size_to of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">画像圧縮後の容量：[byte]です。</div> <div lang=\"en\">Image compression capacity: [byte]</div>   # noqa: E501

        :param size_to: The size_to of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._size_to = size_to

    @property
    def static_image(self):
        """Gets the static_image of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">静止画用の画像かどうかを示します。</div> <div lang=\"en\">This field indicates whether it is a static image.</div>   # noqa: E501

        :return: The static_image of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._static_image

    @static_image.setter
    def static_image(self, static_image):
        """Sets the static_image of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">静止画用の画像かどうかを示します。</div> <div lang=\"en\">This field indicates whether it is a static image.</div>   # noqa: E501

        :param static_image: The static_image of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._static_image = static_image

    @property
    def thumbnail(self):
        """Gets the thumbnail of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">サムネイル画像である/サムネイル画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a thumbnail image image or not.</div>   # noqa: E501

        :return: The thumbnail of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">サムネイル画像である/サムネイル画像ではないことを示します。</div> <div lang=\"en\">This field indicates whether it is a thumbnail image image or not.</div>   # noqa: E501

        :param thumbnail: The thumbnail of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._thumbnail = thumbnail

    @property
    def transparent(self):
        """Gets the transparent of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">透過画像の許可/不許可を示します。</div> <div lang=\"en\">This field indicates whether transparent image is permitted.</div>   # noqa: E501

        :return: The transparent of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: bool
        """
        return self._transparent

    @transparent.setter
    def transparent(self, transparent):
        """Sets the transparent of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">透過画像の許可/不許可を示します。</div> <div lang=\"en\">This field indicates whether transparent image is permitted.</div>   # noqa: E501

        :param transparent: The transparent of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: bool
        """

        self._transparent = transparent

    @property
    def width(self):
        """Gets the width of this DictionaryServiceMediaAdFormat.  # noqa: E501

        <div lang=\"ja\">最小画像サイズ：幅 [pixel]です。</div> <div lang=\"en\">Minimum image size: width [pixel]</div>   # noqa: E501

        :return: The width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this DictionaryServiceMediaAdFormat.

        <div lang=\"ja\">最小画像サイズ：幅 [pixel]です。</div> <div lang=\"en\">Minimum image size: width [pixel]</div>   # noqa: E501

        :param width: The width of this DictionaryServiceMediaAdFormat.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if not isinstance(other, DictionaryServiceMediaAdFormat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DictionaryServiceMediaAdFormat):
            return True

        return self.to_dict() != other.to_dict()
