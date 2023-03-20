#!/usr/bin/env python
import numpy as np
import plotly.graph_objects as go
from rndflow import job

globals().update(job.load())

x = np.linspace(0, 2 * np.pi, size)
s = np.sin(freq * x)
c = np.cos(freq * x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=s, name='sin'))
fig.add_trace(go.Scatter(x=x, y=c, name='cos'))

job.save_package(label='reference',
    files=dict(x=x, sin=s, cos=c),
    images=dict(result=fig))
