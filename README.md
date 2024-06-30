# FASTAPI_URL_SHORTENER

This is a simple shortener for urls 

## Using
To use it first you must load post request:

POST `http://ip:port/shorten/` 

Payload `{"url": "foo.bar"}`

Response `{"short_url": "rAnDv"}`

To get redirection to the original site you just type it in

GET `http://ip:port/rAnDv/` 

Response 308 -> GET `http:///foo.bar`


### Installing 

```shell
python -m venv venv
pip install -r requirements.txt
```
---
### Runnning

Linux
```shell
chmod +x ./run.sh
./run.sh
```
---

Windows
```cmd
./run.sh
```
---