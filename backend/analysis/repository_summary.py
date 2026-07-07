class RepositorySummary:

    def summarize(self, contracts):

        summary = {
            "contracts": len(contracts),
            "functions": 0,
            "roles": 0,
            "dangerous_operations": 0,
            "external_functions": 0,
            "privileged_functions": 0,
        }

        for contract in contracts:

            summary["functions"] += len(contract["functions"])

            summary["roles"] += len(contract["roles"])

            summary["dangerous_operations"] += len(
                contract["security_keywords"]
            )

            for function in contract["functions"]:

                findings = function["security_findings"]

                if "Externally Callable" in findings:
                    summary["external_functions"] += 1

                if "Privileged Function" in findings:
                    summary["privileged_functions"] += 1

        return summary