<center> <h1>AirBnB clone - MySQL</h1> </center>

This repository  involves creating an AirBnB clone with MySQL integration using Python and Object-Oriented Programming (OOP) principles. The implementation encompasses unit testing, *args and **kwargs usage, MySQL database setup, ORM mapping, and the management of two storage engines (FileStorage and DBStorage) with the flexibility to switch between them using environment variables. 

---

<center><h3>Project Tasks</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Fork me if you can! | [AirBnB_clone_v2](https://github.com/germanchuks/AirBnB_clone_v2), [README.md](https://github.com/germanchuks/AirBnB_clone_v2/tree/master/README.md), [AUTHORS](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/AUTHORS) | Forked codebase, updated Readme file and project Authors |
| 1: Bug free! | N/A | Unittests must pass without any errors with each storage engine |
| 2: Console improvements | [console.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/console.py), [/models/](https://github.com/germanchuks/AirBnB_clone_v2/tree/master/models), [tests/](https://github.com/germanchuks/AirBnB_clone_v2/tree/master/tests) | Improve `do_create` method in the command interpreter to allow object creation with given parameters in a specified syntax, including support for strings, floats, and integers. |
| 3. MySQL setup development | [setup_mysql_dev.sql](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/setup_mysql_dev.sql) | Sets up a MySQL server for a project (development) |
| 4. MySQL setup test | [setup_mysql_test.sql](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/setup_mysql_test.sql) | Sets up a MySQL server for a project (test) |
| 5. Delete object | [/models/engine/file_storage.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Add new public instance method `delete(self, obj=None)` to remove the specified object from __objects if it exists, and update the prototype of the existing method `all(self)` to `all(self, cls=None)` allowing optional class filtering |
| 6. DBStorage - States and Cities | [/models/base_model.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/base_model.py), [/models/city.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/city.py), [/models/state.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/state.py), [/models/engine/db_storage.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/engine/db_storage.py), [/models/_ _init_ _.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/__init__.py) | Update `BaseModel` by creating Base = declarative_base(). Modify `City` and `State` to inherit from BaseModel and Base, define or replace class attributes, and set table names. Create `DBStorage` with private class attributes, and public instance methods for initialization, querying, adding, saving, deleting, and reloading. Update `__init__.py` in models to instantiate either DBStorage or FileStorage based on `HBNB_TYPE_STORAGE`. |
| 7. DBStorage - User | [/models/user.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/user.py) | Update the `User` class to inherit from BaseModel and Base, and define or replace class attributes for __tablename__, email, password, first_name, and last_name with corresponding column specifications. |
| 8. DBStorage - Place | [/models/place.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/place.py), [/models/user.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/user.py), [/models/city.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/city.py) | Update the Place class in models/place.py to inherit from BaseModel and Base, and define or replace class attributes with corresponding column specifications. Update the `User` and `City` classes to include or replace class attributes for places representing a relationship with the `Place` class, ensuring that linked objects are automatically deleted when the referencing object is deleted. |
| 9. DBStorage - Review | [/models/review.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/review.py), [/models/user.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/user.py), [/models/place.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/place.py) | Update the Review class in models/review.py to inherit from BaseModel and Base, and add or replace class attributes for __tablename__, text, place_id, and user_id with corresponding column specifications. Update the `User` class with a class attribute `reviews` representing a relationship with the Review class. Update `reviews` class attribute in `Place` class to represent a relationship with the `Review` class. , add a getter attribute reviews in `FileStorage` that returns a list of Review instances with place_id equal to the current Place.id |
| 10. DBStorage - Amenity... and BOOM!| [/models/amenity.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/amenity.py), [/models/place.py](https://github.com/germanchuks/AirBnB_clone_v2/blob/master/models/place.py) | Update the `Amenity` class to inherit from BaseModel and Base and add or replace class attributes for __tablename__ and name. Add an instance of SQLAlchemy Table  `place_amenity` in `Place` class to create a Many-To-Many relationship between Place and Amenity. Update the amenities class attribute in `DBStorage` to represent a relationship with the Amenity class as secondary to place_amenity. Add getter and setter attributes in `FileStorage` for amenities that handle the retrieval and addition of Amenity instances based on the attribute amenity_ids |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Run "console.py" file as follows:
```
/AirBnB_clone_v2$ ./console.py
```
4. The following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. 

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID


##### Supported Models
| Class       | Description                                                      |
|-------------|------------------------------------------------------------------|
| BaseModel   | An abstract class that serves as the base class for all models.  |
| User        | Represents a user account.                                       |
| State       | Represents the geographical state in which a User lives or a City belongs to. |
| City        | Represents an urban area in a State.                             |
| Amenity     | Represents a useful feature of a Place.                          |
| Place       | Represents a building containing rooms that can be rented by a User. |
| Review      | Represents a review of a Place.                                  |


##### Environment Variables
| Variable            | Description                                            |
|---------------------|--------------------------------------------------------|
| HBNB_ENV            | The running environment (dev or test).                 |
| HBNB_MYSQL_USER     | The MySQL server username.                             |
| HBNB_MYSQL_PWD      | The MySQL server password.                             |
| HBNB_MYSQL_HOST     | The MySQL server hostname.                             |
| HBNB_MYSQL_DB       | The MySQL server database name.                        |
| HBNB_TYPE_STORAGE   | The type of storage used (file or db).                 |


<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 1: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c
(hbnb)                   
```
###### Example 2: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c
[BaseModel] (70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c) {'id': '70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c', 'created_at': datetime.datetime(2024, 1, 15, 21, 39, 16, 811362), 
'updated_at': datetime.datetime(2024, 1, 15, 21, 39, 16, 811379)}
(hbnb)  
```
###### Example 3: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c
(hbnb) show BaseModel 70dc28bc-7cf5-4cb4-b7d3-5fbd0fbafd0c
** no instance found **
(hbnb)   
```
###### Example 4: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel e9f8e901-1fae-49ab-ac9b-178177ce740d first_name "Michael"
(hbnb) show BaseModel e9f8e901-1fae-49ab-ac9b-178177ce740d
[BaseModel] (e9f8e901-1fae-49ab-ac9b-178177ce740d) {'id': 'e9f8e901-1fae-49ab-ac9b-178177ce740d', 'created_at': datetime.datetime(2024, 1, 15, 22, 15, 11, 637884), 
'updated_at': datetime.datetime(2024, 1, 15, 22, 15, 11, 637898), 'first_name': 'Michael'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 1: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (d2219b99-c40f-49dc-bf45-56a48a43b5b0) {'updated_at': datetime.datetime(2024, 1, 15, 23, 13, 27, 714395), 'id': 'd2219b99-c40f-49dc-bf45-56a48a43b5b0', 'created_at': datetime.datetime(2024, 1, 15, 23, 13, 27, 714370)}", "[User] (5b0c6fa2-06b1-4f01-92a6-77320d30c3a5) {'updated_at': datetime.datetime(2024, 1, 15, 23, 15, 29, 406725), 'id': '5b0c6fa2-06b1-4f01-92a6-77320d30c3a5', 'created_at': datetime.datetime(2024, 1, 15, 23, 15, 29, 406707)}"]
```

###### Example 2: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("d2219b99-c40f-49dc-bf45-56a48a43b5b0")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (5b0c6fa2-06b1-4f01-92a6-77320d30c3a5) {'updated_at': datetime.datetime(2024, 1, 15, 23, 15, 29, 406725), 'id': '5b0c6fa2-06b1-4f01-92a6-77320d30c3a5', 'created_at': datetime.datetime(2024, 1, 15, 23, 15, 29, 406707)}"]
```
###### Example 3: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) BaseModel.update("e9f8e901-1fae-49ab-ac9b-178177ce740d", first_name "German")
(hbnb)
(hbnb) BaseModel.all()
(hbnb) ["[BaseModel] (e9f8e901-1fae-49ab-ac9b-178177ce740d) {'id': 'e9f8e901-1fae-49ab-ac9b-178177ce740d', 'created_at': datetime.datetime(2024, 1, 15, 22, 15, 11, 637884), 
'updated_at': datetime.datetime(2024, 1, 16, 11, 51, 10, 514696), 'first_name': 'German'}"]
```
###### Example 4: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) BaseModel.update("e9f8e901-1fae-49ab-ac9b-178177ce740d", {'first_name': 'AirBnb'})
(hbnb)
(hbnb) BaseModel.all()
(hbnb) ["[BaseModel] (e9f8e901-1fae-49ab-ac9b-178177ce740d) {'id': 'e9f8e901-1fae-49ab-ac9b-178177ce740d', 'created_at': datetime.datetime(2024, 1, 15, 22, 15, 11, 637884), 
'updated_at': datetime.datetime(2024, 1, 16, 12, 2, 22, 105718), 'first_name': 'AirBnb'}"]
```
<br>
