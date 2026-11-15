"""
RECORD CHECK  -  my version
===========================

Name  : bryan
Lane  :  AI      (delete two)
Date  : 12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here

def status_of(rating):
    """Return OVER LIMIT, WARNING or OK depending on the survey rating."""
    
    if rating <= 2:
        return "OVER LIMIT"
    elif rating == 3:
        return "WARNING"
    else:
        return "OK"


def parse_line(raw_line):
    """Turn one messy survey line into a clean dictionary."""
    
    line = raw_line.strip()
    survey_part, rest = line.split(",", 1)
    survey = survey_part.strip().lower()
    
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())
    
    return {
        "survey": survey,
        "rating": fields["rating"],
        "age": fields["age"]
    }








# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.



with open("messy_lines.txt", "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write(" Survey_2025 , rating=5 , age=22\n")
    f.write(" Survey_2024 , rating=3 , age=25  \n")
    f.write("Survey_2023 , rating=2 , age=27  \n")
    f.write(" Survey_2022 , rating=1 , age=19\n")

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.
  # replace with your code
total_records = 0
flagged_records = 0

with open("messy_lines.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        
        status = status_of(record["rating"])
        
        print(record["survey"], status)
        print(record)
        
        total_records += 1
        
        if status == "OVER LIMIT":
            flagged_records += 1

print("Total records:", total_records)
print("Flagged records:", flagged_records)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
# 1. Define parsing and status evaluation functions

