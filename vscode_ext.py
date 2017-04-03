import requests
from pprint import pprint
import re

proxies = {
    'http':'http://127.0.0.1:3128',
    'https':'https://127.0.0.1:3128'
}
url = input('url: ')
if url == '':
    author = input('author: ')
    name = input('name: ')
    url = 'https://marketplace.visualstudio.com/items?itemName='+author+'.'+name
else:
    data = url.replace('https://marketplace.visualstudio.com/items?itemName=','').split('.')
    author = data[0]
    name = ''.join(data[1:])
print('calculando versión...')
r = requests.get(url, proxies=proxies)
version = re.findall('"version":"(.*?)"',r.text)[0]
ruta = 'https://'+author+'.gallery.vsassets.io/_apis/public/gallery/publisher/'+author+'/extension/'+name+'/'+version+'/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage'
print('Ruta para '+author+'.'+name+':'+version+' --> '+ruta)
print('Nombre propuesto: '+author+'.'+name+'_'+version+'.vsix')