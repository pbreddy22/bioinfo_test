import os

# Config section at the top of the Snakefile
configfile: "config.yaml"

# Access the input and output folder paths from the config
INPUT_FLD = config["input_folder"]
OUTPUT_FLD = config["output_folder"]

# Function to get all input gz files
def get_input_files():
    return [f for f in os.listdir(INPUT_FLD) if f.endswith('.gz')]

# Function to get all output files
def get_output_files(wildcards):
    return expand(f"{OUTPUT_FLD}/{{file}}", file=[f.replace('.gz', '') for f in get_input_files()])

# Rule to process all .gz files in the input folder
rule all:
    input:
        get_output_files

# Rule to gunzip files
rule gunzip_files:
    input:
        f"{INPUT_FLD}/{{file}}.gz"
    output:
        f"{OUTPUT_FLD}/{{file}}"
    shell:
        """
        echo "Unzipping {input} to {output}"
        gunzip -c {{input}} > {{output}}
        """






import os

# Config section at the top of the Snakefile
configfile: "config.yaml"

# Access the input and output folder paths from the config
INPUT_FLD = config["input_folder"]
OUTPUT_FLD = config["output_folder"]

# Function to get all input gz files
def get_input_files():
    return [f for f in os.listdir(INPUT_FLD) if f.endswith('.gz')]

# Function to get all output files
def get_output_files():
    return [os.path.join(OUTPUT_FLD, f.replace('.gz', '')) for f in get_input_files()]

# Rule to process all .gz files in the input folder
rule all:
    input:
        get_output_files()

# Rule to gunzip files
rule gunzip_files:
    input:
        os.path.join(INPUT_FLD, "{file}.gz")
    output:
        os.path.join(OUTPUT_FLD, "{file}")
    shell:
        """
        echo "Unzipping {input} to {output}"
        gunzip -c {input} > {output}
        """







import os

# Config section at the top of the Snakefile
configfile: "config.yaml"

# Access the input and output folder paths from the config
INPUT_FLD = config["input_folder"]
OUTPUT_FLD = config["output_folder"]

# Get all input .gz files
input_files = [f for f in os.listdir(INPUT_FLD) if f.endswith('.gz')]

# Generate output files by replacing .gz with an empty string
output_files = [os.path.join(OUTPUT_FLD, f.replace('.gz', '')) for f in input_files]

# Rule to process all .gz files in the input folder
rule all:
    input:
        output_files

# Rule to gunzip files
rule gunzip_files:
    input:
        os.path.join(INPUT_FLD, "{file}.gz")
    output:
        os.path.join(OUTPUT_FLD, "{file}")
    shell:
        """
        echo "Unzipping {input} to {output}"
        gunzip -c {input} > {output}
        """


import os

# Full paths to the input files
SAMPLES = ["/path/to/sample1.fastq.gz", "/path/to/sample2.fastq.gz"]

# Output directory
OUTPUT_DIR = "unzipped"

# Function to get the base filename without extension
def get_basename(path):
    return os.path.splitext(os.path.splitext(os.path.basename(path))[0])[0]

rule all:
    input:
        expand(os.path.join(OUTPUT_DIR, "{sample}.fastq"), sample=[get_basename(s) for s in SAMPLES])

rule gunzip:
    input:
        lambda wildcards: [s for s in SAMPLES if get_basename(s) == wildcards.sample][0]
    output:
        os.path.join(OUTPUT_DIR, "{sample}.fastq")
    shell:
        "gunzip -c {input} > {output}"

       
