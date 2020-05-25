# MediaServiceImageMedia

<div lang=\"ja\"> MediaServiceImageMediaオブジェクトは、画像を格納するコンテナです。<br> このフィールドは、SET時に必須となります。 </div> <div lang=\"en\"> The MediaServiceImageMedia object is a container for storing image. <br> This field is required in SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | [**MediaServiceType**](MediaServiceType.md) |  | [optional] 
**aspect_ratio** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 画像アスペクト比の種類です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;br&gt; ※指定可能な値は、DictionaryServiceのgetMediaAdFormatで取得されるDictionaryServiceMediaAdFormatのaspectRatioフィールドをご確認ください。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The type of aspect ratio.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;br&gt; * Available values can be referred to aspectRatio field of DictionaryServiceMediaAdFormat object obtained by getMediaAdFormat operation of DictionaryService. &lt;/div&gt;  | [optional] 
**data** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;画像ファイルのbase64エンコードです。ADD時のみ指定可能で、GET時のレスポンスでは値は取得されません。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;The image file in base64 encode. It can be specified on ADD, however no value returns on the response of GET.&lt;/div&gt;  | [optional] 
**file_size** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ファイルサイズです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The file size of image. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**height** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 縦の長さです。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The height of image. &lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**media_ad_format** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 画像フォーマットの種類です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。&lt;br&gt; ※指定可能な値は、DictionaryServiceのgetMediaAdFormatで取得されるDictionaryServiceMediaAdFormatのadFormatフィールドをご確認ください。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The type of image format.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;br&gt; * Available values can be referred to adFormat field of DictionaryServiceMediaAdFormat object obtained by getMediaAdFormat operation of DictionaryService. &lt;/div&gt;  | [optional] 
**media_file_type** | [**MediaServiceFileType**](MediaServiceFileType.md) |  | [optional] 
**width** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 横幅です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; The width of image.&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


