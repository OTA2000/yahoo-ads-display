# RetargetingListServiceRuleTargetList

<div lang=\"ja\"> RetargetingListServiceRuleTargetListオブジェクトは、ルール設定のリストを表します。<br> このフィールドは、ADDおよびSET時に省略可能となります。<br> ※targetListTypeがDEFAULT_LISTまたはRULEの場合は、ADDおよびSET時に必須となります。 </div> <div lang=\"en\"> RetargetingListServiceRuleTargetList object displays the list of rule settings.<br> This field is optional in ADD and SET operation. <br> *If targetListType is DEFAULT_LIST, this field is required in ADD and SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_open** | [**RetargetingListServiceIsOpen**](RetargetingListServiceIsOpen.md) |  | [optional] 
**is_preset** | [**RetargetingListServiceIsPreset**](RetargetingListServiceIsPreset.md) |  | [optional] 
**reach_period** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; リーチの蓄積期間（1日～540日）です。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Cookies validation period. (1 - 540 days) &lt;br&gt; This field is required in ADD operation, and is optional in SET operation. &lt;/div&gt;  | [optional] 
**retargeting_tag_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; リターゲティングタグIDです。&lt;br&gt; このフィールドは、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; ID of Retargeting Tag. &lt;br&gt; This field is required in ADD operation. &lt;/div&gt;  | [optional] 
**rules** | [**list[RetargetingListServiceRule]**](RetargetingListServiceRule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


