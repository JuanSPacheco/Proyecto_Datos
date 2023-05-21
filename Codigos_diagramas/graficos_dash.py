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
                      
     ])
                             
    if __name__ == '__main__':
               app.run_server(debug = False)
        
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexión finalizada")
    
