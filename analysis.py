from data import yield_data
import numpy as np

def get_results():
    total_per_farm = yield_data.sum(axis=1)
    total_per_month = yield_data.sum(axis=0)

    best_farm = np.argmax(total_per_farm)
    worst_farm = np.argmin(total_per_farm)
    average_per_farm = yield_data.mean(axis=1)

    return {
        "total_per_farm": total_per_farm,
        "total_per_month": total_per_month,
        "best_farm": best_farm,
        "worst_farm": worst_farm,
        "average_per_farm": average_per_farm
    }