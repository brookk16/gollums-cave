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

def write_to_leaderboard(player, score):
    now = datetime.now().strftime("%H:%M:%S")
    
    with open('data/highscore_board.txt', 'a') as leaderboard:
        leaderboard.write(str(player) + "\n" + str(score) + "\n")
    leaderboard.close()
        
    

def check_length_and_order():
    players = []
    scores = []
    now = datetime.now().strftime("%H:%M:%S")
    
    with open('data/highscore_board.txt', 'r') as leaderboard:
        lines = leaderboard.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            players.append(text)
        else:
            scores.append(text)
    
    players_scores = zip(players, scores)
    
    sorted_highscores = sorted(players_scores, key=lambda tup: tup[1])
    
    print(sorted_highscores) 
    """ Currently returning the sorted list of tuples (players_scores), next will need to figure out how to delete the entries > 11 and print to highscore board"""
    
    
    

    




wrong_answers = []

high_score = {
    "name": "nobody",
    "score": 0
}

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
    return render_template("highscores.html")

@app.route("/riddle", methods=["GET", "POST"])
def riddle():
    
    
    
    if "player" not in session:
        return redirect(url_for("index"))

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
             
            
            
            

    if session["riddle_num"] >= len(RIDDLES):
        
        write_to_leaderboard(session["player"],session["score"])
        check_length_and_order()
        
        
        
        if session["score"] >= high_score["score"]:
            high_score["score"] = session["score"]
            high_score["name"] = session["player"]
        
        return render_template("highscores.html", player=session["player"],
                               score=session["score"],
                               highscore=high_score["score"],
                               highscorer=high_score["name"])

    new_riddle = RIDDLES[session["riddle_num"]]
    
    return render_template(
        "riddle.html", player=session["player"],
        question=new_riddle["question"], riddle_num=session["riddle_num"], wrong_answers=session["wrong_answers"], attempts=session["riddle_attempts"])


if __name__ == "__main__":
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")),
            debug=True)