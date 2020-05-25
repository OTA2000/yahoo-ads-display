# CampaignServiceUserStatus

<div lang=\"ja\"> CampaignServiceUserStatusは、ユーザーにより広告配信の有無を調整できる設定です。<br> このフィールドは、ADD時は必須、SET時は省略可能となり、REMOVE時は無視されます。 </div> <div lang=\"en\"> CampaignServiceUserStatus serves ad delivery status that can be set by an user.<br> This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation. </div> <hr> <p>* <code>ACTIVE</code> - <span lang=\"ja\">現在、広告は配信されている状態です。</span><span lang=\"en\">Currently ad delivery is active.</span></p> <p>* <code>PAUSED</code> - <span lang=\"ja\">現在、広告は一時停止の状態です。そのため、配信されていません。</span><span lang=\"en\">Currently ad is paused, which the delivery is not active.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


