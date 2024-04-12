import requests


def great_name(text, port="127.0.0.1:5000", history=1):
    # url = f'http://{server}'
    # response = requests.get(f'http://{port}').json()
    sp = []
    response = [
        {
            "name": "Jock",
            "variations": [
                "Jock-like-Toop-but-quieter-him",
                "Jock-larger-than-medium",
                "Jock-quieter-and-greater-not-like-huge-Jock"
            ]
        },
        {
            "name": "Henry",
            "variations": [
                "not-great-Henry-but-smaller-than-the-greatest-Henry",
                "not-medium-Henry-but-larger-than-smallest",
                "Henry-not-little-Henry",
                "greater-greater-Henry"
            ]
        },
        {
            "name": "Mack",
            "variations": [
                "Mack-less-quieter-like-like-Mack",
                "Mack-little-like-smaller-Mack",
                "smaller-than-huge-Mack"
            ]
        },
        {
            "name": "Tim",
            "variations": [
                "Tim-little-and-like-stone",
                "Tim-medium-larger",
                "medium-larger-than-Yavor-like-Tim",
                "smaller-quieter-greater-Tim"
            ]
        },
        {
            "name": "Yavor",
            "variations": [
                "Yavor-smaller-huge-Yavor-but-larger-smallest",
                "Yavor-like-medium-but-not-so-thick",
                "medium-quieter-Yavor"
            ]
        },
        {
            "name": "Woolly",
            "variations": [
                "Woolly-not-greater",
                "medium-Woolly",
                "Woolly-larger-than-Toop-but-smaller-than-large-Woolly"
            ]
        },
        {
            "name": "Toop",
            "variations": [
                "Toop-like-less-little-Toop-Toop",
                "Toop-quieter-than-great-Toop",
                "like-largest-Toop-but-not-largest-Toop"
            ]
        }
    ]
    for slov in response:
        if slov['name'][0] in text:
            for elem in slov["variations"]:
                if len(elem.split('-')) >= history:
                    sp.append(slov["variations"])
                    continue

    # return(sp)
    sp2 = []
    sp.sort(key=lambda s: len(s))
    for elem in sp:
        for x in elem:
            sp2.append(x)
    return (sp2)


print(great_name('TYN', history=5))
