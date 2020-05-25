# AdGroupAdServiceManualCPVAdGroupAdBid

<div lang=\"ja\"> AdGroupAdServiceManualCPVAdGroupAdBidオブジェクトは、広告の手動入札方法（CPV）を表します。<br> ※広告掲載方式がVIDEO_AD（動画広告）のキャンペーンIDを指定した時のみ利用できます。<br> このフィールドは、省略可能となります。<br> ※ADD時、biddingStrategyTypeがMANUAL_CPVの場合は必須です。 </div> <div lang=\"en\"> AdGroupAdServiceManualCPVAdGroupAdBid object displays the manual bidding method for ad (CPV).<br> *It is available only when a campaign ID with ad distribution type 'VIDEO_AD' is specified.<br> This field is optional.<br> *If biddingStrategyType is MANUAL_CPV, this field is required in ADD operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_cpv** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 入札価格です。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Bid amount.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


