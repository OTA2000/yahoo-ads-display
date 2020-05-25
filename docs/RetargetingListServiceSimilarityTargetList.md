# RetargetingListServiceSimilarityTargetList

<div lang=\"ja\"> 類似ユーザーターゲットの情報を保持するオブジェクトです。<br> このフィールドは、ADDおよびSET時に省略可能となります。<br> ※targetListTypeがSIMILARITYの場合は、ADDおよびSET時に必須となります。 </div> <div lang=\"en\"> RetargetingListServiceSimilarityTargetList object is a container for storing the information of Targeting information of users (similar).<br> This field is optional in ADD and SET operation. <br> *If targetListType is SIMILARITY, this field is required in ADD and SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 類似ユーザーをリターゲティングするターゲットIDです。&lt;br&gt; このフィールドは、ADD時に必須となり、SETおよびREMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target ID for retargeting similar users. &lt;br&gt; This field is required in ADD operation, and will be ignored in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**target_list_size** | [**RetargetingListServiceTargetListSize**](RetargetingListServiceTargetListSize.md) |  | [optional] 
**target_list_size_reaches** | [**list[RetargetingListServiceTargetListSizeReaches]**](RetargetingListServiceTargetListSizeReaches.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


