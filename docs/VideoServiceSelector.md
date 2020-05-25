# VideoServiceSelector

<div lang=\"ja\">VideoServiceSelectorオブジェクトは、入稿済みの動画の情報を取得します。</div> <div lang=\"en\">The VideoServiceSelector object is a container for storing added video information and filtering condition.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**approval_statuses** | [**list[VideoServiceApprovalStatus]**](VideoServiceApprovalStatus.md) |  | [optional] 
**media_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;メディアIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Media ID.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**process_statuses** | [**list[VideoServiceProcessStatus]**](VideoServiceProcessStatus.md) |  | [optional] 
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]
**user_statuses** | [**list[VideoServiceUserStatus]**](VideoServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


