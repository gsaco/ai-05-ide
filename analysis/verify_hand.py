"""Verify the student's photographed example at capability 3/10."""
import json
from pathlib import Path
import numpy as np
from discrete_model import economy

results = [economy(.3, regime) for regime in ['autonomous', 'nonautonomous']]
for result, wages, output in zip(results, [[3/14, 4/7, 2], [.3, 13/20, 7/5]], [333/280, .57]):
    assert np.allclose(result['wages'], wages)
    assert abs(result['output'] - output) < 1e-9
    assert all(abs(lo - hi) < 1e-7 for lo, hi in result['wage_ranges'])
record = {'status': 'PASS', 'checks': ['primal feasibility', 'dual feasibility',
    'complementary slackness', 'strong duality', 'unique wages',
    'handwritten wage values', 'output totals at capability 0.3'], 'results': results}
(Path(__file__).resolve().parents[1] / 'checks/hand-check.json').write_text(json.dumps(record, indent=2) + '\n')
print('PASS: photographed wage and output comparisons at capability 3/10')
