# Upload Image to Imgur via API

## Instructions

1. Go to [Imgur](https://imgur.com/) and create an account there.
2. To use Python scripts to upload images you'll need to register an application. [To do this follow this URL](https://api.imgur.com/oauth2/addclient)
3. To Register an application:
  * Fill up the `Application Name` input with a name
  * Select `Authorization Type`, to upload an image to an album `OAuth2` is recommended
  * On `Authorization Callback URL` you can fill it up with any url like `someurl.com`
  * Give your `email` and write a short description in one sentence.
  * Complete the CAPTCHA and press <kbd>Submit</kbd>
4. You'll be provided with an `secret id` and a `secret client` key. These are needed to upload images via script. 
