# CampaignServiceAutoCampaignConversionOptimizer

<div lang=\"ja\">CampaignServiceAutoCampaignConversionOptimizerオブジェクトは、コンバージョン最適化設定情報を表します。</div> <div lang=\"en\">CampaignServiceAutoCampaignConversionOptimizer retains conversion optimization settings.</div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_optimizer_eligibility_flg** | [**CampaignServiceConversionOptimizerEligibilityFlg**](CampaignServiceConversionOptimizerEligibilityFlg.md) |  | [optional] 
**target_cpa** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; コンバージョン単価の目標値です。&lt;br&gt; このフィールドは、SET時に省略可能となり、ADDおよびREMOVE時に無視されます。&lt;br&gt; ※設定範囲：1 - 9,999,999,999&lt;br&gt; ※コンバージョン最適化機能が動作している場合には、手動で設定されている入札設定は無効になります。&lt;br&gt; &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; This field is desired conversion cost value.&lt;br&gt; This field is optional in SET operation, and will be ignored in ADD and REMOVE operation. &lt;br&gt; * Settable range：1 - 9,999,999,999&lt;br&gt; * If function of conversion optimization is running, manual bid settings is invalid.&lt;br&gt; &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


