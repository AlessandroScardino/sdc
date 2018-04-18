# -*- coding: utf-8 -*-

"""
    Simone Franceschini 
    sync.py

    Questo programma permette di trasferire i dati relativi ai ricevimenti dei professori della
    scuola I.T.I. Guglielmo Marconi dal database MySQL (edu-x04) al database SQL Server (edu-w01).

"""

import mysql.connector
import pymssql
import datetime
import sys
import os
import locale

def logmsg(msg_text):
    """
    Scrive su file di log l` `msg_text`

    :param msg_text: Il testo del messaggio
    :type msg_text: string
    :return: None
    :rtype: None
    """

    # se `boold = True` stampa a video il messaggio di testo
    if boold:
        print(msg_text)

    # -- scrive la data attuale e il messaggio
    log_file.write(e_time + " " +  msg_text + "\n")

    return None


if __name__ == "__main__":

    boold = True

    # -- controlla tutti gli argomenti passati
    for i in range(len(sys.argv)):

        # -- se l'argomento passato corrisponde a `-v`, imposta 'bool = True`
        if sys.argv[i] == "-v":
            boold = True

    # -- controlla se il file di log esiste, nel caso non esistesse lo crea
    if not os.path.isfile('./sync.log'):
        log_file = open("sync.log", "w")
    else:
        log_file = open("sync.log", "a")

    # -- prende la data corrente
    if str(locale.getdefaultlocale()[0]) == "it_IT":
        e_time = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S.%f")
    else:
        e_time = datetime.datetime.utcnow().strftime("%m/%d/%Y %H:%M:%S.%f")

    # -- il programma vero e proprio inizia da qui
    error = False

    # -- prova a connettersi al database MySQL
    try:
        mysql_conn = mysql.connector.connect(user='4ci', password='4ci', host='edu-x04', database='ricevimenti')
        logmsg("Connessione al database MySQL avvenuta con successo")
    except:
        logmsg("C'è stato un errore con la connessione al database MySQL")
        sys.exit()

    mysql_cursor = mysql_conn.cursor()

    # -- impostazione delle informazioni da prelevare dal database MySQL dalla tabella
    # --`ricevimenti.ricevimenti` dell'utente `4ci`
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
                  "ricevimenti.ricevimenti"

    # -- prova a selezionare e salvare le informazioni precedentemente definite nella variabile `mysql_query`
    try:
        mysql_cursor.execute(mysql_query)
        logmsg("Salvataggio dei dati della tabella del database MySQL avvenuto con successo")
    except:
        logmsg("C'è stato un errore con il salvataggio dei dati della tabella del database MySQL")
        sys.exit()

    # -- prova a connettersi al database SQL Server
    try:
        mssql_conn = pymssql.connect(user='quartaat', password='quartaat', host='edu-w01', database='db4At')
        logmsg("Connessione al database SQL Server avvenuta con successo")
    except:
        logmsg("C'è stato un errore con la connessione al database SQL Server")
        sys.exit()

    mssql_cursor = mssql_conn.cursor()

    # -- prende le informazioni precedentemente salvate nella variabile `mysql_cursor` e le assegna ai relativi campi
    for (tupla) in mysql_cursor:
        data = str(tupla[0].split("-")[0]) + str(tupla[0].split("-")[1]) + str(
            tupla[0].split("-")[2]) + " 00:00:00 AM"  # input format: yyyy-mm-dd; output: dd-mm-yyyy2
        data_int = tupla[1]
        ora = tupla[2]
        orario = tupla[3]
        docente = tupla[4]
        studente = tupla[5]
        classe = tupla[6]
        plesso = tupla[7]
        luogo = tupla[8]
        cellulare = tupla[9]

        # -- impostazione delle informazioni che andranno inserite nel database SQL Server
        # -- nella tabella `dbo.ricevimenti`
        mssql_query = "INSERT dbo.ricevimenti VALUES ('" \
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

        # -- prova a scrivere e a salvare le informazioni precedentemente definite nella variabile `mssql_query`
        try:
            mssql_cursor.execute(mssql_query)
        except:
            logmsg("C'è stato un errore con l'inserimento dei dati nella tabella del database SQL Server")
            sys.exit()

    logmsg("Inserimento dei dati nella tabella del database SQL Server avvenuto con successo")

    mysql_cursor.close()
    mssql_cursor.close()

    mssql_conn.commit()

     # -- chiusura della connesione MySQL e SQL Server

    mysql_conn.close()
    mssql_conn.close()
    
    log_file.close()
