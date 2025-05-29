import dash 
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go 
import random 
import datetime

#crear la app dash, cres una instancia de aplicacion web (usa flask)
app = dash.Dash(__name__)

#Layout del dashboard 
#html.H2 titulo en la web
#dcc.graph zona donde se dibuja el grafico de barras
#ddc.interval lanza un evento cada  500ms o (5 seg) para activar
#el callback
app.layout = html.Div([
    html.H2('Dashboard de residuos - Tiempo real'),
    dcc.Graph(id='grafico'),
    html.Div(id='tabla-datos', style={"marginTop": 20}),  
    dcc.Interval(id='intervalo', interval=5000, n_intervals=0)
])

@app.callback(
    [Output('grafico', 'figure'),
    Output('tabla-datos', 'children')],
    [Input('intervalo', 'n_intervals')]
)
def actualizar_dashboard(n):
    # #simular datos
    data = {
        'timestamp': datetime.datetime.now().strftime('%H:%M:%S'),
        'Plastico': random.randint(10, 50),
        'Papel': random.randint(5, 40),
        'Organico': random.randint(15, 60)
    }
    
    #construye el grafico de barras con los datos generados
    fig = go.Figure(data=[go.Bar(
        x=list(data.keys())[1:],
        y=list(data.values())[1:],
        marker_color=['#2196f3', '#ffc107', '#4caf50']
    )])
    
    # Actualiza el layout
    fig.update_layout(
        title='Ultima actualizacion: ' + data['timestamp'], 
        yaxis_title='Cantidad (kg)'
    )
    
    # Crea la tabla
    tabla = html.Table([
        html.Thead(
            html.Tr([html.Th("Tipos de residuos"), html.Th("Cantidad (kg)")])  
        ),
        html.Tbody([
            html.Tr([html.Td("Plasticos"), html.Td(data["Plastico"])]),
            html.Tr([html.Td("Papel"), html.Td(data["Papel"])]),
            html.Tr([html.Td("Organico"), html.Td(data["Organico"])]),
        ])
    ],
        style={
            'width': '50%',
            'border': '1px solid #ccc',  
            'borderCollapse': 'collapse',
            'textAlign': 'center',  
            'margin': 'auto'
        }
    )
    
    return fig, tabla

# Lanza la aplicacion web local y se puede ver en Dash is running on http://127.0.0.1:8050/
if __name__ == '__main__':
    app.run(debug=True)