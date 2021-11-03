#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:32:36 2020

@author: sean
"""
## Import the required libraries and the data we just created
import networkx as nx
import pandas as pd

nodes = pd.read_csv('data/node_list.csv', low_memory=False)
edges = pd.read_csv(**, low_memory=False)

## Initialise a graph object which we will assign to the variable G
** = nx.Graph()

## Tranform the data into the correct format for use with NetworkX
# Node inputs are tuples of the node ID and a dictionary of attributes
# Node tuples (ID, dict of attributes)
idList = nodes[**].tolist()
labels =  pd.DataFrame(nodes['Label'])
labelDicts = **.to_dict(orient='records')
nodeTuples = [tuple(r) for r in zip(idList,labelDicts)]

## Edge inputs are tuples of source ID, target ID and a dictionary of attributes
# Edge tuples (Source, Target, dict of attributes)
sourceList = edges[**].tolist()
targetList = edges['Target'].tolist()
weights = pd.DataFrame(edges[**])
weightDicts = **.to_dict(orient='records')
edgeTuples = [tuple(r) for r in zip(sourceList,**,weightDicts)]

## Add the nodes and edges to the graph
G.add_nodes_from(**)
G.add_edges_from(**)

## create the plot layout and draw the graph
## https://networkx.github.io/documentation/stable/reference/drawing.html

## We pass the graph object to a layout algorithm to determine the node coordinates and hence the edge start and end points
pos = nx.kamada_kawai_layout(**) #kamada_kawai_layout(G[, dist, pos, weight, …]) Position nodes using Kamada-Kawai path-length cost-function.

## Finally we draw the graph passing in the graph object G, the position object pos and adjust the node size
plot = nx.draw(**, pos=**, node_size=100, with_labels=True, font_size=10)
