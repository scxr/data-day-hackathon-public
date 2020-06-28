## Inspiration
Our project was originally inspired by a similar project, [Sherlock](https://github.com/sherlock-project/sherlock), which is a command line based tool that "hunt[s] down social media accounts by username across social networks". We were interested in this concept and the overall idea of using the immense amount of data we all put put on the internet. However, instead of just looking for whether an account existed or not, we also wanted to show various other data on the account depending on which platform the account was on. 

## What it does
Our final product is a website that takes the user's inputted username and searches various popular websites for accounts that match that username and then displays various metadata about each of the accounts associated with that username. As of the end of this hackathon, we support searching for accounts on Instagram, Reddit, Stack Overflow, Twitter, Twitch and Youtube.

## How we built it
### Backend
The backend of our website is written in Python using the Flask framework. When a user sends a request to our backend, it uses a patchwork of different methods ranging from webscraping to official APIs to search popular websites for accounts with the provided username.

### Frontend
The frontend of our website is written in Typescript using the Next.js framework and Tailwind and blocks.css as UI libraries. It accepts user input and displays the accounts that the server finds. Since the metadata associated with the account is different depending on which platform the account is associated with, the frontend also contains an algorithm to automatically identify what type of value a given metadata field holds. For example, it can identify URLs and format them as links as opposed to plaintext and also can guess when a number actually represents a UNIX timestamp and format it accordingly.

## Challenges we ran into
One of the primary challenges was the time-consuming task of writing or finding scrapers or APIs for each social media website. Each website posed its unique challenges in terms of data parsing and error handling.

One later issue that went unresolved was that our scraper for Instagram didn't work once we hosted our backend on Heroku because Instagram had blocked associated Heroku IPs, probably because of other scrapers hosted by Heroku. In the future we would use Instagram's official API or have our own hosting to eliminate this problem.

## Accomplishments that we're proud of
We're proud of being able to deliver a fully-workable accesible product, especially given the amount of busy work that had to be done researching and implementing the best ways to gather data from each website.

## What we learned
We learned a lot about the varying degrees of accessibility that social media sites provide to their users' data. Some websites had open APIs, others had APIs with varying levels of authentication, and for others we had to rely on webscraping. In this age where data is being generated at blazingly-fast speeds, it's become increasing politically and socially relevant to see how different companies approach their stewardship over their data.

## What's next for Where Am I Online?
The most clear next step for our project is to continue to add to the number of websites we support so our tool can provide a more comprehensive image of a user's online data footprint.
