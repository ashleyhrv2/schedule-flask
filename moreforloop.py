from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='GET':
        return render_template('personinfo2.html')
    else:
        return Getinfo()

def Getinfo():
    global headings,data
    headings = ("Course","Teacher")
    course1 = request.form.get('txtcoursename1')
    teacher1 = request.form.get('txtteacher1')
    
    course2  = request.form.get('txtcoursename2')
    teacher2 = request.form.get('txtteacher2')
    
    course3 = request.form.get('txtcoursename3')
    teacher3 = request.form.get('txtteacher3')
    
    course4  = request.form.get('txtcoursename4')
    teacher4 = request.form.get('txtteacher4')
    
    course5 = request.form.get('txtcoursename5')
    teacher5 = request.form.get('txtteacher5')
    
    course6  = request.form.get('txtcoursename6')
    teacher6 = request.form.get('txtteacher6')
    
    course7 = request.form.get('txtcoursename7')
    teacher7 = request.form.get('txtteacher7')
    
    course8  = request.form.get('txtcoursename8')
    teacher8 = request.form.get('txtteacher8')
    

    data=(
        (course1,teacher1),
        (course2,teacher2),
        (course3,teacher3),
        (course4,teacher4),
        (course5,teacher5),
        (course6,teacher6),
        (course7,teacher7),
        (course8,teacher1)
        )
    return DisplayInfo()

def DisplayInfo():
    return render_template('output2.html',headings = headings,data = data)

if __name__=='__main__':
    app.run()
