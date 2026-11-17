#!/usr/bin/env python3
"""Example receiver adapter contract. Replace receive() with a local/provider client.
This file deliberately makes no external API call and therefore incurs no spend.
"""
import json,sys
def receive(req):
 return {"answer":"ABSTAIN","confidence":0.0,"sampling_config":"example-noop"}
for line in sys.stdin:
 if line.strip(): print(json.dumps(receive(json.loads(line))))
