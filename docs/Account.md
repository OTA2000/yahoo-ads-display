# Account

<div lang=\"ja\">Accountオブジェクトは、アカウント情報を示します。<br> accountAuthoritiesで返却される値は、以下のとおりです。   <table border='1'>     <tr>       <th>accountAuthorities</th>       <th>キャンペーン目的</th>     </tr>     <tr>       <td>WEBSITE_TRAFFIC</td>       <td>サイト誘導</td>     </tr>     <tr>       <td>VIDEO_VIEW</td>       <td>動画再生</td>     </tr>     <tr>       <td>APP_PROMOTION</td>       <td>アプリ訴求</td>     </tr>     <tr>       <td>CONVERSION</td>       <td>コンバージョン</td>     </tr>     <tr>       <td>ITEM_LIST</td>       <td>商品リスト訴求</td>     </tr>   </table> それぞれのキャンペーン目的の詳細については、<a href=\"https://ads-help.yahoo.co.jp/yahooads/display/articledetail?lan=ja&aid=51512\">目的別キャンペーン作成について</a>をご確認ください。 </div> <div lang=\"en\">Account objects serve account information.<br> Responded values of `accountAuthorities` are as follows.   <table border='1'>     <tr>       <th>accountAuthorities</th>       <th>campaign goal</th>     </tr>     <tr>       <td>WEBSITE_TRAFFIC</td>       <td>Website traffic</td>     </tr>     <tr>       <td>VIDEO_VIEW</td>       <td>Video view</td>     </tr>     <tr>       <td>APP_PROMOTION</td>       <td>App promotion</td>     </tr>     <tr>       <td>CONVERSION</td>       <td>Conversion</td>     </tr>     <tr>       <td>ITEM_LIST</td>       <td>Item list promotion</td>     </tr>   </table> Details of these campaign goal are described on <a href=\"https://ads-help.yahoo.co.jp/yahooads/display/articledetail?lan=ja&aid=51512\">目的別キャンペーン作成について</a> (Japanese context only). </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_authorities** | **list[str]** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt;アカウント権限です。&lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt;Account authority.&lt;/div&gt;  | [optional] 
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; SET時、このフィールドは必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID.&lt;br&gt; This field is required in SET operation. &lt;/div&gt;  | [optional] 
**account_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウント名です。&lt;br&gt; SET時、このフィールドは省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account name.&lt;br&gt; This field is optional in SET operation. &lt;/div&gt;  | [optional] 
**account_status** | [**AccountServiceStatus**](AccountServiceStatus.md) |  | [optional] 
**account_type** | [**AccountServiceType**](AccountServiceType.md) |  | [optional] 
**auth_type** | [**AccountServiceAuthType**](AccountServiceAuthType.md) |  | [optional] 
**auto_tagging_enabled** | [**AccountServiceAutoTaggingEnabled**](AccountServiceAutoTaggingEnabled.md) |  | [optional] 
**budget** | [**AccountServiceBudget**](AccountServiceBudget.md) |  | [optional] 
**delivery_status** | [**AccountServiceDeliveryStatus**](AccountServiceDeliveryStatus.md) |  | [optional] 
**is_test_account** | [**AccountServiceIsTestAccount**](AccountServiceIsTestAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


