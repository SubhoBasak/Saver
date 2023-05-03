sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
chmod 777 db.sqlite3
sudo chmod 777 /home/ubuntu
sudo chown :www-data db.sqlite3
sudo chown :www-data ~/Saver
sudo service apache2 restart
source venv/bin/activate
python3 manage.py collectstatic
exit