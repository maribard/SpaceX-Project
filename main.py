from user_iteration import user_iteration
from mission_stage import most_used_first_stages



print("STAGE 1")
print("Please, provide parameters")

param_a, param_b, param_c = user_iteration()

print(most_used_first_stages(param_a, param_b, param_c))
