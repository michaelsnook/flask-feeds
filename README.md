[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Flask + Vercel

This example shows how to use Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-python-template.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# API Endpoints Usage

This part of the documentation will explain how various APIs can be used to interact with the list services.

## Add User to List

To add a user to a list, send a POST request to the `/add_user_to_list` endpoint with the following JSON payload:

```
{
  "list_uri": "at://did:plc:abcdefg/app.bsky.graph.list/list_rkey",
  "user_did": "did:plc:1234567890"
}
```

### Example using cURL

```
curl -X POST -H "Content-Type: application/json" -d '{"list_uri": "at://did:plc:abcdefg/app.bsky.graph.list/list_rkey", "user_did": "did:plc:1234567890"}' http://localhost:3000/add_user_to_list
```

### Response

On successful addition of a user to a list, the API will return a JSON response:

```
{
  "result": "User [user_did] added to list: [list_uri]"
}
```
