# ReportDefinition

<div lang=\"ja\">ReportDefinitionオブジェクトは、レポート定義を表します。</div> <div lang=\"en\">The ReportDefinition object serves report definitions.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**complete_time** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ジョブ完了日時です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The date and time of Job completion. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**date_range** | [**ReportDefinitionServiceDateRange**](ReportDefinitionServiceDateRange.md) |  | [optional] 
**date_range_type** | [**ReportDefinitionServiceDateRangeType**](ReportDefinitionServiceDateRangeType.md) |  | [optional] 
**download_encode** | [**ReportDefinitionServiceDownloadEncode**](ReportDefinitionServiceDownloadEncode.md) |  | [optional] 
**download_format** | [**ReportDefinitionServiceDownloadFormat**](ReportDefinitionServiceDownloadFormat.md) |  | [optional] 
**fields** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 表示項目です。&lt;br&gt; このフィールドは、ADD時に必須となり、REMOVE時に無視されます。&lt;br&gt; 指定可能な値は、ReportDefinitionServiceのgetReportFieldsで取得されるfieldNameをご確認ください。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Select the fields. &lt;br&gt; This field is required in ADD operation, and will be ignored in REMOVE operation.&lt;br&gt; * Available values can be referred to fieldName field of fields object obtained by getReportFields operation of ReportDefinitionService. &lt;/div&gt;  | [optional] 
**filters** | [**list[ReportDefinitionServiceFilter]**](ReportDefinitionServiceFilter.md) |  | [optional] 
**frequency_range** | [**ReportDefinitionServiceFrequencyRange**](ReportDefinitionServiceFrequencyRange.md) |  | [optional] 
**job_status** | [**ReportDefinitionServiceJobStatus**](ReportDefinitionServiceJobStatus.md) |  | [optional] 
**lang** | [**ReportDefinitionServiceLang**](ReportDefinitionServiceLang.md) |  | [optional] 
**report_job_error_detail** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ジョブエラー詳細です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Job Error Detail. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**report_job_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; レポートジョブIDです。&lt;br&gt; このフィールドは、REMOVE時に必須となり、ADD時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Report Job Id. &lt;br&gt; This field is required in REMOVE operation, and will be ignored in ADD operation. &lt;/div&gt;  | [optional] 
**report_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; レポート名です。&lt;br&gt; このフィールドは、ADD時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Report name. &lt;br&gt; This field is optional in ADD operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**request_time** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ジョブ依頼日時です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The date and time of Job request. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**sort_fields** | [**list[ReportDefinitionServiceReportSortField]**](ReportDefinitionServiceReportSortField.md) |  | [optional] 
**zip** | [**ReportDefinitionServiceZip**](ReportDefinitionServiceZip.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


