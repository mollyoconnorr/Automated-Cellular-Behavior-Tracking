import subprocess

# Paths
cellprofiler_exe = "/Applications/CellProfiler.app/Contents/MacOS/cp"
pipeline_file = "/Users/newuser/Desktop/Internship/PythonProject/pipeline.cppipe"
input_folder = "/Users/newuser/Desktop/Internship/PythonProject/InputImages"
output_folder = "/Users/newuser/Desktop/Internship/PythonProject/TestingOutput"

# Command to run
cmd = [
    cellprofiler_exe,
    "-c",  # run headless
    "-r",  # run the pipeline
    "-p", pipeline_file,
    "-i", input_folder,
    "-o", output_folder
]

print(f"Running CellProfiler pipeline...")

try:
    # Run command, capture output
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    # Only print real errors (stderr)
    if result.stderr:
        print("Errors or warnings from CellProfiler:")
        # Filter out non-critical messages if desired
        for line in result.stderr.splitlines():
            if "Error" in line or "Traceback" in line:
                print(line)

    print("Pipeline finished successfully!")
    print(f"Output folder: {output_folder}")

except subprocess.CalledProcessError as e:
    print("CellProfiler failed to run:")
    print(e.stderr)