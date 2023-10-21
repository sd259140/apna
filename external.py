import request,json
url=""
def get(id=None):
    data={ }
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        b=request.get(url,data=json_data)
        r=b.json()
        print(r)

get() 

def post():
    data={
        'name':'shubham',
        'roll':12,
        'by':'yes'
    }
    json_data=json.dumps(data)
    b=request.post(url,data=json_data)
    r=b.json()
    print(r)

def update():
    data={
        'id':4
        'name':'shubham',
        'roll':12,
        'by':'yes'}
    json_data=json.dumps(data)
    b=request.put(url,data=json_data)
    r=b.json()    
    
def delete():
    data={
        'id':4
    }
    json_data=json.dumps(data)
    b=request.delete(url,data=json_data)
    r=b.json() 
