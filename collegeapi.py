from flask import Flask, request
import requests


app = Flask(__name__)


@app.route("/college_search", methods=["GET"])
def college_search():
    data = request.get_json()
    collegeName = data.get('college_name')
    print(collegeName)
    url = f'https://api.data.gov/ed/collegescorecard/v1/schools?api_key=&school.name={collegeName}&fields=school.name,school.city,school.state,latest.admissions.act_scores.midpoint.cumulative,latest.cost.tuition.out_of_state'

    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":

    app.run(port=9009, debug=True)