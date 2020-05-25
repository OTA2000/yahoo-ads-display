# AdGroupAdServiceBannerVideoAd

<div lang=\"ja\"> AdGroupAdServiceBannerVideoAdオブジェクトは、動画で構成される広告の情報を表します。<br> このフィールドは、省略可能となります。<br> ※ADD時、adTypeがBANNER_VIDEO_ADの場合は必須です。 </div> <div lang=\"en\"> AdGroupAdServiceBannerVideoAd object describes information regarding ads composed of videos.<br> This field is optional.<br> *If adType is BANNER_VIDEO_AD, this field is required in ADD operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 表示URLです。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Display URL.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 
**is_remove_video10_sec_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video25_percent_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video3_sec_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video50_percent_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video75_percent_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video_complete_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**is_remove_video_start_beacon_urls** | [**AdGroupAdServiceIsRemoveFlg**](AdGroupAdServiceIsRemoveFlg.md) |  | [optional] 
**thumbnail_media_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; サムネイルIDです。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Thumbnail ID.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 
**url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; リンク先URLです。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Destination URL.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 
**video10_sec_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 10秒視聴ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Viewing beacon URL (10 seconds).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video25_percent_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 25％再生視聴ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Playback viewing beacon URL (25%).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video3_sec_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 3秒視聴ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Viewing beacon URL (3 seconds).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video50_percent_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 50％再生視聴ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Playback viewing beacon URL (50%).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video75_percent_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 75％再生視聴ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Playback viewing beacon URL (75%).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video_complete_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 再生完了ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Viewing beacon URL (complete).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 
**video_start_beacon_urls** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 再生開始ビーコンURLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※SET時はすべて上書きされます。&lt;br&gt; ※httpsのURLのみ設定可能です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Viewing beacon URL (start).&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Replace all URLs in SET operation.&lt;br&gt; ∗Available URL is only &amp;#34;https&amp;#34;. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

