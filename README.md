# Django_Assignment
This code implements rest api using django rest framework. This rest api uses sqllite as it's backend database. 
Following table structure is used for the same: -
id (auto increment)
name (string)
price (float)
available (string)

It is deployed on AWS elastic beanstalk. Below is the home url for the application:-
http://djangorestapi-env-1.eba-gnnu5cev.us-east-2.elasticbeanstalk.com/app/home/

Following are the urls for GET and POST requests:-
http://djangorestapi-env-1.eba-gnnu5cev.us-east-2.elasticbeanstalk.com/app/hotel_list/ 
And below is the sample POST request:-
{
	"name" : "MARRIOT",
	"price" : 270.00,
	"available" : "NO"
}

Below is the url for getting hotel details with id as filter in the url:-
http://djangorestapi-env-1.eba-gnnu5cev.us-east-2.elasticbeanstalk.com/app/hotel_list/1

