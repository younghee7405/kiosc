from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def screen1():
    return render_template('index.html')

@app.route('/screen2')
def screen2():
    return render_template('sub1.html')

@app.route('/screen3')
def screen3():
    return render_template('sub2.html')

@app.route('/screen4')
def screen4():
    return render_template('sub3.html')

@app.route('/screen5')
def screen5():
    return render_template('sub4.html')

@app.route('/screen6')
def screen6():
    return render_template('sub5.html')


@app.route('/screen7')
def screen7():
    return render_template('sub6.html')

@app.route('/screen8')
def screen8():
    return render_template('sub7.html')

@app.route('/screen9')
def screen9():
    return render_template('sub8.html')


@app.route('/screen10')
def screen10():
    return render_template('sub9.html')

@app.route('/screen11')
def screen11():
    return render_template('sub10.html')

@app.route('/screen12')
def screen12():
    return render_template('sub11.html')


@app.route('/screen13')
def screen13():
    return render_template('sub12.html')

@app.route('/screen14')
def screen14():
    return render_template('sub13.html')

@app.route('/screen15')
def screen15():
    return render_template('sub14.html')

@app.route('/screen16')
def screen16():
    return render_template('sub15.html')


@app.route('/screen17')
def screen17():
    return render_template('sub16.html')


@app.route('/screen18')
def screen18():
    return render_template('sub17.html')



if __name__ == '__main__':
    app.run(debug=True)
