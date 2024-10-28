import csv

def save_job_posting_url(url, filename='csv/job_postings.csv'):
    # Open the CSV file in append mode
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writerow(['jd_url'])
        
        # Write the job posting URL
        writer.writerow([url])

# Example usage
job_posting_url = input("Enter the job posting URL: ")
save_job_posting_url(job_posting_url)