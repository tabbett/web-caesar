#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

form = """
<form>
    <label>
        Enter message
        <input name = "message">
    </label>
    <br>
    <label>
        Enter rotation
        <input name = "rot">
    </label>
    <br>
    <input type = submit>

</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = 'Hello World!'
        self.response.write(caesar.encrypt(message,13))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
