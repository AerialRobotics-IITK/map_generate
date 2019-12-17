import requests
import os

if __name__ == "__main__":
    api_key = "your-api-key-goes-here"
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    center = "26.519608, 80.232266"
    zoom = "20"
    size = "400x400"
    final_url = url+"center="+center+"&zoom="+zoom+"&size="+size
    
    f = open(os.path.expanduser('~') + '/.ros/router/gps.txt')
    text = f.read()
    list_words = text.split('\n')
    num_coords = (int)(list_words[0])
    
    for i in range (1,num_coords+1):
        lat,lon = list_words[i].split(' ')
        final_url = final_url + "&markers=label:" + str(i) + "%7C"+str(lat)+","+str(lon)
    
    final_url = final_url+"&key="+api_key
    final_img = requests.get(final_url)
    img = open (os.path.expanduser('~')+'/.ros/router/map.png', 'wb')
    img.write(final_img.content)
    img.close()

    
