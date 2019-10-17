# DjangoPosts
Create Django posts

sudo apt-get update
apt-get install python3-venv
python3 -m venv env
source env/bin/activate
sudo apt install python3-pip
pip3 install django
git clone https://github.com/Guillermonv/DjangoPosts.git
sudo apt install gunicorn
sudo apt-get install -y nginx

#MYSQL
sudo pip3 install mysqlclient fails with mysql_config not found
sudo apt-get install libmysqlclient-dev
#without pip3 it will not going to work for python3
sudo pip3 install mysqlclient
pip3 install -U mysqlclient
pip3 install -U django-mysql
sudo apt install mariadb-client-core-10.1
mysql -u admin -h database-djangopost.ccuweqklkiiu.sa-east-1.rds.amazonaws.com -p
pip install pillow
gunicorn --bind 0.0.0.0:8000 chango2.wsgi:application
