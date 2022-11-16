from flask import Flask,render_template,request,redirect, session
app = Flask(__name__)
app.secret_key = 'sdasasdasd'

@app.route('/')  #1 Krijojme funksionin i cili do te na tregoje nje faqe me nje forme ne te        
def index():       # pra krijojme nje route index qe do na shfaqi formen tek file_index.html
    return render_template('index.html') #2 Shkojme tek file index.html dhe ndertojme formen sipas tabeles se pare ne ushtrim

@app.route ('/create/user',methods=['POST']) #3 tek file index.html me atributin action ndikuam qe forma/Posti kerkuar do te mbahet ne routin /'users'
def create_user():                      #do hym te server.py dhe e shtojme routin dhe bejme funksionin me emer create_user                
    session['name'] = request.form['name']           # zerat qe duam te na postohen   
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/dashboard")           #ne apost vetem redirect jo render

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', comment = session['comment'])# ben te mundur qe te dali dhe ato qe ke shkruar ne koment

@app.route('/back')                    #6 Log out komanda,opsioni, behet dhe tek dashboard1.html                       
def back():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode