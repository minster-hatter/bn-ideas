from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork

# Create the Bayesian network structure.
alarm_model = BayesianNetwork(
    [
        ("Burglary", "Alarm"),
        ("Earthquake", "Alarm"),
        ("Alarm", "JohnCalls"),
        ("Alarm", "MaryCalls"),
    ]
)

# Create the probability tables for the Bayesian network.
cpd_burglary = TabularCPD(
    variable="Burglary", variable_card=2, values=[[0.999], [0.001]]
)
cpd_earthquake = TabularCPD(
    variable="Earthquake", variable_card=2, values=[[0.998], [0.002]]
)
cpd_alarm = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
)
cpd_johncalls = TabularCPD(
    variable="JohnCalls",
    variable_card=2,
    values=[[0.95, 0.1], [0.05, 0.9]],
    evidence=["Alarm"],
    evidence_card=[2],
)
cpd_marycalls = TabularCPD(
    variable="MaryCalls",
    variable_card=2,
    values=[[0.1, 0.7], [0.9, 0.3]],
    evidence=["Alarm"],
    evidence_card=[2],
)

# Join structure and probability tables.
alarm_model.add_cpds(
    cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls
)

# Check if the model seems OK and write the output to a file.
with open("alarm_model_check.txt", "w") as f_check:
    f_check.write(
        f"The alarm model passed the check: {alarm_model.check_model()}."
    )

# Draw the Bayesian network.
alarm_daft = alarm_model.to_daft(
    node_pos="kamada_kawai", pgm_params={"observed_style": "inner"}
)
alarm_daft.render()
alarm_daft.savefig("alarm_DAG.png")

# Write some independence checks to files.
with open("alarm_indep_burglary.txt", "w") as f_burglary:
    f_burglary.write(str(alarm_model.local_independencies("Burglary")))

with open("alarm_indep.txt", "w") as f_indep:
    f_indep.write(f"Model independencies:\n{alarm_model.get_independencies()}")
