#!/usr/bin/env python
from rndflow import job
from numpy import linspace, pi

# import input values into the global namespace
globals().update(job.load())

print(f'{size = }, {span = }')

# generate linear vector
x = linspace(0, span * pi, size)

# save output package
job.save_package(
    label='x',
    fields=dict(
        size=size,
        span=span,
        job_id=job.job_id),
    files=dict(
        x=x))
