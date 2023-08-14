from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def extract_video_links(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        mp4_links = [a["href"] for a in soup.find_all("a", href=True) if ".mp4" in a["href"]]

        context = {'mp4_links': mp4_links}
        return render(request, 'videolinks/result.html', context)

    return render(request, 'videolinks/extract.html')
