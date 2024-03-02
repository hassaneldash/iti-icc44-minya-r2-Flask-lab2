from flask import Flask,request

app=Flask(__name__) #__main__==>directly , #file ==> non Direct

users=[{"id":1,"name":"mina"},{"id":2,"name":"ahmed"},{"id":3,"name":"mariam"},{"id":1,"name":"ayman"}]

#@app.route('/') #EndPoint
def index():
    #print(name)
    return "<h1 style='text-align:center' >Home Page</h1>"

app.add_url_rule('/','index',index)


@app.route('/users') #EndPoint
def get_users():
    return users
# http://127.0.0.1:5000/user?name=mina&age=30&address=cairo
@app.route('/user') #EndPoint
def get_user():
    #print(dir(request))
    print(request.method)#GET
    print(request.args)#payload #ImmutableMultiDict([('name', 'mina'), ('age', '30'), ('address', 'cairo')])
    name=request.args.get('name')
    age=request.args.get('age')
    address=request.args.get('address')
    
    
    return f"user is name={name} , age ={age} , address={address}"

# @app.route('/user/<string:id>') #EndPoint
# @app.route('/user/<string:id>/<string:id2>') #EndPoint
@app.route('/user/<int:id>') #EndPoint
def get_one_user(id):
    #print(id)
    #print(dir(request))
    # def compare(user):
    #     if user['id'] == id :
    #         return user
    # x=list(filter(lambda user: user['id']==id,users))[0]
    # print(x)
    # return "  ...... "
    for user in users :
        if user['id'] == id :
            return user
    return "Not Found" 
       
# if __name__ == "__main__" :
#     app.run(debug=True)
# =================================================================   
# Next Lec
# =============
# bluePrint
# Render Html Page
# Jinja
# Connect DB


# FastAPI 