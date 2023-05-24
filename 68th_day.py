import argparse
import requests
import sys

# def download_file(url,local_filename):
#     # local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     return local_filename

# parser = argparse.ArgumentParser()

# #add commmand liine arguments
# parser.add_argument("url",help="Url of the file to download")

# parser.add_argument("output",help="by which name do you want to save")

# #parse the arguments
# args = parser.parse_args()


# #Use the arguments  in your code

# print(args.url)
# print(args.output)
# download_file(args.url,args.output)

def calc(args):
    if args.o =='add':
        return args.x + args.y
    
    elif args.o =='sub':
        return args.x - args.y
    
    elif args.o =='div':
        return args.x / args.y
    
    elif args.o =='mul':
        return args.x * args.y

    else:
        return 'something went wrong'
    
    


if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="enter the first number")

    parser.add_argument('--y',type=float,default=3.0,help="Enter second number")

    parser.add_argument('--o',type=str,default="add"
                        ,help="this a a utility for calculations")
    

    args = parser.parse_args()

    sys.stdout.write(str(calc(args)))







