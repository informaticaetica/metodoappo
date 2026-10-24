"""Ricompone Metodo-APPO-2.0-il-romanzo.md da capitoli/ e parti/.

Uso: python3 componi.py
"""
import glob
import re

caps = sorted(glob.glob('capitoli/*.md'))
out = ['# Metodo APPO 2.0\n\n## Osa Realizzarti Oggi\n\n### Il romanzo\n\n**Marco Costanzo**\n']
toc = ['## Indice\n', '- Come leggere questo romanzo', '- Note legali, Avvertenza, Dedica, Lettera al lettore']
for c in caps:
    for l in open(c, encoding='utf-8'):
        if l.startswith('# '):
            toc.append('\n**' + l[2:].strip() + '**\n')
        elif l.startswith('## '):
            toc.append('- ' + l[3:].strip())
toc += ['', '**APPARATO**', '', '- Le schede dei capitoli', '- Note sugli autori', '- Fonti',
        '', '**STRUMENTI**', '', '- Come usare questa parte', '- Eserciziario',
        '- Appendice — Cento righe del mattino', '- Altri libri di Marco Costanzo']
out.append('\n'.join(toc) + '\n')
out.append(open('parti/nota.md', encoding='utf-8').read())
out.append(open('parti/front.md', encoding='utf-8').read())
for c in caps:
    out.append(open(c, encoding='utf-8').read())
out.append('# APPARATO\n\n## Le schede dei capitoli\n\n'
           'Per ogni capitolo, i concetti chiave del metodo, le domande di verifica e l\'esercizio APPO '
           'dell\'edizione saggistica. Puoi usarle dopo aver letto il capitolo corrispondente, oppure da sole, '
           'per ripassare.\n\n' + open('parti/schede.md', encoding='utf-8').read())
out.append(open('parti/apparato.md', encoding='utf-8').read())
out.append('# STRUMENTI\n\n' + open('parti/strumenti.md', encoding='utf-8').read())
text = '\n\n'.join(s.strip() for s in out) + '\n'
text = re.sub(r'\n{3,}', '\n\n', text)
open('Metodo-APPO-2.0-il-romanzo.md', 'w', encoding='utf-8').write(text)
print(len(text.split()), 'parole')
