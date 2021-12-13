import requests
import re

res = requests.get("http://www.columbia.edu/~fdc/sample.html")
sample = r"(?<=>).+(?=</h3>)"
tags = re.findall(sample, res.text)
print(tags)

