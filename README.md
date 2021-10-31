<h1>Steps to set up an EC2 Ubuntu instance<h1> 
<h2> The sever that we created is a t2.micro instance <h2> 
<h3> Server: Ubuntu Server 20.04 LTS (HVM) <h3> 

 <h4>Add security configs: <h4>
<p align="center">
  <img src="Screenshot 2021-10-31 at 10.41.11 AM.png" width="350" title="Security Group configurations on EC2 Instance (Allow all traffic)!">
</p>

  <h4> Connection </h4>
  Windows: https://www.youtube.com/watch?v=f52IOtTqcP8&t=310s <br>
  Mac: using the link from the connect tab! 

<h4>Installations to set up envs:</h4>
sudo apt-get update <br>
sudo apt-get install python3 <br>
sudo apt-get install python3-pip <br>
sudo pip install flask <br>
sudo apt-get install nginx <br>
sudo apt install gunicorn <br>

  <h4>Make a folder </h4>
mkdir flask-app  <br>
sudo nano app.py <br>

  <h4> After creating the flask app set up Gunicorn and nginx </h4> 
cd /etc/nginx <br>
cd sites-enabled <br>
sudo vi flaskapp <br>
<p align="center">
  <img src="Screenshot 2021-10-31 at 10.50.20 AM.png" width="350" title="Security Group configurations on EC2 Instance (Allow all traffic)!">
</p> <br>
sudo service nginx restart <br>
cd ~  <br>

  <h4>To run the app </h4>
python3 app.py (or) gunicorn app:app <br>

