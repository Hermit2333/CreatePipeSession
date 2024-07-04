import requests


headers = {'Content-Type':'application/x-www-form-urlencoded'}
client_id = "fbfc1037-1b63-4a0e-91f0-b2e49422d158"
scope = "files.readwrite offline_access"
redirect_uri = "http://localhost"
client_secret = "bSP8Q~WMox1sBjbHJsnRgDAwbbai5SwO3T4b_avv"


# GET https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={client_id}&scope={scope}&response_type=code&redirect_uri={redirect_uri}
login_link = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_id={client_id}&scope={scope}&response_type=code&redirect_uri={redirect_uri}"
print(login_link)


# code="M.C519_BL2.2.U.e3b98194-1bb5-5af2-8ce7-355dc340667c"

# response = requests.post(
#     'https://login.microsoftonline.com/consumers/oauth2/v2.0/token',
#     data={
#         'client_id': client_id,
#         'redirect_uri': redirect_uri,
#         'client_secret': client_secret,
#         'code': code,
#         'grant_type': 'authorization_code'
#     },
#     headers=headers)

# response                # <Response [200]>
# eval(response.content)


# refresh_token = eval(response.content)['refresh_token']
# refresh_token = 'M.C519_BL2.0.U.-CsPqv0NvyMuZd9oMEll3JeQcZN6BtvCoNxocboSaCgdjiiLQnnXjAgMUr8wrTibhrenIgHE56YHm*DZKW6OKWJl25Oe6vRpve50hIbGClGMe8hSN511708yYGVQA**S60EWwAPe*lYcmr0!CgZc9QfKlckEF6G9y3ed4SLmcHIhteP5Bs5KROB9oR6dTBEswxiaEgCKeU4dqhQUF6fmAH6AuLUFvZ*PluZ24Bqh*wL1yrG7wWhdvkS7J*TPBw63bXQ3S*vPCTU54M0CG3q8uhGveb6a!1Ln*A49txFsmOhbSDLBuaqbNgDDT4v4xFiha1BOSE*EEeujguxv3fi36Jik$'
# response_refresh = requests.post(
#     'https://login.microsoftonline.com/consumers/oauth2/v2.0/token',
#     data = {
#         'client_id': client_id,
#         'redirect_uri': redirect_uri,
#         'client_secret': client_secret,
#         'refresh_token': refresh_token,
#         'grant_type': 'refresh_token'
#     },
#     headers = headers)

# response_refresh        # <Response [200]>
# eval(response_refresh.content)

# b'{"token_type":"Bearer","scope":"Files.ReadWrite","expires_in":3600,"ext_expires_in":3600,"access_token":"EwBoA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AAaL4RM42OYf5JTreaeiU4n8ytoFuuDE3LUin3zGFh7VwrK+B/64E3/raljFVGhcWiN6Kl4aP27aRPEMyFDUf5BcJjLh8U9l67goM8kY/hzAZE7JPtDFjMoFbaYiS0fpsqTkjUw6B05+VWO1ens/0u2Tga/unEOoL7UsWETmKtmRRj9bBk72F/nvmkuuEvUWnxJ+aEwRxtJq6DrRgjoaqEUa2hbWoP6F5TQj8gMncUOSlYK4pGXhzdMAf5z1a148PaJ6R1UllKmKS/U3U4wZ+UlVnYd/Ctkr9uOjIECME977v4oL84G0py4GjmSsiwD+OTcwbbicZ/dvj4Y0CkEl1eTkDZgAACGakVHtsPJJeOAKjy2ETLgSU+XfPKGQnHSDXb5V1POfSw1RV7kgR0PoB9ttDkcPd7OFaMk/f0huVirW76HxrA1QpD66CVdi0PHJ1zHDLHKJUpOhwzJV4DslSWNP0SRMLMjo5WX+suM5Ogqbq9WuTjkM0kZyGgXVJakHcIqR70K6L8y8a6bZ0ftKHB4uOJCafef2qqvmm27viB9JLW3bDdN3xdjuPymt60Ryl9190WtTe5daWrTBZRSSUyoASHLof4/+lA26lgXIumrpRJKsBqNnO60g6gZEXRhtCLg96b7NgMnMNnlM3gV1+zZlKKAUuGb88RtukPIipp2EZPEOeA9/nSV7DliCZI6X2M1v+qej0Mi/4LNGdL0qKrWC3JxYJwXZCVNeBes0DEIagPCNl93gJQWmm/9/X2ipkikg86duD65B9PQFmYACPNqZRCo//tbf35AzxJeWRYjxAPIkgmgEO+ifYArV6a34KnQRLrvQPQAf1YAOvtJFhDimtMb1h8P6EOON11ke/RRwKYz5GogQ6HHzFkWBY2m2ewK0MWRI29CvmAR4brwLS91ozztKu9CdEA4c/QmpwAwZ8V8ZQktxn3EeCGA0rgKWHo60YyNwKsGlYGkdqGF4CuVFsthBNX6+/QugJ6tojkVaRvu4evvmiBBPgcDFG28z52HTihf3mIOAuMAnd+qCkw8gNcplJIrmTaV+Xw8FddG2iPy/RZTCQnQ8euQk7B7nslG6VAezhRlAaSIX+rB+p5GIFkEBBaucGfgI=","refresh_token":"M.C519_SN1.0.U.-CqCeBbEIqxaqWbymmCVrzFFHdkiRntO*IGTIdNLog8FUZn*f*cKyvIalcCzWd3x6sEH3OZ7sovf9lE9eqAecOqtdX6*8SYDARrKv2HI6i5O757FY9yMBDYUkytPFYQ4cOTpnP4vu3uy3BH1BjPGJO3WRQpC8rX80HZElWTjE60DOcoHgXVNYKlFwfzPwUSoYOOCDiq1mQU0wWByAI6*aRgggnpbZbaBHz!uoctTQYSmmVbdxOSsC3cj9WTWdKzNKDwTLQcNaOGK08EINr7iXqNHHW2Lr911SxL*iaz6XkBbUxOmz0Lsmyz79Ya0fXR8cUlPSjNIjsls7YBGU!ZOZHMY$"}'


