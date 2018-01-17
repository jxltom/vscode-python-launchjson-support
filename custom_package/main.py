import os
import custom_package

print('custom package is imported which means PYTHONPATH as env is set appropriately')
print(os.environ.get('ENV'))
print(os.environ.get('ENVFILE'))
