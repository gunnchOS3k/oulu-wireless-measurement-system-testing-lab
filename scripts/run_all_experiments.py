import subprocess, sys
for s in ['run_local_network_measurement.py','generate_measurement_report.py','export_edge_io_format.py']:
    subprocess.check_call([sys.executable,f'scripts/{s}'])
from pathlib import Path; Path('results/calibration_checklist.md').write_text('- [ ] Cable cal\n'); Path('results/experiment_summary.md').write_text('# Measurement e2e PASS\n')
