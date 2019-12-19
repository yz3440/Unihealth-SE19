# Unihealth-SE19
A simple health record web app.

**Installation**
---
Unzip the repo in a directory, install the backend and frontend seperately.

**UH-Backend**
---
In the root directory, 
```
cd Unihealth-SE19/unihealth_back`
```
After get into `unihealth_back`, to install all the dependencies, run 
```
pip install -r requirements.txt
```

Then, to start backend, run
```python
python app.py
```
The database uri to our private AWS Postgre server is already included in the `app.cfg` , you might change it to any database server you like.

**UH-Frontend**
---
In the root directory,
```
cd Unihealth-SE19/unihealth_front
```
After get into `unihealth_front`, to install all the denpendencies, run
```python
npm install
```
To build frontend, run 
```python
npm run build
```

To serve the frontend, you might use the `serve` package in npm. If you don't have it installed already, run 
```python
npm install -g serve
```

To serve the webpage, run 
```python
serve -s dist
```

**Backend Testing**
---
To run test cases, there is no need to run the backend and frontend. In the original directory, `cd Unihealth-SE19/unihealth_back`. After get into `unihealth_back`, run
```python
pytest -vs tests
```