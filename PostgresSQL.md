Intallation and configuration for postgresql and pgadmin4
===

Postgresql
---

`sudo -u postgres psql` # psql inicia postgres: 
`sudo -u o --user postgres` # en este caso el usuario es postgres, usuario por defecto
dentro de postgres la consola se ve algo asi como
`postgres=#` # esto signidica que estoy dentro de postgres
es necesario escribir una contraseña para el usuario postgres, casi obligatorio

`postgres=# alter user postgres password 'admin'`
debe salir ALTER ROLE, en este caso la contraseña es *admin*

`\l # lista las bases de datos`
`\q # sale de postgres`

PgAdmin4
---

Some linux distributions not been updated, in my personal case only find pgadmin 3 in the store, but postgres is in the version
4, when open pgadmin3 with postgres 4 cause incompatibilities. for install pgadmin 4:

1. uninstall pgadmin 3 from store application.
2. go for google and write "pgadmin 4 for linux" or go to next (link)[https://www.pgadmin.org/download/pgadmin-4-apt/] and follow
the instructions.
3. install the public key for repository `sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add`
4. Create repository configuration file. `sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'`
5. Install pgAdmin4, they are 3 options `sudo apt install pgadmin4` for both options destop and web, `sudo apt install pgadmin4-desktop`
only desktop and `sudo apt install pgadmin4-web` only web server
6. Configure web server if you install pgadmin4-web. `sudo /usr/pgadmin4/bin/setup-web.sh`
7. Save the passwords into a password manager.
8. Procure that the password for pgAdmin web-server has been the same for pgAdmin desktop.
