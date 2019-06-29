from pyroutelib3 import Router
import folium
import webbrowser

# creation de la carte
latD, lonD=48.58626, 7.75246  # Depart : pont du Theatre
latA, lonA=48.58167, 7.75048   # Arrivee : Cathedrale
c = folium.Map(location = [(latA+latD)/2, (lonA+lonD)/2], zoom_start=17) #carte centree

# position depart et arrivee
folium.Marker((latD, lonD),popup = "Depart", icon=folium.Icon(
	color = 'green', icon ='home')).add_to(c)
folium.Marker((latA,lonA),popup = "Arrivee", icon=folium.Icon(
	color = 'blue', icon = 'eye-open')).add_to(c)

# itineraire "optimal" apec pyroutelib3
router = Router("foot") # cycle, foot, horse, tram, train , car
depart = router.findNode(latD, lonD) 
arrivee = router.findNode(latA, lonA)
status, route = router.doRoute(depart, arrivee)
if status == 'success':
	routeLatLons = list(map(router.nodeLatLon, route))
	folium.PolyLine(routeLatLons, color="red", weight=2.5, opacity=1).add_to(c)

# sauvegarde et affichage de la carte
c.save('cartev0.42.html')
webbrowser.open('cartev0.42.html')
