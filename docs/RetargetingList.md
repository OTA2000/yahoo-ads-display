# RetargetingList

<div lang=\"ja\">RetargetingListオブジェクトは、サイトリターゲティング のターゲットリストの情報を表します。</div> <div lang=\"en\">RetargetingList object diplays the target list for site retargeting.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**delivery_status** | [**RetargetingListServiceDeliveryStatus**](RetargetingListServiceDeliveryStatus.md) |  | [optional] 
**description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ターゲットリストの説明です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Description of Target List.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**reach** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; リーチ数です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Number of reaches.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**target_list** | [**RetargetingListServiceTargetList**](RetargetingListServiceTargetList.md) |  | [optional] 
**target_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ターゲットリストIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となり、ADD時には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target List ID.&lt;br&gt; This field is required in SET and REMOVE operation, and will be ignored in ADD operation. &lt;/div&gt;  | [optional] 
**target_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ターゲットリスト名です。&lt;br&gt; このフィールドは、ADD時は必須、SET時は省略可能となり、REMOVE時は無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target List name.&lt;br&gt; This field is required in ADD operation, optional in SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


