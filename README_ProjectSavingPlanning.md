
# Python Project (1)

## Saving Planning 


**Saving Planning** is a program that calculates the duration to reach your saving goal by entering salary and goal and monthly expenses.

### Functions:

* Adding A Savings Plan
* Calculate The Duration
* Display Information
* Delete Plan

### Adding a Savings Plan:
```python
saving = {
    "goal" : 0,
    "salary" :  0,
    "financial_obligations" : []
}
def add_saving_plan():
    global financial_sum
    saving["income"] = income
    saving["goal"] = goal
    saving["financial_obligations"] = financial_obligations

```
### Calculate The Duration:
```python

calc_months = lambda x, sum_obligations: math.ceil(x["goal"] / (x["income"] - sum_obligations))
        months = calc_months(x, financial_sum)  # Using the lambda function

```
### Display Information:
```python

if not x or not any(x.values()):
        print("You don't have a plan! \n")
    else:
        print("\nPlan Info:")
        print("\n Income :" , x["income"])
        print(" Goal :" , x["goal"])
        print(" Financial obligations :", financial_sum)
        print(" Net save: " , x["income"] - financial_sum )
        print(" Months: ", months)
        print()

```
### Delete Plan:
```python
def delete_plan():

    global saving
    if not saving or not any(saving.values()):
        print("You don't have a plan to delete it! \n")
    else:
        saving = {
        "goal" : 0,
        "salary" :  0,
        "financial_obligations" : []
        }
        print("Plan Deleted! \n")

```