# {
#     "token_type": "Bearer",
#     "scope": "Files.ReadWrite",
#     "expires_in": 3600,
#     "ext_expires_in": 3600,
#     "access_token": "EwBoA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AAaL4RM42OYf5JTreaeiU4n8ytoFuuDE3LUin3zGFh7VwrK+B/64E3/raljFVGhcWiN6Kl4aP27aRPEMyFDUf5BcJjLh8U9l67goM8kY/hzAZE7JPtDFjMoFbaYiS0fpsqTkjUw6B05+VWO1ens/0u2Tga/unEOoL7UsWETmKtmRRj9bBk72F/nvmkuuEvUWnxJ+aEwRxtJq6DrRgjoaqEUa2hbWoP6F5TQj8gMncUOSlYK4pGXhzdMAf5z1a148PaJ6R1UllKmKS/U3U4wZ+UlVnYd/Ctkr9uOjIECME977v4oL84G0py4GjmSsiwD+OTcwbbicZ/dvj4Y0CkEl1eTkDZgAACGakVHtsPJJeOAKjy2ETLgSU+XfPKGQnHSDXb5V1POfSw1RV7kgR0PoB9ttDkcPd7OFaMk/f0huVirW76HxrA1QpD66CVdi0PHJ1zHDLHKJUpOhwzJV4DslSWNP0SRMLMjo5WX+suM5Ogqbq9WuTjkM0kZyGgXVJakHcIqR70K6L8y8a6bZ0ftKHB4uOJCafef2qqvmm27viB9JLW3bDdN3xdjuPymt60Ryl9190WtTe5daWrTBZRSSUyoASHLof4/+lA26lgXIumrpRJKsBqNnO60g6gZEXRhtCLg96b7NgMnMNnlM3gV1+zZlKKAUuGb88RtukPIipp2EZPEOeA9/nSV7DliCZI6X2M1v+qej0Mi/4LNGdL0qKrWC3JxYJwXZCVNeBes0DEIagPCNl93gJQWmm/9/X2ipkikg86duD65B9PQFmYACPNqZRCo//tbf35AzxJeWRYjxAPIkgmgEO+ifYArV6a34KnQRLrvQPQAf1YAOvtJFhDimtMb1h8P6EOON11ke/RRwKYz5GogQ6HHzFkWBY2m2ewK0MWRI29CvmAR4brwLS91ozztKu9CdEA4c/QmpwAwZ8V8ZQktxn3EeCGA0rgKWHo60YyNwKsGlYGkdqGF4CuVFsthBNX6+/QugJ6tojkVaRvu4evvmiBBPgcDFG28z52HTihf3mIOAuMAnd+qCkw8gNcplJIrmTaV+Xw8FddG2iPy/RZTCQnQ8euQk7B7nslG6VAezhRlAaSIX+rB+p5GIFkEBBaucGfgI=",
#     "refresh_token": "M.C519_SN1.0.U.-CqCeBbEIqxaqWbymmCVrzFFHdkiRntO*IGTIdNLog8FUZn*f*cKyvIalcCzWd3x6sEH3OZ7sovf9lE9eqAecOqtdX6*8SYDARrKv2HI6i5O757FY9yMBDYUkytPFYQ4cOTpnP4vu3uy3BH1BjPGJO3WRQpC8rX80HZElWTjE60DOcoHgXVNYKlFwfzPwUSoYOOCDiq1mQU0wWByAI6*aRgggnpbZbaBHz!uoctTQYSmmVbdxOSsC3cj9WTWdKzNKDwTLQcNaOGK08EINr7iXqNHHW2Lr911SxL*iaz6XkBbUxOmz0Lsmyz79Ya0fXR8cUlPSjNIjsls7YBGU!ZOZHMY$"
# }


