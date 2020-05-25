# VideoServiceSetting

<div lang=\"ja\">VideoServiceSettingオブジェクトは、動画の設定内容を保持します。</div> <div lang=\"en\">VideoServiceSetting object stores the setting information of videos.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画のファイルサイズです。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;File size of the video.&lt;/div&gt;  | [optional] 
**file_type** | [**VideoServiceFileType**](VideoServiceFileType.md) |  | [optional] 
**height** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画の高さ（縦の長さ）です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Height (vertical length) of the video.&lt;/div&gt;  | [optional] 
**playback_time** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画再生時間（秒）です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Play time (sec) of the video.&lt;/div&gt;  | [optional] 
**video_ad_format** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画広告の種類です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Ad format type of the video ad.&lt;/div&gt;  | [optional] 
**video_aspect_ratio** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 動画アスペクト比の種類です。&lt;br&gt; ※指定可能な値は、DictionaryServiceのgetMediaAdFormatで取得されるDictionaryServiceMediaAdFormatのaspectRatioフィールドをご確認ください。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Type of aspect ratio.&lt;br&gt; * Available values can be referred to aspectRatio field of DictionaryServiceMediaAdFormat object obtained by getMediaAdFormat operation of DictionaryService. &lt;/div&gt;  | [optional] 
**width** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;動画の横幅です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Width of the video.&lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


