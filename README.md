# Climate-watch

## Setup

### Hardware
- Set up adafruit IO account
- Set up your device in io.  Add your sensors (mine is Adafruit ESP32-S2 TFT Feather, BME280 and PMSA003I)
- Update feeds to stream every 30 seconds

### Software
- Set up virtual enviroment (run 'source venv/bin/activate' prior to running)
- Install all libs, make migrations etc.
- Run 'python3 manage.py runserver 0.0.0.0:8000'
- In web browser navigate to localhost:8000/airquality

## Changes Required For You To Use
You need to put your credentials here: https://github.com/Jeff-Danowski/climate-watch/blob/cd1183e5c22f726b34bbe8012d041273c084ebe2/climatewatch/airreport/models.py#L46 and update your feed names to retrieve your sensor name. 
