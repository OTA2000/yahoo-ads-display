# ConversionTrackerServiceSelector

<div lang=\"ja\">ConversionTrackerServiceSelectorオブジェクトは、getメソッドの検索条件（実行パラメータ）を保持します。</div> <div lang=\"en\">ConversionTrackerServiceSelector object contains a set of criteria (parameters) for get method.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**app_conversion_platform** | [**ConversionTrackerServiceAppConversionPlatform**](ConversionTrackerServiceAppConversionPlatform.md) |  | [optional] 
**app_ids** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アプリID。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;App ID.&lt;/div&gt;  | [optional] 
**categories** | [**list[ConversionTrackerServiceCategory]**](ConversionTrackerServiceCategory.md) |  | [optional] 
**conversion_tracker_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;コンバージョントラッカーのID。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Conversion Tracker ID.&lt;/div&gt;  | [optional] 
**conversion_tracker_types** | [**list[ConversionTrackerServiceType]**](ConversionTrackerServiceType.md) |  | [optional] 
**counting_type** | [**ConversionTrackerServiceCountingType**](ConversionTrackerServiceCountingType.md) |  | [optional] 
**exclude_from_bidding** | [**ConversionTrackerServiceExcludeFromBidding**](ConversionTrackerServiceExcludeFromBidding.md) |  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**stats_period** | [**ConversionTrackerServiceStatsPeriod**](ConversionTrackerServiceStatsPeriod.md) |  | [optional] 
**stats_period_custom_date** | [**ConversionTrackerServiceStatsPeriodCustomDate**](ConversionTrackerServiceStatsPeriodCustomDate.md) |  | [optional] 
**statuses** | [**list[ConversionTrackerServiceStatus]**](ConversionTrackerServiceStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


