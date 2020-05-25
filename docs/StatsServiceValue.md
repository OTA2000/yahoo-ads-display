# StatsServiceValue

<div lang=\"ja\">StatsServiceValueオブジェクトは、統計情報1件あたりの実行結果（1 Entity）を保持します。</div> <div lang=\"en\">StatsServiceValue object is container for the execution result (1 entity) per single stats information by method.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**ad_group_stats_value** | [**StatsServiceAdGroupStatsValue**](StatsServiceAdGroupStatsValue.md) |  | [optional] 
**ad_stats_value** | [**StatsServiceAdStatsValue**](StatsServiceAdStatsValue.md) |  | [optional] 
**campaign_stats_value** | [**StatsServiceCampaignStatsValue**](StatsServiceCampaignStatsValue.md) |  | [optional] 
**errors** | [**list[Error]**](Error.md) |  | [optional] 
**image_stats_value** | [**StatsServiceImageStatsValue**](StatsServiceImageStatsValue.md) |  | [optional] 
**operation_succeeded** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The process results. If true, the process succeeded. If false, the process failed.&lt;/div&gt;  | [optional] 
**period_custom_date** | [**StatsServicePeriodCustomDate**](StatsServicePeriodCustomDate.md) |  | [optional] 
**stats_period** | [**StatsServiceStatsPeriod**](StatsServiceStatsPeriod.md) |  | [optional] 
**target_stats_value** | [**StatsServiceTargetStatsValue**](StatsServiceTargetStatsValue.md) |  | [optional] 
**type** | [**StatsServiceType**](StatsServiceType.md) |  | [optional] 
**video_stats_value** | [**StatsServiceVideoStatsValue**](StatsServiceVideoStatsValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


