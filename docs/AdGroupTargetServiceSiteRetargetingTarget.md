# AdGroupTargetServiceSiteRetargetingTarget

<div lang=\"ja\"> AdGroupTargetServiceSiteRetargetingTargetオブジェクトは、サイトリターゲティングの設定情報を保持します。<br> ADD、SETおよびREPLACE時、このフィールドは省略可能となります。<br> ※targetTypeがSITE_RETARGETINGの場合は必須です。 </div> <div lang=\"en\"> AdGroupTargetServiceSiteRetargetingTarget object is a container for storing site retargeting settings.<br> This field is optional in ADD, SET and REPLACE operation.<br> ∗If targetType is SITE_RETARGETING, this field is required. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_list_deliver_type** | [**AdGroupTargetServiceTargetListDeliverType**](AdGroupTargetServiceTargetListDeliverType.md) |  | [optional] 
**target_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ターゲットリスト名です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target List name.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


