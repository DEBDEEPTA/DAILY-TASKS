"""
NumPy (Intermediate)
 An online platform tracks time spent (in minutes) by students on 6 courses over 14 days using a NumPy array.
Task:
    Compute total time spent per course
    Identify courses where average daily engagement exceeds a threshold
    Rank courses based on engagement
"""

"""
    # LOGIC THINKING
    [   c1 <- time spend on course 1
        c2 <- ....................
        
        [c1,c2,c3,c4,c5,c6]  <- d1
        []  <- d2
        []  .
        []  .
        []  <- d14
    ]
    (14 , 6)
    
"""
import numpy as np


def total_time_per_course(data):

    """
        each column = time spend on that course
        total time spend on every course -> .sum(axis=0) <- column wise
    """
    net_time_per_crs = data.sum(axis=0)
    return net_time_per_crs

def avg_daily_eng(data):
    """
        let, threshoald = 8*60
    """
    limit = 2*60

    avg_daily_eng_per_crs = data.mean(axis=0)
    filter_crs_indices = np.where(avg_daily_eng_per_crs>limit)
    """
       1. np.where(condition: if_true, if_false)
        
        if only condition is mentioned for np.where() it returnees the indices for the values that 
        satisfies the condition
        
        2. np.where(condition) <- return only indices
    """

    return filter_crs_indices

def course_ranking(data):
    time_spend_crs = total_time_per_course(data)
    ranked_courses = np.argsort(time_spend_crs)[::-1]

    return ranked_courses

if __name__ == "__main__":

    max_min = 6*60 # MAXIMUM MINUTES SHOULD BE STUDIED FOR 1 DAY
    min_min = 0     # MIN MIN FOR 1 DAY
    student_data = np.random.randint(min_min, max_min,(14,6))

    print(f"Sample Student data :\n{student_data}")
    print(f"Total Time Per Course :\n{total_time_per_course(student_data)}")

    print(f" Courses for which Avg Daily Eng > Threshold:\n{avg_daily_eng(student_data)}")

    print(f"Courses Ranked Based On Engajement:\n{course_ranking(student_data)}")