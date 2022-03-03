# Django_Assignment
This code implements rest api using django rest framework. This rest api uses sqllite as it's backend database. 
Following table structure is used for the same: -
id (auto increment)
name (string)
price (float)
available (string)

1) Below is the home page for the app which prints "Hello Canada"
http://127.0.0.1:8000/app/home/

2) Below is the GET request url to fetch all the hotels from backend database
http://127.0.0.1:8000/app/hotel_list/

3)Below is the sample POST request and url is same as GET request:-
{
	"name" : "MARRIOT",
	"price" : 270.00,
	"available" : "NO"
}
This will create entry for this hotel in the backend table, which can then be viewed using GET request

4) Below is the url for GET request with 'id' as a url parameter
5) http://127.0.0.1:8000/app/hotel_list/1

