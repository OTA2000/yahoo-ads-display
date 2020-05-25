# AuditLogServiceSelector

<div lang=\"ja\">getメソッドの検索条件（実行パラメータ）を保持するオブジェクトです。</div> <div lang=\"en\">AuditLogServiceSelector object is container storing the search conditions of get method (execution parameter).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | 
**audit_log_job_ids** | **list[int]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The job ID.&lt;/div&gt;  | [optional] 
**job_statuses** | [**list[AuditLogServiceJobStatus]**](AuditLogServiceJobStatus.md) | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ジョブステータスです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The job status information.&lt;/div&gt;  | [optional] 
**number_results** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの最大件数です。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Maximum number of results to return in this page. This field must be greater than or equal to 1. Also see Entity Limits per operation.&lt;/div&gt;  | [optional] [default to 500]
**start_index** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;ページの先頭のインデックスです。このフィールドは、1以上を指定する必要があります。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Index of the first result to return in this page. This field must be greater than or equal to 1.&lt;/div&gt;  | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


