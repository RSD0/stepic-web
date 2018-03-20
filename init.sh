sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf $HOME/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf $HOME/web/etc/gunicorn-django.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start