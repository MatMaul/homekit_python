#!/usr/bin/env python3

#
# Copyright 2018 Joachim Lusiardi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os.path

from homekit import HomeKitServer

from homekit.model import Accessory, LightBulbService


def light_switched(newval):
    print('=======>  light switched: {x}'.format(x=newval))

if __name__ == '__main__':
    try:
        httpd = HomeKitServer(os.path.expanduser('~/.homekit/demoserver.json'))

        accessory = Accessory('Testlicht')
        lightBulbService = LightBulbService()
        lightBulbService.set_on_set_callback(light_switched)
        accessory.services.append(lightBulbService)
        httpd.accessories.add_accessory(accessory)

        print(httpd.accessories.__str__())

        httpd.publish_device()
        print('published device and start serving')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print('unpublish device')
    httpd.unpublish_device()
    httpd.shutdown()

