#!/usr/bin/env python
from rndflow import job
from numpy import linspace, cos

globals().update(job.load())

y = cos(x)

job.save_package(
    label='cos',
    fields=dict(
        size=size,
        span=span,
        job_id=job_id
        ),
    files={
        'x': x,
        'y': y
        }
    )
