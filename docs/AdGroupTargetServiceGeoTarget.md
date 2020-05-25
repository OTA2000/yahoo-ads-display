# AdGroupTargetServiceGeoTarget

<div lang=\"ja\"> AdGroupTargetServiceGeoTargetオブジェクトは、地域ターゲティングの設定情報を保持します。<br> ADD、SETおよびREPLACE時、このフィールドは省略可能となります。<br> ※targetTypeがGEO_TARGETの場合は必須です。 </div> <div lang=\"en\"> AdGroupTargetServiceGeoTarget object is a container for storing geological targeting settings.<br> This field is optional in ADD, SET and REPLACE operation.<br> ∗If targetType is GEO_TARGET, this field is required. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_en** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 地域名（英語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Region name (English).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 
**geo_name_ja** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 地域名（日本語）です。&lt;br&gt; このフィールドは、レスポンスの際に返却されますが、リクエストの際には無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Region name (Japanese).&lt;br&gt; Although this field will be returned in the response, it will be ignored on input. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


