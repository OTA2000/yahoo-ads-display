# CampaignServiceBudgetDeliveryMethod

<div lang=\"ja\"> CampaignServiceBudgetDeliveryMethodは、配信方法を表します。<br> このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。<br> ※目的ありの場合、ADDおよびSET時に設定不可となります。 </div> <div lang=\"en\"> CampaignServiceBudgetDeliveryMethod serves delivery method of budget.<br> This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. <br> *For campaigns with campaign goal, this field cannot be set in ADD and SET operation. </div> <hr> <p>* <code>STANDARD</code> - <span lang=\"ja\">1日の中で均等に広告を表示します。</span><span lang=\"en\">The budget server will throttle serving evenly across the entire time period.</span></p> <p>* <code>ACCELERATED</code> - <span lang=\"ja\">できるだけ早く広告を配信します。</span><span lang=\"en\">The budget server will not throttle serving, and ads will serve as fast as possible.</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


