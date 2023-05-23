import plotly.graph_objs as go
from colorspacious import cspace_convert

def create_trace(colors):
    # Conversion from CIE L*a*b* to sRGB
    return go.Scatter3d(x=[color[3] for color in colors],
                        y=[color[4] for color in colors],
                        z=[color[2] for color in colors],
                        mode='markers+text',
                        marker=dict(size=10, color=[color[1] for color in colors], opacity=1),
                        text=[color[0] + str(color[1]) for color in colors],
                        textposition="top center")

colors_orange = [
    ['Oikea vastaus: "Tiili"', (242, 108, 63), 61.62, 48.90, 49.28],
    ['Eemeli', (244, 130, 0), 65.90, 37.51, 72.54],
    ['Sami', (255, 132, 0), 67.85, 40.85, 74.50],
    ['Pekka', (236, 113, 28), 61.42, 43.19, 63.37],
    ['Perttu', (250, 130, 36), 66.84, 40.36, 65.95],
    ['Tatu L', (240, 140, 10), 67.50, 30.83, 71.90],
    ['Topias', (245, 135, 23), 67.13, 35.60, 69.55],
    ['Valtteri', (234, 123, 22), 63.11, 37.30, 66.18],
    ['Tatu H', (244, 111, 0), 51.24, 76.68, 65.11]
]
trace_orange = create_trace(colors_orange)
trace_orange.name = 'Oranssi (Tiili)'

colors_blue = [
    ['Oikea vastaus: "Virta"', (10, 46, 89), 18.97, 5.60, -29.42],
    ['Eemeli', (4, 37, 169), 24.37, 43.97, -71.14],
    ['Sami', (21, 40, 145), 22.73, 34.11, -59.16],
    ['Pekka', (12, 70, 137), 30.07, 9.57, -42.24],
    ['Perttu', (65, 158, 248), 63.64, 2.21, -52.73],
    ['Tatu L', (63, 170, 232), 66.24, -10.34, -39.87],
    ['Topias', (64, 166, 240), 65.48, -5.26, -45.44],
    ['Valtteri', (69, 169, 222), 65.68, -12.30, -35.23],
    ['Tatu H', (7, 43, 108), 19.46, 15.99, -41.11],
]
trace_blue = create_trace(colors_blue)
trace_blue.name = 'Sininen (Virta)'

layout = go.Layout(scene=dict(xaxis_title='a*',
                              yaxis_title='b*',
                              zaxis_title='L*'))

fig = go.Figure(data=[trace_orange], layout=layout)

fig.add_trace(trace_blue)

fig.write_html('daily_question_2023-05-23.html')

