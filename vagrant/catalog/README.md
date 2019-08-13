# Item Catalog
An application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Getting Started
### prerequisites
Logs Analysis uses a virtual machine (VM) to run an SQL database server and a web app that uses it.

Logs Analysis requires the following to run:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) the software that actually runs the virtual machine.
* [Vagrant](https://www.vagrantup.com/downloads.html) is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.


### Installing
* First clone the project and virtal machine repository
```
$ git clone https://github.com/AboSalaah/fullstack-nanodegree-vm.git
```
### Running the code
* Change to a folder called vagrant inside the cloned repository
```
$ cd ../cloned_repository/vagrant
```
* Start the virtual machine.
```
$ vagrant up
```
This will cause Vagrant to download the Linux operating system and install it.

* run ```vagrant ssh``` to log in to 
your newly installed Linux VM.
```
$ vagrant ssh
```

* Change folder to /vagrant to access the portion that is shared between your machine and the virtual machine
```
$ cd /vagrant
```
* Change folder to /catalog folder which contains the project installed and run the server
```
cd .../catalog
python server.py
```
### API endpoints
* GET localhost:8000/categories/JSON

Response body:
```
{
  "categories": [
    {
      "id": 1, 
      "items": [
        {
          "category_id": 1, 
          "description": "1911", 
          "id": 1, 
          "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
          "name": "Zamalek", 
          "user_id": 1
        }, 
        {
          "category_id": 1, 
          "description": "1907", 
          "id": 4, 
          "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
          "name": "Ahly", 
          "user_id": 1
        }, 
        {
          "category_id": 1, 
          "description": "my favorite team in Italy", 
          "id": 5, 
          "last_modification": "Mon, 12 Aug 2019 10:00:30 GMT", 
          "name": "Ac Milan", 
          "user_id": 2
        }
      ], 
      "name": "Football"
    }, 
    {
      "id": 2, 
      "items": [
        {
          "category_id": 2, 
          "description": "the king of clay", 
          "id": 2, 
          "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
          "name": "Rafael Nadal", 
          "user_id": 1
        }, 
        {
          "category_id": 2, 
          "description": "King of Tennis", 
          "id": 7, 
          "last_modification": "Mon, 12 Aug 2019 10:09:23 GMT", 
          "name": "Federer", 
          "user_id": 2
        }
      ], 
      "name": "Tennis"
    }, 
    {
      "id": 3, 
      "items": [
        {
          "category_id": 3, 
          "description": "the king of handball", 
          "id": 3, 
          "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
          "name": "Ahmed El-ahmar", 
          "user_id": 1
        }, 
        {
          "category_id": 3, 
          "description": "the best Handball players", 
          "id": 8, 
          "last_modification": "Mon, 12 Aug 2019 10:36:27 GMT", 
          "name": "Mikkel Hansen", 
          "user_id": 2
        }
      ], 
      "name": "Handball"
    }
  ]
}
```
* GET localhost:8000//catalog/<category_name>/items/JSON

Response body:
```
{
  "Items": [
    {
      "category_id": 1, 
      "description": "1911", 
      "id": 1, 
      "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
      "name": "Zamalek", 
      "user_id": 1
    }, 
    {
      "category_id": 1, 
      "description": "1907", 
      "id": 4, 
      "last_modification": "Mon, 12 Aug 2019 09:09:48 GMT", 
      "name": "Ahly", 
      "user_id": 1
    }, 
    {
      "category_id": 1, 
      "description": "my favorite team in Italy", 
      "id": 5, 
      "last_modification": "Mon, 12 Aug 2019 10:00:30 GMT", 
      "name": "Ac Milan", 
      "user_id": 2
    }
  ]
}
```
* GET localhost:8000/catalog/<category_name>/<item_name>/JSON

Response body:
```
{
  "Item": {
    "category_id": 1, 
    "description": "my favorite team in Italy", 
    "id": 5, 
    "last_modification": "Mon, 12 Aug 2019 10:00:30 GMT", 
    "name": "Ac Milan", 
    "user_id": 2
  }
}
```

### Technologies
Project is created with:
* Python 2.7.12
* Flask web development framework
* SQLAlchemy
* HTML
* CSS
* SQLite

### Coding Syle
* Follows PEP 8 — the Style Guide for Python Code


