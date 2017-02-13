# bikekeeper
A python script designed for Ubuntu to remind you when you leave your bike in the rain.

## use
create a cronjob (`crontab -e`, see http://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) to run the following command: 

`python pubscraper.py city_id api_key`

Where city id is the city id of your location found here: http://openweathermap.org/help/city_list.txt, and api_key is your free api key to the openweathermap.org's 5 day/3 hour forecast service.

Make sure to space your cron jobs enough that you aren't requesting data more than once every ten minutes.
