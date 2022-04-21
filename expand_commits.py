from git_history.codeline import Codeline
from git_history.dataline import Dataline

def authors_expansions(lines):
    for line in lines:
        spl = line.author.split(',')
        weight = 1.0 / len(spl)
        for auth in spl:
            yield Codeline(
                line.ch,
                auth.strip(),
                line.data,
                weight
            )

def detail_expansion(commit_detail, weight):
    return (
        Dataline(
            commit_detail.ch,
            commit_detail.author,
            commit_detail.date,
            int(fc.removed * weight),
            int(fc.added * weight),
            fc.name
        )
        for fc in commit_detail.changesInFile
    )

def lines_expansion(git, code_lines):
    for line in code_lines:
        commit_detail = git.show(line.ch, line.date, line.author)
        for data_line in detail_expansion(commit_detail, line.weight):
            yield data_line
