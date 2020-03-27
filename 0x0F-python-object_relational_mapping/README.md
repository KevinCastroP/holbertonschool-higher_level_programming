# Python Object relational mapping (ORM)

## Before you start please make sure your MySQL server is in 5.7 version

### How to install MySQL 5.7

<p> $ sudo apt-get update </p>
<p> $ sudo apt-get install mysql-server-5.7 </p>

### How to connect to your MySQL server:

<p> $ mysql -hlocalhost -uroot -p </p>
<p> Password: </p>
<p> Welcome to the MySQL monitor.  Commands end with ; or \g. </p>
<p> Your MySQL connection id is 42 </p>
<p> Server version: 5.7.8-rc MySQL Community Server (GPL) </p>

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

## More info

### Install MySQLdb module version 1.3.x

<p> $ sudo apt-get install libmysqlclient-dev </p>
<p> $ sudo apt-get install zlib1g-dev </p>
<p> $ sudo pip3 install mysqlclient==1.3.10 </p>
<p>...</p>
<p>$ python3</p>
<p>>>> import MySQLdb</p>
<p>>>> MySQLdb.__version__</p>
<p>'1.3.10'</p>

### Install SQLAlchemy module version 1.2.x

<p>$ pip3 install SQLAlchemy==1.2.5</p>
<p>...</p>
<p>$ python3</p>
<p>>>> import sqlalchemy</p>
<p>>>> sqlalchemy.__version__ </p>
<p>'1.2.5'</p>