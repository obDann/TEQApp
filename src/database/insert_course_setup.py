import sqlite3
import database_methods
import insert_helper
import insert_general
import pandas as pd

def insert_target_group(row_values):
    # check if direct at target group field is Yes
    if (row_values[30] == "Yes"):
        target_id = insert_general.insert_target_group(row_values, 31, 45)
        return target_id
    
    return 0

def insert_instructor_address(row_values):
    index = [(49, 54), (55, 56), (54, 55), (56, 57)]
    add_id = insert_general.insert_address(row_values, index)
    
    return add_id

def insert_course(row_values, target_group_id):
    index = [(2, 14), (17, 19), (25, 31), (45, 48)]
    val = database_methods.fetch_values_list(row_values, index, [])
    val.append(target_group_id)
    
    insert_helper.insert_row(val, "LT_Course")

def insert_instructor(row_values, course_code, add_id):
    index = [(48, 49), (57, 60)]
    val = [course_code, add_id]
    val = database_methods.fetch_values_list(row_values, index, val)
    
    insert_helper.insert_row(val, "Instructor")

def insert_skill_levels(column_values, row_values, course_code):
    insert_general.insert_3_value(column_values, row_values, "Skill_Levels",
                                  course_code, 60, 117)