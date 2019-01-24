import json
import os
from datetime import datetime
from flask import (
    Flask, session, render_template, flash, request, redirect, url_for)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "olorin")

""" player always gets +1 of this number because of the changes i made to include displaying wrong guesses """

MAX_ATTEMPTS = 2  
with open("data/riddles.json") as riddle_file:
    RIDDLES = json.load(riddle_file)

usernames = []
scores = []
wrong_answers = []

high_score = {
    "name": "nobody",
    "score": 0
}

def add_to_scoreboard(name, score):
    """takes users names and scores and appends them each to a list, to be used in the highscore board"""    
    usernames.append(name)
    scores.append(score)
    
def check_length_and_order():
    """takes the usernames and scores lists, combines them and sorts each user from high to low on their score"""
    
    usernames_and_scores = sorted(zip(usernames, scores), key=lambda x: x[1], reverse=True)
    
    """keeps the length of the list to 11 entries"""
    if len(usernames_and_scores) >= 12:
        
        top_11 = usernames_and_scores[:11]
        return top_11
    
    return usernames_and_scores
    

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new_game", methods=["POST"])
def new_game():
    session["player"] = request.form["player"]
    session["score"] = 0
    session["riddle_num"] = 0
    session["riddle_attempts"] = MAX_ATTEMPTS
    session["wrong_answers"] = wrong_answers
     
    return redirect(url_for("riddle"))

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route("/highscores", methods=["GET","POST"])
def highscores():
    
    session["highscore_board"] = check_length_and_order()
    
    return render_template("highscores.html", highscore_board = session["highscore_board"])

@app.route("/riddle", methods=["GET", "POST"])
def riddle():
    
    """If the username has not been logged at the homepage, the user will be redirected there"""
    
    if "player" not in session:
        return redirect(url_for("index"))
    
    """When the user submits an answer the answer is checked from the ridddles.json file. If it is correct, their score and riddle_num is incremented and a feedback message is displayed. If not their riddle_attempts is incremented and a message is displayed to show that the answer was wrong. After 3 wrong attmpts, the current riddle is skipped"""
    
    
    if request.method == "POST" and session["riddle_num"] < len(RIDDLES): 
        
        previous_riddle = RIDDLES[session["riddle_num"]]
        
        answer = request.form["answer"].lower()
        
        if answer == previous_riddle["answer"]:
            session["riddle_num"] += 1
            session["score"] += 1
            
            if session["riddle_num"] < len(RIDDLES): 
                flash("Correct answer, %s! Your score is %s." % (
                      session["player"], session["score"]))
                session["wrong_answers"]=[]
                session["riddle_attempts"] = MAX_ATTEMPTS
                
        elif not session["riddle_attempts"] and session["wrong_answers"]:
            session["riddle_num"] += 1
            session["riddle_attempts"] = MAX_ATTEMPTS
            session["wrong_answers"] = wrong_answers
            
            if session["riddle_num"] < len(RIDDLES):
                flash("Wrong answer, %s. Better luck with this riddle:" % (
                      session["player"]))
        
        else:
            
            session["riddle_attempts"] -= 1
            session["wrong_answers"].append(answer)
            flash("Wrong answer, %s. You have %s attempts left." % (
            session["player"], session["riddle_attempts"]+1))
    
    """ When all the riddles are asked, the players name and score is added to the highscore board"""        

    if session["riddle_num"] >= len(RIDDLES): 
    
        add_to_scoreboard(session["player"], session["score"])
        
        return render_template("game_over.html", player=session["player"],
                               score=session["score"])
    
    new_riddle = RIDDLES[session["riddle_num"]]
    
    return render_template("riddle.html", player=session["player"],
            question=new_riddle["question"], riddle_num=session["riddle_num"], 
            wrong_answers=session["wrong_answers"], attempts=session["riddle_attempts"])


if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")),
            debug=True)