# prpilot-demo

A tiny Flask bookstore API that exists to show [PRPilot](https://github.com/Tejasp-26/PRPilot) reviewing a real pull request.

`main` is clean. The open pull request adds a search endpoint, a sales report and a CSV export, and slips in the kinds of problems a reviewer should catch: SQL injection, a shell command built from user input, a hardcoded secret, an HTTP call per item inside a loop, and a new function with no tests. PRPilot's review comments on that PR show what it found and which tool found it.

```bash
pip install -r requirements.txt
pytest
flask --app bookstore.app run
```
