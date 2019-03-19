from playsound import playsound
import requests
import time
import dash
from dash.dependencies import Output
from dash.dependencies import Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque

db = open("data.txt", "r")

X = deque(maxlen=20)
Y = deque(maxlen=20)

X.append(0)
Y.append(0)

app = dash.Dash(__name__)
app.layout = html.Div(
		
	[
		dcc.Graph(id='live-bitcoin', animate=True),
		dcc.Interval(
			id='graph-update', 
			interval=1000
			)	
	]
)



@app.callback(Output('live-bitcoin', 'figure'), events = [Event('graph-update', 'interval')])
def update_graph():
	global X
	global Y

	datay = ""

	for x in db.readline():
		datay += x

	

	X.append(X[-1]+0.1)
	Y.append(int(datay[0:4]))

	data = go.Scatter(
		x = list(X),
		y = list(Y),
		name = 'Scatter',
		mode = 'lines+markers'
		)

	return {'data':[data], 'layout': go.Layout(	xaxis = dict(range=[min(X), max(X)]),
												yaxis = dict(range=[min(Y), max(Y)])
											)}



if __name__ == '__main__':
	app.run_server(debug=True)

	
	


	