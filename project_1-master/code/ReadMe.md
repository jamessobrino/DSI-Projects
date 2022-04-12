Problem Statement: Standardized test scores have been used to determine college placement as well as a metric for teaching outcomes. This project aims to identify any trends with education spending per pupil, and SAT/ACT scores using U.S. census data.

|Feature|Type|Dataset|Description|
|---|---|---|---|
|column name|int/float/object|ACT/SAT|This is an example| 
|state|object|All|This column labels each state for the dataframe.|
|sat_participation|float|SAT|Participation data for SAT|
|english_sect|int|SAT|Mean scores for the english section of SAT|
|math_sect|int|SAT|Mean scores for the math section of SAT|
|total_score|int|SAT|Mean scores for total score of math and english sections|
|act_participation|float|ACT|Participation data for ACT|
|act_composite|float|ACT|Mean score of ACT|
|total|float|census|Total spending per pupil.|
|emp_wages|float|census|Amounts paid for compensation of school system officers and employees. Consists of gross compensation before deductions for withheld taxes, retirement contributions, or other purposes per pupil|
|emp_benefits|float|census|Total spending on employee benefits per pupil|
|instr_total|float|census|Total spending on instructors per pupil|
|instr_wages|float|census|Total Spending on instructor wages per pupil|
|instr_benefits|float|census|Total spending on instructor benefits|
|sup_total|float|census|Total spending on support services per pupil|
|pupil_sup|float|census|Expenditure for attendance record-keeping, social work, student accounting, counseling, student appraisal, record maintenance, and placement services. This category also includes medical, dental, nursing, psychological, and speech services.|
|staff_sup|float|census|recruitment, staff accounting, noninstructional in-service training, staff health services|
|gen_admin|float|census|Expenditure for board of education and executive administration (office of the superintendent) services|
|school_admin|float|census|Expenditure for the office of principal services|

Summary: 

States that have mandatory standardized testing, tend to have lower mean scores. I predict this is a result
of the population of students taking the test being every student, instead of only students
with college aspirations.


Recomendations: 

For states with high participation rates as a result of using these tests as a measure for student success, investing into an high school exit exam like california could increase test scores.

If your state is Oklahoma, you should audit your education system. While you spend very little on education, you are not producing the same results as a comparable state spender such as Utah. Your SAT test scores are shockingly low for a state with very low participation.

