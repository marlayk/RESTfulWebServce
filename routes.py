
from flask import Flask, render_template, request, Response 
import foursquare
import json 
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/venues')
def venues():
    client = foursquare.Foursquare(client_id='TBSTWCDGYTOKYCC1QTOGSBTTWSGOVOBHIQBV03VGWO4G5OTN', client_secret='FQLOQSEZULTHVVPFFGQZU5YDCSXLYASES52002FUR3WINGDS') 
    result = client.venues.search(params={'near': request.args.get('city', ''),'query':request.args.get('q', '')})
    j=[]
    for venue in result['venues']:
         j.append([venue['name'],venue['location']['lat'],venue['location']['lng']])
    jsond= json.dumps(j)

    return Response(jsond, mimetype='application/json')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

