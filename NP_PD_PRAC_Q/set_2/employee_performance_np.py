"""
NumPy (Intermediate)
An HR system stores employee performance ratings (scale 1–5) for 100 employees over 4 quarters in a NumPy array.
Task:
    Normalize the ratings using min-max normalization
    Calculate the average rating per employee
    Identify employees whose average rating is above the company mean

"""

"""  
    [    # Performance of employees
        [e1,e2,e3,....e100] <- q1
        [] <- q2
        [] <- q3
        [] <- q4
    ]
    -> dim --> (4,100) 
"""
import numpy as np


def normalize(emp_data):
    max = 5
    min = 1

    """
        normalization_formula 
                        -> Xnorm = (X -Xmix)/(Xmax-Xmin) 
                        -> where x is the value at a index
    """

    normalized_emp_data = ((emp_data-min)/(max - min))

    return normalized_emp_data

def avg_rating_per_empl(empl_data):
    # CALCULATING AVERAGE  OF EACH COLUMN
    # AS EACH COLUMN REPRESENTS RATING FOR THE EMPLOYEE
    avg_rt_per_empl =  empl_data.mean(axis=0)

    return  avg_rt_per_empl

def avg_more_than_mean(empl_data):
    avg_rt_per_empl = avg_rating_per_empl(empl_data)
    company_mean = avg_rt_per_empl.mean()

    empl_avg_above_mean = avg_rt_per_empl[avg_rt_per_empl > company_mean]
    return empl_avg_above_mean

if __name__ =="__main__":

    # SETTING SAMPLE DATA
    empl_data = np.full((4,100),5)

    """ APPROACH 1 (SLOWER)"""
    # for (i,j),val in np.ndenumerate(empl_data):
    #     empl_data[i][2] = 2
    #     empl_data[i][3] = 3

    """ APPROACH 2 (FASTER)"""
    empl_data[:, 2] = 2
    empl_data[:, 3] = 3

    empl_data[2] = 2
    empl_data[2][10] = 3
    empl_data[2][20] = 3
    empl_data[2][30] = 1
    empl_data[2][31] = 4
    empl_data[3] = 4

    print(f"SAMPLE EMPLOYEE DATA :\n{empl_data}")

    print(f"NORMALIZED EMPLOYEE DATA:\n{normalize(empl_data)}")


    print(f"AVERAGE RATING FOR EACH EMPLOYEE:\n{avg_rating_per_empl(empl_data)}")

    print(f"EMPLOYEES HAVING AVERAGE MORE THAN COMPANY MEAN:\n{avg_more_than_mean(empl_data)}")
