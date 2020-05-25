# AdGroupTargetServiceDeviceTarget

<div lang=\"ja\"> AdGroupTargetServiceDeviceTargetオブジェクトは、デバイスターゲティングの設定情報を保持します。<br> SET時のみ指定可能です。ADD、REMOVEおよびREPLACE時、このフィールドは無視されます。<br> SET時に必要なtargetIdは、AdGroupオブジェクトにデバイスが設定されている場合にレスポンスされます。<br> ※SET時、入札価格調整率のみ設定可能です。 </div> <div lang=\"en\"> AdGroupTargetServiceDeviceTarget object is a container for storing device targeting settings.<br> This field can be specified only in SET operation and is ignored in ADD, REMOVE and REPLACE operation.<br> The targetId required on SET will be responded when devices are set on AdGroup object.<br> *Can set only bid adjustment in SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_type** | [**AdGroupTargetServiceDeviceType**](AdGroupTargetServiceDeviceType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


