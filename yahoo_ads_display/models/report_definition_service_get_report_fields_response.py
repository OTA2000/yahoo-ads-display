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


class ReportDefinitionServiceGetReportFieldsResponse(object):
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
        'errors': 'list[Error]',
        'rid': 'str',
        'rval': 'ReportDefinitionServiceFieldValue'
    }

    attribute_map = {
        'errors': 'errors',
        'rid': 'rid',
        'rval': 'rval'
    }

    def __init__(self, errors=None, rid=None, rval=None, local_vars_configuration=None):  # noqa: E501
        """ReportDefinitionServiceGetReportFieldsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._rid = None
        self._rval = None
        self.discriminator = None

        self.errors = errors
        if rid is not None:
            self.rid = rid
        self.rval = rval

    @property
    def errors(self):
        """Gets the errors of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501


        :return: The errors of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ReportDefinitionServiceGetReportFieldsResponse.


        :param errors: The errors of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def rid(self):
        """Gets the rid of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501


        :return: The rid of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :rtype: str
        """
        return self._rid

    @rid.setter
    def rid(self, rid):
        """Sets the rid of this ReportDefinitionServiceGetReportFieldsResponse.


        :param rid: The rid of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :type: str
        """

        self._rid = rid

    @property
    def rval(self):
        """Gets the rval of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501


        :return: The rval of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :rtype: ReportDefinitionServiceFieldValue
        """
        return self._rval

    @rval.setter
    def rval(self, rval):
        """Sets the rval of this ReportDefinitionServiceGetReportFieldsResponse.


        :param rval: The rval of this ReportDefinitionServiceGetReportFieldsResponse.  # noqa: E501
        :type: ReportDefinitionServiceFieldValue
        """

        self._rval = rval

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
        if not isinstance(other, ReportDefinitionServiceGetReportFieldsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportDefinitionServiceGetReportFieldsResponse):
            return True

        return self.to_dict() != other.to_dict()
