### Project Description
To make an API to fetch latest videos sorted in reverse chronological order of their 
publishing date-time from YouTube for a given tag/search query in a paginated response.

### API Information
 - To get all videos: http://localhost:8000/api/getStoredVediosData/?q=&page=1
 - To search with a query along with pagination: http://localhost:8000/api/searchStoredVediosData/?title=<Anytitle>&description=<AnyDesciption>&page=1

 ### How To Run The Application Manually
  - Create a .env file in the same directory in which settings.py resides.
  - In the .env file creat a variable named API_KEYS and assign your api keys obtained from google developer console
  - Example API_KEYS = testAPIKey1,testAPIKey2,testAPIKey3 Make sure you are not adding any extra spaces not double qoutes or single qoutes required for it.
  - Create a directory named logs. It should be in the top level directory where requirements.txt and manage.py is residing.

  - On windows
       - `pip install -r requirements.txt`
       - `python manage.py migrate`
       - `python manage.py runserver --noreload`

  - On Mac/ubuntu/linux
       - `pip3 install -r requirements.txt`
       - `python3 manage.py migrate`
       - `python3 manage.py runserver --noreload`

### How to Run Using Dcoker
    - `docker-compose run web python manage.py migrate` 
    - `docker-compose build`
    - `docker-compose up`

