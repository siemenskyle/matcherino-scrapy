import json
import requests
import time

if __name__ == '__main__':
    # SET THESE WITH YOUR OWN VALUES
    matcherinoId = 'ID GOES HERE'
    streamElementsAccountId = 'ID GOES HERE'
    streamElementsToken = 'JWT GOES HERE'
    # SET THESE WITH YOUR OWN VALUES

    # Set up urls and headers and stuff
    matcherinoUrl = 'https://matcherino.com/__api/bounties/findById'
    donationUrl = 'https://api.streamelements.com/kappa/v2/tips/' + streamElementsAccountId
    donationHeaders = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + streamElementsToken,
    }
    refreshIntervalSeconds = 2

    # This serves as a history of donations
    allDonations = dict()

    while True:
        time.sleep(refreshIntervalSeconds)

        # Request to Matcherino, api can be flaky at times I've found
        res = requests.post(matcherinoUrl, data=matcherinoId)
        if not res:
            print('no result')

        js = json.loads(res.content)
        body = js['body']
        if not body:
            print('body not found')
            continue

        donations = body['transactions']
        if not donations:
            print('.', end='')
            continue
        for donation in donations:
            # De-dupe donations already sent
            donationId = str(donation['id'])
            if allDonations.get(donationId):
                continue

            # Parse Donation
            allDonations[donationId] = donation
            amount = donation['amount']
            user = donation['displayName']
            userid = donation['id']
            comment = donation['comment']
            print('New donation from', user, ':', amount, comment)
            donationBody = {
                'user': {
                    'userid': userid,
                    'username': user,
                    'email': 'noemail@example.com',
                },
                'message': comment,
                'amount': str(amount/100),
                'currency': 'USD',
                'provider': 'matcherino',
                'imported': True,
            }
            # Send donation to StreamElements
            res = requests.post(donationUrl, data=json.dumps(donationBody), headers=donationHeaders)
            if res.status_code != 200:
                print("failed request!")
                print(res.content)

        print('.', end='')
