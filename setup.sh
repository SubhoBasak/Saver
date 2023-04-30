sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
chmod 664 db.sqlite3
sudo chown :www-data db.sqlite3
sudo chown :www-data ~/Saver