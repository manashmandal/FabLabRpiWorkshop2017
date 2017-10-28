# Weather Station Basic Data Viz Web App

## Instruction

### Inserting data 

Send `GET` request to this endpoint `/api/insert_data?t=10&h=5&p=5`

Using request library

```python
import requests

print(requests.get('http://website/api/insert_data', params={'h': 29, 't' : 35, 'p' : 500}).text)

```

### Getting latest data

Send `GET` request to this endpoint `/api/data`

```python

import requests

print(requests.get('http://website/api/data').text)
```
