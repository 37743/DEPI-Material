# Task 1
# Yousef Ibrahim Gomaa Mahmoud
# -----------------------------------
import sys, getopt
import pandas as pd
import json
import os, time

def main():
    start = time.time()

    argv = sys.argv[1:]
    opts, _ = getopt.getopt(argv, "i:o:u")
    input_path = ''
    output_path = ''
    unix = False

    print('-----------------------------------')

    try:
        for opt, arg in opts:
            if opt == '-i':
                input_path = arg
            elif opt == '-o':
                output_path = arg
            elif opt == '-u':
                unix = True
    except getopt.GetoptError:
        print('Task-1-YousefGomaa.py -i <input_path> -o <output_path> -u')
        return
    
    files = os.listdir(input_path)
    files = [file for file in files if file.endswith('.json')]

    for file in files:
        with open(input_path + '\\' + file, 'r') as f:
            data = f.readlines()
            data = [json.loads(line) for line in data]

            print(f'{len(data)} records found in:\n\t {input_path + '\\' + file}')

            df = pd.DataFrame(data)
            # "a": "Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/535.11 (KHTML, like Gecko) Chrome\/17.0.963.78 Safari\/535.11"
            # the browser is the part before every first and second '/' in the whole string
            df['browser'] = df['a'].str.extractall(r'([A-Za-z]+\/[0-9.]+)').groupby(level=0).apply(lambda x: ' '.join(x[0]))
            df['operating_sys'] = df['a'].str.extract(r'([A-Za-z]+ .[A-Za-z]+ [0-9.]+)')

            df['from_url'] = df['r'].str.extract(r'(www\.[A-Za-z0-9]+.[A-Za-z]+)')
            df['to_url'] = df['u'].str.extract(r'(www\.[A-Za-z0-9]+.[A-Za-z]+)')

            df['city'] = df['cy']
            df['latitude'] = df['ll'].str[0]
            df['longitude'] = df['ll'].str[1]
            df['time_zone'] = df['tz']

            if unix:
                df['time_in'] = df['t']
                df['time_out'] = df['hc']
            else:
                
                df['time_in'] = pd.to_datetime(df['t'], unit='s', errors='coerce')
                df['time_out'] = pd.to_datetime(df['hc'], unit='s', errors='coerce')
        
            df.drop(['a', 'c', 'nk', 'tz', 'gr', 'g', 'h', 'l', 'al', 'hh', 'r', 'u', 't', 'hc', 'cy', 'll'], axis=1, inplace=True)

            for col in df:
                data_type = df[col].dtype
                if data_type == int or data_type == float:
                    df[col].fillna(0)
                else:
                    df[col].fillna("")
            
            df.drop_duplicates(inplace=True)
            
            df.to_csv(output_path + '\\' + file.split('.')[0] +f"-u={unix}" + '-YousefGomaa' + '.csv', index=False)
           
            print(f'{len(df)} rows transformed and saved to:\n\t {output_path + '\\' + file.split(".")[0] + ".csv"}')
            
    end = time.time()

    print('-----------------------------------')
    print(f'Total execution time: {end - start} seconds')
    return

if __name__ == '__main__':
    main()