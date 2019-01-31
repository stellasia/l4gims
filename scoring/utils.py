from common.choices import DIVERSITY_TYPE
from scoring.models import Score


def get_global_score():
    scores = Score.objects.filter(
        current=True
    )
    data = {v:0 for k, v in DIVERSITY_TYPE}
    for s in scores:
        d = s.get_score_dict()
        for k, v in d.items():
            data[k] += v
    data = {k: v/len(scores) for k, v in data.items()}
    score_data = sorted([{"axis": d, "value": v} for d, v in data.items() ], key = lambda e: e["axis"] )
    return score_data
