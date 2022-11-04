import folium
import pandas

data = pandas.read_csv("stadiums-geocoded.txt")
lat = list(data["latitude"])
lon = list(data["longitude"])
cap = list(data["capacity"])
name = list(data["stadium"])

def markerColorChangeBlue():
    if cap < 20000:
        return 'blue'

def markerColorChangeGreen():
    if cap1 >= 21000 and cap1 <= 50000:
        return 'green'

def markerColorChangeRed():
    if cap2 >= 51000 and cap2 <= 80000:
        return 'red'

def markerColorChangePurple():
    if cap3 >= 81000 and cap3 <= 100000:
        return 'purple'

def markerColorChangeBlack():
    if cap4 > 100000:
        return 'black'

html = """
Stadium Name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Capacity: %s
"""

map = folium.Map(location=[33.18, -86.82], zoom_start=5, titles="Staemen Terrain")

fg1 = folium.FeatureGroup(name="NCAA Football stadium less than 20,000 capacity")

for lat, lon, cap, name in zip(lat, lon, cap, name):
    iframe = folium.IFrame(html=html % (name, name, cap),  width=200, height=100)
    fg1.add_child(folium.CircleMarker(location=[lat, lon], radius=8, popup=folium.Popup(iframe), fill_color=markerColorChangeBlue(), color = "transparent",  fill_opacity=1.0))

fg2 = folium.FeatureGroup(name="NCAA Football Stadiums with 21,000 to 50,000 capacity")

lat1 = list(data["latitude"])
lon1 = list(data["longitude"])
cap1 = list(data["capacity"])
name1 = list(data["stadium"])

for lat1, lon1, cap1, name1 in zip(lat1, lon1, cap1, name1):
    iframe = folium.IFrame(html=html % (name1, name1, cap1),  width=200, height=100)
    fg2.add_child(folium.CircleMarker(location=[lat1, lon1], radius=8, popup=folium.Popup(iframe), fill_color=markerColorChangeGreen(), color="transparent", fill_opacity=1.0))

fg3 = folium.FeatureGroup(name="NCAA Football Stadiums with 51,000 to 80,000 capacity")

lat2 = list(data["latitude"])
lon2 = list(data["longitude"])
cap2 = list(data["capacity"])
name2 = list(data["stadium"])

for lat2, lon2, cap2, name2 in zip(lat2, lon2, cap2, name2):
    iframe = folium.IFrame(html=html % (name2, name2, cap2),  width=200, height=100)
    fg3.add_child(folium.CircleMarker(location=[lat2, lon2], radius=8, popup=folium.Popup(iframe), fill_color=markerColorChangeRed(), color="transparent", fill_opacity=1.0))

fg4 = folium.FeatureGroup(name="NCAA Football Stadiums with 81,000 to 100,000 capacity")

lat3 = list(data["latitude"])
lon3 = list(data["longitude"])
cap3 = list(data["capacity"])
name3 = list(data["stadium"])

for lat3, lon3, cap3, name3 in zip(lat3, lon3, cap3, name3):
    iframe = folium.IFrame(html=html % (name3, name3, cap3),  width=200, height=100)
    fg4.add_child(folium.CircleMarker(location=[lat3, lon3], radius=8, popup=folium.Popup(iframe), fill_color=markerColorChangePurple(), color="transparent", fill_opacity=1.0))

fg5 = folium.FeatureGroup(name="NCAA Football Stadiums with 100,000+ capacity")

lat4 = list(data["latitude"])
lon4 = list(data["longitude"])
cap4 = list(data["capacity"])
name4 = list(data["stadium"])

for lat4, lon4, cap4, name4 in zip(lat4, lon4, cap4, name4):
    iframe = folium.IFrame(html=html % (name4, name4, cap4),  width=200, height=100)
    fg5.add_child(folium.CircleMarker(location=[lat4, lon4], radius=8, popup=folium.Popup(iframe), fill_color=markerColorChangeBlack(), color="transparent", fill_opacity=1.0))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(fg3)
map.add_child(fg4)
map.add_child(fg5)
map.add_child(folium.LayerControl())
map.save("Map1.html")
