# explainable_diabetes_prediction

## Dataset utilizzati
Entrambi i dataset utilizzati per creare quello finale sono stati reperiti dalla piattaforma Gene Expression Omnibus: https://www.ncbi.nlm.nih.gov/geo/
Sono stati utilizzati:
* GSE9006: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE9006
* GSE43488: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi

## Struttura delle cartelle
La struttura è formata da:
* **src**: Contiene i codici in python e i progetti in R utilizzati. In src troviamo:
    * **python** divisa a sua volta in:
        * *ml*: Contiene i codici per gli algoritmi di ML
        * *utils*: Contiene i codici per la manipolazione dei dati, come il merge del dataset di espressione genica con i dati dei pazienti, elimazione delle colonne di pazienti con T2D, etc.
    * **R** divisa in:
        * *R_GSE9006_GSE43488* che è un progetto in R, a sua volta diviso in:
            * *script_GSE43488*: Contiene gli script in R riguardo il dataset GSE43488
            * *script_GSE9006*: Contiene gli script in R riguardo il dataset GSE9006
            * *both*: Contiene gli script in R riguardo entrambi i dataset
        * *R_merge* che è un progetto in R contente gli script utilizzati sul dataset creato dal merge dei precedenti. Gli script hanno il nome delle operazioni utilizzate sul dataset, quindi il threshold per decidere la soglia di espressione dei geni e il t-test. 
* **CEL**: Contiene i file .CEL, i file di espressione genica, riguardo il dataset GSE9006
* **txt**: Contiene i file .txt dove sono stati reperiti i dati di espressione e il .txt riferito ai geni selezionati per creare il datasett finale
* **xlsx** divisa in:
    * *Dataset_1*: Contente il dataset effettivo utilizzato
    * *Dataset_2*: Contenente la prova di un secondo 
    * *xlsx_GSE9006*: Contenti i file di output delle manipolazioni effettuate sui file riguardanti il dataset GSE9006
    * *xlsx_GSE43488*: Contenti i file di output delle manipolazioni effettuate sui file riguardanti il dataset GSE9006
* **png** contenenti i grafici creati sul dataset