# WEATHER APP
       A weather app which updates the weather details in the database once in 24 hours.



# Getting Started
     The main idea behind or project is we need to check whether the city weather is in db,if not then add it and updates once in 24 hours

## Technologies

    Project is created with:
    LANGUAGE: Python-3.8.3
    EDITOR: visual studio code
    DATABASE:sqlite3
    WEATHER:openweatherapi



## Launch

	steps to run the project :
python apps.py  

url=**[http://localhost:5000/]**


	1.The user needs to open the default browser and enter the url given above

	2.Now the user needs to enter the city name.
	  It will redirect us to another page where the weather details of the city is shown.
	  
	3.Now it is stored in the database.db file.
	  if we click the home link it will redirect us to the home page.

	4.If we enter the same city name as again
	  it will check for time difference.
	  
	5.If the difference exceeds 24 hrs it will check the weather details again for the same city.
	  Then update the details in the same db id.

