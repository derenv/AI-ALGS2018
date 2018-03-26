import networkx as nx
import matplotlib.pyplot as plt
import argparse as ap
import os.path as pt

#vars
default_path='/home/deren/Documents/University/4 - AI & ALGORITHMS/2 - datasets/facebook/facebook_combined.txt'

#get arguements
parser = ap.ArgumentParser(description='Draw graph in python', argument_default=default_path)
parser.add_argument('input_path', metavar='I', type=str, nargs='?', help='the input file path')
args=parser.parse_args()

#test if valid input file
print('Input file:')
print(args.input_path)
if pt.isfile(args.input_path):
    print('..valid file..')

    #get graph
    path=args.input_path
else:
    print('..invalid file..')
    print('..using default facebook data..')

    #get graph
    path=default_path


#visualise graph
g=nx.read_edgelist(path,create_using=nx.Graph(),nodetype=int)

print nx.info(g)

sp=nx.spring_layout(g)

plt.axis('off')

nx.draw_networkx(g,pos=sp,with_labels=False,node_size=35)

plt.show()
