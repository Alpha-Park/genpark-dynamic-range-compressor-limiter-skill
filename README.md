# genpark-dynamic-range-compressor-limiter-skill

> Dynamic range compressor and peak limiter with soft-knee smoothing and ballistics level detection.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Audio Input Signal] --> B[Processing Engine]
    B --> C[DSP Core Operations]
    C --> D[Feature / Filtered Result]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`, `cmath`).
- **High Precision DSP**: Optimized algorithms with sub-sample interpolation and direct form structures.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-dynamic-range-compressor-limiter-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-dynamic-range-compressor-limiter-skill.git
cd genpark-dynamic-range-compressor-limiter-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-dynamic-range-compressor-limiter-skill": {
      "command": "python",
      "args": ["-m", "genpark-dynamic-range-compressor-limiter-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
