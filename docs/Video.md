# Video

<div lang=\"ja\">Videoオブジェクトは、動画情報を保持します。</div> <div lang=\"en\">Video object is a container for the information of videos.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**approval_status** | [**VideoServiceApprovalStatus**](VideoServiceApprovalStatus.md) |  | [optional] 
**creation_time** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画の入稿日時です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Time and date when the video was submitted.&lt;/div&gt;  | [optional] 
**disapproval_reason_codes** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画の掲載拒否理由です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Disapproval reason of the video.&lt;/div&gt;  | [optional] 
**media_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; メディアIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Media ID.&lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**process_status** | [**VideoServiceProcessStatus**](VideoServiceProcessStatus.md) |  | [optional] 
**user_status** | [**VideoServiceUserStatus**](VideoServiceUserStatus.md) |  | [optional] 
**video_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画のファイル名です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Video file name.&lt;/div&gt;  | [optional] 
**video_setting** | [**VideoServiceSetting**](VideoServiceSetting.md) |  | [optional] 
**video_title** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 動画名です。&lt;br&gt; このフィールドは、SET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Video name.&lt;br&gt; This field is optional in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


