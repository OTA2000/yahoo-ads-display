# AuditLogServiceDateRange

<div lang=\"ja\"> AuditLogServiceDateRangeは、addメソッド実行時にダウンロード対象とする更新期間を保持するオブジェクトです。<br> このフィールドは、リクエストの場合は省略可能となります。 </div> <div lang=\"en\"> AuditLogServiceDateRange object is container storing the downloading date range of add method.<br> This field is optional in requests. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 終了日付です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能となります。&lt;br&gt; ・入力形式：Ymd形式&lt;br&gt; ・デフォルト値：現在の日付&lt;br&gt; ・指定可能範囲：現在の日付&lt;br&gt; ※終了日付は開始日付以降の日付を指定してください。&lt;br&gt; ※開始日付から終了日付の期間は最大1カ月です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; End date.&lt;br&gt; This field is optional in requests.&lt;br&gt; - Entry format : Ymd format&lt;br&gt; - Default value : Current date&lt;br&gt; - Available range : Current date&lt;br&gt; *Enter the date after Start date.&lt;br&gt; *Maximum length of date range between Start and End is 1 month. &lt;/div&gt;  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 開始日付です。&lt;br&gt; このフィールドは、リクエストの場合は省略可能となります。&lt;br&gt; ・入力形式：Ymd形式&lt;br&gt; ・デフォルト値：現在の日付&lt;br&gt; ・指定可能範囲：前月の月初&lt;br&gt; 例：4/30時点で、開始日付に指定できるもっとも古い日付は3/1 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Start date.&lt;br&gt; This field is optional in requests.&lt;br&gt; - Entry format : Ymd format&lt;br&gt; - Default value : Current date&lt;br&gt; - Available range : Beginning of the last month&lt;br&gt; e.g.: The oldest date selectable as of April 30 is March 1. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


