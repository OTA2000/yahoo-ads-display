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


class ConversionTracker(object):
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
        'all_conversion_value': 'str',
        'all_conversions': 'int',
        'app_conversion': 'ConversionTrackerServiceAppConversion',
        'category': 'ConversionTrackerServiceCategory',
        'conversion_tracker_id': 'int',
        'conversion_tracker_name': 'str',
        'conversion_tracker_type': 'ConversionTrackerServiceType',
        'conversion_value': 'str',
        'conversion_value_via_ad_click': 'str',
        'conversions': 'int',
        'conversions_via_ad_click': 'int',
        'counting_type': 'ConversionTrackerServiceCountingType',
        'cross_device_conversions': 'int',
        'exclude_from_bidding': 'ConversionTrackerServiceExcludeFromBidding',
        'measurement_period': 'int',
        'measurement_period_view': 'int',
        'most_recent_conversion_date': 'str',
        'status': 'ConversionTrackerServiceStatus',
        'user_revenue_value': 'int',
        'web_conversion': 'ConversionTrackerServiceWebConversion'
    }

    attribute_map = {
        'account_id': 'accountId',
        'all_conversion_value': 'allConversionValue',
        'all_conversions': 'allConversions',
        'app_conversion': 'appConversion',
        'category': 'category',
        'conversion_tracker_id': 'conversionTrackerId',
        'conversion_tracker_name': 'conversionTrackerName',
        'conversion_tracker_type': 'conversionTrackerType',
        'conversion_value': 'conversionValue',
        'conversion_value_via_ad_click': 'conversionValueViaAdClick',
        'conversions': 'conversions',
        'conversions_via_ad_click': 'conversionsViaAdClick',
        'counting_type': 'countingType',
        'cross_device_conversions': 'crossDeviceConversions',
        'exclude_from_bidding': 'excludeFromBidding',
        'measurement_period': 'measurementPeriod',
        'measurement_period_view': 'measurementPeriodView',
        'most_recent_conversion_date': 'mostRecentConversionDate',
        'status': 'status',
        'user_revenue_value': 'userRevenueValue',
        'web_conversion': 'webConversion'
    }

    def __init__(self, account_id=None, all_conversion_value=None, all_conversions=None, app_conversion=None, category=None, conversion_tracker_id=None, conversion_tracker_name=None, conversion_tracker_type=None, conversion_value=None, conversion_value_via_ad_click=None, conversions=None, conversions_via_ad_click=None, counting_type=None, cross_device_conversions=None, exclude_from_bidding=None, measurement_period=None, measurement_period_view=None, most_recent_conversion_date=None, status=None, user_revenue_value=None, web_conversion=None, local_vars_configuration=None):  # noqa: E501
        """ConversionTracker - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._all_conversion_value = None
        self._all_conversions = None
        self._app_conversion = None
        self._category = None
        self._conversion_tracker_id = None
        self._conversion_tracker_name = None
        self._conversion_tracker_type = None
        self._conversion_value = None
        self._conversion_value_via_ad_click = None
        self._conversions = None
        self._conversions_via_ad_click = None
        self._counting_type = None
        self._cross_device_conversions = None
        self._exclude_from_bidding = None
        self._measurement_period = None
        self._measurement_period_view = None
        self._most_recent_conversion_date = None
        self._status = None
        self._user_revenue_value = None
        self._web_conversion = None
        self.discriminator = None

        self.account_id = account_id
        self.all_conversion_value = all_conversion_value
        self.all_conversions = all_conversions
        self.app_conversion = app_conversion
        self.category = category
        self.conversion_tracker_id = conversion_tracker_id
        self.conversion_tracker_name = conversion_tracker_name
        self.conversion_tracker_type = conversion_tracker_type
        self.conversion_value = conversion_value
        self.conversion_value_via_ad_click = conversion_value_via_ad_click
        self.conversions = conversions
        self.conversions_via_ad_click = conversions_via_ad_click
        self.counting_type = counting_type
        self.cross_device_conversions = cross_device_conversions
        self.exclude_from_bidding = exclude_from_bidding
        self.measurement_period = measurement_period
        self.measurement_period_view = measurement_period_view
        self.most_recent_conversion_date = most_recent_conversion_date
        self.status = status
        self.user_revenue_value = user_revenue_value
        self.web_conversion = web_conversion

    @property
    def account_id(self):
        """Gets the account_id of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The account_id of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ConversionTracker.

        <div lang=\"ja\"> アカウントIDです。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Account ID.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param account_id: The account_id of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def all_conversion_value(self):
        """Gets the all_conversion_value of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョンの価値（全て）です。 </div> <div lang=\"en\"> Conv. value (all). </div>   # noqa: E501

        :return: The all_conversion_value of this ConversionTracker.  # noqa: E501
        :rtype: str
        """
        return self._all_conversion_value

    @all_conversion_value.setter
    def all_conversion_value(self, all_conversion_value):
        """Sets the all_conversion_value of this ConversionTracker.

        <div lang=\"ja\"> コンバージョンの価値（全て）です。 </div> <div lang=\"en\"> Conv. value (all). </div>   # noqa: E501

        :param all_conversion_value: The all_conversion_value of this ConversionTracker.  # noqa: E501
        :type: str
        """

        self._all_conversion_value = all_conversion_value

    @property
    def all_conversions(self):
        """Gets the all_conversions of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョン数（全て）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions (all).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The all_conversions of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._all_conversions

    @all_conversions.setter
    def all_conversions(self, all_conversions):
        """Sets the all_conversions of this ConversionTracker.

        <div lang=\"ja\"> コンバージョン数（全て）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions (all).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param all_conversions: The all_conversions of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._all_conversions = all_conversions

    @property
    def app_conversion(self):
        """Gets the app_conversion of this ConversionTracker.  # noqa: E501


        :return: The app_conversion of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceAppConversion
        """
        return self._app_conversion

    @app_conversion.setter
    def app_conversion(self, app_conversion):
        """Sets the app_conversion of this ConversionTracker.


        :param app_conversion: The app_conversion of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceAppConversion
        """

        self._app_conversion = app_conversion

    @property
    def category(self):
        """Gets the category of this ConversionTracker.  # noqa: E501


        :return: The category of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ConversionTracker.


        :param category: The category of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceCategory
        """

        self._category = category

    @property
    def conversion_tracker_id(self):
        """Gets the conversion_tracker_id of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョントラッカーIDです。<br> このフィールドは、ADD時は無視され、SET時は必須となります。 </div> <div lang=\"en\"> Conversion Tracker ID.<br> This field will be ignored in ADD operation, and will be required in SET operation. </div>   # noqa: E501

        :return: The conversion_tracker_id of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._conversion_tracker_id

    @conversion_tracker_id.setter
    def conversion_tracker_id(self, conversion_tracker_id):
        """Sets the conversion_tracker_id of this ConversionTracker.

        <div lang=\"ja\"> コンバージョントラッカーIDです。<br> このフィールドは、ADD時は無視され、SET時は必須となります。 </div> <div lang=\"en\"> Conversion Tracker ID.<br> This field will be ignored in ADD operation, and will be required in SET operation. </div>   # noqa: E501

        :param conversion_tracker_id: The conversion_tracker_id of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._conversion_tracker_id = conversion_tracker_id

    @property
    def conversion_tracker_name(self):
        """Gets the conversion_tracker_name of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョントラッカー名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Conversion Tracker Name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :return: The conversion_tracker_name of this ConversionTracker.  # noqa: E501
        :rtype: str
        """
        return self._conversion_tracker_name

    @conversion_tracker_name.setter
    def conversion_tracker_name(self, conversion_tracker_name):
        """Sets the conversion_tracker_name of this ConversionTracker.

        <div lang=\"ja\"> コンバージョントラッカー名です。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> Conversion Tracker Name.<br> This field is required in ADD operation, and will be optional in SET operation. </div>   # noqa: E501

        :param conversion_tracker_name: The conversion_tracker_name of this ConversionTracker.  # noqa: E501
        :type: str
        """

        self._conversion_tracker_name = conversion_tracker_name

    @property
    def conversion_tracker_type(self):
        """Gets the conversion_tracker_type of this ConversionTracker.  # noqa: E501


        :return: The conversion_tracker_type of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceType
        """
        return self._conversion_tracker_type

    @conversion_tracker_type.setter
    def conversion_tracker_type(self, conversion_tracker_type):
        """Sets the conversion_tracker_type of this ConversionTracker.


        :param conversion_tracker_type: The conversion_tracker_type of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceType
        """

        self._conversion_tracker_type = conversion_tracker_type

    @property
    def conversion_value(self):
        """Gets the conversion_value of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョンの価値/コンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conv. value/conv.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The conversion_value of this ConversionTracker.  # noqa: E501
        :rtype: str
        """
        return self._conversion_value

    @conversion_value.setter
    def conversion_value(self, conversion_value):
        """Sets the conversion_value of this ConversionTracker.

        <div lang=\"ja\"> コンバージョンの価値/コンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conv. value/conv.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param conversion_value: The conversion_value of this ConversionTracker.  # noqa: E501
        :type: str
        """

        self._conversion_value = conversion_value

    @property
    def conversion_value_via_ad_click(self):
        """Gets the conversion_value_via_ad_click of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョンの価値（クリック経由）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conv. value (via click).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The conversion_value_via_ad_click of this ConversionTracker.  # noqa: E501
        :rtype: str
        """
        return self._conversion_value_via_ad_click

    @conversion_value_via_ad_click.setter
    def conversion_value_via_ad_click(self, conversion_value_via_ad_click):
        """Sets the conversion_value_via_ad_click of this ConversionTracker.

        <div lang=\"ja\"> コンバージョンの価値（クリック経由）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conv. value (via click).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param conversion_value_via_ad_click: The conversion_value_via_ad_click of this ConversionTracker.  # noqa: E501
        :type: str
        """

        self._conversion_value_via_ad_click = conversion_value_via_ad_click

    @property
    def conversions(self):
        """Gets the conversions of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The conversions of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._conversions

    @conversions.setter
    def conversions(self, conversions):
        """Sets the conversions of this ConversionTracker.

        <div lang=\"ja\"> コンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param conversions: The conversions of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._conversions = conversions

    @property
    def conversions_via_ad_click(self):
        """Gets the conversions_via_ad_click of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョン数（クリック経由）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions (via click).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The conversions_via_ad_click of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._conversions_via_ad_click

    @conversions_via_ad_click.setter
    def conversions_via_ad_click(self, conversions_via_ad_click):
        """Sets the conversions_via_ad_click of this ConversionTracker.

        <div lang=\"ja\"> コンバージョン数（クリック経由）です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Conversions (via click).<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param conversions_via_ad_click: The conversions_via_ad_click of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._conversions_via_ad_click = conversions_via_ad_click

    @property
    def counting_type(self):
        """Gets the counting_type of this ConversionTracker.  # noqa: E501


        :return: The counting_type of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceCountingType
        """
        return self._counting_type

    @counting_type.setter
    def counting_type(self, counting_type):
        """Sets the counting_type of this ConversionTracker.


        :param counting_type: The counting_type of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceCountingType
        """

        self._counting_type = counting_type

    @property
    def cross_device_conversions(self):
        """Gets the cross_device_conversions of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> クロスデバイスコンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Cross-device conv.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The cross_device_conversions of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._cross_device_conversions

    @cross_device_conversions.setter
    def cross_device_conversions(self, cross_device_conversions):
        """Sets the cross_device_conversions of this ConversionTracker.

        <div lang=\"ja\"> クロスデバイスコンバージョン数です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> Cross-device conv.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param cross_device_conversions: The cross_device_conversions of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._cross_device_conversions = cross_device_conversions

    @property
    def exclude_from_bidding(self):
        """Gets the exclude_from_bidding of this ConversionTracker.  # noqa: E501


        :return: The exclude_from_bidding of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceExcludeFromBidding
        """
        return self._exclude_from_bidding

    @exclude_from_bidding.setter
    def exclude_from_bidding(self, exclude_from_bidding):
        """Sets the exclude_from_bidding of this ConversionTracker.


        :param exclude_from_bidding: The exclude_from_bidding of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceExcludeFromBidding
        """

        self._exclude_from_bidding = exclude_from_bidding

    @property
    def measurement_period(self):
        """Gets the measurement_period of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> 計測期間（単位：日）です。<br> ※7～90の範囲内で指定可能です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は30となります。 </div> <div lang=\"en\"> Counting period (Unit: Day).<br> ∗ Can be specified within the range of 7 to 90 days.<br> This field is optional in requests. The default value in ADD operation will be 30. </div>   # noqa: E501

        :return: The measurement_period of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._measurement_period

    @measurement_period.setter
    def measurement_period(self, measurement_period):
        """Sets the measurement_period of this ConversionTracker.

        <div lang=\"ja\"> 計測期間（単位：日）です。<br> ※7～90の範囲内で指定可能です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は30となります。 </div> <div lang=\"en\"> Counting period (Unit: Day).<br> ∗ Can be specified within the range of 7 to 90 days.<br> This field is optional in requests. The default value in ADD operation will be 30. </div>   # noqa: E501

        :param measurement_period: The measurement_period of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._measurement_period = measurement_period

    @property
    def measurement_period_view(self):
        """Gets the measurement_period_view of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> 測定期間（動画視聴）<br> ※1-30の範囲で指定可能です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は1となります。 </div> <div lang=\"en\"> Counting period (Video view).<br> ∗ Can be specified within the range of 1 to 30.<br> This field is optional in requests. The default value in ADD operation will be 1. </div>   # noqa: E501

        :return: The measurement_period_view of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._measurement_period_view

    @measurement_period_view.setter
    def measurement_period_view(self, measurement_period_view):
        """Sets the measurement_period_view of this ConversionTracker.

        <div lang=\"ja\"> 測定期間（動画視聴）<br> ※1-30の範囲で指定可能です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は1となります。 </div> <div lang=\"en\"> Counting period (Video view).<br> ∗ Can be specified within the range of 1 to 30.<br> This field is optional in requests. The default value in ADD operation will be 1. </div>   # noqa: E501

        :param measurement_period_view: The measurement_period_view of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._measurement_period_view = measurement_period_view

    @property
    def most_recent_conversion_date(self):
        """Gets the most_recent_conversion_date of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョンが発生した直近の日付です。<br> ※YYYYMMDD形式です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> The date of the most recent conversion.<br> ∗ Format: YYYYMMDD.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :return: The most_recent_conversion_date of this ConversionTracker.  # noqa: E501
        :rtype: str
        """
        return self._most_recent_conversion_date

    @most_recent_conversion_date.setter
    def most_recent_conversion_date(self, most_recent_conversion_date):
        """Sets the most_recent_conversion_date of this ConversionTracker.

        <div lang=\"ja\"> コンバージョンが発生した直近の日付です。<br> ※YYYYMMDD形式です。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> The date of the most recent conversion.<br> ∗ Format: YYYYMMDD.<br> Although this field will be returned in the response, it will be ignored on input. </div>   # noqa: E501

        :param most_recent_conversion_date: The most_recent_conversion_date of this ConversionTracker.  # noqa: E501
        :type: str
        """

        self._most_recent_conversion_date = most_recent_conversion_date

    @property
    def status(self):
        """Gets the status of this ConversionTracker.  # noqa: E501


        :return: The status of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConversionTracker.


        :param status: The status of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceStatus
        """

        self._status = status

    @property
    def user_revenue_value(self):
        """Gets the user_revenue_value of this ConversionTracker.  # noqa: E501

        <div lang=\"ja\"> コンバージョンの収益値です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は0となります。 </div> <div lang=\"en\"> Revenue value for Conversions.<br> This field is optional in requests. The default value in ADD operation will be 0. </div>   # noqa: E501

        :return: The user_revenue_value of this ConversionTracker.  # noqa: E501
        :rtype: int
        """
        return self._user_revenue_value

    @user_revenue_value.setter
    def user_revenue_value(self, user_revenue_value):
        """Sets the user_revenue_value of this ConversionTracker.

        <div lang=\"ja\"> コンバージョンの収益値です。<br> このフィールドは、リクエストの場合は省略可能です。ADD時のデフォルト設定値は0となります。 </div> <div lang=\"en\"> Revenue value for Conversions.<br> This field is optional in requests. The default value in ADD operation will be 0. </div>   # noqa: E501

        :param user_revenue_value: The user_revenue_value of this ConversionTracker.  # noqa: E501
        :type: int
        """

        self._user_revenue_value = user_revenue_value

    @property
    def web_conversion(self):
        """Gets the web_conversion of this ConversionTracker.  # noqa: E501


        :return: The web_conversion of this ConversionTracker.  # noqa: E501
        :rtype: ConversionTrackerServiceWebConversion
        """
        return self._web_conversion

    @web_conversion.setter
    def web_conversion(self, web_conversion):
        """Sets the web_conversion of this ConversionTracker.


        :param web_conversion: The web_conversion of this ConversionTracker.  # noqa: E501
        :type: ConversionTrackerServiceWebConversion
        """

        self._web_conversion = web_conversion

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
        if not isinstance(other, ConversionTracker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConversionTracker):
            return True

        return self.to_dict() != other.to_dict()
