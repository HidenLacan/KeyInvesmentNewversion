from django.shortcuts import render
from django.views import View
import openai
import requests

class Index(View):
    
 

    def get(self,resquest):
        
        return render(resquest,'index.html')
    
    def post(self,resquest):
        
    
        openai.api_key = 'API_KEY'
        
        sector = resquest.POST.get('sector','')
        habilidad = resquest.POST.get('habilidad','')
        idea = resquest.POST.get('idea','')
        inversion= resquest.POST.get('inversion','')
        ganancia = resquest.POST.get('ganancia','')
        produccion = resquest.POST.get('produccion','')
        location = resquest.POST.get('location','')
        
        url = f'https://www.economia.gob.mx/apidatamexico/tesseract/data.jsonrecords?Municipality=19021&cube=economy_foreign_trade_mun&drilldowns=Chapter%2CHS2%2CHS4%2CMunicipality%2CHS6%2CProduct+Level&locale=es&measures=Trade+Value&parents=false&sort=Trade+Value.desc'
        responses = requests.get(url)
        data_api = responses.json()
        consume_api = data_api['data'][:20]
        data_hs6 = [data_consume_api['HS6'] for data_consume_api in consume_api]
        string_convert_data = ','.join(map(str,data_hs6))
        messages = f"Sector:{sector}\nHabilidad:{habilidad}\nIdea:{idea}\nInversion:{inversion}\nProduccion:{produccion}\nGanancia:{ganancia}\nLocation:{location}\ninformation:{string_convert_data}"
        economia = "Según datos del Censo Económico 2019, los sectores económicos que concentraron más unidades económicas en General Escobedo fueron Comercio al por Menor (4,220 unidades), Otros Servicios Excepto Actividades Gubernamentales (1,646 unidades) y Servicios de Alojamiento Temporal y de Preparación de Alimentos y Bebidas (1,376 unidades)."
        poblacion = "La población total de General Escobedo en 2020 fue 481,213 habitantes, siendo 49.7% mujeres y 50.3% hombres.Los ranos de edad que concentraron mayor población fueron 15 a 19 años (43,932 habitantes), 20 a 24 años (43,591 habitantes) y 10 a 14 años (43,414 habitantes). Entre ellos concentraron el 27.2% de la población total.Según el tipo de institución de educación superior, la mayor cantidad de egresados en el ciclo escolar 2020-2021 en General Escobedo egresaron de: Universidades Públicas Estatales (37.9%, 171,130 egresados), Universidades Tecnológicas (19.2%, 86,875 egresados) y Tecnológico Nacional de México (15.5%, 70,205 egresados).Por nivel educativo, destacan los egresados de licenciatura (80.3%, 362,706 egresados) y técnico superior universitario (11.1%, 50,001 egresados).Los gráficos muestran los egresados por tipo de institución de educación superior y nivel educacional. Puede seleccionar una categoría en uno de los gráficos para filtrar la información mostrada en el otro gráfico."
        print(f'{consume_api}')
        
        
            
        response = openai.ChatCompletion.create(
             ### change the gpt 
             model='gpt-3.5-turbo',
             temperature = 1,
             messages=[
                 {'role': 'system', 'content': 'Eres una inteligencia artificial dedicada a la maximizacion de los negocios financieros'},
                 {'role': 'user', 'content':'Haz una valoracion preliminar de inversion destacando valor presente neto, tasa interna de retorno, metodo de perio de recuperacion, indice de rentabilidad,comportamiento de consumidor'+ 'tomando en cuenta su economia' + economia + 'poblacion y las posibles demandas : '+ poblacion  + messages}
             ]
         )    
            
        reply = response.choices[0].message.content.strip()
        
        datos = []

        
        datos.append(reply)    
            
        message = datos 
        
        
        
        
        
        return render(resquest,'response.html',{'message':message})
    
    