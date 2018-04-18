# -*- coding: utf-8 -*-

"""
    Simone Franceschini 
    sync.py

"""

import mysql.connector
import pymssql
import datetime
import socket
import sys
import os
import locale
import json


def logmsg(msg_text):
    """
    Write the msg_text in the log file and print it if boold.

    :param msg_text: The text message that will be write in the log
    :type msg_text: string
    :return: None
    :rtype: None
    """

    # if boold = True, print the msg text
    if boold:
        print(msg_text)

    # write in the log file the name of the computer, the ip, the execution time and the msg text
    log_file.write(e_time + " " + os.environ['computername'] + " " + str(s.getsockname()[0]) + " " + msg_text + "\n")

    return None


def take_info_from_mysql():
    """
    Take the information relative to the recepciones from the MySQL database.

    :param None
    :type None
    :return: None
    :rtype: None
    """

    try:
        mysql_conn = mysql.connector.connect(user=user_mysql, password=pass_mysql, host=host_mysql, database=db_mysql)
        logmsg("Connessione al database MySQL avvenuta con successo")
        is_mysql_online = True
    except():
        logmsg("C'è stato un errore con la connessione al database MySQL")

    if is_mysql_online:

        mysql_cursor = mysql_conn.cursor()

        # selecting the information from the table 'table_mysql'
        mysql_query = "SELECT data," \
                      " data_int," \
                      " ora," \
                      " orario," \
                      " docente," \
                      " studente," \
                      " classe," \
                      " plesso," \
                      " luogo," \
                      " cellulare" \
                      " FROM " \
                      + table_mysql
        try:
            mysql_cursor.execute(mysql_query)
            logmsg("Salvataggio dei dati della tabella del database MySQL avvenuto con successo")
        except():
            logmsg("C'è stato un errore con il salvataggio dei dati della tabella del database MySQL")

    return None


def write_info_into_sqlserver():
    """
    Write the information that we take from the MySQL database to the SQL Server database.

    :param None
    :type None
    :return: None
    :rtype: None
    """

    try:
        mssql_conn = pymssql.connect(user=user_sqlserver, password=pass_sqlserver, host=host_sqlserver,
                                 database=db_sqlserver)
        logmsg("Connessione al database SQL Server avvenuta con successo")
        is_sqlserver_online = True
    except():
        logmsg("C'è stato un errore con la connessione al database SQL Server")

    if is_sqlserver_online:

        mssql_cursor = mssql_conn.cursor()

        for (tupla) in mysql_cursor:
            data = str(tupla[0].split("-")[0])+str(tupla[0].split("-")[1])+str(tupla[0].split("-")[2]) + " 00:00:00 AM" #input format: yyyy-mm-dd; output: dd-mm-yyyy2
            data_int = tupla[1]
            ora = tupla[2]
            orario = tupla[3]
            docente = tupla[4]
            studente = tupla[5]
            classe = tupla[6]
            plesso = tupla[7]
            luogo = tupla[8]
            cellulare = tupla[9]

            # writing the information into the table 'table_sqlserver'
            mssql_query = "INSERT " + table_sqlserver + " VALUES ('" \
                          + data + "','" \
                          + data_int + "','" \
                          + ora + "','" \
                          + orario + "','" \
                          + docente + "','" \
                          + studente + "','" \
                          + classe + "','" \
                          + plesso + "','" \
                          + luogo + "','" \
                          + cellulare + "',GETDATE());"
            try:
                mssql_cursor.execute(mssql_query)
                error = False
            except():
                logmsg("C'è stato un errore con l'inserimento dei dati nella tabella del database SQL Server")
                error = True

    if not error:
        logmsg("Inserimento dei dati nella tabella del database SQL Server avvenuto con successo")

    return None


if __name__ == "__main__":

    boold = True

    for i in range(len(sys.argv)):

        # if an argument passed equals "-v", set boold = True
        if sys.argv[i] == "-v":
            boold = True

    # if sync.log doesn't exist, create it
    if not os.path.isfile('./sync.log'):
        log_file = open("sync.log", "w")
    else:
        log_file = open("sync.log", "a")

    # take the current time
    if str(locale.getdefaultlocale()[0]) == "it_IT":
        e_time = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S.%f")
    else:
        e_time = datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S.%f")

    # get the ip of the pc
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    # take the info for the authorization for the access to the database from file ./conf.json
    with open('.\conf.json', 'r') as f:
        info = json.load(f)

    user_mysql = info['user_mysql']
    pass_mysql = info['pass_mysql']
    host_mysql = info['host_mysql']
    db_mysql = info['host_mysql']
    table_mysql = info['table_mysql']

    user_sqlserver = info['user_sqlserver']
    pass_sqlserver = info['user_sqlserver']
    host_sqlserver = info['user_sqlserver']
    db_sqlserver = info['user_sqlserver']
    table_sqlserver = info['table_sqlserver']

    # set this variable global
    mysql_conn = ""
    mysql_cursor = ""
    mysql_query = ""

    mssql_conn = ""
    mssql_cursor = ""
    mssql_query = ""

    is_mysql_online = False
    is_sqlserver_online = False

    take_info_from_mysql()

    if is_mysql_online:
        write_info_into_sqlserver()

        mysql_cursor.close()

        if is_sqlserver_online:
            mssql_cursor.close()

            mssql_conn.commit()

            # chiusura connection mysql
            mysql_conn.close()
            mssql_conn.close()

    log_file.close()
