import montage
from montage import client, Query, Field
import sys

script = sys.stdin.read()
code = compile(script, "main.py", "exec")
global_vars = globals()
global_vars.update({
    'client': client,
    'Query': Query,
    'Field': Field,
    'montage': montage,
})
local_vars = {}
exec(code, global_vars, local_vars)
if 'main' in local_vars and callable(local_vars['main']):
    local_vars['main'](client)
