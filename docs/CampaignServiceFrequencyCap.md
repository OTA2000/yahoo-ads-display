# CampaignServiceFrequencyCap

<div lang=\"ja\"> CampaignServiceFrequencyCapは、フリクエンシー制御を表します。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。<br> ※ADDおよびSET時、目的ありの場合は設定不可となります。<br> ※ADD時は全ての項目の指定が必須です。<br> ※SET時は更新する項目のみのリクエストが可能です。<br> ※フリークエンシーキャップの解除方法は、以下の通りです： </div> <div lang=\"en\"> CampaignServiceFrequencyCap object describes frequency restriction.<br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. <br> *In ADD and SET operation, this field cannot be set for campaigns with campaign goal. <br> *All items must be specified in ADD operation.<br> *Only update items can be requested in SET operation.<br> *Method to remove the frequency cap: </div> <code> {   \"frequencyCap\": {     \"impression\": 0   } } </code> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_level** | [**CampaignServiceFrequencyLevel**](CampaignServiceFrequencyLevel.md) |  | [optional] 
**frequency_time_unit** | [**CampaignServiceFrequencyTimeUnit**](CampaignServiceFrequencyTimeUnit.md) |  | [optional] 
**impression** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 同一ユーザに対する広告の最大インプレッション数です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Maximum Number of Ad Impressions to Unique User.&lt;br&gt; This field is optional in ADD and SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


