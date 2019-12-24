import requests
import os

if __name__ == "__main__":
    #Sample URL := https://dev.virtualearth.net/REST/v1/Imagery/Map/imagerySet?pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsAPIKey}
    
    #Required variables. Please refer to the README to know what each variable does 
    api_key = "your-api-key-goes-here"
    center = "26.519608,80.232266"
    pin_style = "50"
    zoom = "19"
    size = "2000,1500"

    #Constructing the URL
    url = "https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/"
    final_url = url + center + "/" + zoom + "?mapSize="+size 

    #Opening gps.txt and reading the coordinates. num_coords specifies the number of points to marks
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    
    for i in range (1,num_coords+1):
        #Adding a pushpin marker for each point with the requisite latitude and longitude
        lat,lon = list_words[i].split(' ')
        final_url = final_url + "&pushpin=" + lat + "," + lon + ";" + pin_style + ";B" + str(i)
    
    #Getting and writing the final image
    final_url = final_url + "&key=" + api_key
    final_img = requests.get(final_url)
    img = open (os.path.expanduser('~')+'/.ros/router/map.jpg', 'wb')
    img.write(final_img.content)
    img.close()
    print (final_url)

    
