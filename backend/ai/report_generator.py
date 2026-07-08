import json

from ai.fireworks_client import FireworksClient
from ai.prompts import SYSTEM_PROMPT


class ReportGenerator:

    def __init__(self):
        self.client = FireworksClient()

    def generate(self, repository_analysis):

        prompt = f"""
Below is structured analysis of a Solidity repository.

Produce a security assessment.

Repository Analysis:

{json.dumps(repository_analysis, indent=2)}

Remember:

- Fill every field.
- Return JSON only.
- Do not leave fields empty.
"""

        response = self.client.chat(
        SYSTEM_PROMPT,
        prompt,
)

        return json.loads(response)