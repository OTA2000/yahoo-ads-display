# FeedSet

<div lang=\"ja\">FeedSetオブジェクトは、商品セット情報を保持します。</div> <div lang=\"en\">FeedSet object contains Item Set information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**condition_sets** | [**list[FeedSetServiceConditionSet]**](FeedSetServiceConditionSet.md) |  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; Feedを識別するIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Feed ID.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**feed_set_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 商品セットIDです。&lt;br&gt; REMOVE時、このフィールドは必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Item Set ID.&lt;br&gt; This field is required in REMOVE operation. &lt;/div&gt;  | [optional] 
**feed_set_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 商品セット名です。&lt;br&gt; ADD時、このフィールドは必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Item Set name.&lt;br&gt; This field is required in ADD operation. &lt;/div&gt;  | [optional] 
**is_default_set** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; デフォルトセット判定です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Default setting of Item Set or not.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**item_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 商品セットの条件に含まれるアイテム数です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Number of items included in Item Set conditions.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


