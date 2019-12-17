import folium 
import os

if __name__ == "__main__":
    center = [26.519608, 80.232266]
    zoom = 20
    map = folium.Map(location = center, zoom_start = zoom )
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    
    for i in range (1,num_coords+1):
        lat,lon = list_words[i].split(' ')
        print(lat)
        print(lon)
        folium.Marker([lat, lon], popup = lat + ", " + lon).add_to(map) 
    
    map.save(os.path.expanduser('~')+'/.ros/router/map.html')