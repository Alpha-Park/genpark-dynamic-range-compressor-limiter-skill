import sys
import json
from client import DynamicRangeCompressor

def handle_call(name, arguments):
    if name == "compress":
        th = arguments.get("threshold", -10.0)
        rat = arguments.get("ratio", 4.0)
        gain = arguments.get("makeup_gain", 0.0)
        comp = DynamicRangeCompressor(th, rat, gain)
        return {"compressed": comp.process(arguments["signal"])}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
