# stex
Grabs reports from the asx site and displays them on a local browser.

The ideal goal for this project was to basically have a constant update of new reports coming in from the asx website, so that you can keep track of when your company releases new information, etc. This was my first experience with Node and a lot of the foundation code is from one of my tutes at Uni. Other than that, I did all the data grabbing and such.

I made this awhile ago too, but now that I'm pushing it here I will probably begin working on this soon and make it a lot neater and fix of server issues, etc. Because so far you cant actually call the '/posts' route from node unless you have a Postgres server running locally, because the javascript writes to the local postgres server. The more I write on this the more I want to work on this hah.

Some points for future guidance:
- tidy up the Node code
- create more friendly UI
- write a good CSS file
- fix up the data management (not requiring a local server)
- extend the use of this software to not grab all reports but to allow you to select few companies
  and then just retrieve all the information from those companies
- incorporate some diagrams? to display the market/dollar growth
- retrieve relevant news on the company
