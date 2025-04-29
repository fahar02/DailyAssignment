'''
Question-11:
Weather mock API 
format comes from below endpoint 
    Parse format, if xml, show xml, 
    if none, show json 
    Put all random temp 
    City name may change based on PATH param 
    (currently not implemented in demo api endpoint)

DO the same as 
http://notepadfromdas.pythonanywhere.com/w/mumbai?format=xml
http://notepadfromdas.pythonanywhere.com/w/mumbai
'''

from flask import Flask,request,Response,jsonify
import random as r
import xml.etree.ElementTree as ET
app=Flask(__name__)

@app.route("/w/<string:city>",methods=['GET'])
def weather(city=None,format='json'):
    if request.method=='GET':
        wcity=request.args.get('city',city)
        wformat=request.args.get('format',format)
        temp=r.randrange(17,35)
        print(f"city is {wcity} format {wformat} temp {temp}")
        if wformat=="xml":
            xml= f'''<?xml version="1.0" encoding="UTF-8"?>
            <weather>
                <city>{wcity}</city>
                <temperature>{temp}</temperature>
            </weather>'''
            return Response(xml, mimetype='application/xml')
        else:
            data={"city":wcity,"temperature":temp}
            print(data)
            return jsonify(data)
    return ""

if __name__=="__main__":
    app.run()