import sys
import json
from client import DynamicRangeCompressorLimiter

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-dynamic-range-compressor-limiter-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "compress_audio",
                    "description": "Compress audio signal dynamic range with soft-knee ballistics",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "signal": {"type": "array", "items": {"type": "number"}},
                            "threshold_db": {"type": "number", "default": -18.0},
                            "ratio": {"type": "number", "default": 4.0},
                            "knee_db": {"type": "number", "default": 3.0},
                            "makeup_gain_db": {"type": "number", "default": 0.0}
                        },
                        "required": ["signal"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "compress_audio":
            comp = DynamicRangeCompressorLimiter()
            sig = args.get("signal", [])
            data = comp.process(
                sig,
                threshold_db=args.get("threshold_db", -18.0),
                ratio=args.get("ratio", 4.0),
                knee_db=args.get("knee_db", 3.0),
                makeup_gain_db=args.get("makeup_gain_db", 0.0)
            )
            res = {"content": [{"type": "text", "text": json.dumps(data)}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
