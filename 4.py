#%%
import folium
import pandas as pd

world_geo=r'/Users/dragonbright/Downloads/san-francisco.geojson'
world_map=folium.Map(location=[37.773972,-122.431297]
                     ,zoom_start=12)

world_map.choropleth(geo_data=world_geo,key_on='feature.properties',
                     fill_color = 'YlOrRd',
                     fill_opacity = 0.7, line_opacity=0.2,
                      legend_title = '% unemployed'
                      )

world_map


#%%
