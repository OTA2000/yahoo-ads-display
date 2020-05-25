# AdGroupServiceBiddingStrategy

<div lang=\"ja\"> AdGroupServiceBiddingStrategyは、広告グループ入札戦略を表します。<br> ADDおよびSET時、このフィールドは省略可能となります。<br> ※目的ありのキャンペーンの場合のみ設定可能です。 </div> <div lang=\"en\"> AdGroupServiceBiddingStrategy object describes bidding strategy of ad group.<br> This field is optional in ADD and SET operation.<br> *This can only be specified for campaigns with campaignGoal. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_bidding_strategy_type** | [**AdGroupServiceCampaignBiddingStrategyType**](AdGroupServiceCampaignBiddingStrategyType.md) |  | [optional] 
**max_cpc_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 広告グループ最大入札価格（CPC）です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※campaignBiddingStrategyTypeがMAX_CPCの場合のみ指定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Ad group MAX_CPC bid value.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *This can only be specified when campaignBiddingStrategyType is MAX_CPC. &lt;/div&gt;  | [optional] 
**max_cpv_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 広告グループ最大入札価格（CPV）です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※campaignBiddingStrategyTypeがMAX_CPVの場合のみ指定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group MAX_CPV bid value.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *This can only be specified when campaignBiddingStrategyType is MAX_CPV. &lt;/div&gt;  | [optional] 
**max_vcpm_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 広告グループ最大入札価格（vCPM）です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※campaignBiddingStrategyTypeがMAX_VCPMの場合のみ指定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad group MAX_VCPM bid value.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *This can only be specified when campaignBiddingStrategyType is MAX_VCPM. &lt;/div&gt;  | [optional] 
**target_cpa_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 広告グループ目標単価（tCPA）です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※campaignBiddingStrategyTypeがTARGET_CPAの場合のみ指定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Ad group TARGET_CPA bid value.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; *This can only be specified when campaignBiddingStrategyType is TARGET_CPA. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


