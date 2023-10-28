class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            arr = queryIP.split(".")
            if len(arr) == 4:
                for val in arr:
                    if len(val) > 1 and val[0] == "0":
                        return "Neither"
                    if not val.isdigit():
                        return "Neither"
                    if int(val) > 255 or int(val) < 0:
                        return "Neither"
                return "IPv4"
                
        elif ":" in queryIP:
            arr = queryIP.split(":")
            if len(arr) == 8:
                for val in arr:
                    if not (1 <= len(val) <= 4):
                        return "Neither"
                    for char in val:
                        if char.isdigit() or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F'):
                            continue
                        else:
                            return "Neither"
                return "IPv6"
        return "Neither"
            