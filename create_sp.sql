USE [frpp_public]
GO
/****** Object:  StoredProcedure [dbo].[getAddresses]    Script Date: 28.05.2022 12:52:48 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[getAddresses]  
AS   
select TOP(100000) Addresses.street_address, ReportingAgencies.agency_name, ReportingAgencies.agency_code, ReportingBureaus.bureau_name, ReportingBureaus.bureau_code, 
UsingAgencies.using_agency_name, UsingAgencies.using_agency_code, UsingBureaus.bureau_name as using_bureau_name, UsingBureaus.bureau_code as using_bureau_code, 
Cities.city_name, Cities.city_code, Cities.zip_code, Countries.country_name, Countries.country_code, Counties.county_name, Counties.county_code,
States.state_name, States.state_code, Installations.installation_name, Installations.installation_code, US_Foreigns.us_foreign_name,
RealPropertyTypes.real_property_name, RealPropertyTypes.real_property_code, RealPropertyUses.name as real_property_use_name, RealPropertyUses.code as real_property_use_code, 
LegalInterests.name as legal_interest_name, LegalInterests.code as legal_interest_code,
Utilizations.utilization, Utilizations.utilization_code, Assets.asset_status, Assets.asset_status_code, HistoricalStatuses.historical_status, latitude, longitude
from Addresses 
inner join ReportingAgencies on Addresses.reporting_agency_id = ReportingAgencies.agency_id
inner join ReportingBureaus on Addresses.reporting_bureau_id = ReportingBureaus.bureau_id
inner join UsingAgencies on Addresses.using_agency_id = UsingAgencies.using_agency_id
inner join UsingBureaus on Addresses.using_bureau_id = UsingBureaus.bureau_id
inner join Cities on Addresses.city_id = Cities.city_id
inner join Countries on Addresses.country_id = Countries.country_id
inner join Counties on Addresses.county_id = Counties.county_id
inner join States on Addresses.state_id = States.state_id
inner join Installations on Addresses.installation_id = Installations.installation_id
inner join US_Foreigns on Addresses.us_foreign_id = US_Foreigns.us_foreign_id
inner join RealPropertyTypes on Addresses.real_property_type_id = RealPropertyTypes.real_property_type_id
inner join RealPropertyUses on Addresses.real_property_id = RealPropertyUses.real_property_use_id
inner join LegalInterests on Addresses.legal_interest_id = LegalInterests.legal_interest_id
inner join Utilizations on Addresses.utilization_id = Utilizations.utilization_id
inner join Assets on Addresses.asset_id = Assets.asset_id
inner join HistoricalStatuses on Addresses.historical_id = HistoricalStatuses.historical_status_id

end

insert into DW_Addresses exec getAddresses