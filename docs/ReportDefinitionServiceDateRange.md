# ReportDefinitionServiceDateRange

<div lang=\"ja\"> ReportDefinitionServiceDateRangeオブジェクトは、レポートの集計対象期間を表します。<br> このフィールドは、ADD時に省略可能となり、REMOVE時に無視されます。<br> DateRangeTypeがCUSTOM_DATEの場合、必須項目です。 </div> <div lang=\"en\"> The ReportDefinitionServiceDateRange object serves the report compilation target period. <br> This field is optional in ADD operation, and will be ignored in REMOVE operation. <br> This field is required if DateRangeType is set to &#34;CUSTOM DATE&#34;. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 集計終了日です。&lt;br&gt; このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The compilation end date. &lt;br&gt; This field is required in ADD operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 集計開始日です。&lt;br&gt; このフィールドは、ADD時に必須となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The compilation start date.&lt;br&gt; This field is required in ADD operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


