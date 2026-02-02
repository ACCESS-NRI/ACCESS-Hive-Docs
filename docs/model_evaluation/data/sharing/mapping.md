# ACCESS Model Output Variable Mapping

This table shows the mapping of [CMIP6](https://airtable.com/appcPYagzahjnnu2E/shrZpx0VItHJ24vuy/tblpo5L8maBIGlM1B/viwNNzrqK5oPL7zk2) 
and [CMIP7](https://github.com/WCRP-CMIP/cmip7-cmor-tables/tree/main/tables) Core variables to ACCESS variables as defined
by the [ACCESS-MOPPy](https://github.com/ACCESS-NRI/ACCESS-MOPPy) CMORisation tool.

The `Mapping` column shows how to map ACCESS-ESM fields to CMIP6/7 fields.
If a cell in the Mapping column is empty then no transformation is required and 
if a cell is 'unknown' then a mapping has not been defined by ACCESS-MOPPy.

<table id="cmip_mapping">
  <thead>
    <tr style="text-align: right;">
      <th>CMIP7 Name</th>
      <th>CMIP6 Name</th>
      <th>CF Standard Name</th>
      <th>Units</th>
      <th>Freq</th>
      <th>ACCESS Name</th>
      <th>Mapping</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>atmos.areacella.ti-u-hxy-u.fx.glb</td>
      <td>fx.areacella</td>
      <td>cell_area</td>
      <td>m2</td>
      <td>fx</td>
      <td>fld_s02i204 (cloud_area_fraction)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.cl.tavg-al-hxy-u.mon.glb</td>
      <td>Amon.cl</td>
      <td>cloud_area_fraction_in_atmosphere_layer</td>
      <td>%</td>
      <td>mon</td>
      <td>fld_s02i261 (total cloud amount on levels)</td>
      <td>level_to_height(fld_s02i261)</td>
    </tr>
    <tr>
      <td>atmos.cli.tavg-al-hxy-u.mon.glb</td>
      <td>Amon.cli</td>
      <td>mass_fraction_of_cloud_ice_in_air</td>
      <td>kg kg-1</td>
      <td>mon</td>
      <td>fld_s02i309 (gridbox lsc qcf in radiation   kg/kg)</td>
      <td>level_to_height(fld_s02i309)</td>
    </tr>
    <tr>
      <td>atmos.clivi.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.clivi</td>
      <td>atmosphere_mass_content_of_cloud_ice</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>fld_s30i406 (atmosphere_cloud_ice_content)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.clt.tavg-u-hxy-u.day.glb</td>
      <td>day.clt</td>
      <td>cloud_area_fraction</td>
      <td>%</td>
      <td>day</td>
      <td>fld_s02i204 (cloud_area_fraction)</td>
      <td>fld_s02i204 * 100</td>
    </tr>
    <tr>
      <td>atmos.clt.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.clt</td>
      <td>cloud_area_fraction</td>
      <td>%</td>
      <td>mon</td>
      <td>fld_s02i204 (cloud_area_fraction)</td>
      <td>fld_s02i204 * 100</td>
    </tr>
    <tr>
      <td>atmos.clw.tavg-al-hxy-u.mon.glb</td>
      <td>Amon.clw</td>
      <td>mass_fraction_of_cloud_liquid_water_in_air</td>
      <td>kg kg-1</td>
      <td>mon</td>
      <td>fld_s02i308 (gridbox lsc qcl in radiation   kg/kg)</td>
      <td>level_to_height(fld_s02i308)</td>
    </tr>
    <tr>
      <td>atmos.clwvi.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.clwvi</td>
      <td>atmosphere_mass_content_of_cloud_condensed_water</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>atmos.evspsbl.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.evspsbl</td>
      <td>water_evapotranspiration_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s03i223 (water_evaporation_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hfls.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.hfls</td>
      <td>surface_upward_latent_heat_flux</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s03i234 (surface_upward_latent_heat_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hfss.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.hfss</td>
      <td>surface_upward_sensible_heat_flux</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s03i217 (surface_upward_sensible_heat_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hur.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.hur</td>
      <td>relative_humidity</td>
      <td>%</td>
      <td>mon</td>
      <td>fld_s30i206 (relative_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hur.tavg-p19-hxy-u.day.glb</td>
      <td>day.hur</td>
      <td>relative_humidity</td>
      <td>%</td>
      <td>day</td>
      <td>fld_s30i206 (relative_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hurs.tavg-h2m-hxy-u.6hr.glb</td>
      <td>6hrPlev.hurs</td>
      <td>relative_humidity</td>
      <td>%</td>
      <td>6hr</td>
      <td>fld_s03i245 (relative_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hurs.tavg-h2m-hxy-u.day.glb</td>
      <td>day.hurs</td>
      <td>relative_humidity</td>
      <td>%</td>
      <td>day</td>
      <td>fld_s03i245 (relative_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hurs.tavg-h2m-hxy-u.mon.glb</td>
      <td>Amon.hurs</td>
      <td>relative_humidity</td>
      <td>%</td>
      <td>mon</td>
      <td>fld_s03i245 (relative_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hus.tavg-p19-hxy-u.day.glb</td>
      <td>day.hus</td>
      <td>specific_humidity</td>
      <td>1</td>
      <td>day</td>
      <td>fld_s30i205 (specific_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.hus.tavg-p19-hxy-u.mon.glb</td>
      <td>Amon.hus</td>
      <td>specific_humidity</td>
      <td>1</td>
      <td>mon</td>
      <td>fld_s30i205 (specific_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.huss.tavg-h2m-hxy-u.day.glb</td>
      <td>day.huss</td>
      <td>specific_humidity</td>
      <td>1</td>
      <td>day</td>
      <td>fld_s03i237 (specific_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.huss.tavg-h2m-hxy-u.mon.glb</td>
      <td>Amon.huss</td>
      <td>specific_humidity</td>
      <td>1</td>
      <td>mon</td>
      <td>fld_s03i237 (specific_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.huss.tpt-h2m-hxy-u.3hr.glb</td>
      <td>3hr.huss</td>
      <td>specific_humidity</td>
      <td>1</td>
      <td>3hr</td>
      <td>fld_s03i237 (specific_humidity)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.pr.tavg-u-hxy-u.1hr.glb</td>
      <td>E1hr.pr</td>
      <td>precipitation_flux</td>
      <td>kg m-2 s-1</td>
      <td>1hr</td>
      <td>fld_s05i216 (precipitation_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.pr.tavg-u-hxy-u.3hr.glb</td>
      <td>3hr.pr</td>
      <td>precipitation_flux</td>
      <td>kg m-2 s-1</td>
      <td>3hr</td>
      <td>fld_s05i216 (precipitation_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.pr.tavg-u-hxy-u.day.glb</td>
      <td>day.pr</td>
      <td>precipitation_flux</td>
      <td>kg m-2 s-1</td>
      <td>day</td>
      <td>fld_s05i216 (precipitation_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.pr.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.pr</td>
      <td>precipitation_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s05i216 (precipitation_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.prc.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.prc</td>
      <td>convective_precipitation_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s05i205 (convective_rainfall_flux),<br>fld_s05i206 (convective_snowfall_flux)</td>
      <td>fld_s05i205 + fld_s05i206</td>
    </tr>
    <tr>
      <td>atmos.prsn.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.prsn</td>
      <td>snowfall_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s05i215 (snowfall_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.prw.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.prw</td>
      <td>atmosphere_mass_content_of_water_vapor</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>fld_s30i404 (total column wet mass  rho grid),<br>fld_s30i403 (total column dry mass  rho grid),<br>fld_s30i405 (atmosphere_cloud_liquid_water_content),<br>fld_s30i406 (atmosphere_cloud_ice_content)</td>
      <td>fld_s30i404 - (fld_s30i403 + fld_s30i405 + fld_s30i406)</td>
    </tr>
    <tr>
      <td>atmos.ps.tavg-u-hxy-u.day.glb</td>
      <td>CFday.ps</td>
      <td>surface_air_pressure</td>
      <td>Pa</td>
      <td>day</td>
      <td>fld_s00i409 (surface_air_pressure)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ps.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.ps</td>
      <td>surface_air_pressure</td>
      <td>Pa</td>
      <td>mon</td>
      <td>fld_s00i409 (surface_air_pressure)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.psl.tavg-u-hxy-u.day.glb</td>
      <td>day.psl</td>
      <td>air_pressure_at_mean_sea_level</td>
      <td>Pa</td>
      <td>day</td>
      <td>fld_s16i222 (air_pressure_at_sea_level)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.psl.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.psl</td>
      <td>air_pressure_at_mean_sea_level</td>
      <td>Pa</td>
      <td>mon</td>
      <td>fld_s16i222 (air_pressure_at_sea_level)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rlds.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rlds</td>
      <td>surface_downwelling_longwave_flux_in_air</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s02i207 (surface_downwelling_longwave_flux_in_air)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rldscs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rldscs</td>
      <td>surface_downwelling_longwave_flux_in_air_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s02i208 (surface_downwelling_longwave_flux_in_air_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rlus.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rlus</td>
      <td>surface_upwelling_longwave_flux_in_air</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s02i207 (surface_downwelling_longwave_flux_in_air),<br>fld_s02i201 (surface_net_downward_longwave_flux),<br>fld_s03i332 (toa_outgoing_longwave_flux),<br>fld_s02i205 (toa_outgoing_longwave_flux)</td>
      <td>((fld_s02i207 - fld_s02i201) + fld_s03i332) - fld_s02i205</td>
    </tr>
    <tr>
      <td>atmos.rluscs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rluscs</td>
      <td>surface_upwelling_longwave_flux_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s02i206 (toa_outgoing_longwave_flux_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rlut.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rlut</td>
      <td>toa_outgoing_longwave_flux</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s03i332 (toa_outgoing_longwave_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rlutcs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rlutcs</td>
      <td>toa_outgoing_longwave_flux_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s02i206 (toa_outgoing_longwave_flux_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsds.tavg-u-hxy-u.day.glb</td>
      <td>day.rsds</td>
      <td>surface_downwelling_shortwave_flux_in_air</td>
      <td>W m-2</td>
      <td>day</td>
      <td>fld_s01i235 (surface_downwelling_shortwave_flux_in_air)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsds.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsds</td>
      <td>surface_downwelling_shortwave_flux_in_air</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i235 (surface_downwelling_shortwave_flux_in_air)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsdscs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsdscs</td>
      <td>surface_downwelling_shortwave_flux_in_air_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i210 (surface_downwelling_shortwave_flux_in_air_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsdt.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsdt</td>
      <td>toa_incoming_shortwave_flux</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i207 (toa_incoming_shortwave_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsus.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsus</td>
      <td>surface_upwelling_shortwave_flux_in_air</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i235 (surface_downwelling_shortwave_flux_in_air),<br>fld_s01i201 (surface_net_downward_shortwave_flux)</td>
      <td>fld_s01i235 - fld_s01i201</td>
    </tr>
    <tr>
      <td>atmos.rsuscs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsuscs</td>
      <td>surface_upwelling_shortwave_flux_in_air_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i211 (surface_upwelling_shortwave_flux_in_air_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsut.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsut</td>
      <td>toa_outgoing_shortwave_flux</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i208 (toa_outgoing_shortwave_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.rsutcs.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.rsutcs</td>
      <td>toa_outgoing_shortwave_flux_assuming_clear_sky</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>fld_s01i209 (toa_outgoing_shortwave_flux_assuming_clear_sky)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.sfcWind.tavg-h10m-hxy-u.day.glb</td>
      <td>day.sfcWind</td>
      <td>wind_speed</td>
      <td>m s-1</td>
      <td>day</td>
      <td>fld_s03i230 (10 metre wind speed on c grid)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.sfcWind.tavg-h10m-hxy-u.mon.glb</td>
      <td>Amon.sfcWind</td>
      <td>wind_speed</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>fld_s03i230 (10 metre wind speed on c grid)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.sftlf.ti-u-hxy-u.fx.glb</td>
      <td>fx.sftlf</td>
      <td>land_area_fraction</td>
      <td>%</td>
      <td>fx</td>
      <td>fld_s03i395 (land_area_fraction)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ta.tavg-p19-hxy-air.day.glb</td>
      <td>day.ta</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>day</td>
      <td>fld_s30i204 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ta.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.ta</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>fld_s30i204 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ta.tpt-p3-hxy-air.6hr.glb</td>
      <td>6hrPlevPt.ta</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>6hr</td>
      <td>fld_s30i204 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tavg-h2m-hxy-u.day.glb</td>
      <td>day.tas</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>day</td>
      <td>fld_s03i236 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tavg-h2m-hxy-u.mon.glb</td>
      <td>Amon.tas</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>fld_s03i236 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tmax-h2m-hxy-u.day.glb</td>
      <td>day.tasmax</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>day</td>
      <td>fld_s03i236_max (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tmaxavg-h2m-hxy-u.mon.glb</td>
      <td>Amon.tasmax</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>fld_s03i236_max (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tmin-h2m-hxy-u.day.glb</td>
      <td>day.tasmin</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>day</td>
      <td>fld_s03i236_min (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tminavg-h2m-hxy-u.mon.glb</td>
      <td>Amon.tasmin</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>fld_s03i236_min (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tas.tpt-h2m-hxy-u.3hr.glb</td>
      <td>3hr.tas</td>
      <td>air_temperature</td>
      <td>K</td>
      <td>3hr</td>
      <td>fld_s03i236 (air_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tauu.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.tauu</td>
      <td>surface_downward_eastward_stress</td>
      <td>Pa</td>
      <td>mon</td>
      <td>fld_s03i460 (x-comp surface bl stress)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.tauv.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.tauv</td>
      <td>surface_downward_northward_stress</td>
      <td>Pa</td>
      <td>mon</td>
      <td>fld_s03i461 (y-comp surface bl stress)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ts.tavg-u-hxy-u.mon.glb</td>
      <td>Amon.ts</td>
      <td>surface_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>fld_s00i024 (surface_temperature)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ua.tavg-p19-hxy-air.day.glb</td>
      <td>day.ua</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>day</td>
      <td>fld_s30i201 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ua.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.ua</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>fld_s30i201 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.ua.tpt-p3-hxy-air.6hr.glb</td>
      <td>6hrPlevPt.ua</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>6hr</td>
      <td>fld_s30i201 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.uas.tavg-h10m-hxy-u.day.glb</td>
      <td>day.uas</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>day</td>
      <td>fld_s03i209 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.uas.tavg-h10m-hxy-u.mon.glb</td>
      <td>Amon.uas</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>fld_s03i209 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.uas.tpt-h10m-hxy-u.3hr.glb</td>
      <td>3hrPt.uas</td>
      <td>eastward_wind</td>
      <td>m s-1</td>
      <td>3hr</td>
      <td>fld_s03i209 (eastward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.va.tavg-p19-hxy-air.day.glb</td>
      <td>day.va</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>day</td>
      <td>fld_s30i202 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.va.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.va</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>fld_s30i202 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.va.tpt-p3-hxy-air.6hr.glb</td>
      <td>6hrPlevPt.va</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>6hr</td>
      <td>fld_s30i202 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.vas.tavg-h10m-hxy-u.day.glb</td>
      <td>day.vas</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>day</td>
      <td>fld_s03i210 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.vas.tavg-h10m-hxy-u.mon.glb</td>
      <td>Amon.vas</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>fld_s03i210 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.vas.tpt-h10m-hxy-u.3hr.glb</td>
      <td>3hrPt.vas</td>
      <td>northward_wind</td>
      <td>m s-1</td>
      <td>3hr</td>
      <td>fld_s03i210 (northward_wind)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.wap.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.wap</td>
      <td>lagrangian_tendency_of_air_pressure</td>
      <td>Pa s-1</td>
      <td>mon</td>
      <td>fld_s30i208 (lagrangian_tendency_of_air_pressure)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.wap.tavg-p19-hxy-u.day.glb</td>
      <td>day.wap</td>
      <td>lagrangian_tendency_of_air_pressure</td>
      <td>Pa s-1</td>
      <td>day</td>
      <td>fld_s30i208 (lagrangian_tendency_of_air_pressure)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.zg.tavg-p19-hxy-air.day.glb</td>
      <td>day.zg</td>
      <td>geopotential_height</td>
      <td>m</td>
      <td>day</td>
      <td>fld_s30i207 (geopotential_height)</td>
      <td></td>
    </tr>
    <tr>
      <td>atmos.zg.tavg-p19-hxy-air.mon.glb</td>
      <td>Amon.zg</td>
      <td>geopotential_height</td>
      <td>m</td>
      <td>mon</td>
      <td>fld_s30i207 (geopotential_height)</td>
      <td></td>
    </tr>
    <tr>
      <td>land.evspsblsoi.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.evspsblsoi</td>
      <td>water_evaporation_flux_from_soil</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s03i296 (water_evaporation_flux_from_soil)</td>
      <td></td>
    </tr>
    <tr>
      <td>land.evspsblveg.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.evspsblveg</td>
      <td>water_evaporation_flux_from_canopy</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s03i297 (water_evaporation_flux_from_canopy)</td>
      <td></td>
    </tr>
    <tr>
      <td>land.lai.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.lai</td>
      <td>leaf_area_index</td>
      <td>1</td>
      <td>mon</td>
      <td>fld_s03i893 (leaf area index (casa-cnp glai)),<br>fld_s03i317 (surface tile fractions),<br>fld_s03i395 (land_area_fraction)</td>
      <td>average_tile(fld_s03i893)</td>
    </tr>
    <tr>
      <td>land.mrro.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.mrro</td>
      <td>runoff_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s08i234 (surface_runoff_flux),<br>fld_s08i235 (subsurface_runoff_flux)</td>
      <td>fld_s08i234 + fld_s08i235</td>
    </tr>
    <tr>
      <td>land.mrros.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.mrros</td>
      <td>surface_runoff_flux</td>
      <td>kg m-2 s-1</td>
      <td>mon</td>
      <td>fld_s08i234 (surface_runoff_flux)</td>
      <td></td>
    </tr>
    <tr>
      <td>land.mrso.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.mrso</td>
      <td>mass_content_of_water_in_soil</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>fld_s08i223 (mass_content_of_water_in_soil_layer)</td>
      <td>sum(fld_s08i223)</td>
    </tr>
    <tr>
      <td>land.mrsofc.ti-u-hxy-lnd.fx.glb</td>
      <td>fx.mrsofc</td>
      <td>soil_moisture_content_at_field_capacity</td>
      <td>kg m-2</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>land.mrsol.tavg-d10cm-hxy-lnd.mon.glb</td>
      <td>Lmon.mrsos</td>
      <td>mass_content_of_water_in_soil_layer</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>fld_s08i223 (mass_content_of_water_in_soil_layer)</td>
      <td>calc_topsoil(fld_s08i223)</td>
    </tr>
    <tr>
      <td>land.orog.ti-u-hxy-u.fx.glb</td>
      <td>fx.orog</td>
      <td>surface_altitude</td>
      <td>m</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>land.rootd.ti-u-hxy-lnd.fx.glb</td>
      <td>fx.rootd</td>
      <td>root_depth</td>
      <td>m</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>land.sftgif.ti-u-hxy-u.fx.glb</td>
      <td>fx.sftgif</td>
      <td>land_ice_area_fraction</td>
      <td>%</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>land.slthick.ti-sl-hxy-lnd.fx.glb</td>
      <td>Efx.slthick</td>
      <td>cell_thickness</td>
      <td>m</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>landIce.mrfso.tavg-u-hxy-lnd.mon.glb</td>
      <td>Lmon.mrfso</td>
      <td>soil_frozen_water_content</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>fld_s08i223 (mass_content_of_water_in_soil_layer),<br>fld_s08i230 (mass_fraction_of_frozen_water_in_soil_moisture),<br>depth (unknown)</td>
      <td>sum((fld_s08i223 * fld_s08i230))</td>
    </tr>
    <tr>
      <td>landIce.snc.tavg-u-hxy-lnd.mon.glb</td>
      <td>LImon.snc</td>
      <td>surface_snow_area_fraction</td>
      <td>%</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>landIce.snw.tavg-u-hxy-lnd.mon.glb</td>
      <td>LImon.snw</td>
      <td>surface_snow_amount</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.areacello.ti-u-hxy-u.fx.glb</td>
      <td>Ofx.areacello</td>
      <td>cell_area</td>
      <td>m2</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.basin.ti-u-hxy-u.fx.glb</td>
      <td>Ofx.basin</td>
      <td>region</td>
      <td>1</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.bigthetao.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.bigthetao</td>
      <td>sea_water_conservative_temperature</td>
      <td>degC</td>
      <td>mon</td>
      <td>temp</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.deptho.ti-u-hxy-sea.fx.glb</td>
      <td>Ofx.deptho</td>
      <td>sea_floor_depth_below_geoid</td>
      <td>m</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.hfds.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.hfds</td>
      <td>surface_downward_heat_flux_in_sea_water</td>
      <td>W m-2</td>
      <td>mon</td>
      <td>sfc_hflux_from_runoff,<br>sfc_hflux_coupler,<br>sfc_hflux_pme,<br>frazil_3d_int_z</td>
      <td>sum_vars(var)</td>
    </tr>
    <tr>
      <td>ocean.hfgeou.ti-u-hxy-sea.fx.glb</td>
      <td>Ofx.hfgeou</td>
      <td>upward_geothermal_heat_flux_at_sea_floor</td>
      <td>W m-2</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.masscello.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.masscello</td>
      <td>sea_water_mass_per_unit_area</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>rho_dzt</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.masscello.ti-ol-hxy-sea.fx.glb</td>
      <td>Ofx.masscello</td>
      <td>sea_water_mass_per_unit_area</td>
      <td>kg m-2</td>
      <td>fx</td>
      <td>rho_dzt</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.mlotst.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.mlotst</td>
      <td>ocean_mixed_layer_thickness_defined_by_sigma_t</td>
      <td>m</td>
      <td>mon</td>
      <td>mld</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.sftof.ti-u-hxy-u.fx.glb</td>
      <td>Ofx.sftof</td>
      <td>sea_area_fraction</td>
      <td>%</td>
      <td>fx</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>ocean.so.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.so</td>
      <td>sea_water_salinity</td>
      <td>1E-03</td>
      <td>mon</td>
      <td>salt</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.sos.tavg-u-hxy-sea.day.glb</td>
      <td>Oday.sos</td>
      <td>sea_surface_salinity</td>
      <td>1E-03</td>
      <td>day</td>
      <td>sss</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.sos.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.sos</td>
      <td>sea_surface_salinity</td>
      <td>1E-03</td>
      <td>mon</td>
      <td>sss</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.tauuo.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.tauuo</td>
      <td>downward_x_stress_at_sea_water_surface</td>
      <td>N m-2</td>
      <td>mon</td>
      <td>tau_x</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.tauvo.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.tauvo</td>
      <td>downward_y_stress_at_sea_water_surface</td>
      <td>N m-2</td>
      <td>mon</td>
      <td>tau_y</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.thetao.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.thetao</td>
      <td>sea_water_potential_temperature</td>
      <td>degC</td>
      <td>mon</td>
      <td>pot_temp</td>
      <td>kelvin_to_celsius(pot_temp)</td>
    </tr>
    <tr>
      <td>ocean.thkcello.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.thkcello</td>
      <td>cell_thickness</td>
      <td>m</td>
      <td>mon</td>
      <td>dht</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.thkcello.ti-ol-hxy-sea.fx.glb</td>
      <td>Ofx.thkcello</td>
      <td>cell_thickness</td>
      <td>m</td>
      <td>fx</td>
      <td>dht</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.tos.tavg-u-hxy-sea.day.glb</td>
      <td>Oday.tos</td>
      <td>sea_surface_temperature</td>
      <td>degC</td>
      <td>day</td>
      <td>surface_temp</td>
      <td>kelvin_to_celsius(surface_temp)</td>
    </tr>
    <tr>
      <td>ocean.tos.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.tos</td>
      <td>sea_surface_temperature</td>
      <td>degC</td>
      <td>mon</td>
      <td>surface_temp</td>
      <td>kelvin_to_celsius(surface_temp)</td>
    </tr>
    <tr>
      <td>ocean.umo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.umo</td>
      <td>ocean_mass_x_transport</td>
      <td>kg s-1</td>
      <td>mon</td>
      <td>tx_trans</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.uo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.uo</td>
      <td>sea_water_x_velocity</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>u</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.vmo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.vmo</td>
      <td>ocean_mass_y_transport</td>
      <td>kg s-1</td>
      <td>mon</td>
      <td>ty_trans</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.vo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.vo</td>
      <td>sea_water_y_velocity</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>v</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.wmo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.wmo</td>
      <td>upward_ocean_mass_transport</td>
      <td>kg s-1</td>
      <td>mon</td>
      <td>tz_trans</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.wo.tavg-ol-hxy-sea.mon.glb</td>
      <td>Omon.wo</td>
      <td>upward_sea_water_velocity</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>wt</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.zos.tavg-u-hxy-sea.day.glb</td>
      <td>Oday.zos</td>
      <td>sea_surface_height_above_geoid</td>
      <td>m</td>
      <td>day</td>
      <td>sea_level</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.zos.tavg-u-hxy-sea.mon.glb</td>
      <td>Omon.zos</td>
      <td>sea_surface_height_above_geoid</td>
      <td>m</td>
      <td>mon</td>
      <td>sea_level</td>
      <td></td>
    </tr>
    <tr>
      <td>ocean.zostoga.tavg-u-hm-sea.mon.glb</td>
      <td>Omon.zostoga</td>
      <td>global_average_thermosteric_sea_level_change</td>
      <td>m</td>
      <td>mon</td>
      <td>pot_temp,<br>dht</td>
      <td>calc_zostoga(pot_temp, dht)</td>
    </tr>
    <tr>
      <td>seaIce.siconc.tavg-u-hxy-u.day.glb</td>
      <td>SIday.siconc</td>
      <td>sea_ice_area_fraction</td>
      <td>%</td>
      <td>day</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.siconc.tavg-u-hxy-u.mon.glb</td>
      <td>SImon.siconc</td>
      <td>sea_ice_area_fraction</td>
      <td>%</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.simass.tavg-u-hxy-si.mon.glb</td>
      <td>SImon.simass</td>
      <td>sea_ice_amount</td>
      <td>kg m-2</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.sithick.tavg-u-hxy-si.mon.glb</td>
      <td>SImon.sithick</td>
      <td>sea_ice_thickness</td>
      <td>m</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.sitimefrac.tavg-u-hxy-sea.mon.glb</td>
      <td>SImon.sitimefrac</td>
      <td>fraction_of_time_with_sea_ice_area_fraction_above_threshold</td>
      <td>1</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.siu.tavg-u-hxy-si.mon.glb</td>
      <td>SImon.siu</td>
      <td>sea_ice_x_velocity</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.siv.tavg-u-hxy-si.mon.glb</td>
      <td>SImon.siv</td>
      <td>sea_ice_y_velocity</td>
      <td>m s-1</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.snd.tavg-u-hxy-sn.mon.glb</td>
      <td>SImon.sisnthick</td>
      <td>surface_snow_thickness</td>
      <td>m</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
    <tr>
      <td>seaIce.ts.tavg-u-hxy-si.mon.glb</td>
      <td>SImon.sitemptop</td>
      <td>surface_temperature</td>
      <td>K</td>
      <td>mon</td>
      <td>unknown</td>
      <td>unknown</td>
    </tr>
  </tbody>
</table>
