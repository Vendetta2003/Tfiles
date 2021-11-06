#this file is to try out visual studio web
import requests
response = requests.get("https://www.google.com/search?q=Challenge&rlz=1C1RLNS_enIN955IN955&oq=Challenge&aqs=chrome..69i57j0i67i433l2j46i512j0i67j69i60l2j69i61.1176j0j7&sourceid=chrome&ie=UTF-8")
print(response.headers)