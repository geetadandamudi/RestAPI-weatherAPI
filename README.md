# RestAPI-weatherAPI

**http://35.160.72.172:5000/historical/** - To see all the dates in the database    
**http://35.160.72.172:5000/historical/20130101** - To see information about a particular date like maximum and minimum temperature.    
**http://35.160.72.172:5000/historical/20170505,29,14** - To insert information about a particular date    
**http://35.160.72.172:5000/historical/delete/20170505**  -  To delete the information about a particular date    

**Tools: Flask, python, sqlite **

1. Run app.py on public IP and the URL for it is <ip-address>:5000  
2. **/historical/** - all dates and their information. 
3. **/historical/date** - GET method will return information about that particular date. 
4. **/historical/date,tmax,tmin** - Inserts information about a new date into database.
5. **/historical/date** - Delete method will delete the information about that particular date.  

Run it on your browser by clicking above links.

