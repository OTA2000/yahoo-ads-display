# PlacementUrlList

<div lang=\"ja\">PlacementUrlListオブジェクトは、プレイスメントUrl情報を保持するオブジェクトです。</div> <div lang=\"en\">The objects to keep Placement Url Information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; This field is required in requests. &lt;/div&gt;  | 
**description** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; urlリストの説明です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Url List Description.&lt;br&gt; This field is optional in ADD and SET operation. &lt;/div&gt;  | [optional] 
**unknown_domain_flg** | [**PlacementUrlListServiceUnknownDomainFlg**](PlacementUrlListServiceUnknownDomainFlg.md) |  | [optional] 
**url_list_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; urlリストIDです。&lt;br&gt; このフィールドは、SETおよびREMOVE時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Url List ID. &lt;br&gt; This field is required in SET and REMOVE operation. &lt;/div&gt;  | [optional] 
**url_list_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; urlリスト名です。&lt;br&gt; このフィールドは、ADD時に必須となり、SET時に省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Url List Name. &lt;br&gt; This field is required in ADD operation, and is optional in SET operation. &lt;/div&gt;  | [optional] 
**urls** | [**list[PlacementUrlListServiceUrlList]**](PlacementUrlListServiceUrlList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


