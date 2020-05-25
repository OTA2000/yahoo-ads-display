# ReportDefinitionServiceFilter

<div lang=\"ja\"> ReportDefinitionServiceFilterオブジェクトは、フィルター定義を表します。<br> このフィールドは、ADD時に省略可能となり、REMOVE時に無視されます。 </div> <div lang=\"en\"> ReportDefinitionServiceFilter object serves filter definitions. <br> This field is optional in ADD operation, and will be ignored in REMOVE operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; フィルター対象となるフィールドです。&lt;br&gt; このフィールドは、ADD時に必須となります。&lt;br&gt; ※getReportFieldsのレスポンスで「filterable&#x3D;true」のフィールドのみ指定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Field to be filtered.&lt;br&gt; This field is required in ADD operation.&lt;br&gt; ※Can be specified for the field with &amp;#34;filterable&#x3D;true&amp;#34; on the response of getReportFields. &lt;/div&gt;  | [optional] 
**filter_operator** | [**ReportDefinitionServiceFilterOperator**](ReportDefinitionServiceFilterOperator.md) |  | [optional] 
**values** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 条件値です。&lt;br&gt; このフィールドは、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Value for condition. &lt;br&gt; This field is required in ADD operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


