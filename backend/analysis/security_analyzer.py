from models.function_model import FunctionInfo


PRIVILEGED_MODIFIERS = {
    "onlyOwner",
    "onlyAdmin",
    "onlyGovernance",
    "onlyGuardian",
}


class SecurityAnalyzer:

    @staticmethod
    def analyze_function(function: FunctionInfo):

        findings = []

        if function.visibility == "external":
            findings.append("Externally Callable")

        if function.visibility == "public":
            findings.append("Public Function")

        if function.state_mutability == "payable":
            findings.append("Receives ETH")

        privileged = any(
            modifier in PRIVILEGED_MODIFIERS
            for modifier in function.modifiers
        )

        if privileged:
            findings.append("Privileged Function")

        return findings