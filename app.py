from flask import Flask, render_template, request
import random

app = Flask(__name__)

ds = [1, 2, 3]

@app.route('/', methods=["GET", "POST"])

def monty_hall():
    if request.method == "POST":
        try:
            trials = int(request.form.get("trials"))
        except:
            return render_template("index.html", error="Number of trials should be in between 1 - 1,000,000!")

        if trials <= 0 or trials > 1000000:
            return render_template("index.html", error="Number of trials should be in between 1 - 1,000,000!")

        switch_wins = 0
        stubborn_wins = 0

        for i in range(trials):
            car = random.choice(ds)
            choice = random.choice(ds)

            if choice == car:
                r = None
                for d in ds:
                    if d != choice:
                        r = d
                        break
            else:
                r = None
                for d in ds:
                    if d != choice and d != car:
                        r = d
                        break

            change_choice = None
            for d in ds:
                if d != choice and d != r:
                    change_choice = d
                    break

            if change_choice == car:
                switch_wins += 1
            else:
                stubborn_wins += 1

            switch_win_rate = round(switch_wins / trials * 100, 2)
            stubborn_win_rate = round(stubborn_wins / trials * 100, 2)

        return render_template("index.html", switch_wins=switch_wins, stubborn_wins=stubborn_wins, trials=trials, switch_win_rate=switch_win_rate, stubborn_win_rate=stubborn_win_rate)

    return render_template("index.html")

if __name__ == '__main__':
    app.run()
