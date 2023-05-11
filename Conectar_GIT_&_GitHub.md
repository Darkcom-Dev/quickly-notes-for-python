# Conectando los repositoios de GIT y GitHub.

Este ha sido un chicharron que apenas logro resolver, como veran no soy muy experto en GIT y llevo mucho tiempo sin sobrevivir
con esta herramienta que no le veo la gracia, sin embargo creé un repositorio para escribir solo documentacion, mis notas
personales que contendra todo tipo de temas relacionados con Python.

## Configurando GitHub.
---------------------------------------------------

- Ingresa a la cuenta de GitHub o crear una cuenta
- Crear un repositorio - con titulo y descripción
- En la pestaña del titulo del repositorio hay un boton verde 'Code ⇓'
- De las opciones HTTPS | SSH | GitHub CLI - elige HTTPS y copia el enlace

## Configurar el Token.
---------------------------------------------------

- Ingresa a la cuenta
- Clic en el Logo del Avatar/Settings/Developer settings/Personal Access Token
- Clic en Generate token, escribe un titulo para el token
- Selecciona los permisos necesarios y Clic en generar token

El titulo del token sirve como nombre de usuario dentro de GIT y el codigo del token sirve como contraseña.
Nota: para poder crear un token debe estar habilitado el doble factor de autenticacion.

## Conectar GIT con el repositorio de GitHub.
--------------------------------------------------

- Crear una carpeta con el mismo nombre del repositorio de GitHub.
- Mueva o cree los archivos dentro de la carpeta de repositorio.
- Abrir una terminal en la misma carpeta de repositorio.
- Escriba los siguientes comandos:
```
	$git init # Convierte la carpeta del sistema en una carpeta de repositorio.
	$git pull 'Direccion HTTPS del repositorio de GitHub' # Esto baja los archivos del repositorio y hace fetch.
	$git status # Esto mostrará los archivos que no sea han agregado a la rama principal.
	$git add . # Esto agrega los archivos al commit
	$git commit -m 'Escribe un mensaje' # Esto crea un mensaje junto a los archivos
```
En este punto puede que te pida configurar GIT con nombre de usuario y email, Escribe el mismo nombre de usuario de GitHub y 
el mismo correo con el que registraste de cuenta de GitHub.
```
	$git branch -M main # Crea una rama en este caso main
	$git pull -u origin main # Hace una peticion de envio desde el origen(local) a main(GitHub)
```
En este paso te pide un nombre de usuario que es el titulo del token y una contraseña que es codigo del token.

## Como solucionar el error de rechazo de historias.

Esto ocurre porque has creado un proyecto en una carpeta local en tu propio PC que no tiene relacion con un repositorio de Github. algo comun que hacemos es conectarnos a Github, Crear un repositorio con el nombre de nuestro proyecto y luego tratar de conectar nuestro repositorio personal usando los comandos de Git. pero como tienen archivos distintos y las ramas son ditintas se presenta este conflicto.

Para solucionarlo:

1. Crea el repositorio, pero no agregues un archivo readme.md y tampoco una licencia.
2. Comprueba que tengas los cambios actualizados con `git status`, actualiza de ser necesarios con `git add .` y `git commit -m "mensaje"`.
3. Agrega el parametro `--allow-unrelated-histories` al pull `git pull --allow-unrelated-histories <URL-del-repositorio-remoto>.` Esto permitirá mezclar las ramas de los repositorios local y github, pero generará conflictos si existen archivos coincidentes, por es necesario el cumplir el punto 1.
4. Agrega el repositorio remoto de GitHub utilizando el comando `git remote add origin <URL-del-repositorio-remoto>`.
5. Envía los cambios al repositorio remoto utilizando el comando git push -u origin master. Si estás trabajando en una rama diferente a la rama principal, reemplaza "master" con el nombre de tu rama.

Con esto es mas que suficiente y deberia funcionar corretamente.

