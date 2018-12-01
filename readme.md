# Project 5 - Unicorn Attractor

##### What does it do and what need does it fulfil?
This project uses skills learnt to build a Django Website that uses a Postgres backend. It is for people to vote on tickets and pay towards features using Stripe API. The Website can be found at [https://unicorn-attractor.herokuapp.com/]

##### Functionality of project
The Website is fully responsive and uses Django's User model to manage user accounts. The user is able to register and login and vote once for each bug and make multiple payments towards the completion of features. The user is also able to create a ticket, which automatically becomes a bug and will show on the ticket list page. Other users are then able to vote on it. 

The ticket list page shows all bugs and features. The features are shown in order of the amount of money that has been donated to solve them. Each ticket shows its created date, title, status, description. The bugs also show whether you have voted or not on it.
  
Each ticket on the ticket list page can be clicked onto and that will load the single ticket page which has the same functionality as the list page (voting / payments) as well as also enabling the user to comment on the ticket. Each comment is added underneath along with their username and time of comment.

The ticket list displays all bugs and features that have a ticket status of TODO or DOING, once a ticket has been completed these are not shown on this page. The tickets completed page shows all tickets that have been completed in date order. 

The graph page incorporates Highcharts API to create the graphs. It uses two speedometer graphs to show features and bugs done since the start. It also uses a Stacked bar chart to show bugs and features that have been attended to in the periods of the last last day, week and month. The page also shows the most voted for bug and highest paid feature.

There is a simple blog page that admin can create inside the admin area. There is also a logout option. If the user is not logged in they cannot see the tickets list or create ticket page nor can they vote. They can however see the welcome, completed tickets, graphs and blog. 

##### Technologies Used

- Python
- HTML5
- CSS / Bootstrap 4
- JS / JQuery
- Postgres
- Stripe and Highcharts API
- Django

##### Deployment

Website was coded initially in VSCode and after spending a month trying that environment I went back to PyCharm, a local GIT directory was used for version control and then uploaded to GITHUB. All static files are served from AWS S3 and the database and django from Heroku. The environment variables are inside Heroku and are parameterised inside the settings.py file.

##### Testing

The apps inside the project do have some basic testing functions that I ran whilst building it. I started off by testing the model creation functions. 

Upon checking those I ran tests that checked the business logic of my views. 

The ticket app was tested by using Django's Test Client class. I tested registration forms password mismatching, checking successful registering redirected the user. 

I also checked for ticket creation and voting, the business logic that stops a user from voting for the same ticket twice. I also tested a ticket being voted for twice (once by two different users) and this highest ticket bug showing on the graph page. 

I tested the business logic of the ticket create page: once entering no data into the form that validation messages would be returned. I also tested that upon entering successfully the ticket was created and user was redirected to the tickets page with the new ticket present on the tickets page.

It is impossible to test at 100% coverage so I followed the Pareto principle (80/20 rule) which I believe I achieved. Most of my testing is done in the Tickets's app tests.py while other tests are present in the Users app tests.py

Upon it being live I asked people on the Code Institute's Slack channels to test it and provide feedback. I received positive feedback with only an indication that I may want to change the layout to use container instead of container-fluid. I did try that but I prefer the full width of container-fluid so I kept it like that.   

I concentrated on logic and functionality with the project, I have no desire to be a designer! That said I kept my design to be usable and simple to navigate with readable font faces and breathable spacing (i.e. negative space).  

As the site is built with a responsive design it works for mobiles and I have checked it on iPhones 6 to X, Samsung Galaxys, iPads (mini to pro), Google's Pixel 2 and 3. I also tested it on various browsers. 

