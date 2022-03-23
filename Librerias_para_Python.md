# Interfaces gráficas comunes.
-----------------------------
GTK - Gimp ToolKit Win/Mac/Linux - Xfce - C/Javascript/Perl/Python/Rust/Vala
TKinter - Win/Mac/Linux - Dinamicos - Perl/Python/Ruby/PHP Nativos -C/C++/Java
PyQt5 - Win/Mac/Linux - C/C++/C#/SystemC/QML/Tcl
Kivy

# Interfaces de consola o (CLI Command Line Interfaces)
-----------------------------------------------------
argparse: libreria estandar para parsear comandos.

curses es muy viejo y ya no tiene soporte, en su lugar esta ncurses o urwid.
urwid tiene mas soporte.
npyscreen
curtsies
Python Prompt Toolkit

fcntl
pyInquirer
win32API
Click
Dockopt
pyFiglet: convierte texto en dibujos de caracteres ascii
Clint

# Otras herramientas CLI para Python
------------------------------------
Cement: proporciona fundaciones para construir cualquier cosa, desde un script basico a un complejo
Cliff: framework para construir programas de lineas de comandos
Plac: simple wraper que usa argparse ocultando complejidad usando decoradores.
EmailCLI: framework para mandar correos en command line Interface.

# Convertir Python en Ejecutables
------------------------------------
Para windows: Auto py to exe: pip install auto-py-to-exe
Desde linux:
- Bulldozer convierte python a apk, pero solo admite la interfaz Kivy
- pyinstaller genera .exe o tar.gz dependiendo del sistema operativo

- cx_Freeze: Multiplataforma
- py2exe: Solo funciona en windows

------------------------------------
- catfish: cat file, es como aplicar el comando cat en un archivo para visualizarlo previamente.

- apturl: ????

- Brlapi: ????

- asn1crypto: Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP

- certifi: Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.

- chardet: Deteccion automatica de encoding.

- click: Composable command line interface toolkit

- colorama: Texto coloreado para terminal multiplataforma.

- command-not-found: ????

- cryptography: is a package which provides cryptographic recipes and primitives to Python developers.

- cupshelpers: ????

- cycler: Composable style cycles ????

- defer: The defer module provides an easy way to write asynchrouns Python programms. It is greatly inspired by Twisted’s defer, but comes without a lot of the dependencies.

- distro-info: Informacion de la distro de linux

- httplib2: A comprehensive HTTP client library, httplib2 supports many features left out of other HTTP libraries.

- idna: Internationalized Domain Names in Applications (IDNA)

- JayDeBeApi:Use JDBC database drivers from Python 2/3 or Jython with a DB-API.

- JPype1:A Python to Java bridge.

- keyring: Store and access your passwords safely.

- languaje-selector: ????

- launchpadlib: Script Launchpad through its web services interfaces. Officially supported.

- lazr.uri: A self-contained, easily reusable library for parsing, manipulating,

- lazr.restfulclient:A programmable client library that takes advantage of the commonalities among

- louis: A simple louis .py file ????

- menulibre: ????

- mugshot: ????

- netifaces: Portable network interface information. ????--- Me ha estado molestando durante algún tiempo que no hay una manera fácil de obtener la(s) dirección(es) de las interfaces de red de la máquina desde Python. Hay una buena razón para esta dificultad, y es que es prácticamente imposible hacerlo de forma portátil. Sin embargo, me parece que debería haber un paquete que pueda instalar fácilmente que se encargue de resolver los detalles para hacerlo en la máquina que está usando, luego puede continuar escribiendo el código de Python sin preocuparse por el meollo del asunto. gran cantidad de API de redes de bajo nivel dependientes del sistema.

- oauth: Library for OAuth version 1.0a. ????

- olefile: Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office)
onboard: ????

- pexpect: Pexpect allows easy control of interactive console applications.
Herramienta hacker como keyboard pero enfocado a aplicaciones de consola.

- power: Cross-platform system power status information.

- psutil: Cross-platform lib for process and system monitoring in Python. - psutil (utilidades de proceso y sistema) es una biblioteca multiplataforma para recuperar información sobre procesos en ejecución y utilización del sistema (CPU, memoria, discos, red, sensores) en Python. Es útil principalmente para la supervisión del sistema, la creación de perfiles y la limitación de los recursos del proceso y la gestión de los procesos en ejecución. Implementa muchas funcionalidades que ofrecen las herramientas clásicas de línea de comandos de UNIX como ps, top, iotop, lsof, netstat, ifconfig, free y otras. psutil actualmente es compatible con las siguientes plataformas:

- pycairo: Pycairo es un módulo de Python que proporciona enlaces para la biblioteca de gráficos cairo. Depende de cairo >= 1.15.10 y funciona con Python 3.6+. Pycairo, incluida esta documentación, tiene licencia solo bajo LGPL-2.1 O MPL-1.1.

Los enlaces de Pycairo están diseñados para coincidir con la API de cairo C lo más cerca posible, y para desviarse solo en casos que claramente se implementan mejor de una manera más 'Pythonic'.

- pycrypto: Cryptographic modules for Python. AES DES RSA ElGamal SHA256 Etc

