# MediaServiceRecord

<div lang=\"ja\">MediaServiceRecordオブジェクトは、画像の情報を表します。</div> <div lang=\"en\">The MediaServiceRecord object is a container for the information of media (image data).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**approval_status** | [**MediaServiceApprovalStatus**](MediaServiceApprovalStatus.md) |  | [optional] 
**campaign_banner_flg** | [**MediaServiceCampaignBannerFlg**](MediaServiceCampaignBannerFlg.md) |  | [optional] 
**creation_time** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;入稿日時です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Date and time of creation.&lt;/div&gt;  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;掲載拒否の理由です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Reason code why it&amp;#39;s disapproved on the review.&lt;/div&gt;  | [optional] 
**logo_flg** | [**MediaServiceLogoFlg**](MediaServiceLogoFlg.md) |  | [optional] 
**image_media** | [**MediaServiceImageMedia**](MediaServiceImageMedia.md) |  | [optional] 
**media_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;画像IDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Media ID (image ID). &lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**media_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 実ファイル名です。&lt;br&gt; このフィールドは、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;File name. &lt;br&gt; This field is required in ADD operation. &lt;/div&gt;  | [optional] 
**media_title** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;画像名です。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Image name. &lt;br&gt; This field is required in ADD operation, and is optional in SET operation. &lt;/div&gt;  | [optional] 
**thumbnail_flg** | [**MediaServiceThumbnailFlg**](MediaServiceThumbnailFlg.md) |  | [optional] 
**user_status** | [**MediaServiceUserStatus**](MediaServiceUserStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


