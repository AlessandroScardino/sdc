# *DATABASE SYNC*
### *Simone Franceschini 4CI*
###

Questo programma permette di trasferire i dati relativi ai ricevimenti dei professori della scuola I.T.I. Guglielmo Marconi dal database MySQL (edu-x04) al database SQL Server (edu-w01)

### **CHANGELOG**
##### *version 01.01* :
- Gestione degli argomenti. **-v"** per attivare il verbose. 
- Scrittura su un file di log, **sync.log**, delle azione compiute ed eventuali errori
- Gestione di un file di configurazione `json` dove è neccessario inserire le informazioni per l'accesso ai database

### **COME INSTALLARE LE LIBRERIE DI PYTHON NECESSARIE AL SOFTWARE (GUIDA PER KALI LINUX / DEBIAN)**
- Aprire il terminale in modalità amministratore.
- Digitare **`pip3 install mysql`** e attendere il completamento dell'installazione. 
	Nel caso si verificassero eventuali errori seguire la guida a questo link: https://www.mysqltutorial.org/getting-started-mysql-python-connector/
- Digitare **`pip3 install pymssql`** e attendere il completamento dell'installazione.

###
#### **PROGRAMMA TESTATO SULLA VERSIONE 3.6.4 DI PYTHON**
#### **PROGRAMMA TESTATO SU KALI LINUX 2018**

------------------------------------------------------
### **PYTHON DOWNLOAD**
###

| LANGUAGE | DOWNLOAD |
| ------ | ------ |
| ENG | https://www.python.org/downloads/ |
| ITA | https://www.python.it/download/ |

###### *Markdown developed with [**Dillinger**](https://dillinger.io/), the Online Markdown Editor.*