import pandas as pd

def createDataframe(student_data: List[List[int]])-> pd.DataFrame:
    column_names = ["student_id","age"]
    result = pd.DataFrame(student_data, columns = ["student_id","age"])
    return result