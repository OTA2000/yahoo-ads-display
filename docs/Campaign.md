# Campaign

<div lang=\"ja\">Campaignオブジェクトは、キャンペーン情報を表します。</div> <div lang=\"en\">Campaign object describes campaign information.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アカウントIDです。&lt;br&gt; このフィールドは、リクエストの場合は必須です。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Account ID. &lt;br&gt; This field is required in requests. &lt;/div&gt;  | [optional] 
**ad_product_type** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 配信方法です。&lt;br&gt; ADD時、このフィールドは目的なしの場合は必須となり、目的ありの場合は設定不可となります。&lt;br&gt; REMOVE時、このフィールドは無視されます。&lt;br&gt; ※指定可能な値は、AccountAdProductServiceのGET操作で取得されるAdProductをご確認ください。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Ad product information.&lt;br&gt; In ADD operation, this field is required for campaigns with no campaign goal, and this field cannot be set for campaigns with campaign goal. &lt;br&gt; In REMOVE operation, this field will be ignored.&lt;br&gt; * Available values can be referred to adProductType field of AdProduct object obtained by GET operation of AccountAdProductService. &lt;/div&gt;  | [optional] 
**app_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; iOS:アプリIDです。&lt;br&gt; Android:パッケージ名です。&lt;br&gt; このフィールドは、ADD時に省略可能となり、SETおよびREMOVE時は無視されます。&lt;br&gt; ※campaignTypeがAPPの場合、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; iOS: APP ID.&lt;br&gt; Android: Package name. &lt;br&gt; This field is optional in ADD operation, and will be ignored in SET and REMOVE operation.&lt;br&gt; *If campaignType is APP, this field is required in ADD operation. &lt;/div&gt;  | [optional] 
**app_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; アプリの名称です。&lt;br&gt; このフィールドは、ADD時に省略可能となり、SETおよびREMOVE時は無視されます。&lt;br&gt; ※campaignTypeがAPPの場合、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; App Name. &lt;br&gt; This field is optional in ADD operation, and will be ignored in SET and REMOVE operation.&lt;br&gt; *If campaignType is APP, this field is required in ADD operation. &lt;/div&gt;  | [optional] 
**bidding_strategy** | [**CampaignServiceBiddingStrategy**](CampaignServiceBiddingStrategy.md) |  | [optional] 
**budget** | [**CampaignServiceBudget**](CampaignServiceBudget.md) |  | [optional] 
**campaign_bidding_strategy** | [**CampaignServiceCampaignBiddingStrategy**](CampaignServiceCampaignBiddingStrategy.md) |  | [optional] 
**campaign_goal** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン目的です。&lt;br&gt; ADD時、このフィールドは目的なしの場合は設定不可となり、目的ありの場合は必須となります。&lt;br&gt; SETおよびREMOVE時、このフィールドは無視されます。&lt;br&gt; ※指定可能な値は、AccountServiceのGET操作で得られるAccountのaccountAuthoritiesフィールドをご確認ください。&lt;br&gt; &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Campaign goal.&lt;br&gt; In ADD operation, this field cannot be set for campaigns with no campaign goal, and will be required for campaigns with campaign goal.&lt;br&gt; In SET and REMOVE operation, this field will be ignored.&lt;br&gt; * Available values can be referred to accountAuthorities field of Account object obtained by GET operation of AccountService.&lt;br&gt; &lt;/div&gt;  | [optional] 
**campaign_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーンIDです。&lt;br&gt; このフィールドはSETおよびREMOVE時に必須となり、ADD時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Campaign ID.&lt;br&gt; This field is required in SET and REMOVE operation, and will be ignored in ADD operation. &lt;/div&gt;  | [optional] 
**campaign_name** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; キャンペーン名です。&lt;br&gt; このフィールドは、ADD時は必須、SET時は省略可能となり、REMOVE時は無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Campaign Name.&lt;br&gt; This field is required in ADD operation, is optional in SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**conversion_optimizer** | [**CampaignServiceConversionOptimizer**](CampaignServiceConversionOptimizer.md) |  | [optional] 
**device_os_type** | [**CampaignServiceDeviceOsType**](CampaignServiceDeviceOsType.md) |  | [optional] 
**end_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 終了日です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; End date.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**feed_id** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; フィードIDです。&lt;br&gt; このフィールドは、ADD時に省略可能となり、SETおよびREMOVE時に無視されます。&lt;br&gt; ※動的ディスプレイ広告の場合、ADD時に必須となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Feed ID.&lt;br&gt; This field is optional in ADD operation, and will be ignored in SET and REMOVE operation. &lt;br&gt; *If adType is Dynamic Ads for Display, this field is required in ADD operation. &lt;/div&gt;  | [optional] 
**frequency_cap** | [**CampaignServiceFrequencyCap**](CampaignServiceFrequencyCap.md) |  | [optional] 
**labels** | [**list[CampaignServiceLabel]**](CampaignServiceLabel.md) |  | [optional] 
**serving_status** | [**CampaignServiceServingStatus**](CampaignServiceServingStatus.md) |  | [optional] 
**start_date** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; 開始日です。&lt;br&gt; このフィールドは、ADDおよびSET時に省略可能となり、REMOVE時に無視されます。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Start date.&lt;br&gt; This field is optional in ADD and SET operation, and will be ignored in REMOVE operation. &lt;/div&gt;  | [optional] 
**type** | [**CampaignServiceType**](CampaignServiceType.md) |  | [optional] 
**user_status** | [**CampaignServiceUserStatus**](CampaignServiceUserStatus.md) |  | [optional] 
**viewable_frequency_cap** | [**CampaignServiceViewableFrequencyCap**](CampaignServiceViewableFrequencyCap.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


