def main():
    fo=open("TxIn.log")
    lines=fo.readlines()
    for i,l in enumerate(lines):
        line=l.split(",")
        scriptSig=line[3]
        frags=scriptSig.split(" ")
        if frags[0]=='4c' and int(frags[1],16) < 76:
            found_mal=True
            print "PUSHDATA1: "+l.rstrip()
        if frags[0]=='4d' and int(frags[2]+frags[1],16)<255:
            found_mal=True
            print "PUSHDATA2: "+l.rstrip()
        if frags[0]=='4e' and int(frags[3]+frags[2]+frags[1],16)<65535:
            found_mal=True
            print "PUSHDATA4: "+l.rstip()


if __name__=="__main__":
    main()
