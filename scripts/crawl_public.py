from pathlib import Path
import requests,json,csv,time,hashlib
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlsplit,urldefrag
from concurrent.futures import ThreadPoolExecutor
def markdownify(html): return BeautifulSoup(html,'html.parser').get_text('\n',strip=True)
root=Path(__file__).resolve().parent.parent/'knowledge-base'/'current-site'; (root/'pages').mkdir(exist_ok=True)
base='https://nexuscreativehq.com';seen=set();queue=[base+'/'];rows=[];assets=set();external=set()
queue += [base+p for p in ['/become-partner','/booking','/booking?location=Accra','/booking?location=London','/booking?location=Shanghai','/esg','/investment','/memberships','/scale-up-journey','/visa-routes','/sitemap_index.xml']]
def fetch(u):
 try:
  r=requests.get(u,timeout=25);return u,r,None
 except Exception as e:return u,None,str(e)
while queue and len(seen)<250:
 batch=[u for u in dict.fromkeys(queue) if u not in seen][:min(8,250-len(seen))];queue=[u for u in queue if u not in batch and u not in seen];seen.update(batch)
 if not batch:break
 for u,r,e in ThreadPoolExecutor(max_workers=4).map(fetch,batch):
  row={'url':u,'status':r.status_code if r is not None else None,'final_url':r.url if r is not None else None,'error':e};rows.append(row)
  if r is None:continue
  row['redirects']=[{'status':h.status_code,'url':h.url} for h in r.history]
  if 'text/html' not in r.headers.get('Content-Type',''):continue
  soup=BeautifulSoup(r.text,'html.parser');row.update(title=soup.title.get_text(' ',strip=True) if soup.title else '',description=(soup.find('meta',attrs={'name':'description'}) or {}).get('content',''),h1=[h.get_text(' ',strip=True) for h in soup.find_all('h1')],canonical=(soup.find('link',rel='canonical') or {}).get('href',''),robots=(soup.find('meta',attrs={'name':'robots'}) or {}).get('content',''))
  row['forms']=[{'action':f.get('action'),'method':f.get('method'),'fields':[i.get('name') for i in f.select('input,select,textarea')]} for f in soup.find_all('form')]
  row['images']=[{'url':urljoin(r.url,i.get('src','').strip()),'alt':i.get('alt')} for i in soup.find_all('img') if i.get('src')];assets.update(i['url'] for i in row['images'])
  row['links']=[]
  for a in soup.find_all('a',href=True):
   link=urldefrag(urljoin(r.url,a['href'].strip()))[0];p=urlsplit(link)
   if p.scheme not in ['http','https']:continue
   row['links'].append({'url':link,'text':a.get_text(' ',strip=True)})
   if p.netloc in ['nexuscreativehq.com','www.nexuscreativehq.com']:
    if not p.path.startswith(('/admin','/login','/logout')) and not any(p.path.lower().endswith(x) for x in ['.jpg','.png','.pdf','.zip','.jpeg','.svg','.webp','.mp4']):
     if link not in seen:queue.append(link)
   else:external.add(link)
  stem=hashlib.sha256(u.encode()).hexdigest()[:12];row['file']=stem
  (root/'pages'/f'{stem}.html').write_text(r.text,encoding='utf-8')
  for n in soup(['script','style','noscript']):n.decompose()
  (root/'pages'/f'{stem}.md').write_text('# '+row['title']+'\n\nSource: '+u+'\n\n'+markdownify(str(soup)),encoding='utf-8')
 print('Pages',len(seen),'queued',len(queue),flush=True)
(root/'inventory.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
(root/'external-links.json').write_text(json.dumps(sorted(external),indent=2),encoding='utf-8')
assetrows=[]
for u,r,e in ThreadPoolExecutor(max_workers=6).map(fetch,sorted(assets)):
 assetrows.append({'url':u,'status':r.status_code if r is not None else None,'error':e})
(root/'image-status.json').write_text(json.dumps(assetrows,indent=2),encoding='utf-8')
with (root/'page-inventory.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['url','status','final_url','title','description','h1','canonical','robots','file'],extrasaction='ignore');w.writeheader();w.writerows(rows)
print('DONE',len(rows),'pages',len(assetrows),'images',len(external),'external links',flush=True)


