"""
Week 7 Build: DevOps MCP Server using FastMCP

Exposes Kubernetes/DevOps tools to Claude Desktop and other MCP clients.

Install: pip install fastmcp
Run: python mcp_server.py

To connect to Claude Desktop, add to ~/Library/Application Support/Claude/claude_desktop_config.json:
{
  "mcpServers": {
    "devops": {
      "command": "python",
      "args": ["/absolute/path/to/mcp_server.py"]
    }
  }
}
"""

# TODO 1: Import FastMCP
# from fastmcp import FastMCP

# TODO 2: Create a FastMCP app instance with a name and description
# mcp = FastMCP("DevOps Assistant", description="Tools for Kubernetes and incident management")

import json
from datetime import datetime, timedelta
import random


# ── Tool Definitions ──────────────────────────
# Use the @mcp.tool() decorator on each function.
# FastMCP uses your function's docstring as the tool description
# and type hints as parameter schemas.

# TODO 3: Implement get_pod_status
# @mcp.tool()
def get_pod_status(namespace: str, deployment: str) -> str:
    """Get the current status of pods for a Kubernetes deployment.

    Args:
        namespace: Kubernetes namespace (e.g., 'prod', 'staging')
        deployment: Deployment name (e.g., 'payment-api', 'order-service')
    """
    # TODO: Return a simulated kubectl output as a formatted string
    # Include: pod names, status (Running/CrashLoopBackOff/Pending), restarts, age
    statuses = ["Running", "Running", "Running", "CrashLoopBackOff"]
    pods = []
    for i in range(3):
        pods.append({
            "name": f"{deployment}-{random.randint(100000, 999999)}-{random.choice(['abc', 'def', 'xyz'])}",
            "status": statuses[i],
            "restarts": random.randint(0, 15),
            "age": f"{random.randint(1, 48)}h"
        })
    return json.dumps({"namespace": namespace, "deployment": deployment, "pods": pods}, indent=2)


# TODO 4: Implement get_recent_logs
# @mcp.tool()
def get_recent_logs(service: str, lines: int = 50) -> str:
    """Fetch recent log lines for a service.

    Args:
        service: Service name to fetch logs for
        lines: Number of recent log lines to return (default: 50)
    """
    # TODO: Return simulated log lines as a string
    # Mix of INFO, WARN, ERROR entries with timestamps
    pass


# TODO 5: Implement create_incident_ticket
# @mcp.tool()
def create_incident_ticket(title: str, severity: str, description: str) -> str:
    """Create an incident ticket in the tracking system.

    Args:
        title: Short title for the incident
        severity: Severity level - P1, P2, or P3
        description: Detailed description of the incident
    """
    # TODO: Return a simulated ticket creation response with ticket ID
    pass


# TODO 6: Implement get_deployment_history
# @mcp.tool()
def get_deployment_history(service: str) -> str:
    """Get the last 5 deployments for a service.

    Args:
        service: Service name to check deployment history
    """
    # TODO: Return simulated deployment history
    # Include: version, timestamp, deployer, status (success/failed/rolled-back)
    pass


# ── Run the Server ────────────────────────────

if __name__ == "__main__":
    # TODO 7: Run the MCP server
    # mcp.run()
    print("MCP Server running. Connect from Claude Desktop.")
    print("Tools available: get_pod_status, get_recent_logs, create_incident_ticket, get_deployment_history")
