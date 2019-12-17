import requests
import os

if __name__ == "__main__":
    #https://dev.virtualearth.net/REST/v1/Imagery/Map/imagerySet?pushpin={pushpin_1}&pushpin={pushpin_2}&pushpin={pushpin_n}&mapLayer={mapLayer}&format={format}&mapMetadata={mapMetadata}&key={BingMapsAPIKey}
    api_key = "your-api-key-goes-here"
    url = "https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/"
    center = "26.519608,80.232266"
    pin_style = "71"
    zoom = "19"
    size = "2000,1500"
    final_url = url + center + "/" + zoom + "?mapSize="+size 
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    
    for i in range (1,num_coords+1):
        lat,lon = list_words[i].split(' ')
        final_url = final_url + "&pushpin=" + lat + "," + lon + ";" + pin_style + ";B" + str(i)
    
    final_url = final_url + "&key=" + api_key
    final_img = requests.get(final_url)
    img = open (os.path.expanduser('~')+'/.ros/router/map.jpg', 'wb')
    img.write(final_img.content)
    img.close()
    print (final_url)

    
