How to run the Application


#Clone the repo or unzip the Source file

git clone https://github.com/creapremnath/Booking-API-Assessment.git


# Change to the Application Directory
#Open the vscode terminal

cd Booking-API-Assessment #if cloned from Github

cd FITNESS STUDIO APP # if unzip from zip file


# Create and activate a virtual environment

python -m venv venv   # Windows
python3 -m venv venv  # Linux/Mac
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


# Install Python Packages

pip install -r requirements.txt

# Run Application

cd app

uvicorn main:app --reload


# Open the Browser using this link to view API

http://127.0.0.1:8000/docs




# API Endpoints using CURL

# METHOD: GET
# ENDPOINTS: /classes


curl -X 'GET' \
  'http://localhost:8000/classes' \
  -H 'accept: application/json'



# METHOD: POST
# ENDPOINTS: /book

curl -X 'POST' \
  'http://localhost:8000/book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "class_id": 1,
  "client_name": "premnath",
  "client_email": "premnath@gmail.com"
}'


# METHOD: GET
# ENDPOINTS: /bookings

curl -X 'GET' \
  'http://localhost:8000/bookings?client_email=premnath%40gmail.com' \
  -H 'accept: application/json'



# Please check the POSTMAN collection.
