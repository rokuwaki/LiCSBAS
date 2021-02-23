#!/usr/bin/env python3
'''
# LiCSBAS_get_ready.py
A python script to make a working directory and fetch batch_LiCSBAS.sh to get you ready for LiCSBAS!

# Example usage
```sh
$ LiCSBAS_get_ready.py 124D_04854_171313
```
'''

import os
import sys
import stat
import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description='Make a working dir. and fetch `batch_LiCSBAS.sh` to get you ready for LiCSBAS!')
    parser.add_argument('FRAME_ID', metavar='FRAME_ID', type=str, help='Frame ID you would like to process: e.g.) 124D_04854_171313')
    args = parser.parse_args()

    # Make a working directory named as `FRAME_ID`
    os.makedirs(args.FRAME_ID, exist_ok=True)
    print('{:27s}'.format('Made a directory:') + './' + str(args.FRAME_ID))

    # Download the script from Github repository
    file_url = 'https://github.com/yumorishita/LiCSBAS/raw/master/batch_LiCSBAS.sh'
    r = requests.get(file_url)
    file_data = r.content
    file_name = os.path.join(args.FRAME_ID, os.path.basename(file_url))
    with open(file_name, 'w+b') as f:
        f.write(bytearray(file_data))
    print('{:27s}'.format('Fetched a script:') + './' + file_name)

    # Make the scirpt executable. Equivalent to $ chmod u+x batch_LiCSBAS.sh
    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)

    print('{:27s}'.format('You\'re ready for LiCSBAS!') + '$ cd ./' + args.FRAME_ID)

if __name__ == '__main__':
    main()
