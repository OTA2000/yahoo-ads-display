# CampaignServiceConversionOptimizer

<div lang=\"ja\"> CampaignServiceConversionOptimizerは、コンバージョン最適化制御を保持するオブジェクトです。<br> このフィールドは、SET時に省略可能となり、ADDおよびREMOVE時に無視されます。<br> ※SET時、目的ありの場合は設定不可となります。 </div> <div lang=\"en\"> CampaignServiceConversionOptimizer retains conversion optimization control.<br> This field is optional in SET operation, and will be ignored in ADD and REMOVE operation. <br> *For campaign with campaign goal, this field cannot be set in SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_campaign_conversion_optimizer** | [**CampaignServiceAutoCampaignConversionOptimizer**](CampaignServiceAutoCampaignConversionOptimizer.md) |  | [optional] 
**conversion_optimizer_type** | [**CampaignServiceConversionOptimizerType**](CampaignServiceConversionOptimizerType.md) |  | [optional] 
**manual_campaign_conversion_optimizer** | [**CampaignServiceManualCampaignConversionOptimizer**](CampaignServiceManualCampaignConversionOptimizer.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


