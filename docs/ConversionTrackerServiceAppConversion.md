# ConversionTrackerServiceAppConversion

<div lang=\"ja\"> ConversionTrackerServiceAppConversionオブジェクトは、アプリコンバージョントラッカーの情報を保持します。<br> このフィールドは、ADD時は省略可能となり、SET時は無視されます。ADD時、conversionTrackerTypeがAPP_CONVERSIONの場合、必須です。 </div> <div lang=\"en\"> ConversionTrackerServiceAppConversion object contains the information for ConversionTrackerServiceAppConversionTracker.<br> This field is optional in ADD operation, and will be ignored in SET operation. If conversionTrackerType is APP_CONVERSION, this field is required in ADD operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_conversion_platform** | [**ConversionTrackerServiceAppConversionPlatform**](ConversionTrackerServiceAppConversionPlatform.md) |  | [optional] 
**app_conversion_type** | [**ConversionTrackerServiceAppConversionType**](ConversionTrackerServiceAppConversionType.md) |  | [optional] 
**app_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 計測対象のアプリIDです。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; App ID of the object to be tracked.&lt;br&gt; This field is required in ADD operation, and will be ignored in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


