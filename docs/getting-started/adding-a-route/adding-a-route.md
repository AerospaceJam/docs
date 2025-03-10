---
sidebar_position: 7
description: We have sensors reporting data to our WebUI, but now we need to be able to send data from the WebUI back to the Pico.
---

# Adding a Route

Now that we've gotten our sensors up and running, we need to be able to send data from the WebUI back to the Pico. To do so, we can add a custom HTTP path, which calls a function on your Pico when it is called and can return some custom data to the WebUI. You can add a route to the server with:

```py
from aerospacejam import AerospaceJamServer, response_html, response_json
import json
# ...trimmed for brevity
pico_server = AerospaceJamServer(WIFI_CONFIG)
# ...trimmed for brevity

def hello_handler(request):
    print("Someone said hello!")
    return response_html("<h1>Hello, world!</h1>")
pico_server.register_path('/hello', hello_handler)
```

Then, when you go to the Pico's static IP (by default, `192.168.4.1`), you can get the response from this from `http://192.168.4.1/hello`. It will also log to the `Shell` window in Thonny:

```txt
Got a request from ('192.168.4.16', 53165)
Someone said hello!
```

Note that this is actually causing code on the Pico to be executed as it recieves the request - so we can change this to do certain things when you were to, say, click a button. In the WebUI's HTML, if you were to add:

```html
<script>
    function send_message() {
        fetch("/message", {
            method: "post",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                message: "Hello, world!"
            })
        })
        .then( (response) => { 
            console.log("Sent!");
        });
    }
</script>
<button onclick="send_message()">Send Message To Pico</button>
```

When the button is clicked, it will send a request to `/message` on the Pico. If you were to add the following handler code to the Pico:

```py
# First, define a function for the handler itself
def message_handler(request):
    # Then, convert the JSON's text to an actual Python object
    data = json.loads(request.body)
    # Then, we can do whatever we want with the object. For instance, since we defined the key `message: "Hello, world!"` in the WebUI's JavaScript,
    # we can access it with data['message']:
    print("Recieved a message:")
    print(data['message'])
    # Now, we have to return a response of some kind. Since there's no real response to return, we can just return a JSON object saying that the
    # request was a success.
    return response_json({"status": "OK"})
# And finally, we register this function as a message handler.
pico_server.register_path('/message', message_handler)
```
