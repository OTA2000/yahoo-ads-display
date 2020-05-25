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


class AdGroupAdServiceResponsiveImageAd(object):
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
        'button_text': 'AdGroupAdServiceButtonText',
        'description': 'str',
        'display_url': 'str',
        'headline': 'str',
        'logo_media_id': 'int',
        'principal': 'str',
        'url': 'str'
    }

    attribute_map = {
        'button_text': 'buttonText',
        'description': 'description',
        'display_url': 'displayUrl',
        'headline': 'headline',
        'logo_media_id': 'logoMediaId',
        'principal': 'principal',
        'url': 'url'
    }

    def __init__(self, button_text=None, description=None, display_url=None, headline=None, logo_media_id=None, principal=None, url=None, local_vars_configuration=None):  # noqa: E501
        """AdGroupAdServiceResponsiveImageAd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._button_text = None
        self._description = None
        self._display_url = None
        self._headline = None
        self._logo_media_id = None
        self._principal = None
        self._url = None
        self.discriminator = None

        self.button_text = button_text
        self.description = description
        self.display_url = display_url
        self.headline = headline
        self.logo_media_id = logo_media_id
        self.principal = principal
        self.url = url

    @property
    def button_text(self):
        """Gets the button_text of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501


        :return: The button_text of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: AdGroupAdServiceButtonText
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this AdGroupAdServiceResponsiveImageAd.


        :param button_text: The button_text of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: AdGroupAdServiceButtonText
        """

        self._button_text = button_text

    @property
    def description(self):
        """Gets the description of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> 説明文です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Description.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The description of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> 説明文です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Description.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param description: The description of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_url(self):
        """Gets the display_url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> 表示URLです。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ・標準キャンペーンの場合<br> &nbsp;&nbsp;ADDでは入力必須です。SETでの入力は任意です。<br> ・アプリキャンペーンの場合<br> &nbsp;&nbsp;ADD、SETのどちらも指定できません。<br> &nbsp;&nbsp;※アプリキャンペーンで指定したDeviceOsTypeに基づき、以下のいずれかのURLが自動で設定されます。<br> &nbsp;&nbsp;&nbsp;&nbsp;- iOSの場合：itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- Androidの場合：play.google.com<br> </div> <div lang=\"en\"> Display URL.<br> This field is optional in ADD and SET operation.<br> - Standard campaign:<br> &nbsp;&nbsp;Required for ADD, optional for SET.<br> - Mobile app campaign:<br> &nbsp;&nbsp;Not allowed for ADD and SET.<br> &nbsp;&nbsp;*Based on DeviceOsType specified on Mobile app campaign, any of the following URLs will be automatically set.<br> &nbsp;&nbsp;&nbsp;&nbsp;- For iOS : itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- For Android : play.google.com<br> </div>   # noqa: E501

        :return: The display_url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: str
        """
        return self._display_url

    @display_url.setter
    def display_url(self, display_url):
        """Sets the display_url of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> 表示URLです。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ・標準キャンペーンの場合<br> &nbsp;&nbsp;ADDでは入力必須です。SETでの入力は任意です。<br> ・アプリキャンペーンの場合<br> &nbsp;&nbsp;ADD、SETのどちらも指定できません。<br> &nbsp;&nbsp;※アプリキャンペーンで指定したDeviceOsTypeに基づき、以下のいずれかのURLが自動で設定されます。<br> &nbsp;&nbsp;&nbsp;&nbsp;- iOSの場合：itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- Androidの場合：play.google.com<br> </div> <div lang=\"en\"> Display URL.<br> This field is optional in ADD and SET operation.<br> - Standard campaign:<br> &nbsp;&nbsp;Required for ADD, optional for SET.<br> - Mobile app campaign:<br> &nbsp;&nbsp;Not allowed for ADD and SET.<br> &nbsp;&nbsp;*Based on DeviceOsType specified on Mobile app campaign, any of the following URLs will be automatically set.<br> &nbsp;&nbsp;&nbsp;&nbsp;- For iOS : itunes.apple.com<br> &nbsp;&nbsp;&nbsp;&nbsp;- For Android : play.google.com<br> </div>   # noqa: E501

        :param display_url: The display_url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: str
        """

        self._display_url = display_url

    @property
    def headline(self):
        """Gets the headline of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> タイトルです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Title.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The headline of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """Sets the headline of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> タイトルです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Title.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param headline: The headline of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: str
        """

        self._headline = headline

    @property
    def logo_media_id(self):
        """Gets the logo_media_id of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> ロゴ画像のメディアIDです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Media ID of logo image.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :return: The logo_media_id of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: int
        """
        return self._logo_media_id

    @logo_media_id.setter
    def logo_media_id(self, logo_media_id):
        """Sets the logo_media_id of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> ロゴ画像のメディアIDです。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> Media ID of logo image.<br> This field is optional in ADD and SET operation. </div>   # noqa: E501

        :param logo_media_id: The logo_media_id of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: int
        """

        self._logo_media_id = logo_media_id

    @property
    def principal(self):
        """Gets the principal of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> 広告の主体者表記です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Advertiser Indication.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The principal of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> 広告の主体者表記です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Advertiser Indication.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param principal: The principal of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def url(self):
        """Gets the url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AdGroupAdServiceResponsiveImageAd.

        <div lang=\"ja\"> リンク先URLです。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Destination URL.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param url: The url of this AdGroupAdServiceResponsiveImageAd.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, AdGroupAdServiceResponsiveImageAd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdGroupAdServiceResponsiveImageAd):
            return True

        return self.to_dict() != other.to_dict()
