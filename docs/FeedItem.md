# FeedItem

<div lang=\"ja\">FeedItemオブジェクトは、商品の情報を格納するコンテナです。</div> <div lang=\"en\">FeedItem object contain information about the product.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**FeedItemServiceAvailability**](FeedItemServiceAvailability.md) |  | [optional] 
**capacity** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 在庫数です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Stock quantity.&lt;br&gt; This field is optional in requests. &lt;/div&gt;  | [optional] 
**display_settings** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 配信設定です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。&lt;br&gt; ※「0:配信しない/1:配信する」を表します。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Display settings.&lt;br&gt; This field is optional in requests.&lt;br&gt; * 0: Off, 1: On. &lt;/div&gt;  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; Feedを識別するIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; ID for identifying Feed.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**formatted_price** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 文字列の価格です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Text strings price.&lt;br&gt; This field is optional in requests. &lt;/div&gt;  | [optional] 
**formatted_sale_price** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 文字列のセール価格です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Sale price of text strings.&lt;br&gt; This field is optional in requests. &lt;/div&gt;  | [optional] 
**in_stock** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 在庫情報です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。&lt;br&gt; ※「0:在庫なし/1:在庫あり」を表します。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Inventory information.&lt;br&gt; This field is optional in requests.&lt;br&gt; 0: Out of stock, 1: In stock. &lt;/div&gt;  | [optional] 
**is_remove_capacity** | [**FeedItemServiceIsRemoveFlg**](FeedItemServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_formatted_price** | [**FeedItemServiceIsRemoveFlg**](FeedItemServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_formatted_sale_price** | [**FeedItemServiceIsRemoveFlg**](FeedItemServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_price** | [**FeedItemServiceIsRemoveFlg**](FeedItemServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_sale_price** | [**FeedItemServiceIsRemoveFlg**](FeedItemServiceIsRemoveFlg.md) |  | [optional] 
**item_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 商品IDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Item ID.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**price** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 価格です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Price.&lt;br&gt; This field is optional in requests. &lt;/div&gt;  | [optional] 
**sale_price** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; セール価格です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Sale price.&lt;br&gt; This field is optional in requests. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


