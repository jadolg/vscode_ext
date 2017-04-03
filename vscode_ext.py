#!/usr/bin/env python3

import re
import requests

PROXIES = {
    'http':'http://127.0.0.1:3128',
    'https':'https://127.0.0.1:3128'
}

url = input('url (dejar vacío para especificar nombre y autor): ')
if url == '':
    author = input('autor: ')
    name = input('nombre: ')
    url = 'https://marketplace.visualstudio.com/items?itemName='+author+'.'+name
else:
    data = url.replace('https://marketplace.visualstudio.com/items?itemName=','').split('.')
    author = data[0]
    name = ''.join(data[1:])
print('calculando versión...')
r = requests.get(url, proxies=PROXIES)
version = re.findall('"version":"(.*?)"',r.text)[0]
ruta = 'https://'+author+'.gallery.vsassets.io/_apis/public/gallery/publisher/'+author+'/extension/'+name+'/'+version+'/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage'
print('Ruta para '+author+'.'+name+':'+version+' --> '+ruta)
print('Nombre propuesto: '+author+'.'+name+'_'+version+'.vsix')
