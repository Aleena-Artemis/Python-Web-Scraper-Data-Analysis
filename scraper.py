import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website (Fake Jobs site for demo)
URL = "Add Url here"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Extract job titles
job_elements = soup.find_all("h2", class_="title")
jobs = [job.text.strip() for job in job_elements]

# Save to CSV
df = pd.DataFrame(jobs, columns=["Job Title"])
df.to_csv("jobs.csv", index=False)

print("✅ Scraped and saved job titles into jobs.csv")

# Simple Analysis
word_counts = df['Job Title'].str.split(expand=True).stack().value_counts().head(10)
print("\n📊 Top Words in Job Titles:")
print(word_counts)
