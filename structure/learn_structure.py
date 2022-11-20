import numpy as np
import pandas as pd
from pgmpy.estimators import HillClimbSearch, BicScore

# Create some data.
data = pd.DataFrame(
    np.random.randint(0, 3, size=(2500, 8)), columns=list("ABCDEFGH")
)
data["A"] += data["B"] + data["C"]
data["H"] = data["G"] - data["A"]

# Hill climbing.
hc = HillClimbSearch(data)
hc_best = hc.estimate(scoring_method=BicScore(data))

with open("hill_climb_edges.txt", "w") as f:
    f.write(str(hc_best.edges()))
