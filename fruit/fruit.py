import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ParameterEstimator, BayesianEstimator, MmhcEstimator

import make_fruit_data as m

# Make a model structure and count the states present in the data.
data = m.make_fruit_data()
model = BayesianNetwork([("fruit", "tasty"), ("size", "tasty")])
pe = ParameterEstimator(model, data)
unconditional_counts = pe.state_counts("fruit")
conditional_counts = pe.state_counts("tasty")

with open("state_counts.txt", "w") as f_state_counts:
    f_state_counts.write(f"Unconditional:\n {unconditional_counts}\n")
    f_state_counts.write(f"\nConditional:\n {conditional_counts}\n")

# Estimate CPDs for the model.
model.fit(data, estimator=BayesianEstimator, prior_type="BDeu")

with open("model_cpds.txt", "w") as f_model_cpds:
    for cpd in model.get_cpds():
        f_model_cpds.write(f"{str(cpd)}\n")
