# AuditLogServiceValue

<div lang=\"ja\">AuditLogServiceValueオブジェクトは、get/addメソッドの実行結果（1エンティティ）を保持するオブジェクトです。</div> <div lang=\"en\">AuditLogServiceValue object is container storing the result of get/add method (1 entity).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_log_job** | [**AuditLogServiceJob**](AuditLogServiceJob.md) |  | [optional] 
**errors** | [**list[Error]**](Error.md) | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;エラー内容です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Error content.&lt;/div&gt;  | [optional] 
**operation_succeeded** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;処理結果です。trueの場合は、処理は成功しました。falseの場合は処理が失敗しています。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The process results. If true, the process succeeded. If false, the process failed.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


