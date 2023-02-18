from xml.etree.ElementPath import get_parent_map
import folium
import pandas
import numpy
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
#print(data.columns)
def color_producer(elevation):
    if(elevation>2500):
        return "red" 
    else:
        return "green"
map=folium.Map(location=[38.58, -99.09],zoom_start=6,tiles = "Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt,ln],radius=15, popup=folium.Popup(str(el)+"m",parse_html=True),icon=folium.Icon(color=color_producer(el))))
    #fg.add_child(folium.PolyLine(locations=[(28.5011226, 77.4099794), (30.5011226, 78.4099794)],line_opacity=0.5))
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red' if x["properties"]["POP2005"]< 100000000 else "green"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