access_token = "EwBoA8l6BAAUbDba3x2OMJElkF7gJ4z/VbCPEz0AAaL4RM42OYf5JTreaeiU4n8ytoFuuDE3LUin3zGFh7VwrK+B/64E3/raljFVGhcWiN6Kl4aP27aRPEMyFDUf5BcJjLh8U9l67goM8kY/hzAZE7JPtDFjMoFbaYiS0fpsqTkjUw6B05+VWO1ens/0u2Tga/unEOoL7UsWETmKtmRRj9bBk72F/nvmkuuEvUWnxJ+aEwRxtJq6DrRgjoaqEUa2hbWoP6F5TQj8gMncUOSlYK4pGXhzdMAf5z1a148PaJ6R1UllKmKS/U3U4wZ+UlVnYd/Ctkr9uOjIECME977v4oL84G0py4GjmSsiwD+OTcwbbicZ/dvj4Y0CkEl1eTkDZgAACGakVHtsPJJeOAKjy2ETLgSU+XfPKGQnHSDXb5V1POfSw1RV7kgR0PoB9ttDkcPd7OFaMk/f0huVirW76HxrA1QpD66CVdi0PHJ1zHDLHKJUpOhwzJV4DslSWNP0SRMLMjo5WX+suM5Ogqbq9WuTjkM0kZyGgXVJakHcIqR70K6L8y8a6bZ0ftKHB4uOJCafef2qqvmm27viB9JLW3bDdN3xdjuPymt60Ryl9190WtTe5daWrTBZRSSUyoASHLof4/+lA26lgXIumrpRJKsBqNnO60g6gZEXRhtCLg96b7NgMnMNnlM3gV1+zZlKKAUuGb88RtukPIipp2EZPEOeA9/nSV7DliCZI6X2M1v+qej0Mi/4LNGdL0qKrWC3JxYJwXZCVNeBes0DEIagPCNl93gJQWmm/9/X2ipkikg86duD65B9PQFmYACPNqZRCo//tbf35AzxJeWRYjxAPIkgmgEO+ifYArV6a34KnQRLrvQPQAf1YAOvtJFhDimtMb1h8P6EOON11ke/RRwKYz5GogQ6HHzFkWBY2m2ewK0MWRI29CvmAR4brwLS91ozztKu9CdEA4c/QmpwAwZ8V8ZQktxn3EeCGA0rgKWHo60YyNwKsGlYGkdqGF4CuVFsthBNX6+/QugJ6tojkVaRvu4evvmiBBPgcDFG28z52HTihf3mIOAuMAnd+qCkw8gNcplJIrmTaV+Xw8FddG2iPy/RZTCQnQ8euQk7B7nslG6VAezhRlAaSIX+rB+p5GIFkEBBaucGfgI="

# 上传小文件
# PUT /me/drive/items/{item-id}/content
# 要上传的文件路径
 
# 上传的目标路径，例如：'/drive/root:/new_file_name.txt'
target_path = 'drive/root:/file.txt'
file_path = 'C:/Users/x/Desktop/OneDrive/file.txt'
 
# 读取文件内容
with open(file_path, 'rb') as f:
    file_content = f.read()
 
# 上传文件
upload_url = f'https://graph.microsoft.com/v1.0/me/drive/items/root:/file.txt:/content'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/octet-stream'
}
response = requests.put(upload_url, data=file_content, headers=headers)

if response.status_code == 200:
    print('File uploaded successfully')
else:
    print('Error uploading file:', response.json())