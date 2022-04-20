# matcherino-scrapy
Scrapes matcherino donations and forwards them to Streamelements for alerts

So this thing is pretty hacky but it gets the job done. There's an api endpoint you can hit that gets back everything you need from Matcherino, its the exact same one their own overlay uses actually:

`https://matcherino.com/__api/bounties/findById`

All this script does is poll that endpoint on some set interval (no websockets or anything fancy, just doing a request every X seconds, same as what their overlay does actually), takes the response from the endpoint and forwards donations over to StreamElements. Then in SE you can do whatever with them, they behave like normal dontaions! Alerts ahoy!

## Setup

At the top of the `main` function there's some IDs you need to set:
```python
# SET THESE WITH YOUR OWN VALUES
matcherinoId = 'ID GOES HERE'
streamElementsAccountId = 'ID GOES HERE'
streamElementsToken = 'JWT GOES HERE'
# SET THESE WITH YOUR OWN VALUES
```

* `MatcherinoId` can be grabbed from the matcherino, either from the URL or in the Admin Page, its the number next to "General"
* `streamElementsAccountID` can be grabbed on your StreamElements account page.
* `streamElementsToken` can also be grabbed on the account page, you need to click the "Show Secrets" button. You want the one marked "JWT Token" **be careful with this token, it is dangerous as it gives full api controller to whoever uses it**. If you happen to leak the token it can be reset on the Security tab of the profile.

When you're done it should look something like this:
```python
# SET THESE WITH YOUR OWN VALUES
matcherinoId = '55486'
streamElementsAccountId = '6c1a8474e32267cfadc56c94'
streamElementsToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
# SET THESE WITH YOUR OWN VALUES
```
