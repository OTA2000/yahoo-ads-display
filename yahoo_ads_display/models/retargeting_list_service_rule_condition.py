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


class RetargetingListServiceRuleCondition(object):
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
        'compare_operator': 'RetargetingListServiceCompareOperator',
        'rule_type': 'RetargetingListServiceRuleType',
        'value': 'str'
    }

    attribute_map = {
        'compare_operator': 'compareOperator',
        'rule_type': 'ruleType',
        'value': 'value'
    }

    def __init__(self, compare_operator=None, rule_type=None, value=None, local_vars_configuration=None):  # noqa: E501
        """RetargetingListServiceRuleCondition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._compare_operator = None
        self._rule_type = None
        self._value = None
        self.discriminator = None

        self.compare_operator = compare_operator
        self.rule_type = rule_type
        self.value = value

    @property
    def compare_operator(self):
        """Gets the compare_operator of this RetargetingListServiceRuleCondition.  # noqa: E501


        :return: The compare_operator of this RetargetingListServiceRuleCondition.  # noqa: E501
        :rtype: RetargetingListServiceCompareOperator
        """
        return self._compare_operator

    @compare_operator.setter
    def compare_operator(self, compare_operator):
        """Sets the compare_operator of this RetargetingListServiceRuleCondition.


        :param compare_operator: The compare_operator of this RetargetingListServiceRuleCondition.  # noqa: E501
        :type: RetargetingListServiceCompareOperator
        """

        self._compare_operator = compare_operator

    @property
    def rule_type(self):
        """Gets the rule_type of this RetargetingListServiceRuleCondition.  # noqa: E501


        :return: The rule_type of this RetargetingListServiceRuleCondition.  # noqa: E501
        :rtype: RetargetingListServiceRuleType
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this RetargetingListServiceRuleCondition.


        :param rule_type: The rule_type of this RetargetingListServiceRuleCondition.  # noqa: E501
        :type: RetargetingListServiceRuleType
        """

        self._rule_type = rule_type

    @property
    def value(self):
        """Gets the value of this RetargetingListServiceRuleCondition.  # noqa: E501

        <div lang=\"ja\"> ルールで評価する値です。<br> このフィールドは、ADDおよびSET時に必須となり、REMOVE時に無視されます。<br> ※ruleTypeがEVENT_TYPEの場合、以下のイベント種別に記載の値のみ指定可能となります。 </div> <div lang=\"en\"> Matching Rules Value. <br> This field is required in ADD and SET operation, and will be ignored in REMOVE operation.<br> ∗If ruleType is EVENT_TYPE, only the values listed in the table below can be specified. </div> <details>   <summary>     <div lang=\"ja\">イベント種別</div>     <div lang=\"en\">Event Type</div>   </summary>   <table>     <thead>       <tr>         <th>           <div lang=\"ja\">イベント種別</div>           <div lang=\"en\">Event Type</div>         </th>         <th>           <div lang=\"ja\">イベント種別名</div>           <div lang=\"en\">Name of event type</div>         </th>       </tr>     </thead>     <tbody>       <tr>         <td>app_install</td>         <td>           <div lang=\"ja\">アプリをインストール</div>           <div lang=\"en\">App install</div>         </td>       </tr>       <tr>         <td>app_launch</td>         <td>           <div lang=\"ja\">アプリ起動</div>           <div lang=\"en\">App start</div>         </td>       </tr>       <tr>         <td>app_update</td>         <td>           <div lang=\"ja\">アプリをアップデート</div>           <div lang=\"en\">App update</div>         </td>       </tr>       <tr>         <td>view_listing</td>         <td>           <div lang=\"ja\">商品一覧画面の閲覧</div>           <div lang=\"en\">View item list</div>         </td>       </tr>       <tr>         <td>view_product</td>         <td>           <div lang=\"ja\">商品詳細画面の閲覧</div>           <div lang=\"en\">View item description</div>         </td>       </tr>       <tr>         <td>view_cart</td>         <td>           <div lang=\"ja\">商品カートを閲覧</div>           <div lang=\"en\">View cart</div>         </td>       </tr>       <tr>         <td>add_wishlist</td>         <td>           <div lang=\"ja\">お気に入りに追加</div>           <div lang=\"en\">Add to wishlist</div>         </td>       </tr>       <tr>         <td>add_cart</td>         <td>           <div lang=\"ja\">商品カートに追加</div>           <div lang=\"en\">Add to cart</div>         </td>       </tr>       <tr>         <td>check_out</td>         <td>           <div lang=\"ja\">商品購入確認</div>           <div lang=\"en\">Confirm purchasing</div>         </td>       </tr>       <tr>         <td>purchase</td>         <td>           <div lang=\"ja\">商品購入</div>           <div lang=\"en\">Purchase</div>         </td>       </tr>       <tr>         <td>payment_info</td>         <td>           <div lang=\"ja\">お支払い明細を発行</div>           <div lang=\"en\">Payment details</div>         </td>       </tr>       <tr>         <td>sign_up</td>         <td>           <div lang=\"ja\">登録完了</div>           <div lang=\"en\">Registration complete</div>         </td>       </tr>       <tr>         <td>login</td>         <td>           <div lang=\"ja\">ログイン</div>           <div lang=\"en\">Login</div>         </td>       </tr>       <tr>         <td>search</td>         <td>           <div lang=\"ja\">検索</div>           <div lang=\"en\">Search</div>         </td>       </tr>       <tr>         <td>review</td>         <td>           <div lang=\"ja\">コンテンツをレビュー</div>           <div lang=\"en\">Review contents</div>         </td>       </tr>       <tr>         <td>share</td>         <td>           <div lang=\"ja\">コンテンツをシェア</div>           <div lang=\"en\">Share contents</div>         </td>       </tr>       <tr>         <td>invite</td>         <td>           <div lang=\"ja\">アプリへ招待</div>           <div lang=\"en\">Invite to app</div>         </td>       </tr>       <tr>         <td>reservation</td>         <td>           <div lang=\"ja\">予約完了</div>           <div lang=\"en\">Reservation complete</div>         </td>       </tr>       <tr>         <td>tutorial</td>         <td>           <div lang=\"ja\">チュートリアルを完了</div>           <div lang=\"en\">Tutorial complete</div>         </td>       </tr>       <tr>         <td>deeplink</td>         <td>           <div lang=\"ja\">ディープリンクから流入</div>           <div lang=\"en\">Traffic from deep link</div>         </td>       </tr>       <tr>         <td>start_level</td>         <td>           <div lang=\"ja\">ゲームイベントを開始</div>           <div lang=\"en\">Start game event</div>         </td>       </tr>       <tr>         <td>end_level</td>         <td>           <div lang=\"ja\">ゲームイベントを完了</div>           <div lang=\"en\">End game event</div>         </td>       </tr>       <tr>         <td>level_achieved</td>         <td>           <div lang=\"ja\">ゲームのレベル到達</div>           <div lang=\"en\">Level achieved</div>         </td>       </tr>       <tr>         <td>unlock_achievement</td>         <td>           <div lang=\"ja\">ゲームの目標達成</div>           <div lang=\"en\">Unlock achievement</div>         </td>       </tr>       <tr>         <td>app_purchase</td>         <td>           <div lang=\"ja\">アプリ内購入</div>           <div lang=\"en\">App purchasing</div>         </td>       </tr>       <tr>         <td>spent_credits</td>         <td>           <div lang=\"ja\">クレジットカードの利用</div>           <div lang=\"en\">Credit card</div>         </td>       </tr>       <tr>         <td>custom1</td>         <td>           <div lang=\"ja\">カスタムイベント1</div>           <div lang=\"en\">Custom event 1</div>         </td>       </tr>       <tr>         <td>custom2</td>         <td>           <div lang=\"ja\">カスタムイベント2</div>           <div lang=\"en\">Custom event 2</div>         </td>       </tr>       <tr>         <td>custom3</td>         <td>           <div lang=\"ja\">カスタムイベント3</div>           <div lang=\"en\">Custom event 3</div>         </td>       </tr>     </tbody>   </table> </details>   # noqa: E501

        :return: The value of this RetargetingListServiceRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RetargetingListServiceRuleCondition.

        <div lang=\"ja\"> ルールで評価する値です。<br> このフィールドは、ADDおよびSET時に必須となり、REMOVE時に無視されます。<br> ※ruleTypeがEVENT_TYPEの場合、以下のイベント種別に記載の値のみ指定可能となります。 </div> <div lang=\"en\"> Matching Rules Value. <br> This field is required in ADD and SET operation, and will be ignored in REMOVE operation.<br> ∗If ruleType is EVENT_TYPE, only the values listed in the table below can be specified. </div> <details>   <summary>     <div lang=\"ja\">イベント種別</div>     <div lang=\"en\">Event Type</div>   </summary>   <table>     <thead>       <tr>         <th>           <div lang=\"ja\">イベント種別</div>           <div lang=\"en\">Event Type</div>         </th>         <th>           <div lang=\"ja\">イベント種別名</div>           <div lang=\"en\">Name of event type</div>         </th>       </tr>     </thead>     <tbody>       <tr>         <td>app_install</td>         <td>           <div lang=\"ja\">アプリをインストール</div>           <div lang=\"en\">App install</div>         </td>       </tr>       <tr>         <td>app_launch</td>         <td>           <div lang=\"ja\">アプリ起動</div>           <div lang=\"en\">App start</div>         </td>       </tr>       <tr>         <td>app_update</td>         <td>           <div lang=\"ja\">アプリをアップデート</div>           <div lang=\"en\">App update</div>         </td>       </tr>       <tr>         <td>view_listing</td>         <td>           <div lang=\"ja\">商品一覧画面の閲覧</div>           <div lang=\"en\">View item list</div>         </td>       </tr>       <tr>         <td>view_product</td>         <td>           <div lang=\"ja\">商品詳細画面の閲覧</div>           <div lang=\"en\">View item description</div>         </td>       </tr>       <tr>         <td>view_cart</td>         <td>           <div lang=\"ja\">商品カートを閲覧</div>           <div lang=\"en\">View cart</div>         </td>       </tr>       <tr>         <td>add_wishlist</td>         <td>           <div lang=\"ja\">お気に入りに追加</div>           <div lang=\"en\">Add to wishlist</div>         </td>       </tr>       <tr>         <td>add_cart</td>         <td>           <div lang=\"ja\">商品カートに追加</div>           <div lang=\"en\">Add to cart</div>         </td>       </tr>       <tr>         <td>check_out</td>         <td>           <div lang=\"ja\">商品購入確認</div>           <div lang=\"en\">Confirm purchasing</div>         </td>       </tr>       <tr>         <td>purchase</td>         <td>           <div lang=\"ja\">商品購入</div>           <div lang=\"en\">Purchase</div>         </td>       </tr>       <tr>         <td>payment_info</td>         <td>           <div lang=\"ja\">お支払い明細を発行</div>           <div lang=\"en\">Payment details</div>         </td>       </tr>       <tr>         <td>sign_up</td>         <td>           <div lang=\"ja\">登録完了</div>           <div lang=\"en\">Registration complete</div>         </td>       </tr>       <tr>         <td>login</td>         <td>           <div lang=\"ja\">ログイン</div>           <div lang=\"en\">Login</div>         </td>       </tr>       <tr>         <td>search</td>         <td>           <div lang=\"ja\">検索</div>           <div lang=\"en\">Search</div>         </td>       </tr>       <tr>         <td>review</td>         <td>           <div lang=\"ja\">コンテンツをレビュー</div>           <div lang=\"en\">Review contents</div>         </td>       </tr>       <tr>         <td>share</td>         <td>           <div lang=\"ja\">コンテンツをシェア</div>           <div lang=\"en\">Share contents</div>         </td>       </tr>       <tr>         <td>invite</td>         <td>           <div lang=\"ja\">アプリへ招待</div>           <div lang=\"en\">Invite to app</div>         </td>       </tr>       <tr>         <td>reservation</td>         <td>           <div lang=\"ja\">予約完了</div>           <div lang=\"en\">Reservation complete</div>         </td>       </tr>       <tr>         <td>tutorial</td>         <td>           <div lang=\"ja\">チュートリアルを完了</div>           <div lang=\"en\">Tutorial complete</div>         </td>       </tr>       <tr>         <td>deeplink</td>         <td>           <div lang=\"ja\">ディープリンクから流入</div>           <div lang=\"en\">Traffic from deep link</div>         </td>       </tr>       <tr>         <td>start_level</td>         <td>           <div lang=\"ja\">ゲームイベントを開始</div>           <div lang=\"en\">Start game event</div>         </td>       </tr>       <tr>         <td>end_level</td>         <td>           <div lang=\"ja\">ゲームイベントを完了</div>           <div lang=\"en\">End game event</div>         </td>       </tr>       <tr>         <td>level_achieved</td>         <td>           <div lang=\"ja\">ゲームのレベル到達</div>           <div lang=\"en\">Level achieved</div>         </td>       </tr>       <tr>         <td>unlock_achievement</td>         <td>           <div lang=\"ja\">ゲームの目標達成</div>           <div lang=\"en\">Unlock achievement</div>         </td>       </tr>       <tr>         <td>app_purchase</td>         <td>           <div lang=\"ja\">アプリ内購入</div>           <div lang=\"en\">App purchasing</div>         </td>       </tr>       <tr>         <td>spent_credits</td>         <td>           <div lang=\"ja\">クレジットカードの利用</div>           <div lang=\"en\">Credit card</div>         </td>       </tr>       <tr>         <td>custom1</td>         <td>           <div lang=\"ja\">カスタムイベント1</div>           <div lang=\"en\">Custom event 1</div>         </td>       </tr>       <tr>         <td>custom2</td>         <td>           <div lang=\"ja\">カスタムイベント2</div>           <div lang=\"en\">Custom event 2</div>         </td>       </tr>       <tr>         <td>custom3</td>         <td>           <div lang=\"ja\">カスタムイベント3</div>           <div lang=\"en\">Custom event 3</div>         </td>       </tr>     </tbody>   </table> </details>   # noqa: E501

        :param value: The value of this RetargetingListServiceRuleCondition.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, RetargetingListServiceRuleCondition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RetargetingListServiceRuleCondition):
            return True

        return self.to_dict() != other.to_dict()
