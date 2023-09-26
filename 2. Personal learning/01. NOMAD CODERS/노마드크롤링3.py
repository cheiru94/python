from requests import get
from bs4 import BeautifulSoup as bs

def wwrExtractJobs(keyword):
  baseUrl = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
  
  response = get(f"{baseUrl}{keyword}")
  
  if response.status_code != 200:
    print("프로토콜을 가져오지 못했어요.")

  else:  
    soup = bs(response.text, "html.parser")
    
    jobs = soup.find_all('section', class_="jobs")
    
    results = []
    
    for job in jobs:
      job = job.find_all('li')
      job.pop(-1)
      
      for a in job:
        a = a.find_all('a')
        anchor = a[1]
        link = anchor['href']
    
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_='title')
        jobData = {
          'link' : f"https://weworkremotely.com/{link}",
          'company' : company.string,
          'region' : region.string,
          'position' : title.string
        }
        results.append(jobData) if jobData not in results else None
    return results