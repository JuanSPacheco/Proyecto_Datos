from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'proyecto_datos'
    )
    print("Conexión exitosa")
    cursor = connection.cursor()
    cursor.execute("select municipio.nombre, count(caso.id) from caso, municipio, persona where caso.cedula_persona = persona.cedula and municipio.codigo = persona.codigo_municipio group by municipio.nombre")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    app = Dash(__name__)
    fig1 = px.bar(rows, x = 0, y = 1, color_discrete_sequence = ["#b52a64"], title = "Casos por municipio")       
    fig1.update_xaxes(title_text='Municipio')
    fig1.update_yaxes(title_text='Frecuencia')
    
    cursor.execute("SELECT departamento.nombre, COUNT(codigo_municipio) FROM persona INNER JOIN caso ON persona.cedula = caso.cedula_persona INNER JOIN municipio ON persona.codigo_municipio = municipio.codigo INNER JOIN departamento ON municipio.codigo_departamento = departamento.codigo GROUP BY departamento.nombre")
    rows2 = cursor.fetchmany(30)
    for row in rows2:
        print(row)
    fig2 = px.bar(rows2, x = 0, y = 1, color_discrete_sequence = ["#3584EE"], title = "Casos por departamento")       
    fig2.update_xaxes(title_text='Departamento')
    fig2.update_yaxes(title_text='Frecuencia')
    
    
    cursor.execute("select sexo, count(sexo) from persona group by sexo")
    rows3 = cursor.fetchmany(30)
    for row in rows3:
        print(row)
    fig3 = px.pie(rows3, values=1, names=0, color_discrete_sequence = ["#0AF514"], title = "Casos por sexo")
    
    cursor.execute("select edad, count(edad) from persona group by edad order by edad desc")
    rows4 = cursor.fetchall()
    for row in rows4:
        print(row)
    fig4 = px.bar(rows4, x = 0, y = 1, color_discrete_sequence = ["#AB97DA"], title = "Casos por edad")       
    fig4.update_xaxes(title_text='Edad')
    fig4.update_yaxes(title_text='Frecuencia')
    
    cursor.execute("select tipo_de_contagio, count(tipo_de_contagio) from contagio group by tipo_de_contagio")
    rows5 = cursor.fetchmany(30)
    for row in rows5:
        print(row)
    fig5 = px.pie(rows5, values=1, names=0, color_discrete_sequence = ["#FA70A0"], title = "Casos por tipo de contagio")
    
    cursor.execute("select estado, count(estado) from contagio group by estado")
    rows6 = cursor.fetchall()
    for row in rows6:
        print(row)
    fig6 = px.histogram(rows6, x = 0, y = 1, color_discrete_sequence = ["#EA7171"], title = "Casos por estado")       
    fig6.update_xaxes(title_text='Estado Caso')
    fig6.update_yaxes(title_text='Frecuencia')
    
    cursor.execute("select recuperado, count(recuperado) from recuperacion group by recuperado")
    rows7 = cursor.fetchall()
    for row in rows7:
        print(row)
    fig7 = px.pie(rows7, values=1, names=0, color_discrete_sequence = ["#15897D"], title = "Casos por estado de recuperacion")
    
    cursor.execute("select nombre, count(nombre) from persona join etnia on codigo = codigo_etnia group by nombre")
    rows8 = cursor.fetchall()
    for row in rows8:
        print(row)
    fig8 = px.bar(rows8, x = 0, y = 1, color =range(len(rows8)), color_continuous_scale='Viridis', title = "Casos por etnia")       
    fig8.update_xaxes(title_text='Etnia')
    fig8.update_yaxes(title_text='Frecuencia')
    
    app.layout = html.Div(children = [    
        html.H1(children = 'Casos Positivos COVID en Colombia', style={'text-align': 'center', 'font-family': 'Segoe UI Black'}),
        html.Div([    
            html.H1(children = 'Escenario 1: Análisis de distribución geográfica.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
            html.Div(children = '''
                        ● Distribución de casos por municipio.
                     ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
            dcc.Graph(
                id = 'graph1',
                figure = fig1
                ),
        ]),
                     
         html.Div([    
             html.H1(children = 'Escenario 1: Análisis de distribución geográfica.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
             html.Div(children = '''
                        ● Distribución de casos por departamento.
                      ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
             dcc.Graph(
                 id = 'graph2',
                 figure = fig2
                 ),
         ]),   
                      
         html.Div([    
             html.H1(children = 'Escenario 2: Análisis demográfico.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
             html.Div(children = '''
                         ● Distribución de casos positivos por sexo.
                      ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
             dcc.Graph(
                 id = 'graph3',
                 figure = fig3
                 ),
         ]),
                      
          html.Div([    
              html.H1(children = 'Escenario 2: Análisis demográfico.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
              html.Div(children = '''
                         ● Distribución de casos positivos por edad.
                       ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
              dcc.Graph(
                  id = 'graph4',
                  figure = fig4
                  ),
          ]),    
                       
        html.Div([    
            html.H1(children = 'Escenario 3: Análisis por tipo de contagio.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
            html.Div(children = '''
                       ● Distribución de casos positivos por tipo de contagio.
                     ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
            dcc.Graph(
                id = 'graph5',
                figure = fig5
                ),
        ]),  

        html.Div([    
            html.H1(children = 'Escenario 4: Análisis estado de caso.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
            html.Div(children = '''
                       ● Distribución de casos positivos por estado.
                     ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
            dcc.Graph(
                id = 'graph6',
                figure = fig6
                ),
        ]), 
                     
        html.Div([    
            html.H1(children = 'Escenario 5: Análisis de recuperación.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
            html.Div(children = '''
                       ● Distribución de casos positivos por estado de recuperación.
                     ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
            dcc.Graph(
                id = 'graph7',
                figure = fig7
                ),
        ]),
                     
        html.Div([    
            html.H1(children = 'Escenario 6: Análisis de contagio por etnia.', style={'font-family': 'Segoe UI', 'margin': '20px'}),
            html.Div(children = '''
                       ● Distribución de casos positivos por etnia.
                     ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px'}),
            dcc.Graph(
                id = 'graph8',
                figure = fig8
                ),
        ]),

         html.Div([    
             html.H1(children = 'Discusión', style={'font-family': 'Segoe UI', 'margin': '20px'}),
             html.H2(children = 'Análisis de distribución geográfica:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
             html.Div(children = '''
                        ● Distribución de casos por municipio:
                      ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
             
            html.P(children = '''Como podemos observar en la gráfica de casos por municipios, Barranquilla es el municipio con más casos registrados, albergando casi el 30% de casos positivos de Covid en la base de datos. Después de Barranquilla las ciudades con más contagios fueron Medellín y Manizales, con 24 y 20 casos respectivamente, como podemos analizar, los tres municipios con más registros de covid en nuestra base de datos son ciudades capitales de sus respectivos departamentos, Atlántico, Antioquia y Caldas. Que las tres sean capitales nos lleva a pensar en tres razones para que esto ocurra:
Mayor densidad de población: Las capitales suelen tener una mayor concentración de personas en comparación con las áreas rurales. Cuantas más personas estén en un área determinada, mayor será el potencial de transmisión del virus.
Movilidad y transporte: Las capitales son centros de actividad económica y social, lo que implica un mayor movimiento de personas a través de sistemas de transporte público y privado. 
Interacciones sociales: Las áreas urbanas suelen ser lugares donde las interacciones sociales son más frecuentes, ya sea en el trabajo, en establecimientos comerciales o en eventos culturales.
También nos damos cuenta que hay 36 municipios que solamente registraron de a un caso, siendo estos poco provechosos para el análisis ya que entre estos 36 municipios sólo representan el 12% de la base de datos.
Entre Barranquilla, Medellín, Manizales, Palmira y Jamundí se concentran exactamente el 50% de los datos.
                                     
                   ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} )    
            
         ]),
                   
         html.Div([    
             html.Div(children = '''
                        ● Distribución de casos por departamento:
                      ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
             
            html.P(children = '''Como podemos ver en el análisis, Atlántico, Antioquia , Valle del Cauca y Caldas albergan la mayoría de los casos, sumando un total de 226 representando el 75% de la base de datos. Algo que era de esperarse puesto que las ciudades de estos departamentos tuvieron una representación significativa en el análisis por municipio, ya que entre los 4 departamentos con más casos aparecen los departamentos de las tres ciudades con más casos.
También nos damos cuenta que tan solo dos departamentos registraron solamente un caso, Córdoba y Sucre.
Analizamos que si bien en la base de datos no tenemos representación de todos los departamentos, tenemos una representación significativa, puesto que tenemos registros de 21 departamentos de 32 que son en colombia representando el 66% de los departamentos, algo importante a tener en cuenta es que tenemos registros de los 17 departamentos más poblados del país que ordenados por número de habitantes de mayor a menor son:  Antioquia, Valle del Cauca, Cundinamarca, Atlántico, Santander, Bolívar, Córdoba, Norte de Santander, Nariño, Cauca, Magdalena, Cesar, Tolima, Boyacá, Huila, Meta, Caldas.

                                     
                   ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'}), 
            
         ]),
                   
            html.Div([    
                html.H2(children = 'Análisis demográfico:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
                html.Div(children = '''
                           ● Distribución por sexo:
                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''Como podemos notar en la gráfica el 54,3% de las personas registradas son mujeres, algo que aunque no parezca significativo lo es porque nos lleva a pensar en las razones por las cuales las mujeres sufrieron más contagios que los hombres.
Según el estudio realizado por la Organización Mundial de la Salud (OMS), al 28 de enero de 2021, los números globales eran los siguientes: encontraron que, a escala mundial alcanzaron 863,4 millones de casos confirmados de COVID-19, de los cuales 447,3 millones (51,6%) fueron mujeres y 416,1 millones (48,4%) fueron hombres.
                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
               
                html.P(children = '''Como podemos notar, las mujeres se contagiaron más que los hombres, 31 millones de mujeres más, esto se podría deber a que sus trabajos muchas veces les exigen un contacto cercano con otras personas, lo que significa que el riesgo de exposición al virus es mayor. Además, los roles de atención, tareas domésticas y familiares significan que muchas mujeres también tienen que viajar a menudo para atender a los miembros de la familia a pesar de la intensa transmisión del virus, y posiblemente tener una mayor vulnerabilidad al virus que los hombres debido a factores biológicos.
                                           
                         ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} )      

        
            ]),          
                 
            html.Div([    
                html.Div(children = '''
                           ● Distribución de edad:
                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''
Podemos notar gracias a la gráfica como los datos se agrupan hacia el centro en un intervalo entre los 20 y 50 años aproximadamente. Podemos notar como antes de los 10 años y después de los 70 se notan muy pocos registros. 
Según la Organización Mundial de la Salud (OMS), el intervalo de edad que, hasta ahora, ha experimentado el mayor número de casos de COVID-19 es el de los adultos jóvenes de 20 a 40 años. Esta población es especialmente susceptible porque generalmente trabaja fuera de la casa, tiene el grupo más amplio de compañeros de trabajo y es más propensa a ir de fiesta y a viajar. Además, muchas personas de esta edad han tenido una escasa adherencia al distanciamiento social recomendado. Por lo que podemos ver la base de datos con la que estamos trabajando se asemeja bastante a los datos brindados por la OMS, por lo cual podemos suponer que la base de datos tiene buena representación.


                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
               
               
            ]),
                      
            html.Div([    
                html.H2(children = 'Análisis por tipo de contagio:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
                html.Div(children = '''
                           ● Distribución por tipo de contagio: 
                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''Como podemos extrapolar del gráfico, el 64,3% de las personas se contagiaron de manera comunitaria mientras que solo el 35,7% lo hicieron de manera relacionada. Definimos el contagio por transmisión comunitaria a la propagación de la enfermedad dentro de una comunidad o área geográfica determinada, sin que se pueda rastrear fácilmente el origen de cada caso. En este caso, las personas infectadas no tienen un vínculo claro con otros casos conocidos ni han viajado a zonas de alta transmisión. El contagio comunitario indica que el virus está circulando ampliamente en la comunidad, lo que aumenta el riesgo de infección para las personas que residen en esa área.

                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
               
                html.P(children = '''El contagio relacionado se refiere a la propagación de la enfermedad a través de contactos directos o cercanos con casos confirmados de COVID-19. En este caso, se puede rastrear la cadena de transmisión y se sabe que los nuevos casos están relacionados con casos conocidos.  Haciendo un análisis a las entradas de la base de datos, nos damos cuenta que se podría establecer una relación entre la distribución por tipo de contagio y la distribución por edad, puesto que en el intervalo establecido de las personas que en época de covid les tocaba ir a trabajar tienen en su mayoría tipo de contagio comunitario, esto debido a que su contagio no fue específicamente por haber tratado con alguien portador del virus sino porque se debían movilizarse mientras que el virus circula ampliamente en la comunidad.

                                           
                         ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} )      
            ]), 
                       
            html.Div([    
                html.H2(children = 'Análisis de estado de caso:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
                html.Div(children = '''
                           ● Distribución por estado del caso: 
                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''Podemos ver en la gráfica que solamente 9 personas tienen por estado del caso fallecidos, lo cual solo representa el 3% de la base de datos, mientras que el 96,3% de los datos son leves, lo cual indica un bajo porcentaje de mortalidad por covid en nuestra base de datos. Además, podemos relacionar la distribución por estado del caso con la distribución por edad, puesto que las personas fallecidas en la base de datos son la mayoría adultos mayores, teniendo un intervalo desde 58 años a 92 años, entre ese intervalo están las edades de las personas fallecidas. Por lo que podemos concluir que la edad tiene una relación directa con las complicaciones que puede generar el covid en nuestros organismos.



                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
               
                html.P(children = '''Se ha identificado que los mayores de 70 años han experimentado los resultados más graves. Esto se debe principalmente a que esta población es más susceptible a complicaciones relacionadas con el virus, como problemas respiratorios graves, enfermedades cardiovasculares, presión arterial alta o diabetes. La posibilidad de hospitalización es tres veces mayor para los mayores de 70 años que para los adultos jóvenes. Esto significa que una población más joven puede convertirse en una cadena de transmisión del virus para las personas mayores porque como pudimos ver en el análisis de distribución por edad los más contagiados son los adultos aunque estos no tienen las consecuencias más graves.


                                           
                         ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} )      

               
            ]),                     
                   
                        
            html.Div([    
                html.H2(children = 'Análisis de recuperación:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
                html.Div(children = '''
                           ● Distribución por estado de recuperación: 
                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''Esta distribución la analizamos bastante parecida a la anterior ya que las personas cuyo estado del caso fue fallecido, en la distribución de recuperación no cambia, también sale fallecido. Todos los que tenían por estado leve, en recuperación salen como recuperados, manteniendo así los mismos porcentajes.



                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
               
               
            ]),
                      
                          
            html.Div([    
                html.H2(children = 'Análisis de contagio por etnia:', style={'font-family': 'Segoe UI', 'margin': '20px'}),
                html.Div(children = '''
                           ● Distribución por etnia

                         ''', style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'22px', 'font-weight':'bold'}),
                
               html.P(children = '''En esta distribución tenemos los valores de Indígena, palenquero, negro y otro que tienen respectivamente 13, 23, 37, 237 entradas. Esto nos muestra que el 79% de la población no se siente identificada con una etnia en específico. 

                      ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),  
           
            html.P(children = '''
Las personas que se identifican con la comunidad indígena pertenecen a Atlántico, Valle del Cauca y Magdalena y representan el 9% de la base de datos. Las personas que se identifican como palenqueros pertenecen en su mayoría a Cesar, Caldas, Antioquia y Meta, siendo César el departamento con más registros de palenqueros 4/23. De las personas que se identifican como negros hay 20 que pertenecen al departamento del Atlántico que corresponden al 74% de las persona que se identifican como negros, complementando esto, Magdalena y Valle del Cauca tienen de a 2 registros.
                         ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} )      


               
            ]),           
            
                   html.Div([    
             html.H1(children = 'Conclusiones', style={'font-family': 'Segoe UI', 'margin': '20px'}),
              
            html.P(children = '''● En lo referente a la selección de las fuentes de datos. Es de reconocer que fue información la cual tuvo fácil acceso, ya que, se encontraba en la base de datos del gobierno, que se encuentra abierta para todos. He de recalcar, que los datos son obtenidos por el Ministerio de Salud. 
Sobre la base de datos original se realizó una reducción tanto de número de tuplas como de columnas, llegando a pasar de 6 millones de registros a 300 registros y de 23 columnas a 17 columnas. Esto se realizó con fines prácticos en busca de hacer un correcto análisis.
                   ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'} ),    
            
                
            html.P(children = '''● Para poder hacer el diseño de la base de datos en PgAdmin, se realizó una normalización de los datos seleccionados, quedando con un total de 7 tablas (persona, municipio, etnia, departamento, contagio, recuperación y caso). Para lograr esta normalización tuvimos que agregar unos datos nuevos, como por ejemplo, se creó una cédula para cada persona. Ya que por defecto no existía en la base de datos un atributo único con la persona y solo se relacionaba con el ID del caso. A su vez tuvimos que definir algunas relaciones, como por ejemplo: cada caso único se relaciona únicamente con una cédula de persona (esto sucede de la misma manera para las relaciones de persona con contagio y persona con recuperacion), a su vez, cada persona está relacionada con un único municipio y un municipio puede tener muchas personas. De la misma manera a cada municipio le corresponde un único departamento. En lo referente a la etnia se establece una relación de uno a muchos, ya que una persona tiene una única etnia y una etnia puede categorizar a muchas personas. 
                   ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'}),

            html.P(children = '''● Con respecto a la carga de datos: primero se realizó una base de datos en pgadmin llamada “sec_entrega” está nos permitirá crear las tablas y almacenar cada uno de los datos seleccionados. Accediendo al “Query Tool” de la base de datos, se crean cada una de las tablas correspondientes, las cuales se encuentran en el archivo llamado “script_pgadmin” dentro del repositorio. Posteriormente se descargan los archivos en formato .cvs que se encuentran en la carpeta “Tablas_normalizadas” (también dentro del repositorio) y se copian en la carpeta Publics del sistema. Luego se realiza la carga de información mediante la función “copy” relacionando cada tabla con sus respectivas columnas junto con su dirección de ubicación correspondiente. Para hacer efectivo la carga de la información, le indicamos a la función “copy” dentro de sus atributos, que los datos están delimitados por “;” ya que están en formato .cvs, además de esto, le indicamos que el encabezado de las tablas se encuentran de mismo modo en este formato para que reconozca la primera fila como el nombre de cada columna. Por último se corre el código y se realiza exitosamente la inserción de los datos a su correspondiente tabla generada.
Para el proceso de carga de datos, no tuvimos problemas mayores a algunos en la escritura del código y en la organización de los archivos csv en la carpeta correspondiente.  Un problema que fue necesario corregir fue que los archivos que contenían fechas cambian de orden dependiendo la configuración que tuviera el lenguaje del computador.
                   ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'}),
                   
             html.P(children = '''● Acerca de la conexión entre python y sql, es de destacar la dificultad de la instalación de los módulos (psycopg2) y la selección del path en spyder. Ya que en ciertas ocasiones se presentaban errores dentro del cmd o dentro de la ruta, los cuales no permitían la correcta instalación de los módulos. Con respecto al código de conexión no presentamos problemas, simplemente era agregarle el nombre de la base de datos y la consulta correspondiente. 
Pasando ahora con el desarrollo de gráficos con dash, destacamos que este fue el proceso que más nos costó realizar, no por la dificultad de este sino por la extensión del código y la instalación del módulo, ya que para instalar dash se presentaban algunos errores dentro del cmd que atrasaron un poco el proceso. Además, también se debían instalar los módulos pandas() y ploty.express() en estos si no hubo problemas en la instalación. Para el código de creación de las gráficas se nos presentaron varias dificultades, ya que tocaba tener mucho cuidados con los Div’s de html para que spyder pudiese interpretarlos, además, al ser un código extenso el margen de error era amplio ya que muchas veces nos tocó hacer correcciones en variables o en la definición de cada tipo de gráfico, debido a que cada uno de estos mantiene un código en particular y unos parámetros diferentes. Sumándole a esto, había que lidiar con la sintaxis de python, especialmente con los bloques de indentación, debido a que era un código extenso y se podían presentar confusiones en la jerarquización del código.

                    ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'}),
                    
             html.P(children = '''● Para finalizar, con respecto a la resolución del problema planteado (Determinar cuál departamento tuvo la menor cantidad de casos positivos de COVID-19 en Colombia) se concluyó, gracias a las gráficas realizadas con el módulo dash(), que los departamentos de Córdoba y Sucre fueron los que menores casos positivos presentaron en nuestros datos seleccionados, contando únicamente con un caso. 
        Sobre la base de datos original se realizó una reducción tanto de número de tuplas como de columnas, llegando a pasar de 6 millones de registros a 300 registros y de 23 columnas a 17 columnas. Esto se realizó con fines prácticos en busca de hacer un correcto análisis.
                           ''',style={'font-family': 'Segoe UI', 'margin': '40px', 'font-size':'20px', 'text-align': 'justify'}),
             
                         
             html.P(children = '''
Como conclusión general podemos decir que este proyecto fue una actividad muy interesante, la cual nos permitió desarrollar las habilidades de programación en SQL y en Python. Además de que nos permitió fortalecer nuestro manejo en las bases de datos y nuestra autocrítica al momento de clasificar (normalizar) cada una de las tuplas en la base propuesta. Pensamos que en un futuro esto podría sernos de utilidad en nuestro ámbito profesional, por lo que es importante tener conocimientos previos de esto para poder escalar en la vida laboral.


                           ''',style={'font-family': 'Segoe UI', 'margin': '30px', 'font-size':'20px', 'text-align': 'justify'}),
              
         ]),
                    
                      
     ])
                             
    if __name__ == '__main__':
               app.run_server(debug = False)
        
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada")
    