#!/usr/bin/env python
from rndflow import job
from numpy import linspace, sin
import time

globals().update(job.load())

y = sin(x)

time.sleep(2)

job.save_package(
    label='sin',
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