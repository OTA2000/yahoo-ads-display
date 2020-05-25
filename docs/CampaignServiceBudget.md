# CampaignServiceBudget

<div lang=\"ja\"> CampaignServiceBudgetオブジェクトは、キャンペーン予算に関する情報を表します。<br> このフィールドは、ADD時は必須、SET時は省略可能となり、REMOVE時は無視されます。 </div> <div lang=\"en\"> The CampaignServiceBudget object serves campaign budgets.<br> This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーンの一日あたりの予算（一日単位の利用金額）です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時は無視されます。&lt;br&gt; budgetDeliveryMethodがSTANDARDの場合はADDおよびSET時に必須です。&lt;br&gt; ※目的ありの場合、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The daily budget. &lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;br&gt; This field is required in ADD and SET operation if budgetDeliveryMethod is STANDARD.&lt;br&gt; *For campaigns with campaign goal, this field is required in ADD operation. &lt;/div&gt;  | [optional] 
**budget_delivery_method** | [**CampaignServiceBudgetDeliveryMethod**](CampaignServiceBudgetDeliveryMethod.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


