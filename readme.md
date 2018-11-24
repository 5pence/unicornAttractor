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

The apps inside the project do have some basic testing functions that I ran whilst building it. Upon it being live I asked people on the Code Institute's Slack channels to test it and provide feedback. I received positive feedback with only an indication that I may want to change the layout to use container instead of container-fluid. I did try that but I prefer the full width of container-fluid so I kept it like that.   
As all the forms have been extended from Django's models all the validation is built in. 

