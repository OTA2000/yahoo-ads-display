# RetargetingListServiceTargetList

<div lang=\"ja\"> RetargetingListServiceTargetListオブジェクトは、リターゲティングのターゲット種類とターゲットリストの情報を表します。<br> このフィールドは、ADDおよびSET時に必須となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> RetargetingListServiceTargetList object displays the types of target and target list for site retargeting. <br> This field is required in ADD and SET operation, and will be ignored in REMOVE operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combination_target_list** | [**RetargetingListServiceCombinationTargetList**](RetargetingListServiceCombinationTargetList.md) |  | [optional] 
**custom_audience_target_list** | [**RetargetingListServiceCustomAudienceTargetList**](RetargetingListServiceCustomAudienceTargetList.md) |  | [optional] 
**rule_target_list** | [**RetargetingListServiceRuleTargetList**](RetargetingListServiceRuleTargetList.md) |  | [optional] 
**similarity_target_list** | [**RetargetingListServiceSimilarityTargetList**](RetargetingListServiceSimilarityTargetList.md) |  | [optional] 
**target_list_type** | [**RetargetingListServiceTargetListType**](RetargetingListServiceTargetListType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


