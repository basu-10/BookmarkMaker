# BookmarkMaker
This handy tool will help you to make HTML bookmarks from a sinle python script. Doesn't require installation. Takes input from text file. So, can be trigerred by bash commands as well. Only requirement is python >3.5

To Run, 

	1. 	Meet the Prequisites. See Below
		
	2. 	Run the BookmarkMaker.pyc file by double clicking on it. [Linux]
			[Everytime youy run the Python code, a HTML file with the same 
			name - Bookmarks.html will be created. So the previous HTML file, 
			if any, will be overwritten. To protect that file from being 
			overwritten, rename it to anything other than "topics" "Bookmarks"]


[IMPORTANT]
> In Chrome or other Modern browsers, the tabs will not be created the 
  first time the html file is opened in Browser.
  
	This is the default behavior of browsers.
	You need to click on a rectangular box at the right end of the URL bar, and select "Allow ......." 
	You need to do this every time you copy the files to a new location.




Prequisites:

> Python 3+	

> Javascript supported browser (Chrome reccommended)

> Input file must be named "topics" OR "topics.txt" (Depending on your OS)
	Input file must have the following rules:
		> Newlines (blank lines) are ignored
		> Every line can have one type of input.
		input = Big Heading , Category Heading , Topic Heading,  URL list
		
		> The first line will be taken as Big Heading. 
		> Any word ending with : is a Category Name (Small Heading)
		> Any word will be taken as Topic Heading (Link)
		> Any line beginning with http or https is taken as the URL and put into URL List. 
			This URL List will be set as a link to open all the URLs at once.
			So make sure the order is : 
				Big Heading , Category Heading , Topic Heading,  URL list

The topics file is already set with a template. Replace the texts with your own. 
Or create a new text file named "topics" OR "topics.txt" (Depending on your OS)
