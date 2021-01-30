from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        my_dict = request.form
        fever = float(my_dict['fever'])
        age = int(my_dict['age'])
        Pain = int(my_dict['bodyPain'])
        Nose = int(my_dict['runnyNose'])
        Breath = int(my_dict['diffBreath'])
        inputPara = [fever, Pain, age, Nose, Breath]
        inf_prob = clf.predict_proba([inputPara])[0][1]
        print(inf_prob)
        return render_template('show.html', inf=round(inf_prob*100))
    return render_template('index.html')
    # return 'Hello, World!' + str(inf_prob)

if __name__ == '__main__':
    app.run(debug=True)