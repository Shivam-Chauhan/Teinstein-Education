from datetime import date,timedelta
from dateutil.parser import parse

def standard_date(given):  # Converting the given date to formatted date
    return date(int(given[0:4]),int(given[5:7]),int(given[8:11]))

def date_formatter(content): # Changing 3 Jun,2021 to 3,6,2021
    stri=content[1].strip()+" "+content[0]
    return str(parse(stri))
    
def modify_file(input_file,yesterday,tomorrow): # Changing the content of the file "yesterday"-> yesterday date and same for 
                                                # "tomorrow"-> to tomorrow's date.
    content=input_file.read()
    if "Yesterday" in content or "yesterday" in content:
        content=content.replace("Yesterday",str(yesterday)) # replacing every instance.
        content=content.replace("yesterday",str(yesterday))
    if "Tomorrow" in content or "tomorrow" in content:
        content=content.replace("Tomorrow",str(tomorrow)) # replacing every instance.
        content=content.replace("tomorrow",str(tomorrow))
    return content
    


if __name__=='__main__':
    input_file=open(r' ',"r") # ' ' input the file path from where you want to READ the file.
    out_file=open(r'',"w")    # ' ' similar to the above
    content=list(input_file.readline().split(","))
    inputed_date=date_formatter(content)
    current_date=date.today().isoformat()
    date1=standard_date(inputed_date)
    date2=standard_date(current_date)
    if date1 !=date2:               # If the date inputed don't match to the actual date than replacing the conditions by calling
                                    # modify_file function.
        difference =date2-date1
        difference=str(difference).split(" ")
        yesterday=(date.today()-timedelta(days=int(difference[0])+1)) # Calculating yesterday's date.
        tomorrow=(date.today()-timedelta(days=int(difference[0])-1))  # Calculating tomorrow's date.
        out_file.write(modify_file(input_file,yesterday,tomorrow))
    else:
        out_file.write(input_file)  # Else inputing everything onto the file 
    out_file.close()
    input_file.close()  # Closing both the files.



# Since the given date is not formatted in the file, the main work is done to format the date to actual ISO format.
# Rest of the work is done by the Python datetime module and parse function.
# Sample file is inputed in variable -> input_file and output is given to out_file.
# Both are in .txt format.

