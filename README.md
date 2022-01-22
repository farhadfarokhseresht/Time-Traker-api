# Time-Traker-api
### An simpel example of ( https://clockify.me/ )  REST-based API

you can (Add,Get all or Get a specific,Update,Delete) data by this api cod

#### request parameters
#
| parameter | more | type |
| ------ | ------ |------ |
| description | Optional | string |
| billable |True or Fals , Optional , default=Fals | Boolean |
| start_at | like : 2022-01-23 14:29:00 | date time
| end_at | Should be less than #start_at | date time
| pk | necessary | integer
---
## Add a new time entry
to add new time tracker to data base
##### path : 
##### 127.0.0.1:8000/time_tracker
#
#####  method : POST
######  body exampel :
#
```{
    {"description": "Writing documentation",
    "billable": "True",
    "start_at": "2022-01-22 15:29",
    "end_at": "2021-01-23 14:29"}
```
---
## Get all time entry
return an dictionary of all time entry
##### path : 
##### 127.0.0.1:8000/time_tracker
#
#####  method : GET
---
## Get specific time entry
find and return specific time entry from data base with id = pk
##### path : 
##### 127.0.0.1:8000/time_tracker/pk
#
#####  method : GET
---
## Stop currently running timer
stop running timer with id = pk 
##### path : 
##### 127.0.0.1:8000/time_tracker/pk
#
#####  method : PATCH
---
## Delete time entry
Delete time entry with id = pk 
##### path : 
##### 127.0.0.1:8000/time_tracker/pk
#
#####  method : DELETE
---
## Update time entry 
Update time entry with id = pk 
##### path : 
##### 127.0.0.1:8000/time_tracker/pk
#
#####  method : PUT
######  body exampel :
#
```{
    {"description": "Writing documentation",
    "billable": "True",
    "start_at": "2022-01-22 15:29",
    "end_at": "2021-01-23 14:29"}
```
## Installation

Dillinger requires Python 3 to run.

open CMD , go to your dir and type
```sh
git clone https://github.com/farhadfarokhseresht/Time-Traker-api.git
#after Download go to proj directory and type in your CMD :
python manage.py runserver
#use Postman app
```



