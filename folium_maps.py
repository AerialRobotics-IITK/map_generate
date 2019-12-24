import folium 
import os

if __name__ == "__main__":
    #Required variables. Please refer to the README to know what each variable does     
    center = [26.519608, 80.232266]
    zoom = 20

    #Constructing folium map object
    map = folium.Map(location = center, zoom_start = zoom )

    #Opening gps.txt and reading the coordinates. num_coords specifies the number of points to marks    
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    
    for i in range (1,num_coords+1):
        #Adding a pushpin marker for each point with the requisite latitude and longitude
        lat,lon = list_words[i].split(' ')
        print(lat,lon,sep=' ')
        folium.Marker([lat, lon], popup = lat + ", " + lon).add_to(map) 
    
    #Saving the map
    map.save(os.path.expanduser('~')+'/.ros/router/map.html')