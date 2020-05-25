# CampaignServiceServingStatus

<div lang=\"ja\"> CampaignServiceServingStatusは、キャンペーンレベルの配信状況です。 ユーザーによる広告配信の調整に関わらず、キャンペーンとしての状態を表します。<br> このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 </div> <div lang=\"en\"> CampaignServiceServingStatus serves delivery status in campaign level. Display the campaign status, regardless of userStatus setting.<br> Although this field will be returned in the response, it will be ignored on input. </div> <hr> <p>* <code>SERVING</code> - <span lang=\"ja\">キャンペーンは、現在配信されています。</span><span lang=\"en\">The campaign is currently serving ads.</span></p> <p>* <code>ENDED</code> - <span lang=\"ja\">配信が終了しています。<br>設定されたキャンペーン期間後のため、現在配信されていません。</span><span lang=\"en\">The campaign has ended.<br>It is already past the delivery period, so the campaign is currently not serving ads.</span></p> <p>* <code>PENDING</code> - <span lang=\"ja\">配信が開始していません。<br>設定されたキャンペーン期間前のため、現在まだ配信されていません。</span><span lang=\"en\">The campaign has not started.<br>It has not reached the delivery period, so the campaign is currently not serving.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

