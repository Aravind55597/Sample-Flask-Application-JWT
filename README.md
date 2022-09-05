# WebApp boilerplate with React JS and Flask API (Removed Gitpod and Heroku files ; this example has been MODIFIED FROM https://start.4geeksacademy.com/ ) 

> Documentation: https://start.4geeksacademy.com/

- Integrated with Pipenv for package managing.
- Use of .env file.
- SQLAlchemy integration for database abstraction.

### Back-End Manual Installation:

It is recomended to install the backend first, make sure you have Python 3.8, Pipenv and a database engine (Posgress recomended)

1. Install the python packages: `$ pipenv install`
2. Create a .env file based on the .env.example: `$ cp .env.example .env`
3. Install your database engine and create your database, depending on your database you have to create a DATABASE_URL variable with one of the possible values, make sure yo replace the valudes with your database information:

| Engine    | DATABASE_URL                                        |
| --------- | --------------------------------------------------- |
| SQLite    | sqlite:////test.db                                  |
| MySQL     | mysql://username:password@localhost:port/example    |
| Postgress | postgres://username:password@localhost:5432/example |

4. Create migratiosn folder (if it does not exist) `$ pipenv run init `
5. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
6. Run the migrations: `$ pipenv run upgrade`
7. Start the virtual env `$ pipenv shell`
8. Run this command to seed the database `$ flask insert-test-users 5`
9. Run the application: `$ pipenv run start`

### Backend Populate Table Users

To insert test users in the database execute the following command:

```sh
$ flask insert-test-users 5
```

And you will see the following message:

```
  Creating test users
  test_user1@test.com created.
  test_user2@test.com created.
  test_user3@test.com created.
  test_user4@test.com created.
  test_user5@test.com created.
  Users created successfully!
```
