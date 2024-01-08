import argparse
import os
from os.path import splitext
from glob import glob
from fileinput import filename 
from flask import *  
app = Flask(__name__)   

# TODO (cara): this is sorta gross
directory = ""

@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/uploadMedia', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file']
        if f:
            existingFiles = glob(directory + "*")
            for file in existingFiles:
                os.remove(file)
            extension = splitext(f.filename)[1]
            f.save(directory + "toplay" + extension)   
        return render_template("uploaded.html")   
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Web server")
    parser.add_argument('-d', '--directory', required=True)
    args = parser.parse_args()
    directory = os.path.join(args.directory, "")
    app.run(host="0.0.0.0",debug=True)
