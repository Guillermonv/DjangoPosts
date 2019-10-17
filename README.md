# DjangoPosts
Create Django posts

sudo apt-get update <br>
apt-get install python3-venv <br>
python3 -m venv env <br>
source env/bin/activate<br>
sudo apt install python3-pip<br>
pip3 install django<br>
git clone https://github.com/Guillermonv/DjangoPosts.git<br>
sudo apt install gunicorn<br>
sudo apt-get install -y nginx<br>
<br><br>
#MYSQL<br>
sudo pip3 install mysqlclient fails with mysql_config not found<br>
sudo apt-get install libmysqlclient-dev<br>
#without pip3 it will not going to work for python3<br>
sudo pip3 install mysqlclient<br>
pip3 install -U mysqlclient<br>
pip3 install -U django-mysql<br>
sudo apt install mariadb-client-core-10.1<br>
mysql -u admin -h database-djangopost.ccuweqklkiiu.sa-east-1.rds.amazonaws.com -p<br>
pip install pillow<br>
gunicorn --bind 0.0.0.0:8000 chango2.wsgi:application<br>
