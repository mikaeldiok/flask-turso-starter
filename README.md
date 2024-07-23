based on [Jelmerdejong's flask-app-blueprint](https://github.com/jelmerdejong/flask-app-blueprint)

updated the requirements for flask 2 and other

Turso database ready! just modify the env

# start the app:
1. make a virtual env `python3 -m venv venv`
2. activate it `. venv/bin/activate`
3. install req `pip3 install -r requirements.txt`
4. modify the .flaskenv
5. migrate the db `flask db upgrade`
6. seed the admin and sample user `flask seed_db`
7. run the app `flask run` or hot reload `flask --debug run`
