"""Export actual user/assistant text, without reconstructing or polishing it.

Usage: python3 analysis/export_prompts.py /path/to/this-session.jsonl
System/developer messages, hidden reasoning, tool payloads, and automatically
injected environment/plugin inventories are not public conversation answers.
"""
import json
import sys
from pathlib import Path

source=Path(sys.argv[1])
blocks=["# Raw conversation\n\nActual user prompt and assistant-facing answers from the session that created this repository. Text is unedited. System instructions, hidden reasoning, tool calls/results, and injected environment/plugin metadata are excluded. Tool evidence is recorded separately in `checks/` and the generated `lean/` folder; its `docs/AGENT_RUN_PROMPTS.md` retains the relevant Lean task prompts and responses. This export is a snapshot before the final handoff, not a fabricated dialogue.\n"]
for line in source.open():
    d=json.loads(line)
    if d.get('type')!='response_item': continue
    p=d['payload']
    if p.get('type')!='message' or p.get('role') not in ('user','assistant'):continue
    if p.get('channel')=='analysis':continue
    parts=[c.get('text','') for c in p.get('content',[]) if c.get('type') in ('input_text','output_text')]
    parts=[x for x in parts if not x.startswith(('<environment_context>','<recommended_plugins>'))]
    if parts: blocks.append('\n## '+p['role'].capitalize()+'\n\n'+'\n'.join(parts)+'\n')
Path(__file__).resolve().parents[1].joinpath('prompts.md').write_text('\n'.join(blocks))
print('Exported actual message text to prompts.md')
