import requests
import datetime as dt
import smtplib

MY_LAT = -53.792240
MY_LONG = 75.134850

my_email = "robwalker8280@gmail.com"
password = 'blank'
to_addrs = 'robwalker2106@gmail.com'

now = dt.datetime.now()

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_lat = float(response.json()["iss_position"]['latitude'])
iss_lng = float(response.json()["iss_position"]['longitude'])

lat_diff = abs(iss_lat) - abs(MY_LAT)
lng_diff = abs(iss_lng) - abs(MY_LONG)

response = requests.get(url='http://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
sunrise = int(response.json()['results']['sunrise'].split('T')[1].split(":")[0])
sunset = int(response.json()['results']['sunset'].split('T')[1].split(":")[0])

in_the_sky = lat_diff <= 5 and lng_diff <= 5
right_time = sunrise > now.hour > sunset

if in_the_sky and right_time:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_addrs,
                            msg=f"Subject:Find the ISS\n\nLook up into the sky. The ISS is near.")
