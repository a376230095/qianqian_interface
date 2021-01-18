#-*- coding: utf-8 -*-
from pprint import pprint

import requests

url="https://auth-test.dapengjiaoyu.cn/account-login?redirect_url=https%3A%2F%2Fauth-test.dapengjiaoyu.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Db4cd9c34%26redirect_uri%3D%2F%2Ftest.dapengjiaoyu.cn%2Fdp-course%2Fcallback%26state%3D1"
data={
    "type":"USERNAME",
    "source":"NORMALLOGIN",
    "pointerValue":"PASSWORD;Win",
    "account":"13172661165",
    "password":"tongtong"
}
headers={
"Origin":"https://auth-test.dapengjiaoyu.cn",
"Referer":"https://auth-test.dapengjiaoyu.cn/login?redirect_url=https%3A%2F%2Fauth-test.dapengjiaoyu.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Db4cd9c34%26redirect_uri%3D%2F%2Ftest.dapengjiaoyu.cn%2Fdp-course%2Fcallback%26state%3D1"
}
s = requests.session()
res=s.post(url=url,data=data)

# pprint(res.headers)
url="https://test.dapengjiaoyu.cn/api/favorites"
headers=s.headers.update({"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJranY3cWh0aGluIiwib3JpZ2luIjp7InN0YXR1cyI6IkFjY291bnRWZXJpZmljYXRpb24iLCJtc2ciOiLotKblj7flt7Lpqozor4EiLCJ1c2VycyI6W3sidXNlcklkIjoia2p2N3FodGhpbiIsInR5cGUiOiJNT0JJTEUiLCJhY2NvdW50IjoiMTMxKioqKioqNjUiLCJtb2JpbGUiOiIxMzEqKioqKio2NSIsImxvZ2luTmFtZSI6bnVsbCwibmlja05hbWUiOiJkcDk5NDUxOTk2Iiwic3BhcmU0IjoiZHA5OTQ1MTk5NiIsImF2YXRhciI6Imh0dHBzOi8vaW1hZ2UuZGFwZW5namlhb3l1LmNuL2ltYWdlcy9hdmF0YXJzLzU2YXZhdGFyLmpwZyIsInNjaG9vbCI6bnVsbH1dfSwic2NvcGUiOlsicmVhZCIsIndyaXRlIl0sImV4cCI6MTYxMTE1NDg4MSwiYXV0aG9yaXRpZXMiOlsiVVNFUiJdLCJqdGkiOiJlZTNjZWExMi0xOWY2LTRhYzEtOTUxMi03NTg5OTUzNzc4YzciLCJjbGllbnRfaWQiOiJiNGNkOWMzNCJ9.eWNBXbU_cGJAd3UP66abIJCQ-M1xomQHUNqro3Zsr1VfTLqfGIWmNmJD7RR_HvOTN8r7lxLw7q6tlCG7I8KA9XpRVMMvorKrnP6TukYN54yYWV4tUakgOWGDYsH0Bn-06a-jAkf7Grmua45wQZKKQwdB1dsVilWLrNA5iocwDRLDMoaqiSCXunvrbKKcYO2vX9fRZ39FtPuerO09fKh9l4NEdhVrS3sSYi6Z3vfAQp1szf8ATOxixVPFwKKKUhjtHvVXQE8hMNGFpST18c5b2EHv7SjWeG2y6dXVs7WMZUlUFQb_e7c7gaxP-PP3o_WCBkc-tvviH_Gvo-yrtYLVSQ"})
data={"contentType":"TEXT","id":"bc2d116b03a146adbf2c6a70ad4b8b3a","createdId":"k12ygbm1ow","type":"HOMEWORK"}
res=s.post(url=url,json=data)
print(res.text)