from flask import Flask,request,render_template,redirect,url_for

# app=Flask(__name__, tempalte_folder = 'test') #__main__==>directly , #file ==> non Direct
app=Flask(__name__) #__main__==>directly , #file ==> non Direct
users = [
  {
    "id": 1,
    "name": "mina",
    "age": 30,
    "location": "cairo"
  },
  {
    "id": 2,
    "name": "mariam",
    "age": 32,
    "location": "minya"
  }
]

def get_next_id():
  if len(users)>0:
    return users[-1]['id']+1
  else:
    return 1

# @app.route("/")
# def index():
#   return render_template('index.html')

# http://127.0.0.1:5000/users?name=ahmed&age=20&location=Giza

# @app.route('/users')
@app.route('/')
def get_users():
  name=request.args.get("name")
  age=request.args.get("age")
  location=request.args.get("location")
  if(name!=None or age!=None or location !=None):
    users.append({'id':get_next_id(), 'name' : name , 'age' : age , 'location' : location})
  print(users)
  if users != []:
    return render_template('users.html', users_html =  users)
  else:
    return "<h1>Not Users</h1>"



@app.route('/delete/<int:id>')
def delete_user(id):
  if id != None and len(users) != 0:
    for i  in range(len(users)):
      if users[i]['id'] == id:
        del users[i]
        print("Found and Delete")
        break
  return redirect('/users')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")
        location = request.form.get("location")
        if name is not None or age is not None or location is not None:
            for user in users:
                if user['id'] == id:
                    user['name'] = name
                    user['age'] = age
                    user['location'] = location
                    break
        return redirect('/users')
    else:
        user_to_edit = None
        for user in users:
            if user['id'] == id:
                user_to_edit = user
                break
        return render_template('edit_user.html', user=user_to_edit)


if __name__=="__main__":
  app.run(debug=True)