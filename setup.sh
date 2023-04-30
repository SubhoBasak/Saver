sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
chmod 777 db.sqlite3
python3 manage.py coll
sudo chown :www-data db.sqlite3
sudo chown :www-data ~/Saver
sudo service apache2 restart
