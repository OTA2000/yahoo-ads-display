# LabelServiceSelector

<div lang=\"ja\">LabelServiceSelectorオブジェクトは、操作の対象とするラベルの情報およびフィルタ条件を表します。</div> <div lang=\"en\">LabelServiceSelector object describes the information of label to be operated and filter conditions.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;検索条件：アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search Condition: Account ID.&lt;/div&gt;  | 
**label_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 検索条件：ラベルID&lt;br&gt; 指定しない場合は、フィルタ条件に すべてのラベルが含まれます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Search Condition: Label ID.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 2000]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


