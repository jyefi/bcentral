## Read data from Banco Central de Chile

### Use
Pull this project or download.

### Make and .env file
To run bcentral-api.py you MUST register and get credentials from https://si3.bcentral.cl/Siete/es/Siete/API?respuesta=

.env file must content the following variables:
BANCO_CENTRAL_USER=myuser
BANCO_CENTRAL_PASSWORD=mysupersecretpass

After that you can use Banco Central API ejecuting "bcentral-api.py" replacing the data series name.

You can find all avaiable data series in 
https://si3.bcentral.cl/estadisticas/Principal1/Web_Services/Webservices/series.xlsx

##### Disclaimer
This program is distributed AS IS, with no warranties.
Use with care, don't abuse 