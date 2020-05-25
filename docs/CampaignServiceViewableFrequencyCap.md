# CampaignServiceViewableFrequencyCap

<div lang=\"ja\"> CampaignServiceViewableFrequencyCapは、ビューアブルフリクエンシー制御を表します。<br> ADDおよびSET時、このフィールドは目的なしの場合は設定不可となり、目的ありの場合は省略可能となります。<br> REMOVE時は無視されます。<br> ※ADD時は全ての項目の指定が必須です。<br> ※SET時は更新する項目のみのリクエストが可能です。<br> ※ビューアブルフリークエンシーキャップの解除方法は、以下の通りです： </div> <div lang=\"en\"> CampaignServiceViewableFrequencyCap object describes viewable frequency restriction.<br> In ADD and SET operation, this field cannot be set for campaigns with no campaign goal, and will be optional for campaigns with campaign goal. <br> In REMOVE operation, this field will be ignored.<br> *All items must be specified in ADD operation.<br> *Only update items can be requested in SET operation.<br> *Method to remove the viewable frequency cap: </div> <code> {     \"viewableFrequencyCap\": {         \"vImps\": 0     } } </code> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_level** | [**CampaignServiceFrequencyLevel**](CampaignServiceFrequencyLevel.md) |  | [optional] 
**frequency_time_unit** | [**CampaignServiceFrequencyTimeUnit**](CampaignServiceFrequencyTimeUnit.md) |  | [optional] 
**v_imps** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 同一ユーザに対する広告の最大ビューアブルインプレッション数です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Maximum number of ad viewable impressions to same user.&lt;br&gt; This field is optional in ADD and SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


