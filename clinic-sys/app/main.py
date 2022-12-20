from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('./components/home.html')

@app.route('/list')
def list_page():
    return render_template('./components/list.html')

@app.route('/more_info/<id_patient>')
def more_info(id_patient):
    return render_template('./components/moreInfoPatient.html', patient=id_patient)



if __name__ == '__main__':
    app.run(debug=True)

