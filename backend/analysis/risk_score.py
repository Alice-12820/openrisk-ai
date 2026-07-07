class RiskScorer:

    def score(self, summary):

        score = 0

        score += summary["dangerous_operations"] * 5

        score += summary["privileged_functions"] * 2

        score += summary["external_functions"]

        if score <= 10:
            rating = "Low"

        elif score <= 25:
            rating = "Medium"

        elif score <= 50:
            rating = "High"

        else:
            rating = "Critical"

        return {
            "score": score,
            "rating": rating,
        }