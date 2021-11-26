# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'



slab = {
    1: 21.96,
    2: 26.01,
    3: 33.36
}

slab_limit = {
    'slab1': 0.60,
    'slab2': 1.50,
    'slab3': 1.51
}
slab1_overflow_amount = round(slab_limit['slab1'] * 61 * slab[1],2)
slab2_overflow_amount = round((slab_limit['slab2'] - slab_limit['slab1']) * 61 * slab[2],2)
@app.route('/bill-calculate/', methods =["GET", "POST"])
def calculate_total_amount():
    if request.method == "POST":
        cmr = request.form.get('cmr')
        pmr = request.form.get('pmr')
    elif request.method == "GET":
        cmr = request.args.get('cmr')
        pmr = request.args.get('pmr')
    cmr = int(cmr)
    pmr = int(pmr)
    amount = round(core_calculate(cmr,pmr),2)
    # return f"Your calculated bill amount is {round(core_calculate(cmr,pmr),2)}"
    return render_template('result.html',amount=amount)
    # return 'Welcome to GMP calculator'
@app.route('/mgl-bill-calc/')
def index():
    return render_template('main.html')
def core_calculate(cmr,pmr):
    print('pmr: ',pmr, '| cmr: ',cmr)
    SCM = cmr - pmr
    SCMD = round(SCM/61 , 2)
    print(f'SCM: {SCM} | SCMD: {SCMD}')
    if SCMD <= slab_limit['slab1']:
        print('in slab1')
        return SCMD * 61 * slab[1]
    elif (SCMD > slab_limit['slab1']) & (SCMD < slab_limit['slab3']):
        print('in slab2')
        return (slab1_overflow_amount) + ((SCMD - slab_limit['slab1']) * 61 * slab[2])
    elif SCMD >= slab_limit['slab3']:
        print('slab3')
        return (slab1_overflow_amount + slab2_overflow_amount) + ((SCMD - slab_limit['slab2']) * 61 * slab[3])