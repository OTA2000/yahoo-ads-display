# CampaignServiceType

<div lang=\"ja\"> CampaignServiceTypeは、キャンペーンタイプを表します。<br> このフィールドは、ADD時に省略可能となり、SETおよびREMOVE時に無視されます。<br> ※ADD時のデフォルト設定値はSTANDARDとなります。<br> 目的ありの場合、ADD時に設定不可となり、設定値はSTANDARDに固定されます。 </div> <div lang=\"en\"> CampaignServiceType serves type of campaign.<br> This field is optional in ADD operation, and will be ignored in SET and REMOVE operation. <br> *The default value in ADD operation will be STANDARD. <br> For campaigns with campaign goal, this field cannot be set in ADD operation, and the value will be automatically STANDARD. </div> <hr> <p>* <code>STANDARD</code> - <span lang=\"ja\">標準キャンペーン</span><span lang=\"en\">Standard campaign</span></p> <p>* <code>APP</code> - <span lang=\"ja\">アプリインストール広告キャンペーン</span><span lang=\"en\">App Install Ads campaign</span></p> <p>* <code>UNKNOWN</code> - <span lang=\"ja\">未知の値です。</span><span lang=\"en\">Unknown Value</span></p> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


