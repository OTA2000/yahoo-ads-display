# FeedFtpServiceSchedule

<div lang=\"ja\"> FeedFtpServiceScheduleオブジェクトは、定期アップロードのスケジュールを表します。<br> このフィールドは、ADD時は必須となり、SET時は省略可能となります。 </div> <div lang=\"en\"> FeedFtpServiceSchedule object displays Periodic Upload schedule.<br> This field is required in ADD operation, and will be optional in SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_daily** | [**FeedFtpServiceScheduleDaily**](FeedFtpServiceScheduleDaily.md) |  | [optional] 
**schedule_hourly** | [**FeedFtpServiceScheduleHourly**](FeedFtpServiceScheduleHourly.md) |  | [optional] 
**schedule_type** | [**FeedFtpServiceScheduleType**](FeedFtpServiceScheduleType.md) |  | [optional] 
**schedule_weekly** | [**FeedFtpServiceScheduleWeekly**](FeedFtpServiceScheduleWeekly.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


