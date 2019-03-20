# Gollum's Cave

This is a python3 and Flask riddle game app based on the encounter bewteen the creature Gollum, and Bilbo Baggins the hero of J.R.R Tolkien's "The Hobbit".

This is the 3rd milestone project, required for completing the code institute's full stack web development course.

## User experience 

This website is designed for fans of J.R.R Tokien's work (i.e: author of The hobbit, Lord of The Rings, The Silmarillion, e.t.c) to live through Bilbo's meeting with Gollum. Just as in the book, players will attempt to escape from Gollum by answering his riddles correctly. The aim of this project was to create a flask based riddle game, to showcase skills in the use of Python3, flask and front-end design.


Below you can read some of the user stories:

* As a user, I want to play a riddle game that allows me to compete with friends.
* As a user who doesn't know about the background of the story, I want to be able to learn more about it.
* As a fan of The Hobbit, I want the game to feel like being in the cave under the Misty Mountains.

Below you can see the wireframes:


## Features

The main feature of this application is the riddle game. The game is simple: players will be shown 5 riddles and must answer more than 3 correctly to win. Players will be given 3 attempts per riddle, then the player loses the opportunity to get that point and the next riddle is displayed. After all riddles have been  responded to the player's score and username will be submitted to the highscore board. 
All correct answers should be: all lowercase, one word and singular (i.e: non plural)

The layout for each page can be seen [above](#wireframes) in the wireframes.

Below you can find a summary of a player's game: 

1. Once the user has read the welcome message and the rules, they can submit a username to start. 
2. They will then be taken to the riddle page, where each riddle is displayed
3. Players answer the riddle by typing their answer in the box (below the riddle): 
   * **If correct**: The gollum picture remains the same and a message appears ("Correct answer x. Your score is x")
   * **If incorrect**: A menacing picture of Gollum is displayed, your incorrect guess is displayed below the riddle input, you loose one of your 3 attempts and a message appears ("Wrong answerx. You have x remaining attempts left")
   * If the player looses all their 3 guesses, a message is displayed ("Wrong answer, x. Better luck with this riddle:") and the next riddle is shown
4. When all 5 riddles have been answered, the player is taken to a new page where a congratulations message is shown ("Congratulations x, you've completed the game! Your final score is x. Check the highscore board to see where you are"). 
   * If the player scored more than 3: you escaped with the ring (so a picture of the one ring is displayed)
   * If the player scored 3 or less: you were captured/eaten by Gollum (so an excited picture of Gollum is displayed)
     
Players can then view the highscore board by clicking the link in the head navigation bar. Highscores are displayed highest to lowest, and newest to oldest. Thus if 2 players score 5, the last one to submit their score would be displayed above the other.

> Note: This project does not use a database. The riddles and answers are stored in JSON file, but the players: username, final score, attempts, wrong-answers, e.t.c are stored as session variables. Therefore each time the broswer is closed the heighscore board will be emptied. 
 

## Technologies Used

#### Front-end

[Fonts awesome](https://fontawesome.com):
* Provide the icons for the project 

[Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) (4.0.0):
* Provides a grid system to structure html code and basic css styling

[JQuery](https://jquery.com)(3.2.1):
* Provides DOM manipulation

[Jinja2](http://jinja.pocoo.org/docs/2.10/) (2.10):
* Used to render data/variables from the main app (run.py) 

#### Back-end

[Python3](https://www.python.org/download/releases/3.0/) (3.4.3):
* Used to write the logic for this app (which can be seen in [run.py](https://github.com/brookk16/gollums-cave/blob/master/run.py))

[Flask](http://flask.pocoo.org) (1.0.2):
* Acts as a framework for the app


The code editor used to create the project was [Cloud9](https://c9.io/signup).

The project uses [Git](https://git-scm.com) for version control.

For the additional tools and libraries needed to run the app, please refer to [requirements.txt](https://github.com/brookk16/Cuisine/blob/master/requirements.txt)


## Testing


<details>
<summary>User stories</summary>
<br>
User stories were checked to ensure this project meets their requests:

1. 

</details>

<details>
<summary>Manual Testing</summary>
<br>
Manual testing was conducted on all main features of the app (features outlined [here](#features)).

> note: all tests begin by starting at the index/welcome page.

> note: all tests are from the desktop perspective. For mobile, any references to a "nav bar", will require clicking on the "ring" symbol first to reveal the menu (screen sizes < 575px).


</details>

<details>
<summary>Further testing and Issues</summary>
<br>
1. HTML and CSS code were both validated using W3C [HTMl](https://validator.w3.org) and [CSS](https://jigsaw.w3.org/css-validator/) validator.

> note: HTML validation threw up errors, although these were concerning the Jinja2 templating language used in the html templates.


Issues:


* The author is not yet skilled in automated testing, and as such was unable to adhere to a test driven development approach. 
</details>


## Deployment

The project is deployed on Heroku, and can be accessed [here]() 

The Github for this project can be found [here](https://github.com/brookk16/gollums-cave). And can also be accessed via the github logo in the footer of the website.

Download the code from github, and place into your project. 

Or clone the project into your working environment, using the command line:

~~~
git clone https://github.com/brookk16/gollums-cave
~~~



## Credits

#### Content

The fonts used were taken from [thehut](http://www.thehutt.de/tolkien/fonts.html)

The photos used in this site were obtained from [Google images](https://www.google.com/search?rls=en&q=google+images+Gollum&tbm=isch&source=univ&client=safari&sa=X&ved=2ahUKEwjjztKioJHhAhWYTBUIHXriCmwQsAR6BAgJEAE&biw=1440&bih=769)

#### Acknowledgements

I received inspiration for this project from the works of J.R.R Tokien. Please see [middle-earth](https://www.middleearth.com) for more information.