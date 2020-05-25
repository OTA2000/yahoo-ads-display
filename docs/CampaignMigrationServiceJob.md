# CampaignMigrationServiceJob

<div lang=\"ja\">CampaignMigrationServiceJobオブジェクトは、マイグレーションジョブの処理状況を示すオブジェクトです。</div> <div lang=\"en\">CampaignMigrationServiceJob object indicates processing status of migration job.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID&lt;/div&gt;  | [optional] 
**failed_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;失敗キャンペーン数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of failed campaigns&lt;/div&gt;  | [optional] 
**in_progress_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;進行中キャンペーン数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of progressing campaigns&lt;/div&gt;  | [optional] 
**job_status** | [**CampaignMigrationServiceJobStatus**](CampaignMigrationServiceJobStatus.md) |  | [optional] 
**migration_job_end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;マイグレーションジョブ終了日時&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Migration job end date&lt;/div&gt;  | [optional] 
**migration_job_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;マイグレーションジョブID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Migration job ID&lt;/div&gt;  | [optional] 
**migration_job_submit_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;マイグレーションジョブ登録日時&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Migration job submit date&lt;/div&gt;  | [optional] 
**scope** | [**CampaignMigrationServiceScope**](CampaignMigrationServiceScope.md) |  | [optional] 
**succeeded_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;正常終了キャンペーン数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of completed campaigns&lt;/div&gt;  | [optional] 
**total_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;全キャンペーン数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of total campaigns&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


