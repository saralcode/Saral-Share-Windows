# import asyncio
# import requests, netifaces, socket

# def checkConnection():
#     try:
#         gateways = netifaces.gateways()
#         print(gateways)
#         default_gateway = gateways['default'][netifaces.AF_INET][0]
#         return default_gateway
#     except:
#         return None


# address = None
# ip=""
# a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# async def checkPort():
#     data = a_socket.connect_ex(("192.168.131.147", 8081))
#     print(data)

# asyncio.run(checkPort())
# # data =  requests.get("http://192.168.131.147:8080")
# # print(data.status_code)
# import requests

import os
print(os.path.join(os.getenv("APPDATA"), "Saral Share", "myqr.png"))
# requests.get("http://")