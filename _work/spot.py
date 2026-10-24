import sys,random,glob,re,json,os
sys.stdout.reconfigure(encoding='utf-8')
random.seed(11)
rows=[json.loads(l) for l in open('_meta/questions.jsonl',encoding='utf-8')]
print('--- random sample')
for r in random.sample(rows,28): print(r['id'],'G' if r['generated'] else 'h',r['difficulty'],'|',r['q'][:150])
dr=[]
for f in glob.glob('_work/curated/*.dropped.txt'):
    k=os.path.basename(f).replace('.dropped.txt','')
    for l in open(f,encoding='utf-8'):
        p=l.rstrip('\n').split('\t')
        if len(p)>1 and p[1]=='offscope': dr.append((k,p[0]))
pools={}
print('--- offscope drop sample')
for k,ref in random.sample(dr,18):
    if k not in pools: pools[k]={l.split('\t')[0]:l.rstrip('\n').split('\t')[2] for l in open(f'_work/pools/{k}.tsv',encoding='utf-8') if l.count('\t')>=2}
    print(k,ref,'|',pools[k].get(ref,'?')[:140])
