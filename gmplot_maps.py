import gmplot
import os
if __name__ == "__main__":
    #Required variables. Please refer to the README to know what each variable does     
    center = [26.519608, 80.232266]
    zoom = 20
    size = 10

    #Opening gps.txt and reading the coordinates. num_coords specifies the number of points to marks    
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])

    #Constructing the list of latitudes and longitudes
    latitude_list = []
    longitude_list = []
    for i in range (1,num_coords+1):
        lat,lon = list_words[i].split(' ')    
        latitude_list.append(float(lat))
        longitude_list.append(float(lon))

    #Plotting the map with the requisite markers and storing it
    gmap = gmplot.GoogleMapPlotter(center[0], center[1], zoom) 
    gmap.scatter( latitude_list, longitude_list, '# FF0000', size, marker = False ) 
    gmap.draw(os.path.expanduser('~')+'/.ros/router/map.html') 