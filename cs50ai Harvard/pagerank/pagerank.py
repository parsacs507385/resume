import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probDist = {}
    for pageName in corpus:
        probDist[pageName] = 0

    if len(corpus[page])==0:
        for pageName in probDist:
            probDist[pageName] = 1/len(corpus)
        return probDist
    

    randomProb = (1-damping_factor)/len(corpus)
    linkProb = damping_factor/len(corpus[page])

    for pageName in probDist:
        probDist[pageName] += randomProb
        
        if pageName in corpus[page]:
            probDist[pageName] += linkProb
    return probDist

    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    visiteds = {}
    for pageName in corpus:
        visiteds[pageName] = 0
    
    currentPage = random.choice(list(visiteds))
    visiteds[currentPage] += 1

    for i in range(n-1):
        transModel = transition_model(corpus, currentPage, damping_factor)
        randProb = random.random()
        totalProb = 0

        for pageName, prob in transModel.items():
            totalProb += prob
            if randProb <= totalProb:
                currentPage = pageName
                break
        visiteds[currentPage] += 1

    
    pageRanks = {}
    for pageName, visitNum in visiteds.items():
        pageRanks[pageName] = (visitNum/n)
    
    return pageRanks



    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    startRank = 1/len(corpus)
    randProb = (1-damping_factor)/len(corpus)
    its = 0

    pageRanks = {pageName: startRank for pageName in corpus}
    newRanks = {pageName: None for pageName in corpus}
    maxRankDelta = startRank

    while 0.001 < maxRankDelta:
        maxRankDelta = 0
        its += 1

        for pageName in corpus:
            surfProb = 0
            for page in corpus:
                if len(corpus[page]) == 0:
                    surfProb += (pageRanks[page]*startRank)
                elif pageName in corpus[page]:
                    surfProb += pageRanks[page]/len(corpus[page])
            newRank = randProb+(damping_factor*surfProb)
            newRanks[pageName] = newRank
            
        normalFac = sum(newRanks.values())
        newRanks = {ppage: (rank/normalFac) for ppage, rank in newRanks.items()}

        for pageName in corpus:
            rankDelta = abs(pageRanks[pageName]-newRanks[pageName])
            if maxRankDelta < rankDelta:
                maxRankDelta = rankDelta
        pageRanks = newRanks.copy()
    
    return pageRanks



    # raise NotImplementedError


if __name__ == "__main__":
    main()
