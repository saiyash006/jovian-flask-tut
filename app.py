from flask import  render_template, jsonify, Flask

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Delhi, India',
        'salary': 'Rs. 90,000'
    },
    {
        'id':2,
        'title':'Security Engineer',
        'location': 'Bangalore, India',
        'salary': 'Rs. 150,000'
    },{
        'id':3,
        'title':'Soc Analyst',
        'location': 'Lucknow, India',
        'salary': 'Rs. 50,000'
        }
    ,{
        'id':4,
        'title':'Penetration tester',
        'location': 'Los Angels, USA',
        'salary': 'USD. 100,000'
    }
]



@app.route("/")
def helloWorld():
    return render_template('home.html', jobs=JOBS, companyName='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)