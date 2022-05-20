def preprocess_transcript_aishell3(dict_info, dict_transcript):
    for v in dict_transcript:
        if not v:
            continue
        v = v.strip().replace("\n","").replace("\t"," ").split(" ")
        transList = [v[i] for i in range(2, len(v), 2)]
        dict_info[v[0]] = " ".join(transList)


def preprocess_transcript_magicdata(dict_info, dict_transcript):
    for v in dict_transcript:
        if not v:
            continue
        v = v.strip().replace("\n","").replace("\t"," ").split(" ")
        dict_info[v[0]] = " ".join(v[2:])
       