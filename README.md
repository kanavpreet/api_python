Build the image using the following command



$ sudo  docker build -t simple-flask-app:latest .

Run the Docker container using the command shown below.

$ sudo docker run -d -p 5000:5000 simple-flask-app

The application will be accessible at http:127.0.0.1:5000/hello will show hello Stranger and http:127.0.0.1:5000/hello/name will show hello name
