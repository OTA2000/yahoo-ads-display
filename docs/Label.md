# Label

<div lang=\"ja\">Labelオブジェクトは、ラベルの情報を表します。</div> <div lang=\"en\">Label object describes label information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**color** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; カラーです。&lt;br&gt; ADD時およびSET時、このフィールドは省略可能となります。ADD時のデフォルト設定値は#FFFFFFとなります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Color.&lt;br&gt; This field is optional in ADD and SET operation. The default value in ADD operation will be #FFFFFF. &lt;/div&gt;  | [optional] 
**description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 説明文です。&lt;br&gt; ADD時およびSET時、このフィールドは省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Description.&lt;br&gt; This field is optional in ADD and SET operation. &lt;/div&gt;  | [optional] 
**label_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ラベルIDです。&lt;br&gt; SET時およびREMOVE時、このフィールドは必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Label ID.&lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**label_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ラベル名です。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Label Name.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


