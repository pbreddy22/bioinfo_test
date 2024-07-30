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
