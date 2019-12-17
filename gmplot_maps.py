import gmplot
import os
if __name__ == "__main__":
    center = [26.519608, 80.232266]
    zoom = 20
    size = 10
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    latitude_list = []
    longitude_list = []
    for i in range (1,num_coords+1):
        lat,lon = list_words[i].split(' ')    
        latitude_list.append(float(lat))
        longitude_list.append(float(lon))
    gmap3 = gmplot.GoogleMapPlotter(center[0], center[1], zoom) 

    gmap3.scatter( latitude_list, longitude_list, '# FF0000', size, marker = False ) 
    
    gmap3.draw(os.path.expanduser('~')+'/.ros/router/map.html') 