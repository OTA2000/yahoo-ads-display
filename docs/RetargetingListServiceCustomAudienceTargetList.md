# RetargetingListServiceCustomAudienceTargetList

<div lang=\"ja\"> RetargetingListServiceCustomAudienceTargetListオブジェクトは、Yahoo! DMPの行動履歴を利用するターゲットリストを表します。ご利用にはYahoo! DMPのご契約が必要です。<br> このフィールドは、ADDおよびSET時に省略可能となります。<br> ※targetListTypeがCUSTOM_AUDIENCEの場合は、ADDおよびSET時に必須となります。 </div> <div lang=\"en\"> RetargetingListServiceCustomAudienceTargetList object displays Target List using users' visit/activity history from Yahoo! JAPAN DMP. To use the data, it is required to conclude a contract for Yahoo! DMP. <br> This field is optional in ADD and SET operation. <br> *If targetListType is CUSTOM_AUDIENCE, this field is required in ADD and SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_audience_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;Yahoo! DMPに連携するIDです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;ID to configure Yahoo! JAPAN DMP.&lt;/div&gt;  | [optional] 
**reach_period** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 行動履歴の保持期間です（1日～60日）。&lt;br&gt; このフィールドは、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Duration of user data configured from DMP (1-60days). &lt;br&gt; This field is required in ADD operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