- pycups: This is a set of Python bindings for the libcups library from the CUPS project. ????

- pycurl: PycURL es una interfaz de Python para libcurl, la biblioteca de transferencia de archivos multiprotocolo. De manera similar al módulo de Python urllib, PycURL se puede usar para obtener objetos identificados por una URL de un programa de Python. Sin embargo, más allá de las búsquedas simples, PycURL expone la mayor parte de la funcionalidad de libcurl.

- pygobject: PyGObject is a Python package which provides bindings for GObject based libraries such as GTK, GStreamer, WebKitGTK, GLib, GIO and many more.

- pyparsing: The pyparsing module is an alternative approach to creating and executing simple grammars, vs. the traditional lex/yacc approach, or the use of regular expressions. The pyparsing module provides a library of classes that client code uses to construct the grammar directly in Python code.

- pySimpleSOAP: Python simple and lightweight SOAP library for client and server webservices interfaces, aimed to be as small and easy as possible, supporting most common functionality. Initially it was inspired by PHP Soap Extension (mimicking its functionality, simplicity and ease of use), with many advanced features added.

- pytz: World timezone definitions, modern and historical

- pyxdg: PyXDG contains implementations of freedesktop.org standards in python.

- pyYAML: YAML is a data serialization format designed for human readability and interaction with scripting languages. PyYAML is a YAML parser and emitter for Python.

- requests: allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

- scour: Scour is an SVG optimizer/cleaner that reduces the size of scalable vector graphics by optimizing structure and removing unnecessary data.

- SecretStorage: Python bindings to FreeDesktop.org Secret Service API. This module provides a way for securely storing passwords and other secrets.

- setuptools: Easily download, build, install, upgrade, and uninstall Python packages

- simplejson: Simple, fast, extensible JSON encoder/decoder for Python

- six: Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions. See the documentation for more information on what is provided

- typing-extensions: Extensiones de escritura: sugerencias de escritura retroportadas y experimentales para Python

El módulo de escritura se agregó a la biblioteca estándar en Python 3.5, pero desde entonces se han agregado muchas características nuevas al módulo. Esto significa que los usuarios de versiones anteriores de Python que no puedan actualizar no podrán aprovechar los nuevos tipos agregados al módulo de escritura, como escribir.Protocolo o escribir.TypedDict.

- ufw: ????

- urllib3: HTTP library with thread-safe connection pooling, file post, and more.

- usb-creator: ????

- wadllib: Navigate HTTP resources using WADL files as guides.

- wheel: This library is the reference implementation of the Python wheel packaging standard, as defined in PEP 427.

- xkit: ????

- re: libreria nativa muy util para expreiones regulares y validar strings.

- collections: colecciones para python

- Pillow - Fork de PIL (Python Image Library), libreria para trabajar con imagenes.

- Keyboard: Libreria para simular un teclado, herramienta hacker.

- Requests: Libreria HTTP famosa
# Scrapy: Libreria de webscraping
# Scrapy: Un sencillo analizador de python desarrollado con python.???

- wxPython: GUI toolkit que se dice es mejor que tkinter
# SQLAlchemy: Bibloteca polemica para gestionar bases de datos, muchos la aman otros la odian.
# PeeWee: Un ORM como SQLAlchemy, mas facil de aprender y tambien esta capacitado para manejar SQLite, Postgress y MySQL, util con django.

- BeautifulSoup: buena para parsear XML y html, util para comenzar a programar
pandas: Buenisima para manejar datos CSV y JSON
psycopg2: Gentiona PostgresSQL
pygame: Libreria de juegos

- reportlab: Libreria para crear archivos PDF
# Twisted: Herramienta para desarrolladores de aplicaciones de red ???

- numpy: ofrece funcionalidades matematicas
# SciPy: Funcionalidades matematicas para cientificos.
# Sympy: Hace evaluaciones algebraicas, expansiones, calculos de numeros complejos
# Numba: Traduce funciones optimizadas que corre en LLVM maquina virtual, es matematica, usa decoradores.
# Scikit-Learn: Inteligencia artificial.
# TensorFlow: Inteligencia artificial.
# Keras: Inteligencia artificial.
# PyTorch: Inteligencia artificial.
# SHAP: Inteligencia artificial.

- matplotlib: Biblioteca de trazado numerico, util para cientificos de datos.
# Seaborn: Lo mismo que matplotlib pero mas bonito
# Bokeh: Lo mismo que matplotlib pero para paginas web
# Pyglet: motor de animacion y creacion de juegos 3D, el responsable de minecraft.
# pyQT: Conjunto de herramientas GUI basado en QT
# pyGTK: Conjunto de herramientas GUI basado en Gimp Tool Kit

- pygobject: Alternativa a pyGTK
# pywin32: Proporciona metodos utiles para windows
# NTLK: Libreria para manipular cadenas, (Natural Lengage Tool Kit)
# Gensim: Libreria de Lenguaje Natural
# SpaCy: Lenguaje Natural mas rapido de todos.
# nose: Framework de testing para python, libreria de test unitarios y similares
# IPython: Aumenta las capacidades de Python
