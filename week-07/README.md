# Week 7: MCP — Model Context Protocol

## Goal
Build your own MCP server that exposes your tools to any MCP-compatible client (Claude Desktop, Claude Code, Cursor, etc.).

---

## Watch + Build (free)

| Resource | URL |
|----------|-----|
| MCP with Anthropic (DeepLearning.AI) | https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/ |
| MCP Official Spec | https://modelcontextprotocol.io/introduction |
| MCP Docs — Build a Server | https://modelcontextprotocol.io/docs/develop/build-server |

Complete the DeepLearning.AI course. It's the official Anthropic MCP course.

---

## Key MCP Concepts

```
MCP Server  — A process that exposes tools, resources, and prompts over a standard protocol
MCP Client  — An AI app (Claude Desktop, Claude Code) that connects to MCP servers
Tool        — A callable function (like a REST endpoint) that the AI can invoke
Resource    — A data source the AI can read (files, DB queries, API responses)
FastMCP     — Python library that makes building MCP servers easy
```

---

## Build Assignment

**Build a DevOps MCP server that exposes your team's tools to Claude.**

The server should expose these tools:
1. `get_pod_status(namespace, deployment)` — Returns simulated Kubernetes pod status
2. `get_recent_logs(service, lines)` — Returns simulated recent log lines
3. `create_incident_ticket(title, severity, description)` — Creates a mock JIRA ticket
4. `get_deployment_history(service)` — Returns last 5 deployments

Then connect it to Claude Desktop so you can call these tools in chat.

**Starter file:** `starter/mcp_server.py`

---

## Quiz

1. What is the difference between an MCP **Tool** and an MCP **Resource**?
2. Why does MCP matter more than just calling functions directly in your Python code?
3. How would you expose your team's Jenkins/GitHub Actions pipelines as MCP tools?
