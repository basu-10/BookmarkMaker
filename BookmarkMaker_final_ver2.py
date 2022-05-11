
topic_name=""
main_heading=""
dict_cat_topic_url = {}

'''
expect to have:
dict_cat_topic_url = {cat1: {'topic1': 'urllist', 'topic2': 'urllist', 'topic3': 'urllist'},
          cat2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
'''


def prepare_input():
    #
    print("\n\nStarting to create Bookmark")
    last_used_topic=""
    last_used_category = ""

    global topic_name , main_heading
    file1 = open('topics', 'r')

    count =0; #to keep track of line number/ to detect first line heading name
    print("\n  Processing the \"topics\" file...")
    while True:
        count+=1

        # Get next line from file
        line = file1.readline()
        line = line.strip(' ')#remove spaves

        line = line.replace("\n"," ") #replacing newline with space if its a blank line


        if count == 1:
            main_heading = line

        else:#if not first line...

            if line =="\n" or line==" " or line.startswith('#'): #blank line or line with space only
                continue
            else:
                #print("Line: "+ line)
                pass


                    # if line is empty
            # end of file is reached
            if not line:
                break

            elif line.find(':')>5: #this is a category name
                #print(line.find(':'))
                line = line.strip(':')
                last_used_category = line
                #print("cat name^ ")
                dict_cat_topic_url[last_used_category]={} #making the key = dict


            elif line.startswith('https://') or line.startswith('http://'): #link confirmed
                #print("link^")
                try:
                    dict_cat_topic_url[last_used_category][last_used_topic]+="window.open('"+line+"'); "
                except Exception as e:
                    print("Exception occured while creating HTML from dict"+e)
                    '''if str(e).find("KeyError"):
                        print("Either Heading/Category name or Topic name not given")
                        print("Proceeding with shortened version of the url as key ")'''

            elif line.startswith('www'): # append https:// #link confirmed
                #print("append https://")
                line = "https://"+line
                dict_cat_topic_url[last_used_category][last_used_topic]+="window.open('"+line+"'); "
    


            else: # topic name

                #print("topic name")
                topic_name = line
                last_used_topic=line
                dict_cat_topic_url[last_used_category][last_used_topic] = ""



    file1.close()
    #print("dict:")
    #print(dict_cat_topic_url)





def create_bookmark():
    global main_heading

    html_part1="<!DOCTYPE HTML><!DOCTYPE HTML><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><script src='Bookmark.js'>    </script><link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css'><style> body {background-color:hsl(0, 0%, 14%);}</style></head><body>"

    html_part2 = "</div><h1 class=\"has-text-centered is-family-code is-size-3 has-text-white has-background-black-ter\" >"+ main_heading +"</h1><br><br><div class=''>"


    #html_part3 = "" #all categories and topics and links
    html_part5 = "</body></html>"

    #prepare body

    html_code=html_part1+html_part2
    for cat, topic in dict_cat_topic_url.items():
        #print("\n\n\n")
        #print(cat)

        temp_string = "</div><br><br><br><h2 class=\" is-size-4 has-text-white \" > " + cat + "</h2><br><div class='box has-background-grey-darker'>"
        html_code+=temp_string

        print()
        for topicc, urls  in topic.items():#python ruby scala are topics... they willhave links...
            #all urls are together as a giant string
            temp_string2 = " &nbsp;&nbsp;&nbsp;&nbsp; <label class='checkbox'><input type='checkbox'></label>&nbsp;&nbsp;<a class=\" is-size-5 has-text-white\" href=\"#\"onclick="+"\""+urls+"\">"+topicc+"</a><br><br>"
            html_code+=temp_string2


        #end of printing for all values of 1 category


    html_code+=html_part5

    #print("to write: " + html_code)


    print("  Creating HTML file...\n")

    with open('Bookmarks_testing.html', 'w') as f:
        f.write(html_code)






if __name__ == "__main__":
    print("Welcome to Bookmark Maker, a free, open source (FOSS) project.")
    print()

    user_state="y"

    while (user_state=="y"):

        ip= input('Make sure your \"topics\" file is written correctly...\n(press h or help now for rules) \n\n\nProceed? (y/n)  ')

        if ip.casefold() =="y" or ip.casefold() =="yes" :
            #try:
            prepare_input()
            create_bookmark()
            #except Exception as e:
                #print(e)

            user_state="done"
            print("Bookmark successfully made... \n\n")
            print("Thank you for using. \n-A.Basu")

        elif ip.casefold() =="n" or ip.casefold() =="no" :
            user_state="break"

        elif ip.casefold() == "h" or ip.casefold() == 'help':
            print("As input, you need to provide a txt file with some rules")
            print("Rules of formatting txt file:")
            print("\t txt file must be named topics.txt ")
            print("\t First line is the Main Page Heading")
            print("\t Any lne ending with a : will be considered as Category Name")
            print("\t any line startting with https or http will be considered as url")
            print("\t Any line without a colon at end and https at beginning will be considered as Topic Name")

        else:
            print("\nINVALID INPUT")
            print("You can Enter 'y' for yes 'n' for no and 'h' for help")



    #a=input("(press any key to exit)")
