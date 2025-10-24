## We have Spotify at home

In this project, you will create a full-stack web application to create a feature similar to Spotify's *Daylist* feature. A "tech stack" is the set of technologies you use in order to complete a projects, such as programming languages and libraries. Full stack projects use technologies for all different kinds of applications, hence the name "full stack".

We'll introduce a lot of new vocabulary throughout this project, including "front end" which refers to the side of the website the user sees. Our front end is in the `\templates` directory and is written in `html` and `css`. `html` creates the layout of the webpage and `css` styles the page by customizing things such as font, colors, and font size. Everything that the user *can't* see is considered `backend`; things like OOP class designs, databases, and data manipulation are things that the user doesn't see when they visit a webpage. The backend of this project is written in Python and is available in `flask_app`.

For this project we will ask you to utilize knowledge you've acquired through different parts of this course. Our song database is a *SQL Table* and the code we use to construct the database is in `db.py`. For now, don't worry about this code. Instead, read through `schema.sql` to familiarize yourself with the structure of the SQL table we'll be using.

The code that sets up our website lives in `__init__.py`. Just like how a class in Python needs to be initialized before you can use it, our web app also needs to be initialized before it can run.  

Inside `__init__.py`, you’ll see code that connects different parts of the website to specific URLs—these are called *endpoints*. Each endpoint tells the app what to do when someone visits a certain web address (for example, `/home` or `/login`). Our song can be found in the `\songs` endpoint.


## Important Commands
- run `flask --app __init__.py run` to run

- you might need to initalize the db with `flask --app __init__.py init-db`

- create a folder `instances` within `flask_app` to store all db instances

- go to http://127.0.0.1:5000/songs to view the songs in the front end

