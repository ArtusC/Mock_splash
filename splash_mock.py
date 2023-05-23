"""
Para rodar:
    1) Através do arquivo python:
    * Na pasta onde estará o arquivo HTML rodar o server que terá o arquivo HTML: 
        python3 -m http.server 8000
        Poderá ver através de localhost:8000
    * Subir o container do splash:
        docker run --name splash -p 8050:8050 scrapinghub/splash
    * Pegar o IP do Gateway do container Splash:
        docker inspect splash
        Algo assim: "Gateway": "172.17.0.1",
    * A URL da response deverá ser: hhtp://(IP do Gateway do container):(porta do server)
        url = 'http://172.17.0.1:8000'
    * Alterar o script lua
    * Rodar o comando do arquivo python


    2) Através da API do Splash:
    * A única diferença será o último passo:
        * Acessar a API usando a porta do Splash: localhost:8050
        * No lugar da url irá: http://172.17.0.1:8000
        * Colocar o script lua que deseja testar
        * Render me!

"""

import requests

script = """
function main(splash, args)
  splash:go(args.url)
  splash:wait(0.5)
  local click_button = splash:jsfunc([[
    function () {
      var element = document.querySelector('a[onclick*="mojarra.jsfcljs"] img[title="IPTU - Não Residencial"]');
      var event = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
      });
      element.parentElement.dispatchEvent(event);
    }
  ]])
  click_button()
  splash:wait(1)
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
"""

url = 'http://172.17.0.1:8000'

splash_url = 'http://localhost:8050/run'

response = requests.post(splash_url, json={
    'lua_source': script,
    'url': url
})
png_data = response

print(f"RESPONSE: {png_data.text}")

# if response.status_code == 200:
#     html_content = response.text
#     print(html_content)
# else:
#     print('Request failed with status code:', response.status_code)