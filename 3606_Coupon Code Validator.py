class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        valid = []
        allowed = ["electronics", "grocery", "pharmacy", "restaurant"]
        e = []
        g = []
        p = []
        r = []
        for i in range(len(code)):
            random = ""
            if "_" in code[i]:
                random = code[i].replace("_","Q")
                if random != "" and random.isalnum():
                    if businessLine[i] in allowed:
                        if isActive[i]:
                            if businessLine[i] == "electronics":
                                e.append(code[i])
                            if businessLine[i] == "grocery":
                                g.append(code[i])
                            if businessLine[i] == "pharmacy":
                                p.append(code[i])
                            if businessLine[i] == "restaurant":
                                r.append(code[i])
            else:
                if code[i] != "" and code[i].isalnum():
                    if businessLine[i] in allowed:
                        if isActive[i]:
                            if businessLine[i] == "electronics":
                                e.append(code[i])
                            if businessLine[i] == "grocery":
                                g.append(code[i])
                            if businessLine[i] == "pharmacy":
                                p.append(code[i])
                            if businessLine[i] == "restaurant":
                                r.append(code[i])
        e.sort()
        for i in e:
            valid.append(i)
        g.sort()
        for i in g:
            valid.append(i)
        p.sort()
        for i in p:
            valid.append(i)
        r.sort()
        for i in r:
            valid.append(i)
        return valid
