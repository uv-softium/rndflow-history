select
    array[c.id, s.id] as packages,
    s.size,
    s.span,
    s.x,
    s.sin,
    c.cos
from sin s join cos c on s.job_id = c.job_id