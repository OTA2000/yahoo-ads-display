# AdGroupServiceManualCPCBid

<div lang=\"ja\"> AdGroupServiceManualCPCBidオブジェクトは、広告グループの入札価格を保持します。<br> このフィールドは、省略可能となります。<br> ※ADD時、typeがMANUAL_CPCの場合は必須です。<br> ※広告掲載方式がVIDEO_AD（動画広告）のキャンペーンIDを指定した時は利用できません。<br> 詳細は、「<a href=\"https://ads-help.yahoo.co.jp/yahooads/ydn/articledetail?lan=ja&aid=1281\">広告グループの作成 - 広告グループの入札価格を入力</a>」を参照してください。 </div> <div lang=\"en\"> AdGroupServiceManualCPCBid object stores the bid amount of ad group.<br> This field is optional.<br> *If type is MANUAL_CPC, this field is required in ADD operation.<br> *It is not available when a campaign ID with ad distribution type 'VIDEO_AD' is specified.<br> More details are described on <a href=\"https://ads-help.yahoo.co.jp/yahooads/ydn/articledetail?lan=en&aid=487\">Create Ad Group - Enter the Bid amount of the Ad Group</a>. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_cpc** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 入札価格です。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Bid amount.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


