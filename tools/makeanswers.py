# Scan a file of problem definitions and produce corresponding answer and
# solution rst files

import os, sys, re


# scan the source file for unique question identifiers
sourcepath = sys.argv[1]
retitle = re.compile(" *(.*) *(Example|Practice) +(.+)")
requestion = re.compile("Question.*")
reanswer = re.compile("Answer.*")
resolution = re.compile("Solution.*")
redict = {"Question": requestion, "Answer": reanswer, "Solution": resolution}


def stripblanks(lines):
    if lines[0].strip() == "" and len(lines)>1:
        return stripblanks(lines[1:])
    return lines
    
def stripunderlines(lines):
    if lines[0][0] in ['-','~']:
        return lines[1:]
    return lines

def parsetitle(lines):
    next = stripblanks(lines)
    next = stripunderlines(next)
    f = retitle.match(next[0])
    if f:
        next = stripunderlines(next[1:])
        return f.groups()[0], f.groups()[1], f.groups()[2], next
    else:
        return "","","",[]

def parseprompt(lines):
    next = stripblanks(lines)
    prompt = []
    while next[0][0] not in ['~','-']:
        prompt.append(next[0])
        next = next[1:]
    return ''.join(prompt), next

def parseitem(lines, itemtype):
    next = stripblanks(lines)
    next = stripunderlines(next)
    content = []
    f = redict[itemtype].match(next[0])
    if f:
        next = stripunderlines(next[1:])
        if len(next) > 0:
            next = stripblanks(next)
            while len(next) and next[0][0] not in ['~', '-']:
                content.append(next[0])
                next = next[1:]
        else:
            next = next[:1]
        return ''.join(content), next
    else:
        return "", next[1:]


lines = file(sourcepath).readlines()
questions = []
next = lines
while len(next):
    title, exampletype, ID, next = parsetitle(next)
    if len(next):
        prompt, next = parseprompt(next)
        question, next = parseitem(next, "Question")
        answer, next = parseitem(next, "Answer")
        solution, next = parseitem(next, "Solution")
    questions.append([title, exampletype, ID, prompt, question, answer, solution])

folder = os.path.basename(os.path.splitext(sys.argv[1])[0])  # examples or practice
folderpath = os.path.join(os.path.dirname(sourcepath), folder)
if not os.path.exists(folderpath):
    os.mkdir(folderpath)
    
for q in questions:
    f = file(os.path.join(folderpath, q[2] + 'q.rst'), 'w')
    f.write(q[4]+"\n")
    f.close()
    f = file(os.path.join(folderpath, q[2] + 'p.rst'), 'w')
    f.write(q[3]+"\n")
    f.close()
    f = file(os.path.join(folderpath, q[2] + 'a.rst'), 'w')
    title = q[0]+' '+q[1]+' '+q[2]
    f.write(":orphan: \n\n" + title + "\n"+'-'*len(title)+"\n"+q[3]+"\n\n"+
        "Question\n~~~~~~~~\n"+q[4]+"\n\n"+
        "Answer\n~~~~~~\n"+q[5]+"\n\n")
    f.close()
    f = file(os.path.join(folderpath, q[2] + 's.rst'), 'w')
    f.write(":orphan: \n\n" + title + "\n"+'-'*len(title)+"\n"+q[3]+"\n\n"+
        "Question\n~~~~~~~~\n"+q[4]+"\n\n"+
        "Answer\n~~~~~~\n"+q[5]+"\n\n"+
        "Solution\n~~~~~~~~\n"+q[6]+"\n\n")

    f.close()



