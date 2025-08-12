from pathlib import Path
import json
path = Path('numbers.json')
contents= path.read_text()
print(contents)
print(type(contents))
contents=json.loads(contents)

print(contents)
print(type(contents))