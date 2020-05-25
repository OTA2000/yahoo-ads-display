# AdGroupTargetServiceAdScheduleTarget

<div lang=\"ja\"> AdGroupTargetServiceAdScheduleTargetオブジェクトは、時間帯ターゲティングの設定情報を保持します。<br> ADD、SETおよびREPLACE時、このフィールドは省略可能となります。<br> ※targetTypeがAD_SCHEDULE_TARGETの場合は必須です。 </div> <div lang=\"en\"> AdGroupTargetServiceAdScheduleTarget object is a container for storing day of week/hours targeting settings.<br> This field is optional in ADD, SET and REPLACE operation.<br> *If targetType is AD_SCHEDULE_TARGET, this field is required. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | [**AdGroupTargetServiceDayOfWeek**](AdGroupTargetServiceDayOfWeek.md) |  | [optional] 
**end_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 終了時間（時のみ）です。&lt;br&gt; このフィールドは、ADD時は必須となり、REPLACE時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; End time (hour only).&lt;br&gt; This field is required in ADD operation, and will be optional in REPLACE operation. &lt;/div&gt;  | [optional] 
**start_hour** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 開始時間（時のみ）です。&lt;br&gt; このフィールドは、ADD時は必須となり、REPLACE時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Start time (hour only).&lt;br&gt; This field is required in ADD operation, and will be optional in REPLACE operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


