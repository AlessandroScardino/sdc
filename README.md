# *DATABASE SYNC*
### *Simone Franceschini 4CI*
###

Questo programma permette di trasferire i dati relativi ai ricevimenti dei professori della scuola I.T.I. Guglielmo Marconi dal database MySQL (edu-x04) al database SQL Server (edu-w01).

### **CHANGELOG**
- Gestione dell`argomento **-v"** per attivare il verbose. 
- Scrittura su un file di log, **sync.log**, delle azione compiute ed eventuali errori

### **COME INSTALLARE LE PYTHON E LE LIBRERIE NECESSARIE AL PROGRAMMA (GUIDA PER KALI LINUX / DEBIAN)**
- Aprire il terminale in modalità amministratore.
- Assicurarsi di avere l`ultima versione di Python installata.
- Fare un update digitando **`apt-get update`**.
- Per installare Python digitare **`apt-get install python3`**.
- Per installare il **`pip`** di Python  e successivamente **`apt-get install -y python3-pip`**
- Digitare **`pip3 install mysql`** e attendere il completamento dell'installazione. 
	Nel caso si verificassero eventuali errori seguire la guida a [**questo link**](https://www.mysqltutorial.org/getting-started-mysql-python-connector/).
- Digitare **`pip3 install pymssql`** e attendere il completamento dell'installazione.

###
#### **PROGRAMMA TESTATO SULLA VERSIONE 3.6.4 DI PYTHON**
#### **PROGRAMMA TESTATO SU KALI LINUX 2018**

------------------------------------------------------


###### *Markdown developed with [**PyCharm 2018**](https://https://www.jetbrains.com/pycharm//)*