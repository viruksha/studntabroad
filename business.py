import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['states'].tolist())

    states         = df['states'].tolist()

    students       = df['students'].tolist()

    

    # print(df['quebec'].tolist())

    result_dict = {
        'states'          : states,
        'students '       :  students,
        
    }

    # print(result_dict)

    return result_dict

def add_row(states,students):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'states'      : states, 
        'students'    : students , 

    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()