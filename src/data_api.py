from flask import Flask, request
from data_service import db_create_entry

app = Flask(__name__)


#needed:
#input whole row


@app.route("/entry", methods=['POST'])
def create_entry():
    try: 
        data = request.get_json()
        consultantName = data['consultantName']
        customerName = data['customerName']
        startTime = data['startTime']
        endTime = data['endTime']
        lunchStart = data['lunchStart']
        lunchEnd = data['lunchEnd']
        db_create_entry(consultantName, customerName, startTime, endTime, lunchStart, lunchEnd)
        return {"success": "created entry: %s" % consultantName}
    except:
        return {"error": "error creating entry"}
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
