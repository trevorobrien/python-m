docker build -t flask-heroku:latest .
docker run -d -p 5000:5000 flask-heroku
heroku container:login
heroku container:push web --app test-cci
heroku container:release web --app