import plotly.express as px
import numpy as np
raw_data = np.genfromtxt("dipole_pattern.csv", delimiter=',')

#theta = np.arange(0, (2 * np.pi)+np.pi/180 , np.pi/180)

theta = np.arange(0,361,1)



fig = px.line_polar(r=raw_data, theta=theta,start_angle=0)
fig.show()
#
# print(type(df))