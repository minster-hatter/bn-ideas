from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork

# Create the Bayesian network structure.
earthquake_model = BayesianNetwork(
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
earthquake_model.add_cpds(
    cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls
)

# Check if the model seems OK and write the output to a file.
with open("earthquake_model_check.txt", "w") as f_check:
    f_check.write(
        "The earthquake model passed the check: "
        f"{earthquake_model.check_model()}."
    )

# Draw the Bayesian network.
earthquake_daft = earthquake_model.to_daft(
    node_pos="kamada_kawai", pgm_params={"observed_style": "inner"}
)
earthquake_daft.render()
earthquake_daft.savefig("earthquake_DAG.png")

# Write some independence checks to files.
with open("earthquake_indep_burglary.txt", "w") as f_burglary:
    f_burglary.write(str(earthquake_model.local_independencies("Burglary")))

with open("earthquake_indep.txt", "w") as f_indep:
    f_indep.write(
        f"Model independencies:\n{earthquake_model.get_independencies()}"
    )

# Output a conditional probability distribution (CPD).
with open("earthquake_cpd_alarm.txt", "w") as f_cpd_alarm:
    f_cpd_alarm.write(str(earthquake_model.get_cpds("Alarm")))

# Make some inferences and predictions. and write to a file.
infer = VariableElimination(earthquake_model)
mary_calls_dist = infer.query(["MaryCalls"])
mary_calls_alarm_dist = infer.query(["MaryCalls"], evidence={"Alarm": 1})
mary_calls_prediction = infer.map_query(["MaryCalls"])
mary_calls_alarm_prediction = infer.map_query(
    ["MaryCalls"], evidence={"Alarm": 1}
)

with open("earthquake_Mary_inference.txt", "w") as f_Mary:
    f_Mary.write(f"{mary_calls_dist}")
    f_Mary.write(f" Prediction: {mary_calls_prediction}\n")
    f_Mary.write("When there has been an alarm...\n")
    f_Mary.write(str(mary_calls_alarm_dist))
    f_Mary.write(f" Prediction: {mary_calls_alarm_prediction}")
