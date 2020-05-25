# CampaignServiceCampaignBiddingStrategy

<div lang=\"ja\"> CampaignServiceCampaignBiddingStrategyオブジェクトは、キャンペーン入札戦略です。<br> ADDおよびSET時、このフィールドは目的なしの場合は設定不可となり、目的ありの場合は必須となります。<br> REMOVE時、このフィールドは無視されます。 </div> <div lang=\"en\"> CampaignServiceCampaignBiddingStrategy object describes campaign bidding strategy.<br> In ADD and SET operation, this field cannot be set for campaigns with no campaign goal, and this field will be required for campaigns with campaign goal.<br> This field will be ignored in REMOVE operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_bidding_strategy_type** | [**CampaignServiceCampaignBiddingStrategyType**](CampaignServiceCampaignBiddingStrategyType.md) |  | [optional] 
**max_cpc_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン最大入札価格(CPC)です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Max bid of campaign (CPC). &lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**max_cpv_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン最大入札価格(CPV)です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Max bid of campaign (CPV). &lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**max_vcpm_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン最大入札価格(vCPM)です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Max bid of campaign (vCPM).&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**target_cpa_bid_value** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン目標単価(tCPA)です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target bid of campaign (tCPA). &lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


