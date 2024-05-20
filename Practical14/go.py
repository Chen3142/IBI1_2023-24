#import the libraries
import os
import xml.dom.minidom as minidom
import xml.sax as sax
from datetime import datetime
import matplotlib.pyplot as plt

#change the working directory
os.chdir("D:\\桌面\\IBI\\IBI1_2023-24\\Practical14")

#Define a function that parses an XML file using DOM methods
def parse_with_dom(file_path):
    doc = minidom.parse(file_path) #read the XML file
    terms = doc.getElementsByTagName("term") #find the "term" element
    
    #creat dictionary "counts" to record the counts of the three different ontologies.
    counts = {
        "molecular_function": 0,
        "biological_process": 0,
        "cellular_component": 0
    }
    
    #loop through all points of the "term" and get "namespace" to updata the counts
    for term in terms:
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        if namespace in counts:
            counts[namespace] += 1 #if the "namespace" in the dictionary "counts", the corresponding counts add 1.
    
    return counts #return to the dictionary

#Define a function that parses XML using SAX
class GOHandler(sax.ContentHandler):
    def __init__(self): #set the initial data and dictionary
        self.current_data = ""
        self.namespace = ""
        self.counts = {
            "molecular_function": 0,
            "biological_process": 0,
            "cellular_component": 0
        }
    
    def startElement(self, tag, attributes):
        self.current_data = tag #store the data
    
    def endElement(self, tag):
        if self.current_data == "namespace":
            if self.namespace in self.counts:
                self.counts[self.namespace] += 1 #if the "self.namespace" value in the dictionary, the counts add 1.
        self.current_data = "" #Reset to an empty string
    
    def characters(self, content):
        if self.current_data == "namespace": 
            self.namespace = content #if the element is "namespace", store the "namespace" content in "slef.namespace"

def parse_with_sax(file_path):
    handler = GOHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    
    return handler.counts

#Measure execution time
file_path = "go_obo.xml"

#measure DOM time
start_time = datetime.now()
dom_counts = parse_with_dom(file_path)
dom_time = datetime.now() - start_time

#measure SAX time
start_time = datetime.now()
sax_counts = parse_with_sax(file_path)
sax_time = datetime.now() - start_time

#Print results
print("DOM Counts:", dom_counts)
print("DOM Time:", dom_time)
print("SAX Counts:", sax_counts)
print("SAX Time:", sax_time)

#explain which was fastest
if dom_time < sax_time:
    print("DOM was faster")
elif dom_time > sax_time:
    print("SAX was faster")
else:
    print("DOM and SAX have the same time.")

#define the function to draw the figure
def plot_counts(dom_counts, sax_counts):
    labels = list(dom_counts.keys()) #get the labels and values
    dom_values = list(dom_counts.values())
    sax_values = list(sax_counts.values())
    
    x = range(len(labels)) #x axis
    
    #Creates a figure with two subgraphs
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6)) 
    
    #DOM bar charts 
    ax1.bar(x, dom_values, color='b', alpha=0.7)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_title("DOM Counts")
    
    #SAX bar charts
    ax2.bar(x, sax_values, color='g', alpha=0.7)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    ax2.set_title("SAX Counts")
    
    #adjusts subgraph layout to avoid overlapping
    plt.tight_layout()
    plt.show()
    plt.clf()

#apply the function
plot_counts(dom_counts, sax_counts)