import os
from vastai import VastAI

k = os.getenv('VASTAI_API_KEY')

print("KEY=", k)
vast_sdk = VastAI(api_key=k)

output = vast_sdk.show_instances()
print(output)