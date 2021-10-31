<h1>Steps to set up an EC2 Ubuntu instance<h1> <br>
<h3> The sever that we created is a t2.micro instance <h3> <br>
<h3> Server: Ubuntu Server 20.04 LTS (HVM) <h3> <br>

  <b>Add security configs: </b> <br>
<p align="center">
  <img src="Screenshot 2021-10-31 at 10.41.11 AM.png" width="350" title="Security Group configurations on EC2 Instance (Allow all traffic)!">
</p>


#Installations to set up envs: <br>
sudo apt-get update <br>
sudo apt-get install python3 <br>
sudo apt-get install python3-pip <br>
sudo pip install flask <br>
sudo apt-get install nginx <br>
sudo apt install gunicorn <br>

#Make a folder <br>
mkdir flask-app  <br>
sudo nano app.py <br>

#After creating the flask app set up Gunicorn and nginx <br>
cd /etc/nginx <br>
cd sites-enabled <br>
sudo vi flaskapp <br>
<p align="center">
  <img src="Screenshot 2021-10-31 at 10.50.20 AM.png" width="350" title="Security Group configurations on EC2 Instance (Allow all traffic)!">
</p> <br>
sudo service nginx restart <br>
cd ~  <br>

#To run the app <br>
python3 app.py (or) gunicorn app:app <br>

