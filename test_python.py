# Config section at the top of the Snakefile
configfile: "config.yaml"



# Access the input and output folder paths from the config
INPUT_FLD = config["input_folder"]
OUTPUT_FLD = config["output_folder"]

# Rule to process all .gz files in the input folder
rule all:
    input:
        expand(f"{OUTPUT_FLD}/{{file}}", file=[f.replace('.gz', '') for f in os.listdir(INPUT_FLD) if f.endswith('.gz')])

# Rule to gunzip files
rule gunzip_files:
    input:
        f"{INPUT_FLD}/{{file}}.gz"
    output:
        f"{OUTPUT_FLD}/{{file}}"
    shell:
        """
        echo "Unzipping {input} to {output}"
        gunzip -c {input} > {output}
        """

