# SearchKeywordList

<div lang=\"ja\">SearchKeywordListオブジェクトは、サーチキーワードリストを表します。</div> <div lang=\"en\">SearchKeywordList object displays the search list.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**delivery_status** | [**SearchKeywordListServiceDeliveryStatus**](SearchKeywordListServiceDeliveryStatus.md) |  | [optional] 
**keyword_frequency** | [**SearchKeywordListServiceKeywordFrequency**](SearchKeywordListServiceKeywordFrequency.md) |  | [optional] 
**keyword_recency** | [**SearchKeywordListServiceKeywordRecency**](SearchKeywordListServiceKeywordRecency.md) |  | [optional] 
**search_keyword** | [**list[SearchKeywordListServiceSearchKeyword]**](SearchKeywordListServiceSearchKeyword.md) |  | [optional] 
**search_keyword_list_description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; サーチキーワードリストの説明文です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Description of Search keyword list.&lt;br&gt; This field is optional in ADD and SET operation. &lt;/div&gt;  | [optional] 
**search_keyword_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; サーチキーワードリストIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Search keyword list ID.&lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**search_keyword_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; サーチキーワードリスト名です。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Name of Search keyword list.&lt;br&gt; This field is required in ADD operation, and is optional in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


