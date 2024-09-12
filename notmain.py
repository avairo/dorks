import webbrowser

def generate_dork(domain, dorks_opt):
    dorks = {
        1: f"site:{domain} intitle:index.of",  # directory listing
        2: f"site:{domain} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini",  # config files
        3: f"site:{domain} ext:sql | ext:dbf | ext:mdb",  # database
        4: f"site:{domain} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:downlaod",  # wordpress1
        5: f"site:{domain} ext:log",  # log files
        6: f"site:{domain} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",  # old files
        7: f"site:{domain} inurl:login | inurl:signin | intitle:Login | intitle:signin | inurl:auth",  # login page
        8: f'site:{domain} intext:"sql syntax near" | intext:"syntax error has occured" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"',  # sql error
        9: f"site:{domain} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",  # exposed docs
        10: f"site:{domain} ext:php intitle:phpinfo 'published by the PHP Group'",  # php info
        11: f"site:{domain} inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor",  # backdoor
        12: f"site:{domain} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http",  # open redirect
        13: f'site:http://ideone.com | site:http://codebeautify.org | site:http://codeshare.io | site:http://codepen.io | site:http://repl.it | site:http://justpaste.it | site:http://pastebin.com | site:http://jsfiddle.net | site:http://trello.com | site:*.atlassian.net | site:bitbucket.org "{domain}"',  # 3rd party exposure
        14: f'site:pastebin.com "{domain}"',  # pastebin
        15: f"https://crt.sh/?q={domain}",  # subdomain
        16: f"site:{domain} inurl:wp-content | inurl:wp-includes",  # wordpress2
        17: f'site:atlassian.net | site:bitbucket.org "{domain}"',  # bitbucket/atlassian
        18: f'site:stackoverflow.com "{domain}"',  # stack overflow
        19: f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey",  # all wayback urls
        20: f'https://github.com/search?q=%22*.{domain}%22',  # github search
    }
    return dorks.get(dorks_opt, "Select a valid option")

def menu():
    print("Select a category for your search:")
    print("1. Directory listing")
    print("2. Config files")
    print("3. Database")
    print("4. Wordpress1")
    print("5. Log files")
    print("6. Old/backup files")
    print("7. Login pages")
    print("8. Sql errors")
    print("9. Exposed docs")
    print("10. Php info")
    print("11. Backdoor")
    print("12. Open redirect")
    print("13. 3rd party exposure")
    print("14. Pastebin")
    print("15. Subdomain")
    print("16. Wordpress2")
    print("17. Bitbucket/atlassian")
    print("18. Stack overflow")
    print("19. All wayback urls")
    print("20. Github search")
    print("0. Exit")

def main():
    while True:
        menu()
        try:
            option = int(input("\nEnter your option: "))
            if option == 0:
                print("Exiting...")
                break
            domain = input("Enter your target domain (e.g. example.in): ")
            query = generate_dork(domain, option)
            if query != "Select a valid option":
                print("\nGenerated dork:", query)
                print("\nOpening browser...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                print(query)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()


 


