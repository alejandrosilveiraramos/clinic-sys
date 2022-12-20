from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./components/home.html')

@app.route('/new_patient')
def new_patient_page():
    return render_template('./components/newPatient.html')

@app.route('/list')
def list_page():
    return render_template('./components/list.html')

@app.route('/more_info/<id_patient>')
def more_info(id_patient):
    return render_template('./components/moreInfoPatient.html', patient=id_patient)

@app.route('/login')
def login_page():
    return render_template('./components/login.html')

@app.route('/register')
def register_page():
    return render_template('./components/register.html')

if __name__ == '__main__':
    app.run(debug=True)

