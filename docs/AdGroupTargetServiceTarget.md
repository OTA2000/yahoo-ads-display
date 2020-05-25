# AdGroupTargetServiceTarget

<div lang=\"ja\"> AdGroupTargetServiceTargetオブジェクトは、ターゲティング設定情報を保持します。<br> このフィールドは、リクエストの場合は必須です。 </div> <div lang=\"en\"> AdGroupTargetServiceTarget object is a container for storing targeting settings.<br> This field is required in requests. </div> 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_schedule_target** | [**AdGroupTargetServiceAdScheduleTarget**](AdGroupTargetServiceAdScheduleTarget.md) |  | [optional] 
**age_target** | [**AdGroupTargetServiceAgeTarget**](AdGroupTargetServiceAgeTarget.md) |  | [optional] 
**app_target** | [**AdGroupTargetServiceAppTarget**](AdGroupTargetServiceAppTarget.md) |  | [optional] 
**audience_category_target** | [**AdGroupTargetServiceAudienceCategoryTarget**](AdGroupTargetServiceAudienceCategoryTarget.md) |  | [optional] 
**carrier_target** | [**AdGroupTargetServiceCarrierTarget**](AdGroupTargetServiceCarrierTarget.md) |  | [optional] 
**device_target** | [**AdGroupTargetServiceDeviceTarget**](AdGroupTargetServiceDeviceTarget.md) |  | [optional] 
**gender_target** | [**AdGroupTargetServiceGenderTarget**](AdGroupTargetServiceGenderTarget.md) |  | [optional] 
**geo_target** | [**AdGroupTargetServiceGeoTarget**](AdGroupTargetServiceGeoTarget.md) |  | [optional] 
**interest_category_target** | [**AdGroupTargetServiceInterestCategoryTarget**](AdGroupTargetServiceInterestCategoryTarget.md) |  | [optional] 
**is_remove** | **bool** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; trueの場合、ターゲティング種別をすべて削除します。&lt;br&gt; このフィールドは、ADD、SETおよびREMOVE時は無視され、REPLACE時は省略可能となります。 &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; If true, delete all targeting types.&lt;br&gt; This field will be ignored in ADD, SET and REMOVE operation, and will be optional in REPLACE operation. &lt;/div&gt;  | [optional] 
**os_target** | [**AdGroupTargetServiceOsTarget**](AdGroupTargetServiceOsTarget.md) |  | [optional] 
**os_version_target** | [**AdGroupTargetServiceOsVersionTarget**](AdGroupTargetServiceOsVersionTarget.md) |  | [optional] 
**placement_target** | [**AdGroupTargetServicePlacementTarget**](AdGroupTargetServicePlacementTarget.md) |  | [optional] 
**search_target** | [**AdGroupTargetServiceSearchTarget**](AdGroupTargetServiceSearchTarget.md) |  | [optional] 
**site_category_target** | [**AdGroupTargetServiceSiteCategoryTarget**](AdGroupTargetServiceSiteCategoryTarget.md) |  | [optional] 
**site_retargeting_target** | [**AdGroupTargetServiceSiteRetargetingTarget**](AdGroupTargetServiceSiteRetargetingTarget.md) |  | [optional] 
**target_id** | **str** | &lt;div lang&#x3D;\&quot;ja\&quot;&gt; ターゲットIDです。&lt;br&gt; このフィールドは、ADDおよびREPLACE時は省略可能となり、SETおよびREMOVE時は必須となります。&lt;br&gt; ※ADD時、targetTypeが以下のいずれかの場合は必須です。&lt;br&gt; ‐SITE_RETARGETING&lt;br&gt; ‐PLACEMENT_TARGET&lt;br&gt; ‐SEARCH_TARGET&lt;br&gt; ‐GEO_TARGET&lt;br&gt; ‐INTEREST_CATEGORY&lt;br&gt; ‐SITE_CATEGORY&lt;br&gt; ‐AUDIENCE_CATEGORY_TARGET&lt;br&gt; ※REPLACE時、isRemoveがtrueの場合は設定不要です。&lt;br&gt; &lt;br&gt; ‐SITE_RETARGETING: targetListId&lt;br&gt; ‐PLACEMENT_TARGET: placementUrlListId&lt;br&gt; ‐SEARCH_TARGET: searchKeywordListId&lt;br&gt; ‐GEO_TARGET: IM地域コード(geo)&lt;br&gt; ‐INTEREST_CATEGORY: カテゴリーコード(category)&lt;br&gt; ‐SITE_CATEGORY: カテゴリーコード(category)&lt;br&gt; ‐OS_VERSION_TARGET: osVersion&lt;br&gt; ‐AUDIENCE_CATEGORY_TARGET: オーディエンスカテゴリーコード(audience category) &lt;/div&gt; &lt;div lang&#x3D;\&quot;en\&quot;&gt; Target ID.&lt;br&gt; This field is optional in ADD and REPLACE operation, and is required in SET and REMOVE operation.&lt;br&gt; *If targetType is any of the following, this field is required in ADD operation.&lt;br&gt; ‐SITE_RETARGETING&lt;br&gt; ‐PLACEMENT_TARGET&lt;br&gt; ‐SEARCH_TARGET&lt;br&gt; ‐GEO_TARGET&lt;br&gt; ‐INTEREST_CATEGORY&lt;br&gt; ‐SITE_CATEGORY&lt;br&gt; ‐AUDIENCE_CATEGORY_TARGET&lt;br&gt; *If isRemove is true, this field does not need to be set in REPLACE operation.&lt;br&gt; &lt;br&gt; ‐SITE_RETARGETING: targetListId&lt;br&gt; ‐PLACEMENT_TARGET: placementUrlListId&lt;br&gt; ‐SEARCH_TARGET: searchKeywordListId&lt;br&gt; ‐GEO_TARGET: IM area code(geo)&lt;br&gt; ‐INTEREST_CATEGORY: category code(category)&lt;br&gt; ‐SITE_CATEGORY: category code(category)&lt;br&gt; ‐OS_VERSION_TARGET: osVersion&lt;br&gt; ‐AUDIENCE_CATEGORY_TARGET: audience category code(audience category) &lt;/div&gt;  | [optional] 
**target_type** | [**AdGroupTargetServiceTargetType**](AdGroupTargetServiceTargetType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


