library(affy)
library(affyio)


#### Prima piattaforma
cel_path = "CEL\\piattaforma_1"

cel_files <- as.character(list.files(cel_path, pattern = "\\.CEL$", full.names = TRUE))

data = ReadAffy(filenames = cel_files)
print(data)

##### Seconda piattaforma

cel_path_2 = "D:\\Uni\\Tesi\\Dataset\\GSE9006\\Dataset_GSE9006\\CEL\\piattaforma_2"

cel_files_2 <- as.character(list.files(cel_path_2, pattern = "\\.CEL$", full.names = TRUE))
print(cel_files_2)

if (!is.character(cel_files_2)) {
  stop("Errore: cel_files non è un vettore di caratteri")
}

if(length(cel_files_2) == 0) {
  stop("Nessun file CEL trovato nel percorso specificato.")
}

data_2 = ReadAffy(filenames = cel_files_2)
print(data_2)
