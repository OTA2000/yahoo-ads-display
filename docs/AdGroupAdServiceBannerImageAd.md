# AdGroupAdServiceBannerImageAd

<div lang=\"ja\"> AdGroupAdServiceBannerImageAdオブジェクトは、画像で構成される広告の情報を表します。<br> このフィールドは、省略可能となります。<br> ※ADD時、adTypeがBANNER_IMAGE_ADの場合は必須です。 </div> <div lang=\"en\"> AdGroupAdServiceBannerImageAd object describes information regarding ads composed of images.<br> This field is optional.<br> *If adType is BANNER_IMAGE_AD, this field is required in ADD operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 表示URLです。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ・標準キャンペーンの場合&lt;br&gt; &amp;nbsp;&amp;nbsp;ADDでは入力必須です。SETでの入力は任意です。&lt;br&gt; ・アプリキャンペーンの場合&lt;br&gt; &amp;nbsp;&amp;nbsp;ADD、SETのどちらも指定できません。&lt;br&gt; &amp;nbsp;&amp;nbsp;※アプリキャンペーンで指定したDeviceOsTypeに基づき、以下のいずれかのURLが自動で設定されます。&lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;- iOSの場合：itunes.apple.com&lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;- Androidの場合：play.google.com&lt;br&gt; &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Display URL.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; - Standard campaign:&lt;br&gt; &amp;nbsp;&amp;nbsp;Required for ADD, optional for SET.&lt;br&gt; - Mobile app campaign:&lt;br&gt; &amp;nbsp;&amp;nbsp;Not allowed for ADD and SET.&lt;br&gt; &amp;nbsp;&amp;nbsp;*Based on DeviceOsType specified on Mobile app campaign, any of the following URLs will be automatically set.&lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;- For iOS : itunes.apple.com&lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;- For Android : play.google.com&lt;br&gt; &lt;/div&gt;  | [optional] 
**url** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; リンク先URLです。&lt;br&gt; このフィールドは、ADD時は必須となり、SET時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Destination URL.&lt;br&gt; This field is required in ADD operation, and will be optional in SET operation. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


