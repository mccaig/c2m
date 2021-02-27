# c2m

generate files from mustache template using csv as a data source

## Install
```
pip3 install -r requirements.txt
```

## Usage
```
python3 c2m.py [csvFile] [templateFile] [outFileField] [outFileExtension]
```

Example:
```
python3 c2m.py example.csv example.md Name md
```
* Reads data from example.csv (assumes first row is the field names)
* Uses example.md as a template
* Output files are named according to 'Name' field in each CSV row
* Output file extension is md