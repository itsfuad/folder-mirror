"""Generate dry-run copy plans from two directory inventory listings."""

def analyze(text):
    left={};right={}
    for line in text.splitlines():
        if not line.strip():continue
        parts=line.strip().split('|',2)
        if len(parts)!=3 or parts[0] not in ('left','right'):continue
        side,path,size=parts
        (left if side=='left' else right)[path]=size
    copy=sorted(p for p,size in left.items() if right.get(p)!=size)
    extra=sorted(p for p in right if p not in left)
    return {'copy':copy,'target_only':extra,'missing_count':len(copy)}
