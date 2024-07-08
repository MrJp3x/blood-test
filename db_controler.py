from base_vars import present_date


def add_test(test_type: str,
             score: float,
             date: str = present_date(),
             description=None):
    match test_type:
        case 'INR':
            with open(f'INR.txt', 'w') as f:
                f.write(f'{date} : INR={score} | description={description}\n')
        case 'CBC':
            with open(f'CBC.txt', 'w') as f:
                f.write(f'{date} : CBC={score} | description={description}\n')


def read_test(test_type: str, date: str):
    with open(f'{test_type}.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            print(line)
