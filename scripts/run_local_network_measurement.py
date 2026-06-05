import json
from pathlib import Path
from gunnchos_measurement.wifi_probe import probe_fixture

out = Path("results/measurement_data_sample.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({"samples": [probe_fixture()]}))
