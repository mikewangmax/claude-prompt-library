Here is the converted CSV data based on your JSON input and requirements:

```csv
"name";"age";"city";"email"
"John Doe";"30";"New York";"john.doe@example.com"
"Jane Smith";"25";"London";"jane.smith@example.com"
"Bob Johnson";"35";"Paris";"bob.johnson@example.com"
```

### Breakdown of the Conversion

1. **Column order**: The columns follow the specified order -- `name`, `age`, `city`, `email`.
2. **Delimiter**: Semicolons (`;`) are used as delimiters instead of the default comma.
3. **Quoting**: All values, including numeric ones like `age`, are enclosed in double quotes (`"`), as requested.

### How to Save and Use the CSV File

1. Copy the CSV content above (without the code block markers).
2. Open a plain text editor (e.g., Notepad on Windows, TextEdit on macOS in plain text mode, or VS Code).
3. Paste the content and save the file with a `.csv` extension (e.g., `contacts.csv`).
4. Make sure the file encoding is set to **UTF-8** for maximum compatibility.

### Importing into Spreadsheet Applications

- **Microsoft Excel**: When opening the file, Excel may launch the Text Import Wizard. Select "Delimited", then check "Semicolon" as the delimiter and set the text qualifier to double quotes (`"`).
- **Google Sheets**: Use `File > Import`, upload the CSV, and set the separator type to "Custom" with `;` as the separator.
- **LibreOffice Calc**: On the import dialog, select semicolon as the separator and double quote as the text delimiter.

### Notes

- Since the `age` field is numeric but enclosed in quotes, some spreadsheet applications may import it as text. If you need it as a number, you can remove the quotes around the age values or convert the column after import.
- If any future data contains semicolons or double quotes within the values themselves, the double quotes inside the value should be escaped by doubling them (e.g., `"value with ""quotes"""`).
