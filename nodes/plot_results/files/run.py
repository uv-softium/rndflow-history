#!/usr/bin/env python
import numpy as np
import plotly.graph_objects as go
from rndflow import job

print('Reading inputs...')
globals().update(job.load())

print('Plotting data')
fig = go.Figure()
#+
fig.add_trace(go.Scatter(x=x, y=cos, name='cos(x)'))
fig.add_trace(go.Scatter(x=x, y=sin, name='sin(x)'))
fig.add_trace(go.Scatter(x=ref_x, y=ref_cos, name='ref_cos(x)', line={'dash': 'dash'}))
fig.add_trace(go.Scatter(x=ref_x, y=ref_sin, name='ref_sin(x)', line={'dash': 'dash'}))

fig.update_layout(
    legend=dict(orientation='h'),
    margin=dict(r=30),
    title='$\sum_{i=0}$')
#+
print('Saving output')
report = """\
# Report

::: info
Good news everyone!
:::

Below is a code block:

```py
print("hello world")
```

And here is a formula:
$e = mc^2$
"""
job.save_package(
    label='result',
    files={
        'x': x,
        'sin': sin,
        'cos': cos,
        'ref_x': ref_x,
        'ref_sin': ref_sin,
        'ref_cos': ref_cos,
        'test.md': lambda f: f.write_text(report)
        },
    fields=dict(size=size, span=span),
    images=dict(result=fig)
    )