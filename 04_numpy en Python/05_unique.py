import numpy as np

survey_responses = np.array([['Yes', 'No', 'Yes', 'No', 'No'], ['No', 'No', 'Yes', 'Yes', 'Yes'], ['Yes', 'Yes', 'Yes', 'No', 'No'], ['No', 'No', 'No', 'No', 'Yes'], ['Yes', 'Yes', 'No', 'No', 'Yes']])

print(np.unique(survey_responses))

yes_responses = survey_responses == 'Yes'
print(yes_responses)

yes_count = np.sum(yes_responses, axis=0)
print(yes_count)

no_responses = survey_responses == 'No'
print(no_responses)

array_x = np.arange(1, 250)
view_y = array_x[1:200]
print(view_y)

array_y = np.arange(1, 250)
copy_x = array_y[1:200].copy()
print(copy_x)

