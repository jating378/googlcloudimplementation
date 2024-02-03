# app.py

from flask import Flask, render_template, request, jsonify
import tablecreator
import showtables
import showdata
import deletetables
from loadcsv import load_csv_into_teams, load_csv_into_match_data  # Import the functions from loadcsv module
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-tables')
def create_tables_route():
    tablecreator.create_tables()
    return 'Tables created successfully!'

@app.route('/show-tables')
def show_tables_route():
    return showtables.show_tables()

@app.route('/delete-tables')
def delete_tables_route():
    return deletetables.delete_tables()

@app.route('/load-data', methods=['POST'])
def load_data():
    teams_result = load_csv_into_teams(os.path.join(os.getcwd(), 'cwcteams.csv'))
    matches_result = load_csv_into_match_data(os.path.join(os.getcwd(), 'cwcmatch.csv'))

    return f'Teams loaded successfully! {teams_result}\nMatches loaded successfully! {matches_result}'

@app.route('/show-teams')
def show_teams_route():
    teams_data = showdata.show_teams()
    print(teams_data)  # Add this line to print teams_data to the console
    return render_template('show_teams.html', teams_data=teams_data)

@app.route('/show-match-data')
def show_match_data_route():
    match_data = showdata.show_match_data()
    return render_template('show_match_data.html', match_data=match_data)

@app.route('/show-matches-for-team', methods=['POST'])
def show_matches_for_team():
    team_id = request.form.get('team_id')


    matches_data, matches_won_count = showdata.show_matches_for_team(team_id)

    return render_template('show_matches_for_team.html', matches_data=matches_data, matches_won_count=matches_won_count)

if __name__ == '__main__':
    app.run(debug=True)
