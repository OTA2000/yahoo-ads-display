# AdGroupServiceAutoConversionOptimizer

<div lang=\"ja\"> AdGroupServiceAutoConversionOptimizerオブジェクトは、コンバージョン最適化設定情報を表します。<br> ADDおよびSET時、このフィールドは省略可能となります。 </div> <div lang=\"en\"> AdGroupServiceAutoConversionOptimizer displays the contents of conversion optimization 'Auto Bidding' settings.<br> This field is optional in ADD and SET operation. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility_flg** | [**AdGroupServiceEligibilityFlg**](AdGroupServiceEligibilityFlg.md) |  | [optional] 
**target_cpa** | **int** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; コンバージョン単価の目標値です。&lt;br&gt; ADDおよびSET時、このフィールドは省略可能となります。&lt;br&gt; ※設定範囲は1 - 9,999,999,999です。&lt;br&gt; ※コンバージョン最適化機能が動作している場合には、手動で設定されている入札設定は無効になります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target cost per conversion.&lt;br&gt; This field is optional in ADD and SET operation.&lt;br&gt; ∗Settable range is 1 - 9,999,999,999.&lt;br&gt; ∗If function of conversion optimization is running, manual bid settings is invalid. &lt;/div&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


