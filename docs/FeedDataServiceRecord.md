# FeedDataServiceRecord

<div lang=\"ja\">FeedDataServiceRecordオブジェクトは、アップロードした商品情報(ファイル形式)の状態を保持する。</div> <div lang=\"en\">FeedDataServiceRecord object retains status of uploaded item list(file format).</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウントID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account ID.&lt;/div&gt;  | [optional] 
**complete_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;取り込み完了日(yyyyMMdd)&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Complete date.&lt;br&gt; Format: yyyyMMdd &lt;/div&gt;  | [optional] 
**error_count** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;不備がある商品情報の件数&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Number of item list with error.&lt;/div&gt;  | [optional] 
**error_rate** | **float** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;エラー率&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Error rate.&lt;/div&gt;  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;Feedを識別するId&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Feed ID.&lt;/div&gt;  | [optional] 
**file_upload_src** | [**FeedDataServiceFileUploadSrc**](FeedDataServiceFileUploadSrc.md) |  | [optional] 
**file_upload_status** | [**FeedDataServiceFileUploadStatus**](FeedDataServiceFileUploadStatus.md) |  | [optional] 
**is_debug** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;trueはデバッグモードでの実行を意味します。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;&amp;#34;true&amp;#34; means to run in debug mode.&lt;/div&gt;  | [optional] 
**item_list_upload_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アップロードした商品情報を識別するID&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Uploaded item list ID.&lt;/div&gt;  | [optional] 
**item_list_upload_type** | [**FeedDataServiceItemListUploadType**](FeedDataServiceItemListUploadType.md) |  | [optional] 
**upload_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アップロード日(yyyyMMdd)&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Upload date.&lt;br&gt; Format: yyyyMMdd &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


