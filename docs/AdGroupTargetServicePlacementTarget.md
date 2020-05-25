# AdGroupTargetServicePlacementTarget

<div lang=\"ja\"> AdGroupTargetServicePlacementTargetオブジェクトは、プレイスメントターゲティングの設定情報を保持するオブジェクトです。<br> ADD、SETおよびREPLACE時、このフィールドは省略可能となります。<br> ※targetTypeがPLACEMENT_TARGETの場合は必須です。 </div> <div lang=\"en\"> AdGroupTargetServicePlacementTarget object is a container for storing placement targeting settings.<br> This field is optional in ADD, SET and REPLACE operation.<br> ∗If targetType is PLACEMENT_TARGET, this field is required. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_url_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; プレイスメントリスト名です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Placement List Name.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**placement_url_list_type** | [**AdGroupTargetServicePlacementUrlListType**](AdGroupTargetServicePlacementUrlListType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


