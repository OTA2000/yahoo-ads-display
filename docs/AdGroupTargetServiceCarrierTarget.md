# AdGroupTargetServiceCarrierTarget

<div lang=\"ja\"> AdGroupTargetServiceCarrierTargetオブジェクトは、モバイルキャリアターゲティングの設定情報を保持します。<br> SET時のみ指定可能です。ADD、REMOVEおよびREPLACE時、このフィールドは無視されます。<br> SET時に必要なtargetIdは、AdGroupオブジェクトにキャリアが設定されている場合にレスポンスされます。<br> ※SET時、入札価格調整率のみ設定可能です。 </div> <div lang=\"en\"> AdGroupTargetServiceCarrierTarget object is a container for storing mobile carrier targeting settings.<br> This field can be specified only in SET operation and is ignored in ADD, REMOVE and REPLACE operation.<br> The targetId required on SET will be responded when carriers are set on AdGroup object.<br> *Can set only bid adjustment in SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_type** | [**AdGroupTargetServiceCarrierType**](AdGroupTargetServiceCarrierType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


