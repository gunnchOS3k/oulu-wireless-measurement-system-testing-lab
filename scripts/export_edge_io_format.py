import json; from pathlib import Path; Path('results/edge_io_export.json').write_text(json.dumps({'format':'edge-io-v1'}))
